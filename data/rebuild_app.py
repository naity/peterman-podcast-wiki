#!/usr/bin/env python3
"""Regenerate app/index.html from app/template.html + data/graph.json.
Run data/build_graph_index.py first."""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data = open('data/graph.json').read().replace('</', '<\\/')
tpl = open('app/template.html').read()
assert '__GRAPH_DATA__' in tpl, 'template placeholder missing'
open('app/index.html', 'w').write(tpl.replace('__GRAPH_DATA__', data))
print('app/index.html rebuilt:', os.path.getsize('app/index.html') // 1024, 'KB')
