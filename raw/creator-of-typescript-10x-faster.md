---
type: raw-transcript
slug: creator-of-typescript-10x-faster
title: "Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg"
guest: "Anders Hejlsberg"
date: 2026-08-17
url: https://www.developing.dev/p/creator-of-typescript-10x-faster
fetched: 2026-08-17
complete: false
capture: structured
capture_note: >
  Like episodes 56 and 57 (and unlike 58), the fetch pipeline returned a
  detailed section-by-section capture of the episode rather than a word-for-word
  transcript. All 13 published timestamped sections are covered, from the 00:48
  opening through the 01:04:58 sign-off, and three targeted follow-up passes
  (00:00-20:12, whole-page keyword sweep, and 42:57-end) were used to pull
  specific figures, names and quotes into the notes below. Quotes are short and
  attributed with approximate timestamps; the surrounding text is summary, not
  transcription. No section of the episode is missing.
coverage_note: >
  Verified NOT discussed anywhere on the page, so nothing should be attributed
  to this episode on these points: the "10x" figure of the title is never
  defined in the body (Hejlsberg quantifies only JavaScript's 2-3x penalty vs
  native and TypeScript 6 running ~50% the speed of TypeScript 1.5); TypeScript
  team size, how the Go port was kept in sync with the JavaScript codebase, and
  TypeScript 7 release plans are not covered; Hejlsberg never names the people,
  labs or CEOs making the aggressive AI predictions he pushes back on (Peterman
  is the one who raises Anthropic).
---

# Pass 1 — structured section capture (00:48 → 01:04:58)

**Title:** Creator of TypeScript: 10x Faster Typescript, Why AI Won't Replace SWEs | Anders Hejlsberg
**Guest:** Anders Hejlsberg — creator of TypeScript and C# (also Turbo Pascal, Delphi)
**Host:** Ryan Peterman
**Published:** 2026-08-17

## Host's intro (as published)
Peterman frames the conversation around the rewrite of the TypeScript compiler in Go — why Go rather than Rust, and how much LLMs were used during the port. The episode also covers Hejlsberg's views on AI's impact on software engineering: whether AI will write all code within 1–2 years, whether it replaces junior engineers, and whether IDEs go away. Peterman notes Hejlsberg's opinions diverge from "more AI-pilled companies like the labs."

## Timestamps (as published)
- 00:48 — Why write a compiler in JavaScript
- 07:29 — Why rewrite the compiler in Go
- 14:49 — LLMs for large migrations
- 20:12 — Why Javascript is so popular
- 26:32 — Why ever use Javascript on the backend
- 32:59 — What it takes to build a programming language
- 37:06 — Will there be fewer languages in 10 years
- 42:57 — Hands on engineering vs delegation
- 49:14 — Why fast tooling matters more now
- 51:16 — AI software engineering predictions
- 58:52 — The most technically challenging work
- 01:02:04 — Top book recommendation
- 01:03:50 — Advice for his younger self

---

## 00:48 — Why write a compiler in JavaScript
TypeScript's compiler was originally written in JavaScript, which is surprising because compilers are conventionally written in compiled languages. Early prototypes were in C, adapting an Internet Explorer JavaScript parser. Moving to JavaScript bought two strategic things: (1) self-hosting — the team became daily users of their own product, so issues surfaced immediately; (2) ubiquity — the compiler ran everywhere JavaScript ran, including in the browser, which native code could not do before WebAssembly existed. Hejlsberg notes V8's optimization work brought JavaScript to within 2–3x of native performance, making it viable for compute-heavy work provided the algorithms are good.

> "If you can self-host in the ecosystem that you want to be a part of, that is dramatically better than targeting from outside." (~03:00)

TypeScript's compiler is unlike a traditional compiler: it does not emit machine code, it transpiles to JavaScript and type-checks. The type checker is the unusual part — types exist purely for tooling, developer guidance, statement completion and refactoring.

> "The types have no impact whatsoever on the runtime behavior of the code." (~05:30)

