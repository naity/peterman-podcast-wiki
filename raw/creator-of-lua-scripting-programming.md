---
type: raw-transcript
slug: creator-of-lua-scripting-programming
title: "Creator of Lua: Scripting, Programming Languages, Predictions | Roberto Ierusalimschy"
guest: "Roberto Ierusalimschy"
date: 2026-08-03
url: https://www.developing.dev/p/creator-of-lua-scripting-programming
fetched: 2026-08-03
complete: false
capture: structured
capture_note: >
  The fetch pipeline returned a detailed section-by-section capture of the full
  episode (all 10 timestamped sections, 00:43 through the 01:04:16 close)
  rather than a word-for-word transcript. Every section is covered and the
  guest's specific claims, examples and timestamped quotes below are as
  reported by the fetch; connective narration between quotes is condensed
  rather than verbatim. No section of the episode is missing. Two fetch passes
  were used (whole-episode pass, then a deep pass on origins / design
  decisions / AI predictions); the deep pass explicitly confirmed that Lua's
  institutional origin story (PUC-Rio, Tecgraf, co-creators, the games
  adoption path, licensing/governance) is NOT discussed anywhere in this
  interview - it is a design-philosophy conversation, not a history one. No
  adversarial prompting was used.
---

# Creator of Lua: Scripting, Programming Languages, Predictions | Roberto Ierusalimschy

**Guest:** Roberto Ierusalimschy (creator and lead designer of Lua)
**Host:** Ryan Peterman
**Publish Date:** Aug 3, 2026
**Runtime:** ~1:04:16

## Host's Intro (condensed)

Peterman frames the episode from his own experience at Instagram: Python codebases with occasional C++ bindings, and no real mental model of how the two languages actually called each other. He brought the question to the creator of the language built specifically to be embedded in other languages — Lua, which powers scripting in games including World of Warcraft and Roblox — and the conversation widens into language design philosophy generally.

## Timestamps

- 00:43 - What sets Lua apart
- 08:35 - Comparing Lua with Python
- 13:04 - Top book recommendation on language design
- 14:20 - How JIT works and why it is hard
- 23:21 - Compiling Python and interpreting C
- 30:31 - How cross language calls work
- 36:58 - Lua unique design decisions
- 51:17 - Predictions for AIs impact on languages
- 01:00:10 - Top 3 languages to learn to become a better engineer
- 01:03:21 - Advice for his younger self

## Section capture

### 00:43 — What sets Lua apart

Lua is designed to sit alongside C/C++, taking the dynamic, frequently-changing parts of a program while the resource-intensive parts stay in the compiled language. Ierusalimschy separates two labels people conflate: a *scripting* language coordinates other code; a *dynamic* language is a broader category. The distinction he cares about is **embedding vs extending** — most scripting languages do one well; Lua was built for both.

The architectural consequence is that Lua is a library first, and the `lua` command-line binary is just a client of it.

> [04:11] "Lua has a standalone program ... that program is just a client of the official client of the library."

> [04:11] "Since the beginning, Lua was written as a library."

That decision propagates into fundamentals: no shared global state (independent Lua states, so multiple instances can run in one host process, [07:14]), and `load()` rather than `eval()`, which keeps compilation and execution as separate steps ([05:31]).

### 08:35 — Comparing Lua with Python

Opposed philosophies rather than a quality ranking. Python optimizes for developer convenience and ships an extensive standard library; Lua stays minimal and expects the host application to supply the domain-specific functions.

> [10:23] "Lua does have this focus on performance ... it doesn't want to compete with C or C++."

On why Lua benchmarks faster than Python, his explanation is architectural rather than clever-optimization:

> [11:27] "Most of the virtual machine fits in your cache."

### 13:04 — Top book recommendation on language design

*JavaScript: The Good Parts* — thin next to the comprehensive references, and better for it.

> [13:37] "It discusses the language, the bad parts, and it focuses on the good parts, but then explains why it's there."

He values books written by language creators explaining their design decisions, rather than manuals.

### 14:20 — How JIT works and why it is hard

LuaJIT (Mike Pall) works unusually well because Lua is simple enough to be amenable to JIT. It is a **trace** compiler: rather than compiling functions, it records a hot execution path — including through inlined function calls — until the loop closes, then emits an optimized version specialized to the observed types.

> [16:47] "It gets recording everything that the code is doing, including function calls, et cetera, until it closes the loop."

The hard parts are machine dependence and deoptimization — when a specialized trace's assumptions fail, you have to reconstruct the interpreter's state from compiled registers:

> [18:05] "You have to translate the state that it's all compressed into register, et cetera. For instance, you don't even have a call stack because you didn't do the calls."

Pall's answer was a pseudo-assembler retargeted to several machine architectures. Standard Lua takes the other road: compile to VM bytecode, run a loop-based interpreter written in C, and get portability from the C compiler.

### 23:21 — Compiling Python and interpreting C

"Compiled" and "interpreted" describe a toolchain, not a language. You could compile Python to machine code, or interpret C — the latter would be "extremely slow" ([24:21]) but is not incoherent. The property that actually forces a compiler into the runtime is `eval`-style dynamic code generation.

Type information is what buys efficient compilation:

