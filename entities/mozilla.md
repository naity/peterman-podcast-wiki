---
type: entity
entity_kind: org
updated: 2026-07-19
sources: [ex-head-of-eng-at-instagram-career.md, mozilla-firefox-cto-on-browser-war.md]
---

# Mozilla

Mozilla — the open-source organization behind Firefox — appears in two episodes that together tell its whole arc: James Everingham was at Netscape when the Mozilla codebase was open-sourced, and Bobby Holley went from 2008 Mozilla intern to CTO of Firefox.

## What the episodes reveal

- **Origin: a parting shot at Microsoft.** Open-sourcing Netscape's code (suggested by Jamie "jwz" Zawinski) was a way for dozens of Netscape engineers to compete with [Microsoft](microsoft.md)'s thousands after IE's free bundling destroyed the browser business; shipping it required stripping SSL (legally a munition then), obfuscating its APIs, and hand-censoring swear-word variable names with highlighters on printouts ([James Everingham](../sources/ex-head-of-eng-at-instagram-career.md)). Volunteers — like Holley's hero Boris Zbarsky, who started because his MIT dorm browser kept crashing — then built Firefox (Phoenix → Firebird → Firefox) out of the bloated suite while Microsoft parked IE in maintenance mode ([Bobby Holley](../sources/mozilla-firefox-cto-on-browser-war.md)).
- **Culture: anti-onboarding by design.** Early Mozilla deliberately had almost no guardrails ("get on IRC and Bugzilla and figure out some things to do") — the open-source project selected for self-motivated people; ownership worked by "who owns this?" — "you do now" ([Bobby Holley](../sources/mozilla-firefox-cto-on-browser-war.md)).
- **The Google relationship.** [Google](google.md) was originally Firefox's biggest ally (the default-search deal funded Mozilla; staff had Google lunch badges) until Chrome launched in 2008; decay came through organizational incentives, not villainy — the "year of a hundred oopses" of always-unintentional "Download Chrome" banners shown to Firefox users ([Bobby Holley](../sources/mozilla-firefox-cto-on-browser-war.md)). Firefox genuinely fell behind (Chrome's multi-process architecture, V8) while the Firefox OS mobile bet drained resources at the worst moment ([same](../sources/mozilla-firefox-cto-on-browser-war.md)).
- **Technical legacy.** Rust was Mozilla's answer to two structural C++ problems — memory-safety exploits and single-threaded engines on multi-core hardware — co-evolved with Servo; a dozen people couldn't out-build hundreds of Chromium engineers, so Mozilla uplifted Servo's parallel CSS engine into Firefox Quantum (led by Holley), yielding the fastest CSS engine in the market and Holley's principal promotion ([Bobby Holley](../sources/mozilla-firefox-cto-on-browser-war.md)).
- **The DE bar and the AI stakes.** CTO Eric Rescorla told Holley new Distinguished Engineers were being minted for the first time in ~a decade — and he wouldn't be one, because the bar had shifted from Firefox-codebase mastery to industry-wide impact; Holley found it inspiring, "like discovering an untrained muscle." Today he argues Firefox is the last fully independent engine, most "AI browsers" are Chromium front ends, and Gecko is a cost center that buys Mozilla a seat at the standards table ([Bobby Holley](../sources/mozilla-firefox-cto-on-browser-war.md)).

## People

- [Bobby Holley](bobby-holley.md) — intern to Distinguished Engineer to CTO of Firefox
- [James Everingham](james-everingham.md) — Netscape engineering leader during the open-sourcing

## Related

- [open-source](../concepts/open-source.md) — the founding act and its mechanics
- [security-and-cryptography](../concepts/security-and-cryptography.md) — Holley's exploit-class work, the SSL-as-munition story
- [programming-languages](../concepts/programming-languages.md) — Rust's origin
- [Google](google.md), [Microsoft](microsoft.md) — the two browser-war adversaries