## 07:29 — Why rewrite the compiler in Go
Two motivations: raw performance (the 2–3x JavaScript penalty on compute-intensive work) and, more importantly, concurrency. JavaScript is single-threaded; web workers cannot share data structures, so shared-memory concurrency across cores is unavailable. As Moore's Law shifted from faster CPUs to more cores, TypeScript was leaving that on the table.

> "Moore's Law has stopped giving us faster CPUs, it's giving us more CPUs." (~09:00)

Language selection: they decided to **port**, not rewrite, in order to preserve semantics and backward compatibility. The existing codebase assumes garbage collection and first-class functions. Go checked the critical boxes — good native code generation across platforms, GC, and strong shared-memory concurrency.

On why not Rust: Rust has no GC, and the borrow checker cannot express the circular data structures that permeate the compiler (parent pointers, recursive types, symbol references). A ground-up rewrite could have restructured around that, but at substantial extra cost.

> "We tried, and it just wasn't feasible... Go is just great." (~12:30)

## 14:49 — LLMs for large migrations
The project started roughly two years ago, when LLMs were much weaker than today. The team instead wrote a **syntactic translator** from TypeScript to Go; it produced syntactically valid but non-compiling code that then needed type-system refactoring. Hejlsberg says if they were starting today LLMs might help differently, but pointing an LLM at half a million to a million lines still leaves you needing to verify everything against hallucination.

> "If we just let AI loose on a million lines of code... you probably still have to check all of that." (~17:00)

His preferred pattern: use AI to **generate a deterministic tool** that performs the translation, rather than have AI perform the translation itself — this removes non-determinism and shrinks the validation surface. Personal anecdote: settling trip expenses with friends — asking the AI for the answer directly failed; asking it to write a spreadsheet program worked.

## 20:12 — Why Javascript is so popular
Hejlsberg defends JavaScript's design, crediting Brendan Eich's decisions made in three to four weeks. First-class functions and closures were a powerful call. The quirks (automatic conversions, `==` vs `===`) are real but a type checker manages them. TypeScript's popularity comes partly from capturing JavaScript's strengths while fencing off the bad parts.

> "TypeScript has managed to capture all the badness and park it." (~22:30)

JavaScript's genuine cross-platform ubiquity distinguishes it from Java, which never achieved universal deployment. He contrasts TypeScript's success against CoffeeScript and Dart's decline: TypeScript set out to **fix** JavaScript rather than replace it. He predicts AI strengthens incumbent languages, because training data heavily favors established ones — AI is best where it has seen the most, and teaching it a niche language costs prompt tokens.

> "AI is best at the languages it's seen the most of in its training set." (~25:00)

TypeScript became the number-one used language on GitHub last year, passing JavaScript and Python — striking for what is nominally an improvement layer over another language.

## 26:32 — Why ever use Javascript on the backend
Even with 10x gains available from native rewrites, JavaScript stays viable on the backend depending on use case: strong web frameworks shorten time-to-solution, and performance often isn't the bottleneck. Python is the same story — used for orchestrating extremely time-critical LLM training even though the intensive computation is native code underneath. TypeScript plays the same orchestration role in web servers (database calls, business logic), where inner-loop speed matters less than overall architecture.

> "Often performance of your code isn't the bottleneck." (~28:30)

Measure before optimizing. Hejlsberg notes TypeScript 6 runs only about 50% as fast as TypeScript 1.5 despite more advanced features — projects got bigger and type checking got more sophisticated. Combined with the end of CPU frequency scaling and JavaScript's concurrency ceiling, the pressure accumulated until the rewrite was justified.

## 32:59 — What it takes to build a programming language
Requires both the mechanics (parsers, scanners, code generators) and the art (design ergonomics). Every language is roughly 10% novel and 90% standard tedium. You need to know the existing languages and the paradigms — procedural, object-oriented, functional. And it requires sustained devotion: 10+ years and several versions.

> "It's really never until version three that it truly starts to get okay." (~35:30)

He admires functional programming's mathematical grounding and its influence across the field, and has pulled functional principles into TypeScript — notably immutable data structures, which let multiple threads read shared state safely without mutation races or deadlocks.

