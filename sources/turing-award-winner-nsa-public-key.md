---
type: source
updated: 2026-07-19
raw: ../raw/turing-award-winner-nsa-public-key.md
guest: "Martin Hellman"
guest_role: "Turing Award winner, Stanford professor emeritus, co-inventor of public-key cryptography"
date: 2026-07-06
url: https://www.developing.dev/p/turing-award-winner-nsa-public-key
---

# Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman

[Martin Hellman](../entities/martin-hellman.md) co-invented public-key cryptography and the Diffie-Hellman key exchange at [Stanford](../entities/stanford.md), work that won him the Turing Award and put him in direct conflict with the NSA. The episode covers the crypto wars (the NSA claiming his publications broke arms-export law), how encryption worked before public keys, the strongbox intuition behind Diffie-Hellman, the RSA patent fight he lost, why simultaneous invention happens, and his later work on nuclear risk — plus unusually personal reflections on marriage, courage, and death.

## Key takeaways

- Hellman's early [security-and-cryptography](../concepts/security-and-cryptography.md) work was framed by the NSA as illegal: under ITAR, anything cryptographic was an "implement of war," so publishing papers in international journals was "exporting technical data on implements of war." A July 1977 letter from an NSA employee (writing from his Maryland home address) to the IEEE triggered the fight; Stanford's general counsel thought that interpretation unconstitutional, and Hellman personally presented his students' papers at Cornell so Stanford could defend him instead of them.
- The first crypto war was over two things: freedom to publish, and DES's 56-bit key. Hellman and Diffie estimated in 1975 that a $20M machine of million-key-per-second search chips could break DES for ~$10,000 per solution — and that being off by 10x would be erased by Moore's Law in five years. NSA wanted the small key precisely because only they had enough problems (and budget) to keep such a machine loaded — a crude trapdoor via superior computing resources.
- The second crypto war (1990s Clipper Chip key escrow) and third (San Bernardino iPhone, "Keys Under Doormats") were the same idea recycled: Hellman's CRISIS committee concluded key escrow's problems were unsolvable, and — critically — that classified briefings "filled in details but did not change our fundamental conclusions," defusing the "if you knew what we knew" argument.
- You cannot give strong encryption only to good guys — his analogy: if cars had been invented in the classified world, government would have decried civilian cars while losing ambulances, commuting, and vacations.
- All his colleagues told him he was crazy to work in cryptography against a multibillion-dollar NSA with a decades head start; he argues the best work looks crazy a priori (GPS, Nobel-winning work) and credits his contrarian streak — bullied as a Jewish kid in an Irish Catholic Bronx neighborhood, he adopted "who would want to be like anybody else?" and came to believe it.
- Diffie-Hellman explained via the double-lock strongbox: both parties add their own lock, remove them in either order — which is why the underlying operation must be a commutative one-way function (exponentiation in modular arithmetic over a finite field). Digital signatures (Diffie's concept, RSA's first instance) are what GCHQ's claimed prior invention never had; signatures are why an iPhone can verify [Apple](../entities/apple.md)'s software updates with only a public key on the device.
- Ralph Merkle deserves co-credit: as a Berkeley student he independently invented public-key distribution in a term project his professor dismissed and CACM rejected ("Has no one thought of doing anything like this before?" — answer: no). Hellman recruited him to Stanford and helped rewrite the paper.
- The Stanford patent was written by a law school intern, not a patent attorney; only claims matter, so it failed to cover RSA — RSA sold for $250M, Hellman made virtually nothing. He deliberately buried the hatchet with RSA's Jim Bidzos because "friends are better than enemies," a lesson from repairing his own toxic marriage (59 years married; his wife's "crazy" ideas taught him to stop dismissing what he didn't understand).
- Simultaneous invention (him/Diffie, Merkle, GCHQ; Newton/Leibniz; Darwin/Wallace) he half-jokes is "a muse" — but notes the technological substrate matters: 50 years earlier there was no computing power to implement public-key cryptography.
- Post-cryptography he works on nuclear risk ([regrets-and-advice](../concepts/regrets-and-advice.md) meets activism): he estimates a child born today has worse-than-even odds of living out a natural life due to nuclear weapons alone, and is pushing H.R. 3564 to limit sole presidential launch authority (with a launch-on-warning exception that makes it "so bad it's passable, but so good it's a game changer").
- Advice to his younger self: the guru would say "become as famous and rich as you can, come back in 10 years" — an apparent detour that was the shortest path, because reputation and money are what let him work on saving the world at 35.

## Notable quotes

- "I'm from the Bronx... I'm a street fighter with my mouth and my mind. And they picked the wrong person, basically. I wasn't going to back down." — Martin Hellman, ~04:20
- "You cannot make strong encryption and give it only to the good guys and not to the bad guys." — Martin Hellman, ~25:23
- "All my colleagues, and it's not an exaggeration, told me I was crazy to work in cryptography... And the best ideas often seem crazy ahead of time." — Martin Hellman, ~31:52
- "If humanity were to die now, it would be an infant. It would be infant mortality... We need to save humanity from an infant death. We've only been around about 100,000 years." — Martin Hellman, ~58:38

## Connections

- [Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson](turing-award-winner-p-vs-np-zero.md) — Hellman explicitly ties cryptography's existence to P vs NP and one-way functions, Wigderson's home turf.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — fellow Turing Award winner; both preach courage/standing up to powerful opposition and credit long marriages with simple rules.
- [Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov](turing-award-winner-data-abstraction.md) — Ryan directly references his Liskov interview when discussing simultaneous coast-to-coast invention.
- [MIT Complexity Theorist: Why You Can Do Better Than 'Optimal' On Leetcode & SAT | Ryan Williams](mit-complexity-theorist-on-leetcode.md) — complexity theory (P vs NP, hardness) is the foundation Hellman says cryptography rests on.
