---
type: concept
updated: 2026-07-19
sources: [turing-award-winner-nsa-public-key.md, turing-award-winner-p-vs-np-zero.md, turing-award-winner-on-working-with.md, mozilla-firefox-cto-on-browser-war.md, co-creator-of-haskell-functional.md, ex-head-of-eng-at-instagram-career.md, googlex-chief-scientist-on-imposter.md, mit-complexity-theorist-on-leetcode.md, creator-of-c-bell-labs-negative-overhead.md]
---

# Security and cryptography

Two intertwined threads across the episodes: the invention and politics of cryptography (told by the people who fought the crypto wars), and the practice of security engineering in browsers, antivirus, and language design.

## What the guests say

### The crypto wars: publishing as a battlefield

[Martin Hellman](../entities/martin-hellman.md) recounts the NSA framing his publications as arms export under ITAR ("exporting technical data on implements of war"), presenting his students' papers personally at Cornell so Stanford could defend him instead of them, and the DES 56-bit key fight — the NSA wanted a key small enough that only its budget could brute-force it, "a crude trapdoor via superior computing resources." His throughline over three crypto wars (DES/publishing, the 1990s Clipper Chip, San Bernardino): "you cannot make strong encryption and give it only to the good guys," and the classified-briefing argument dissolves on inspection — his CRISIS committee found briefings "filled in details but did not change our fundamental conclusions" ([episode](../sources/turing-award-winner-nsa-public-key.md)). [James Everingham](../entities/james-everingham.md) corroborates the era from the trenches: open-sourcing Netscape's code as Mozilla required legally stripping SSL, then still classified as a munition ([episode](../sources/ex-head-of-eng-at-instagram-career.md)).

### The foundations: one-way functions all the way down

Hellman explains Diffie-Hellman with the double-lock strongbox — the underlying operation must be a commutative one-way function — and stresses that digital signatures (Diffie's concept) are what GCHQ's claimed prior invention never had, and why an iPhone can verify [Apple](../entities/apple.md)'s updates with just a public key ([episode](../sources/turing-award-winner-nsa-public-key.md)). [Leslie Lamport](../entities/leslie-lamport.md) adds a footnote to the same history: he wrote the first digital signature scheme on a napkin after Whit Diffie described the open problem, before Diffie-Hellman was published ([episode](../sources/turing-award-winner-on-working-with.md)). [Avi Wigderson](../entities/avi-wigderson.md) supplies the theory: assuming one-way functions exist, zero-knowledge proofs are universal — anything provable can be proved while revealing nothing else — and Shor's algorithm drove the post-quantum program (lattices, learning-with-errors) ([episode](../sources/turing-award-winner-p-vs-np-zero.md)). [Ryan Williams](../entities/ryan-williams.md) notes techniques flow back from cryptanalysis into algorithms (meet-in-the-middle) ([episode](../sources/mit-complexity-theorist-on-leetcode.md)). See [complexity-theory](complexity-theory.md).

### Security engineering in practice: get ahead of the attacker structurally

- [Bobby Holley](../entities/bobby-holley.md)'s career-making work was the self-initiated year-plus "Slaughterhouse" project fixing an entire class of JS/DOM-binding exploits — vindicated when a threat actor exfiltrated ~45 security bugs from Mozilla's own Bugzilla and all but ~2 were already fixed. His lesson: "sometimes you don't have the luxury of time," so eliminate vulnerability classes architecturally rather than patching instances. His wildest story — recognizing the "handwriting" of an in-the-wild zero-day and wrongly accusing a friendly researcher who then went off the grid — shows how attribution folklore actually works ([episode](../sources/mozilla-firefox-cto-on-browser-war.md)).
- [Carey Nachenberg](../entities/carey-nachenberg.md) built the defender's side at Symantec (detecting self-mutating polymorphic viruses — his master's thesis, shipped in product) and later Chronicle's Backstory at Google X: petabytes/week of enterprise telemetry indexed so threat investigations dropped from ~30 minutes per query to ~2 seconds ([episode](../sources/googlex-chief-scientist-on-imposter.md)).
- Everingham's origin story is the attacker's side: FBI at the door at 16 for phone-phreaking software he'd proudly signed with his own name ([episode](../sources/ex-head-of-eng-at-instagram-career.md)).

### Disagreement — is memory safety the security problem?

[Simon Peyton Jones](../entities/simon-peyton-jones.md) argues the Internet's infrastructure is "a boat built out of paperclips": writing it in safe languages would remove ~99% of exploits (buffer overruns, pointer bugs) by construction — though no language prevents deadlock or bad logic ([episode](../sources/co-creator-of-haskell-functional.md)). [Bjarne Stroustrup](../entities/bjarne-stroustrup.md) pushes back sharply ("I'm so tired of that"): over 90% of exploited C++ safety bugs come from C-style raw-pointer code, hardened libraries and C++26's hardened option already close most of the gap ([episode](../sources/creator-of-c-bell-labs-negative-overhead.md)). Mozilla's revealed preference sits with Peyton Jones: Rust was created precisely because memory-safety exploits in C++ were structural, and Firefox Quantum shipped Rust components into the browser ([episode](../sources/mozilla-firefox-cto-on-browser-war.md)). See [programming-languages](programming-languages.md) for the full debate.

## Practical takeaways

- Fix vulnerability classes, not vulnerabilities — architectural projects like Slaughterhouse pay off when (not if) your bug tracker leaks ([Holley](../sources/mozilla-firefox-cto-on-browser-war.md)).
- Choose memory-safe languages for new attack-surface code; if staying in C++, adopt hardened modes and purge C-style pointer code ([Peyton Jones](../sources/co-creator-of-haskell-functional.md), [Stroustrup](../sources/creator-of-c-bell-labs-negative-overhead.md)).
- Treat "only the good guys get the backdoor" proposals as technically incoherent — three crypto wars ended the same way ([Hellman](../sources/turing-award-winner-nsa-public-key.md)).
- Make security data queryable at interactive speed; investigation latency is a defense metric ([Nachenberg](../sources/googlex-chief-scientist-on-imposter.md)).
- Plan for the post-quantum transition; the hardness assumptions under today's key exchange are not permanent ([Wigderson](../sources/turing-award-winner-p-vs-np-zero.md)).
- Contrarian bets against powerful incumbents can define a career — Hellman took on the NSA when every colleague called it crazy ([Hellman](../sources/turing-award-winner-nsa-public-key.md)).

## Related

- [complexity-theory](complexity-theory.md) — the hardness assumptions cryptography rests on; [programming-languages](programming-languages.md) — the memory-safety debate; [incident-management](incident-management.md) — Holley's breach response; [open-source](open-source.md) — the Mozilla SSL-stripping story.
- Key people: [Martin Hellman](../entities/martin-hellman.md), [Bobby Holley](../entities/bobby-holley.md), [Carey Nachenberg](../entities/carey-nachenberg.md), [Avi Wigderson](../entities/avi-wigderson.md).
- Most relevant episodes: [Hellman](../sources/turing-award-winner-nsa-public-key.md), [Holley](../sources/mozilla-firefox-cto-on-browser-war.md), [Wigderson](../sources/turing-award-winner-p-vs-np-zero.md).