> [25:54] "If you know the type of A and the type of B at compile time ... you just generate the machine code to add integers."

Without it the runtime must check and possibly coerce on every operation, which is where the performance goes.

### 30:31 — How cross-language calls work

Function pointers, in both directions. When the C host initializes Lua, it registers C function pointers under names; Lua stores them in its own data structures, and when the interpreter hits a call instruction it retrieves and invokes the pointer.

> [31:28] "Lua stores that in some data structure ... when it's doing the interpretation, oh, this instruction is call."

The reverse direction works because a Lua function is itself a data structure (an array of bytecode) that C can hand back to the interpreter. Calls nest arbitrarily: Lua → C → Lua → C.

He then makes the security argument that follows from embedding. Because Lua states are isolated and can only reach C functions that were explicitly registered, the host application defines the entire attack surface — a sandbox by construction. His example: a financial company embedded Lua inside Python so users could write their own scripts against a restricted set of authorized functions, with no ability to corrupt the surrounding program state.

### 36:58 — Lua unique design decisions

The governing principle is **conceptual integrity** — that the parts cohere — which he argues is structurally hard for committees to achieve.

> [37:20] "A camel is a horse designed by a committee."

> [38:11] "If you have a committee writing a language, everyone wants to put something from themselves into the language."

He notes the asymmetry that makes this a ratchet: people fight far harder to get their feature in than anyone fights to keep features out. Small teams work because "everybody knows what everybody else is thinking" ([39:17]), and the default is refusal:

> [39:53] "When in doubt, the rule is always don't put it. If you're not very sure, don't put it. We can always add that later."

**Booleans.** Lua originally had none, following C's 0/non-zero convention. They arrived for a specific reason: tables needed to distinguish a key that is absent (nil) from a key whose value is `false` ([41:43]). Once `false` had to exist, `true` came along for symmetry — he says "true is almost useless" ([40:57]).

**1-based indexing**, the decision he is most often argued with about:

> [45:26] "Everything in the real world is 1-indexed. If you have a book, you have chapter 1, chapter 2."

> [46:03] "Everything is written before. Only in programming language there is this idea of zero."

His history: Fortran and Pascal allowed arbitrary index bases; 0-indexing won because C won, and languages copied C's syntax ([46:50]). In C, indexing is "just an illusion" over pointer arithmetic ([47:29]) — 0 is required by that implementation, not by the concept. And for the end-user programmers Lua is aimed at, "the first element is 0" is the harder thing to explain ([48:45]).

### 51:17 — Predictions for AI's impact on languages

He opens with genuine uncertainty rather than a thesis:

> [51:43] "If you go to an extreme, it's completely feasible that we won't have programming languages."

> [52:21] "I mean, I don't know what's going to happen in a few years."

But the conclusion he does commit to runs against the intuitive one — AI makes simplicity *more* valuable, not less, because the human is now mostly reading:

> [54:14] "I think it's even more important for the language to be simple, to be understandable, for you to be able to really understand that the code that you are seeing does what you think it should do."

He adds that AI does not do the maintainability reasoning a human designer does — judging whether an obscure trick needs a comment is not the kind of thinking it brings ([54:14]).

On which costs AI actually removes:

> [55:19] "Implementation is the part that AI can really help you. It's not a really important cost."

The cost that stays is the learning burden — conceptual complexity in the language and cognitive load on the reader — and that is the one his design philosophy targets.

**Career advice under this uncertainty**, asked whether to study CS at all:

> [56:43] "We have no idea what AI will do in five years ... nobody has any idea what the world, your profession, will be like in four years from now."

His answer is to pick what you actually like rather than what looks employable, on the grounds that the forecast is worthless anyway:

> [57:31] "I program because I like that."

### 01:00:10 — Top 3 languages to learn to become a better engineer

**Haskell**, for functional programming taught rigorously, and for what type inference does to the shape of the work:

> [01:00:28] "If you write a program in Haskell and in C, in C you really spend one week to make it efficient, and then you spend one year to make it correct. In Haskell, you spend one week to make it correct."

**Assembly — but a historical one**, e.g. the Intel 8080. Modern assembly is too complex to learn from; an old architecture shows you plainly what a machine does.

**Scheme**, for its "economy of ideas" — how much it accomplishes with how few concepts.

He also flags SNOBOL as historically interesting for pioneering pattern matching, and makes a general argument for reading old languages:

> [01:03:06] "Nowadays a lot of languages tend to ... be too uniform in some aspects."

### 01:03:21 — Advice for his younger self

Time. There is no compression algorithm for depth.

> [01:03:34] "To know a lot of stuff, you really have to study a lot of stuff. And it takes time."

He is dismissive of the "Learn Lua in 30 minutes" genre — you can learn the syntax that fast and will not understand the language for years.

> [01:04:07] "There is no magic there ... a lot of different things."

## Coverage note

Lua's institutional history — PUC-Rio, Tecgraf, the Petrobras origin, co-creators Waldemar Celes and Luiz Henrique de Figueiredo, the path into World of Warcraft and Roblox, and the project's licensing and governance — is not discussed anywhere in this interview. The episode is a design-philosophy and implementation conversation. Nothing about that history should be attributed to this episode.
