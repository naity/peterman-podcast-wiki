---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [airbnb-staff-eng-on-how-to-not-get.md, cloudkitchens-cto-on-intelligence.md, meta-distinguished-eng-ic9-on-influencing.md, turing-award-winner-nsa-public-key.md, turing-award-winner-tpu-vs-gpu-vs.md]
---

# Apple

Apple appears in five episodes — never as a guest's main employer, but as the platform vendor Meta's iOS engineers fought and worked around, the company in a famous Steve Jobs intern story, and a touchstone in hardware and cryptography history.

## What the episodes reveal

- **Apple frameworks at Meta scale.** Adam Ernst's E6 promotion came from replacing Apple's Core Data ORM — fine for a two-engineer startup but "falls over completely" at 100–200 engineers — against pushback from "Apple-y engineers" who insisted on vanilla Apple frameworks; his team disassembled Core Data's closed source to show exactly why it couldn't work. His ComponentKit later brought React's concepts to iOS in 2014, before Apple shipped Swift or SwiftUI. He also names Nolan O'Brien as the engineer managing "the delicate Meta-Apple relationship" ([Adam Ernst](../sources/meta-distinguished-eng-ic9-on-influencing.md)).
- **The Steve Jobs story.** As an Apple intern, Brian Attwell built a sunlight-readability OS tweak; when his mentor's praise drew Jobs over, Attwell downplayed it ("it's like 50, a hundred lines of code"), Jobs rolled his eyes and walked off, and the project died. Attwell's lesson isn't pitch regret — at 18 he couldn't have done better — but about the times he knew the truth mid-project and stayed quiet ([CloudKitchens CTO](../sources/cloudkitchens-cto-on-intelligence.md)).
- **Hardware history.** ARM was renamed "Advanced RISC Machine" when Apple adopted it for the Newton — the beginning of the architecture that now ships in essentially all phones ([David Patterson](../sources/turing-award-winner-tpu-vs-gpu-vs.md)).
- **Cryptography.** Digital signatures are why an iPhone can verify Apple's software updates with only a public key on the device ([Martin Hellman](../sources/turing-award-winner-nsa-public-key.md)); the San Bernardino iPhone fight was the third "crypto war," recycling the same key-escrow idea Hellman's CRISIS committee had concluded was unsolvable ([same](../sources/turing-award-winner-nsa-public-key.md)).
- Laurent Charignon had an early stint at Apple before his Instagram/Airbnb/[Stripe](stripe.md) developer-productivity career ([Airbnb Staff Eng](../sources/airbnb-staff-eng-on-how-to-not-get.md)).

## People

- [Adam Ernst](adam-ernst.md) — built [Meta](meta.md)'s replacements for Apple's iOS frameworks
- [Brian Attwell](brian-attwell.md) — Apple intern (the Steve Jobs story)
- [Laurent Charignon](laurent-charignon.md) — early-career stint

## Related

- [big-tech-culture](../concepts/big-tech-culture.md)
- [computer-architecture](../concepts/computer-architecture.md) — ARM/RISC lineage
- [security-and-cryptography](../concepts/security-and-cryptography.md) — code signing, crypto wars
- [Meta](meta.md) — the Meta-Apple platform relationship