## 37:06 — Will there be fewer languages in 10 years
AI favors incumbents because of training-data prevalence. The bar for a successful new language keeps rising: you now need a compiler, tooling, language services, debuggers, profilers, frameworks and code generators across multiple platforms. Asked whether LLMs might skip the language and emit machine code directly, he argues against: a program in text form is the most compressed representation, closest to the meaning; machine code carries a lot of noise (memory addresses, register allocation) irrelevant to the logic. Like humans, AI probably works better at higher levels of abstraction.

> "Teasing the truth out of that noise is harder than having a program where the variable is called I." (~41:00)

## 42:57 — Hands on engineering vs delegation
He worked solo on Turbo Pascal, then had to learn delegation as machine capacity outgrew what one person could manage. During C# he was mostly on design while others coded — a prestigious role, but he gradually felt unfulfilled and drifted toward being an "architecture astronaut," disconnected from deep technical problems.

> "I'm just a happy coder." (~46:00)

TypeScript brought him back to hands-on compiler work and restored the fulfillment. He remains an individual contributor and does not pursue management, because coding is the core motivation. He stresses this is a personal fit question — different people thrive in different arrangements. Staying in some corner of the code lets an architect understand the implementation, propose real refactorings, and keep technical credibility.

## 49:14 — Why fast tooling matters more now
AI changes the calculus on tool speed. Agents increasingly write code in the background and make mistakes like humans do, only multiplied in volume. If type checking takes two minutes on every LLM edit, the workflow collapses.

> "If type checking takes two minutes every time the LLM writes something, that's horrible." (~50:00)

As AI performs semantic operations (refactoring across interfaces, intelligent rename), it needs compiler support via language services or CLI tools. Modern AI does semantic search rather than grep, which requires compiler analysis. That background compilation is invisible but makes speed matter more, not less.

## 51:16 — AI software engineering predictions
On "AI will write 90%+ of code within a year": he grants that AI already writes 100% of some categories of application, but questions whether it writes 90% of high-quality, never-before-written code. The claim is partly self-fulfilling, because AI's sheer volume skews the statistic.

> "High quality code that no one has ever written before, it's not clear AI will write 90% of that." (~53:00)

The TypeScript compiler itself is his example of code AI cannot write well — novel algorithms and architecture outside the training distribution. AI extrapolates well from memorized patterns and struggles with the genuinely novel.

On IDEs going away: he strongly disagrees. You have to understand the system to direct AI properly. Legal liability stays with humans — if an AI-built system causes harm, a person is responsible. Without understanding the underlying code you cannot fix issues or respond to a security breach. He is not willing to give up the oversight.

On juniors being replaced: he questions the sustainability — if juniors disappear, where do seniors come from later? He observes the pyramid narrowing at the entry level and pushing advancement upward faster. The role shifts from typing code to reviewing agent output. The craft changes rather than disappears.

> "You do more reviewing, less typing... it is but a tool and there are still programmers involved." (~57:30)

## 58:52 — The most technically challenging work
Most recently: shared-memory concurrency in the Go rewrite. Sequential reasoning is natural; running on many CPUs simultaneously over shared data structures means preventing accidental cross-modification, managing synchronization, and avoiding deadlocks and races.

> "How do you do all of this at the same time and share data structures without anyone accidentally modifying the other guy's data structure?" (~59:30)

Earlier in his career: Turbo Pascal in assembly on 8-bit machines with 64k of memory, where the team counted bytes — replacing a long jump with a short jump to an adjacent jump to save a byte, to fit in ROM. It was craftsmanship under tight constraint, like woodworking; that constraint has been replaced by effectively bottomless capacity and much higher user expectations.

## 01:02:04 — Top book recommendation
*Algorithms + Data Structures = Programs* by Niklaus Wirth (creator of Pascal, Modula-2, Oberon). Light on mathematics, rich in instructive examples, clearly explained. He learned hash tables from it: Turbo Pascal's symbol tables were originally linked lists, so search time blew up as variable counts grew; switching to hash tables made the compiler twice as fast.

> "Hash tables let you achieve basically linear lookup time and the compile went twice as fast." (~01:03:00)

Out of print for 30 years but available as a free PDF.

