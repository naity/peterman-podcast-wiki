#!/usr/bin/env python3
"""Build data/graph.json and index.md from extracts + pages. Also lint links."""
import json, glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

episodes = {e['slug']: e for e in json.load(open('data/episodes.json'))}
extracts = {}
for f in sorted(glob.glob('data/extracts/*.json')):
    d = json.load(open(f))
    extracts[d['slug']] = d

CONCEPT_ALIAS = {'truth-seeking': 'startups-and-founding'}

def fm(path):
    """Parse simple YAML frontmatter."""
    txt = open(path).read()
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip('"')
    body = txt[m.end():] if m else txt
    h1 = re.search(r'^# (.+)$', body, re.M)
    # first non-empty paragraph after H1
    desc = ''
    if h1:
        after = body[h1.end():]
        for para in after.split('\n\n'):
            p = para.strip()
            if p and not p.startswith('#') and not p.startswith('>'):
                desc = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', p.replace('\n', ' '))
                break
    return meta, (h1.group(1) if h1 else os.path.basename(path)), desc

# ---------- graph ----------
nodes, links = [], []
def add_node(nid, ntype, label, **kw):
    nodes.append(dict(id=nid, type=ntype, label=label, **kw))

org_count = collections.Counter()
concept_count = collections.Counter()
for d in extracts.values():
    for c in d.get('companies', []): org_count[c] += 1
    for c in d.get('concepts', []): concept_count[CONCEPT_ALIAS.get(c, c)] += 1

ORG_MIN = 2
orgs = {o for o, n in org_count.items() if n >= ORG_MIN}
concepts = set(concept_count)

persons = {}  # guest_slug -> info
for slug, d in sorted(extracts.items(), key=lambda kv: -kv[1].get('n', 0)):
    gs = d.get('guest_slug')
    if gs:
        persons.setdefault(gs, {'name': d.get('guest', gs), 'role': d.get('guest_role', ''), 'episodes': []})
        persons[gs]['episodes'].append(slug)

for slug, d in sorted(extracts.items(), key=lambda kv: -kv[1].get('n', 0)):
    e = episodes[slug]
    add_node('ep:' + slug, 'episode', d.get('title', e['title']),
             n=d.get('n', e['n']), date=e['date'], url=d.get('url', f"https://www.developing.dev/p/{slug}"),
             guest=d.get('guest', ''), guest_role=d.get('guest_role', ''),
             takeaways=d.get('key_takeaways', []), quotes=d.get('notable_quotes', []),
             sections=d.get('sections', []), complete=bool(d.get('transcript_complete', True)))

for gs, p in persons.items():
    add_node('p:' + gs, 'person', p['name'], role=p['role'])
    for slug in p['episodes']:
        links.append({'source': 'p:' + gs, 'target': 'ep:' + slug, 'kind': 'guest_of'})

for o in sorted(orgs):
    add_node('o:' + o, 'org', o.replace('-', ' ').title().replace('Uc Berkeley','UC Berkeley').replace('Mit','MIT').replace('Ibm','IBM').replace('Aws','AWS').replace('Openai','OpenAI').replace('Ucla','UCLA').replace('Nvidia','NVIDIA'), count=org_count[o])
for c in sorted(concepts):
    add_node('c:' + c, 'concept', c.replace('-', ' ').title().replace('Ai ', 'AI '), count=concept_count[c])

for slug, d in extracts.items():
    for o in set(d.get('companies', [])):
        if o in orgs:
            links.append({'source': 'ep:' + slug, 'target': 'o:' + o, 'kind': 'features_org'})
    for c in set(CONCEPT_ALIAS.get(x, x) for x in d.get('concepts', [])):
        links.append({'source': 'ep:' + slug, 'target': 'c:' + c, 'kind': 'discusses'})
    for r in d.get('related', []):
        rs = r.get('slug')
        if rs in episodes and rs != slug:
            pair = tuple(sorted([slug, rs]))
            links.append({'source': 'ep:' + pair[0], 'target': 'ep:' + pair[1], 'kind': 'related', 'reason': r.get('reason', '')})

# dedupe related edges
seen, deduped = set(), []
for l in links:
    key = (l['source'], l['target'], l['kind'])
    if key in seen: continue
    seen.add(key); deduped.append(l)
links = deduped

graph = {'generated': '2026-07-19', 'nodes': nodes, 'links': links,
         'stats': {'episodes': len(extracts), 'people': len(persons), 'orgs': len(orgs), 'concepts': len(concepts), 'links': len(links)}}
json.dump(graph, open('data/graph.json', 'w'), indent=1)
print('graph:', graph['stats'])

# ---------- index.md ----------
def section(title, items):
    out = [f'## {title}', '']
    out += [f'- [{t}]({p}) — {d[:180].rstrip(".")}' if d else f'- [{t}]({p})' for p, t, d in items]
    out.append('')
    return out

idx = ['# Index', '',
       f'Knowledge base for The Peterman Post podcast (developing.dev) — {len(extracts)} episodes ingested, '
       f'{len(persons)} guests, {len(orgs)} organizations, {len(concepts)} concepts. Last updated 2026-07-19.', '']

items = []
for f in sorted(glob.glob('sources/*.md'), key=lambda f: -extracts.get(os.path.basename(f)[:-3], {}).get('n', 0)):
    meta, title, desc = fm(f)
    slug = os.path.basename(f)[:-3]
    n = extracts.get(slug, {}).get('n', '?')
    items.append((f, f'#{n}: {title}', desc))
idx += section('Sources (episodes, newest first)', items)

ppl, org_items = [], []
for f in sorted(glob.glob('entities/*.md')):
    meta, title, desc = fm(f)
    (ppl if meta.get('entity_kind') == 'person' else org_items).append((f, title, desc))
idx += section('Entities — people', ppl)
idx += section('Entities — organizations', org_items)

items = [(f,) + fm(f)[1:] for f in sorted(glob.glob('concepts/*.md'))]
idx += section('Concepts', items)
notes = [(f,) + fm(f)[1:] for f in sorted(glob.glob('notes/*.md'))]
if notes:
    idx += section('Notes', notes)
open('index.md', 'w').write('\n'.join(idx))
print('index.md written:', len(ppl), 'people,', len(org_items), 'orgs,', len(items), 'concepts')

# ---------- lint ----------
broken = []
for f in glob.glob('sources/*.md') + glob.glob('entities/*.md') + glob.glob('concepts/*.md') + glob.glob('notes/*.md') + ['index.md']:
    base = os.path.dirname(f)
    for m in re.finditer(r'\]\(([^)#]+?\.md)\)', open(f).read()):
        target = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.exists(target):
            broken.append((f, m.group(1)))
print('broken links:', len(broken))
for b in broken[:60]: print('  ', b[0], '->', b[1])