## 01:03:50 — Advice for his younger self
Two things. First, learn teamwork earlier — his early solo-contributor perfectionism later had to be deliberately unlearned. Second, don't accept other people's proclamations that something is impossible. When people told them Turbo Pascal couldn't exist, that reflected the limits of the speaker's understanding, not objective reality.

> "Don't let people tell you that it can't be done... that doesn't mean you couldn't possibly do it." (~01:04:30)

LAST POINT REACHED: 01:04:58 (end of transcript)

---

# Addendum — targeted follow-up passes

Three additional passes were run over specific windows to pull out figures, names
and quotes the first pass compressed away. Findings merged below, with the window
each came from.

## Pass 2 — window 00:00 to 20:12
- The host opens directly on the substance rather than with a formal guest
  introduction: Peterman frames the episode as being about "TypeScript 7 with the
  native rewrite."
- No performance multiplier for the Go port is given in this window. The only
  quantified figure is JavaScript's "2 to 3x perf penalty" versus native code.
- Microsoft is not discussed as an employer or org anywhere in this window — no
  team structure, no Microsoft Research, no C#/.NET history in the first 20
  minutes.

## Pass 3 — whole-page keyword sweep
- **"10x"** appears only in the episode title and is never defined in the body.
  On the port he says only that "we knew that the easy part was getting the
  native code."
- **Visual Studio / VS Code**: TypeScript is "deeply integrated into Visual
  Studio, Visual Studio Code, all sorts of other editors."
- **Copilot**: comes up as a matter-of-fact part of the team's own workflow —
  when something breaks, the "first thing we do is put Copilot on and see if it
  can fix it for us."
- **Turbo Pascal / Borland**: this was Borland, not Microsoft; the work was in
  Z80 assembly.
- **C#**: he created it; it comes up as a stage in his career arc (the design-only
  period), not as a language-design deep dive.
- **Delphi / .NET**: incidental mentions only, no substantive discussion.
- TypeScript team composition, keeping the Go port in sync with the JavaScript
  codebase, and TypeScript 7 release strategy are **not present** anywhere on the
  page.
- Sign-off: Peterman thanks him; Hejlsberg closes with "You're welcome. No, this
  is a lot of fun."

## Pass 4 — window 42:57 to end
- **IC vs delegation.** On why coding still wins over the senior-design role:
  "coding is like, man, that's what gets me up in the morning, make coffee and
  write some code." His generalized advice is to "do the thing that makes you the
  most happy" rather than follow the expected trajectory.
- **The 2.3M-line number.** "Visual Studio Code is like 2.3 million lines of
  code." The point is scale escalation over time: TypeScript started in 2012,
  when nobody anticipated projects of that magnitude, so the need for a native
  compiler emerged gradually as codebases exploded — the original JavaScript
  choice was not a mistake, the workload changed underneath it.
- **Semantic search vs grep.** The concrete example: if you're renaming a
  property called `version`, "you can't just grep for version" without hitting
  unrelated interfaces. His claim: "The only thing that can do semantic search is
  a compiler" — which is why agents now hammer the compiler constantly through
  LSP or a CLI, and why compiler speed is suddenly load-bearing.
- **The 90% claim.** "AI writes so much code" that the statistic becomes a "self
  fulfilling prophecy"; he doubts AI writes 90% of "super high quality code that
  no one has ever written before."
- **IDEs going away.** Dismissed flatly — "Good luck to you." The reasoning is
  accountability: "Someone has to take responsibility," and he couldn't "go to
  sleep at night" vouching for something he doesn't understand.
- **Junior engineers.** "If it does, then how do we ever get senior software
  engineers?" He expects the pyramid to narrow at the base and the work to shift
  from typing to reviewing agent output.
- **Turbo Pascal byte-counting.** The whole product — compiler, editor, runtime
  library — was "all written in Z80 assembly code." The constraint was brutal:
  "I'm 20 bytes over budget here," resolved with tricks like converting a long
  jump into a short jump to an adjacent jump to reclaim single bytes. He compares
  the craft to "woodworking almost."
- **Who he's arguing with.** He never names people, labs or CEOs. He refers to
  "people" who "take it all the way to 100%." Anthropic is named by Peterman in
  the question, not by Hejlsberg.
