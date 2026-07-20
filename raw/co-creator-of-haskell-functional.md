---
type: raw-transcript
slug: co-creator-of-haskell-functional
title: "Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Peyton Jones"
guest: "Simon Peyton Jones"
date: 2026-06-08
url: https://www.developing.dev/p/co-creator-of-haskell-functional
fetched: 2026-07-19
complete: true
---

# Episode Transcript Reproduction

## Episode Information
**Title:** Co-Creator of Haskell: Functional Programming, Thinking in Types, Useless Languages | Simon Jones

**Guest:** Simon Peyton Jones

**Publish Date:** Jun 08, 2026

## Host's Intro

Simon Peyton Jones is the co-creator of Haskell (pure functional programming language) and I interviewed him about functional programming, why it matters, and his thoughts on other programming languages.

Check out the episode wherever you get your podcasts: YouTube, Spotify, Apple Podcasts.

## Timestamps

- 00:39 - What functional programming is
- 09:18 - Downsides of functional programming
- 10:53 - Specialized hardware for functional programming
- 21:47 - Haskell is useless
- 25:59 - Rust vs C
- 28:26 - Haskell vs OCaml
- 35:26 - Side effects in Haskell
- 44:26 - Type systems
- 57:30 - How the Haskell compiler works
- 01:04:35 - Why Haskell is talked about more than used
- 01:09:07 - Avoiding success at all costs
- 01:11:12 - LLMs and programming languages
- 01:13:57 - New programming language design
- 01:15:59 - Should students continue to learn programming
- 01:22:33 - Why Excel is is 2nd favorite programming language
- 01:25:04 - Advice for his younger self

## Transcript

### 00:39 — What functional programming is

**Ryan:**

I wanted to start by asking you, what is functional programming in your words? And why does it matter to people who might use the other languages, the imperative languages?

**Simon:**

Functional programming is about programming with values instead of mutation. So in a conventional imperative programming, computation proceeds by, if I want to add up the numbers between 1 and 100, I have a mutable cell containing a running total. And then as computation proceeds, I keep adding to my running total. So there's a cell that changes its value over time. Computation proceeds step by step.

There's a program counter. Now, that's very unlike mathematics. If I say three plus four times seven, you don't think of a mutable cell that changes its value over time. You think, well, three plus four is seven, seven times seven is 49. Just the answer is 49. So, in a sense, it's more declarative than imperative. Another way to think of it is it's more like what a spreadsheet does. In a spreadsheet formula, if you put in a cell, you'd say, in A1, you put the formula =A2 * A3 + 7.

Well, then that's just the formula that is evaluated. And you expect to compute the values of A2 and A3 automatically before computing A1. It wouldn't make any sense to compute A1 from the old values of A2 and A3, right? So, and there's no notion of a program counter. There's no notion of do this and then do that. It wouldn't be sensible to say equals print X plus 3, because who knows when or even whether that cell will ever that formula will ever be evaluated.

Now, the surprise is that it is possible to do useful things in such a limited language. When I learned programming, I learned it by writing machine code in which the fundamental mode of computation is registers and program counters and mutation of registers as you go along. And memory, like, computation and mutation seem to be inextricably interwoven, right? That's how computation gets done. So it was a surprise to me when I learned that, well, it is possible to do useful things with functional programs.

I still remember that amazing revelation. Now, in fact, one way to look at it is this: right back in the late 1920s, early 1930s, Alan Turing was doing a PhD in Princeton under the supervision of Alonzo Church. Now, Alan Turing, as we all know, invented the Turing machine, which is fundamentally about mutation, right? It has a little tape, and you can read things from the tape, and then you write back new things onto the tape, and it has an immutable program.

Now, Alonzo Church at the very same time, was working on something he called the lambda calculus, in which there's no mutation. The lambda calculus is like the essence of functional programming. Programs execute just by reduction. Now, so these were two different models of computation. You might ask, what can you compute with a Turing machine? And what can you compute with a lambda term? And the astonishing thing that turned out, which is completely nonobvious, is that anything you compute with a lambda term, you can compute with a Turing machine.

And anything you compute with a Turing machine, you can compute with lambda calculus. So that means that the two are identical from the point of view of their computational power. Big surprise to me. Okay, so they're equally powerful. And then the question is, which might you want to choose? As I say, I started life from my baseline of imperative programming. Of course, that's the way you write programs.

And functional programming is a kind of weird, anomalous, rather nerdy, academic thing. But I became hooked on the idea that by excluding side effects by default, i.e., imperative programming has side effects by default. By excluding side effects by default, we could make programs that are easier to write, easier to maintain, easier to reason about. And then the question is, what are the practical obstacles?

Is it slower? Is it less convenient, and so forth? So, in effect, I've devoted my research life to exploring that hypothesis. The wonderful thing about being a researcher is you can take something which, at the time back in 1980, functional programming was very nerdy, geeky, academic. But I was allowed to spend my professional life just saying, what would happen if you took that one idea, programming with values, and just ran with it?

Where would you get? And I think we got somebody somewhere pretty interesting. I don't want to say that it's better fundamentally, because after all, Haskell on that journey started with functional programming. Then we learned how to mix functional imperative programming together in a way that we might talk about later, right? So it's not really an either-or; it's more of a both-and in the end. But my position now is, as I often say, when the limestone of imperative programming has worn away, the granite of functional programming will be revealed underneath.

**Ryan:**

And why do you say that?

**Simon:**

Well, functional programming is the language of mathematics. That's how we fundamentally think about things when we want to be formal. Indeed, if we want to reason about and say, what does this imperative program do? We have to wheel out a lot of mathematics and Hoare triples and so forth. But that's all in the world of maths, which is just functional programming. Functional programming is just mathematics brought to life and made executable.

So you might wonder, I suppose you may be saying, well, isn't imperative programming just enough? And I think that there you have to just look at the broad sweep of things. I think what's happened is that from the world of functional programming, lots of ideas have got adopted into the imperative arena, right? So they grew up over here in functional programming, and then they have been adopted by the imperative programming thing.

So you might think garbage collection, you might think lambdas, you might think language integrated query, you might think about lots about type systems, polymorphism and static typing, tons of that. So at least it has been an intellectually interesting experiment that has been a very fertile laboratory in which to grow up ideas that can infect the mainstream. Now my instinct now is that we should start from functional programming and do imperative programming where necessary.

I think probably the mainstream is we should start with imperative programming and sort of add bits of functional programming where possible. And I'm not going to say that they're wrong to do that, just to say that I think it's a pretty interesting dialogue. Now you do have to think very differently about the act of programming, right? You do have to rewire your brain quite a bit. But just let me.

This is something we might want to come back to. I said easier to maintain. As programs get old. Think of a 10-year-old program, right? If you have a piece of 10-year-old code written by somebody who's long since left your company that mutates some more or less global variables, then you might be a little bit afraid about, oh, and there's other bits of code scattered about that also read or write those global variables, then you might be a little cautious about making modifications, right?

Lest, oh, if I put these two things, if I do B and then A instead of A and then B, maybe the global variable that I read somewhere deep inside the code no longer has the value that it was expected to. So reading and writing shared variables that are visible outside the scope, sort of somewhat global variables, is a form of coupling between bits of code that is very invisible, very invisible.

So functional programming forces that to become visible. It forces it into the open, and by the act of forcing it into the open, that strongly encourages a style of programming in which you don't have such interactions because they are painful to manage. So it encourages a style in which programs execute in modular boxes without interacting. Now, every imperative programmer would want to do that, but I want them to do that in a provably secure way so you can know that these programs don't interact, rather than just say I've done my best.

### 09:18 — Downsides of functional programming

**Ryan:**

Then I guess on the flip side, what are the downsides of a functional programming language?

**Simon:**

Oh, well, it can be very tiresome and inconvenient, right? So you're somewhere deep in the, you know, a subroutine of a subroutine of a subroutine of a software stack, and you want to reach out and, I don't know, grab the time of day. Oh dear, that's a side effect. But we're in a pure functional language, the time of day. And indeed there's a good reason, because everybody else higher in the stack is assuming that if I call this function, apply to, you know, seven, it will give me the same answer if I call it again, apply to seven.

But if it could interrogate the time of day, certainly it might give a different answer, right? So a simple thing as I was asking for, the time of day, invalidates a whole set of assumptions and so is not by default allowed at all. And that can be inconvenient because all you say, look guys, all I want to do is get hold of the time of day. Don't give me grief. And so every functional programming language, including Haskell, provides you with a little trapdoor.

Haskell's is called unsafePerformIO, and it says, trust me, I'm going to do something that has side effects, but you can pretend there weren't any. All right, so it's called, it is literally spelled unsafePerformIO, with a long name that has unsafe in the title, so that you, the programmer, are taking on the obligation to make sure that what you're doing is okay. Whereas in imperative language, everything you do could be unsafePerformIO-ish.

### 10:53 — Specialized hardware for functional programming

**Ryan:**

I was watching one of your lectures, and you did go over a little bit of the history of functional programming languages. And you mentioned somewhere that there was this idea of people building hardware for functional programming languages. This just made me curious because I didn't. I only know the von Neumann architecture. Do you have any idea what that might look like? And some high-level thoughts?

**Simon:**

Well, I did. I now think it's probably a bad idea. But back in 19, when was John Backus's Turing Award lecture? I think it was 1978 or thereabout. What was it called?

**Ryan:**

Can Programming Be Liberated from the von Neumann Style?

**Simon:**

That's it. Now he was saying two things. Firstly, the designer of Fortran, a quintessentially imperative language, was saying, guys, we should do functional programming. That was what the talk was about. And he introduced a language called FP for functional programming. It was a very particular, somewhat idiosyncratic functional programming language. But there it was. So that was rather amazing, right?

This was 1977. He was saying, guys, give up on imperative programming. Just do functional programming. Here's how you do it. But he also said in the same lecture, we might imagine designing new hardware to execute this new kind of language. So if you like, we've got Turing machines, they give rise to register machines and microprocessors and so forth. Maybe lambda calculus. Perhaps if we designed a machine from the ground up to do lambda calculus, it would look different.

So that was, of course, very exciting. And similar kind of thinking led to an actual commercial machine called a Lisp machine. That was a piece of hardware that was designed by Symbolics to execute Lisp programs. Lisp is a mostly functional programming language. And so, at the time, I was in my early 20s. We were thinking, oh crumbs. What would a piece of hardware look like that was primarily designed to execute functional programs?

Would it have a different kind of instruction set and architecture? So the nearest we got to it actually was, although there was a big strand of work then that was called the MIT Dataflow project. So dataflow languages, functional languages, they're definitely the same kind of category, right? And so MIT had this great group led by Arvind called the MIT Dataflow Group. And they designed, in the end, a machine called Monsoon that was specifically designed to execute dataflow programs, that is, functional programs.

It was based on a token store and matching, and tokens flowing around and getting matched up and executing. You might imagine data flowing, going through a graph, when 3 arrives at a plus node and 4 arrives at the other input of the plus node. Bam. You could fire that plus node, right? And the hardware did all of that. At a similar kind of time in England, my colleagues Thomas Clark, Joe Stoy, and others built something called the SKI machine, SKIM.

There's a paper about this in the FPCA conference. And SKIM was designed to execute SK combinators. So at the time, David Turner's written a lovely paper in which he described how to take lambda calculus programs and translate them into SK combinators. So you can read about that in my book. It's a very simple translation. You can give the whole translation in half a dozen lines, but then you have this mess of S's and K's, and S and K reduction is very, very easy.

So it's like the machine code of functional programs.

**Ryan:**

What is a SK combinator? Just for context, there are three combinators,

**Simon:**

S, K, and I, and they have simple reduction rules. Here they are: I of X equals X, KXY equals X, S X, Y, Z is X of Z applied to Y of Z. End of story. That's all so very simple, right? So now all I've got to do is take my lambda, translate it into a giant tree of SK combinators, right? S applied to K applied to I of 3 and S of Z of just a huge tree of S's and K's, right? Now simply apply the rewrite rules I gave you, and that is program execution.

It's rather astonishing that that can execute arbitrarily complicated programs, but it can. Don't you think that's rather amazing? Now, I can take an arbitrary Haskell program and could translate it into lambda terms, and I could translate those lambda terms into S and K. Very simple transformation. And I can just write those, run those three rules, and it'll produce the output of the Haskell program.

That's pretty amazing. And indeed, there is an implementation of Haskell that uses exactly this. It's called MicroHs, and my colleague Lennart Augustsson has built it. And its execution mechanism is SK combinator reduction. And if you sit in MicroHs, you can ask it to show you the S's and K's that it produces. If we had a shared screen, I could probably show you. So, long story short, then the SKI machine was designed to take SK trees, big trees of S's and K combinators, and just execute them directly.

So it was built in hardware and it ran perfectly well, reasonably fast. Now, why didn't this catch on? Why don't we have functional programming machines? I mean, at the time it was a big idea. We even had a conference called Functional Programming and Computer Architecture. FPCA was right there in the title of the conference. But slowly we became aware that what was really happening is we were doing at runtime what we could do instead at compile time.

And that is always a bad idea. Imagine an interpreter for, I don't know, Pascal or something, or for Java. We can compile Java to bytecode and we could interpret the bytecode, right? So then we're doing something at runtime. At runtime, the interpreter is looking at the bytecode, saying, dispatching to say which instruction, blah, blah, blah, right? Now what does JIT do? It takes a sequence of bytecode and says, oh no, no, I'm going to take that sequence of bytecode and compile it to a sequence of machine instructions that, when executed, will do the same thing much faster because it can take advantage of bytecode sequences, for example, to say if you swap and then swap, it's a no-op or something like that.

So what, in fact, it turned out is this whole SKI business, and any other, and indeed dataflow machines also were simply doing at runtime what you could do better at compile time. We were building an interpreter in hardware. So don't build the interpreter in hardware. Instead, build a compiler that translates your lambda term into a sequence of machine instructions that, when executed, will behave as if you had done this reduction business.

And then you might think, well, machine instructions for what machine? Well, from a practical point of view, it was very hard to compete with Intel, right? They were just spending bazillions of man years on making x86 go faster, and Arm likewise. So we can leverage all of that work by compiling into their instruction set. But even if you say you are God, you are the chief executive in Intel and can tell them to add new instructions or computation mechanisms to support functional programming.

What would you add? Not very much. Little bits to do with garbage collection, barriers, I think, and such like, but nothing major. So, in other words, I think the whole build hardware to execute functional programming directly thing turned out to be a mistake. Inspiring mistake, fun mistake. I had a great time. But a mistake. It's better to build a compiler.

**Ryan:**

I would have thought there might be some unique opportunities for parallelism given the immutability in these functional programming languages. So yeah, you described that graph or that SK combinator graph. I imagine you could execute that all in parallel, assuming there's no connections across the graph.

**Simon:**

And indeed, that was the dataflow machine. The MIT Dataflow machine was all based on that idea. So you throw the whole graph into the token store and just run all the nodes that are runnable.

But that's incredibly fine grained. You've got to imagine this big tree of a million nodes, and your processor is sort of wandering around over it, doing little things in parallel. There's a lot of memory traffic going on there. And if these little threads are operating on the same bit of tree, then there's synchronization costs. So very, very fine grained parallel computation like this turns out to be impractical, or not impractical.

You could do it, but it's very slow. So the dataflow people, their history, if you look at the history of the MIT Dataflow project, they started with micro parallelism. Every individual instruction was a separate parallel computation that might take place, and the token store would match it up. And then they built more and more compiler technology that grouped these things together into larger units.

So they expanded from micro threads of single instruction threads into 10 instruction threads or 100 instruction threads. Right. But even that never really caught on. So you're right though, that if I say in a Haskell program E1 plus E2, then I can do E1 and E2 in parallel. And GHC does support you in doing that. But nowadays, rather than expecting the compiler to do that automatically for every subexpression, you can spark a computation. You say E1 par E2, and that says do E1 and E2 in parallel.

There's a project at Carnegie Mellon for a strict power, a strict language called ML that has a very good variant of Parallel ML going in a similar way. So essentially, we've moved away from the dream of automatically getting parallel, very, very fine grain to the programmer. We give the programmer clues about where it's a good idea to do parallelism, and still the compiler will try not to fork two tiny grains.

### 21:47 — Haskell is useless

**Ryan:**

I was searching on YouTube and I searched your name, and this video came up. It said, "Haskell is useless." Simon Peyton Jones, and it's a video from a long time ago, and someone's got a low-quality handheld camera. There's a group of researchers that are all talking. Butler Lampson is across the table. And it's a fun little video. And in the video you lay out this two-dimensional graph where on one dimension there is the useful versus useless axis, and then on the other dimension there is the safe versus dangerous.

And then you're placing programming languages on this two-dimensional graph. And I think you started by putting C as very useful, but it's incredibly dangerous. And then you put Haskell on the polar opposite side. You said it's useless, but it's very safe. What are the least safe and most useful languages? And why do you place them there? C, for instance.

**Simon:**

Well, yeah, so let's see. In C, you program by mutation. So it's unsafe in the sense that any function can mutate any variable at any time. It has a lot. You pass pointers around a lot, and functions mutate the memory pointed to by those pointers. And moreover, typically they can mutate it anywhere. There's no array bounds checks or anything. So it's kind of like super unsafe. And in fact, and this is demonstrated by the fact, can you imagine all of these exploits that we get every day, right, that Mythos is discovering in huge numbers?

But why is the Internet so insecure? Primarily because all of our software infrastructure is written in unsafe languages. If we'd written all of our Internet software and operating systems in Haskell or maybe in OCaml or ML, 99% of all these exploits would be removed by construction. It's like we've built a boat out of paperclips and we're surprised that it's leaky.

I mean, you shouldn't build boats out of paperclips, right, because they have holes in them. You should build it out of a secure substance, right? But then it's too late. So we spend incredible amounts of human ingenuity and effort patching the holes in our boat built of paperclips. It's tragic. It's tragic how much effort and ingenuity and money has been lost and waste of resources just because we wrote our computational infrastructure for the world in an insecure language.

That's what I mean by unsafe.

**Ryan:**

I mean, are there not vulnerabilities? If I wrote something in Haskell, there's gotta be some new type of.

**Simon:**

Of course there are vulnerabilities. I just said 99%, I didn't say 100. If I write a Haskell program that says receive message, if the message says tell me everything, then spit out my entire database in reply, no language can stop you doing that, right? But if you look at the program and it doesn't have any such things, right? So, I mean, nothing can prevent you against high-level attacks to insecure programs.

Or, I mean, another example might be deadlock, right? Services, no matter how securely written. If A waits for B and B waits for A, deadlock. Sorry, no. And no language is going to stop you doing that. You might hope for some high-level verification tools, but it's like surely if you're trying to do something hard, like prove that that doesn't happen, you want to have a foundation that is, you know, in which you've got some bedrock to stand on.

If you're standing on sand and trying to prove some advanced property, it's very, very difficult. But good point. I'm not talking about 100% security. Absolutely not. But how many exploits are based on buffer overruns or pointer manipulation that's gone wrong? If you couldn't have a buffer overrun, you couldn't do pointer manipulation gone wrong. Those bars just wouldn't exist.

### 25:59 — Rust vs C

**Ryan:**

So, I mean, C's maybe half a century old now. What about more modern versions of those lower-level languages like Rust?

**Simon:**

Much, much better. Much, much, much better. Right. If we rewrote all of our software infrastructure in Rust, things would be way, way better. I'm not actually even sure whether Rust has array bounds checks built in, but suppose. But it must have the ability to promise that you're not indexing out of bounds. I don't quite know quite now, but if you compile all your code with that switched on, you are in a way better situation, way better.

So yes, this is not just functional programming. But you did ask about why I thought C was an insecure, unsafe language.

**Ryan:**

If we imagine that graph, there's the upper right quadrant, which is useful and safe, and you described that as nirvana in the video. And I guess maybe over time, I mean, C is somewhat really unsafe, really useful, yes.

**Simon:**

So C, Rust has moved along the axis from useful but very unsafe to stay useful and become safer. Now, Haskell started life as being very safe but useless. So it's worth just rehearsing that because in the first version of Haskell there was no I/O. The only Haskell program was a function of type string to string. It's functional programming, after all; it could do I/O. All it could do was take a string and produce a string.

So obviously that's not very useful. It's a little bit more useful. A language that is very, very safe and completely useless is no-op, that does nothing ever, very safe, but very useful. Haskell was a bit better, right? At least it lets you apply a function to a string and get back another string. So, of course, we then worked on how could we do I/O in Haskell in a safe way that will lead to monads and stuff, but just as the, you know, we're moving from C horizontally to go safer and safer, but staying useful.

So from Haskell, we're moving sort of vertically to get more and more useful without stopping being safe. And nirvana is when we sort of meet up, right? But the point is not to say one is better than the other, but just to say that we both seek things that are useful and safe.

### 28:26 — Haskell vs OCaml

**Ryan:**

When I think of functional languages, I guess in the mainstream, or what people are kind of thinking about, I hear Haskell. I also hear OCaml. How do these two programming languages compare if someone was trying to pick a functional language to work with?

**Simon:**

So OCaml is a strict language that is called by value. So when you say F applied to 3, 4, it'll add 3 plus 4 and then call F to get 7, right? In Haskell, if you say F of 3, 4, it'll build a little suspension that says, well, if you ever need this three, four, you can evaluate it, but maybe you'll never need it. And then it calls F. That's a lazy language. So because OCaml is strict, it has a defined order of evaluation.

So if you say F of 3, 4 and a second parameter, 8, 9, it'll evaluate 3 plus 4 and then 8 plus 9 in that order. So it makes sense to say you can say F of print hello, print goodbye, right? Because you get hello and then goodbye printed. So once you have a defined order of evaluation, then it's pretty easy to incorporate I/O, right? Even though it's, quote, a functional language, OCaml allows you to do I/O without saying unsafePerformIO or anything.

In fact, it has a defined order of evaluation, and it's perfectly kosher to do that as a sort of unintended consequence of being called by value. It was also, by default, impure. Now, good OCaml programmers won't use many side effects, but OCaml doesn't prevent you. Haskell prevents you. Why does it prevent you? Because if we'd allowed you to say F of print hello, comma, print goodbye, those would be thunks, right?

Not yet evaluated. Right. So if F happened to evaluate its first argument and then its second, we'd print hello and then goodbye. If it evaluated its second and then its first, we'd print goodbye and then hello. If it didn't evaluate either, we wouldn't print either of them. That doesn't sound very good if you want to control what I/O is happening. Laziness forced Haskell to stay pure. Strictness allowed OCaml, which grew out of the ML tradition, by the way.

ML is another functional language that predated Haskell. It was always strict, and it always had I/O by default. It wasn't a goal. But that's just the way it worked out at the time. Nobody thought about it. It was just obvious.

So that's a big difference between OCaml and Haskell, right? Is that now, then, since then, they've both grown up. Haskell's gained sort of monads. OCaml's gained lots of fancy type systems.

Some of them look at how Haskell and OCaml have learned from each other. OCaml has got an interesting effect system recently and a whole lot of new extensions. It's an absolute hotbed of innovation at the moment. OCaml. So I view OCaml and Haskell as kind of siblings. Brothers and sisters, right? We love each other, we learn from each other, we compete with each other, all of the things that siblings do, but they're not the same, right?

So siblings don't say, I'm just better than you. You shouldn't exist. We say, let's enjoy our life together. And that's what it is. That's the way it is.

**Ryan:**

You describe the laziness and the strict. And as a programmer, my initial thought is I would like to control the order of execution, and when I say print X and then print Y, I want it to happen that order. Otherwise it would be a little unintuitive. What is the main benefit of laziness?

**Simon:**

Why is laziness good? Well, John Hughes did this rather well way back, in 1980-something. He wrote a paper called Why Functional Programming Matters. And one of its main theses was that lazy evaluation lets you compose programs in a particularly modular way. So imagine a program that is, I mean, his classic example is a program that plays chess, right? So one thing you could do is you could imagine building a tree of all possible moves, starting from the position we're at.

It would be a very, very big tree. It would be too big, because first of all I compute the tree and then I'd start deciding what move to do. It couldn't possibly do that because the tree of all possible moves has more nodes in it than the number of protons in the universe. So let's not do that. Now, if instead you could build the tree, having got this tree, supposing you had it, you could then walk over the tree saying, ah, let me do some minimaxing, and seeing, oh, this looks like a good position.

Let me go this way. I could explore the tree right now, then. So in OCaml, then you would have to put the tree generation and the tree exploration in one function, right? In Haskell, with lazy evaluation, you can generate an infinite tree, and then the explorer that prunes the tree and explores just the bits of it that are necessary is completely modularly separated. I can build a different generator and a different pruner.

They're just completely separate programs. So lazy evaluation is very powerful glue that lets you glue together two programs that you'd like to be distinct. Strict evaluation forces you to merge them together.

**Ryan:**

Yeah, this reminds me, so in Python, for instance, they have the idea of a generator where you could lazily retrieve things.

**Simon:**

Every strict language, every serious strict language has lazy evaluation in it. They're called iterators or generators, and so does OCaml. All right, but in Haskell, that's the default. Now instead, in Haskell, so this is a bit like, again, the two are converging on the middle, right? Haskell, lazy by default. But you can make things strict. You can put in exclamation marks to say, please evaluate this before the call, right?

Or the IO monad to say value. But that's a more brutal strict annotation. So in Haskell, you can make things stricter. In OCaml, you can make things lazier. So it really boils down to what's the default? We both want to have a mixture of the two. And then it becomes a bit cultural. As to which you prefer, I don't know. Some people sometimes ask me. They say, well, well, if you were designing Haskell again, would you make it strict by default with really good support for laziness?

And I often say, well, I might. Yeah, that does seem attractive because frequently I found myself cursing laziness as an implementer. But I strongly suspect that 10 years after that I'd be thinking, man, if only it was lazy by default. Oh, when I said strict by default, I would definitely mean strict, but pure, right, no side effects.

### 35:26 — Side effects in Haskell

**Ryan:**

A few times in our conversation, you've mentioned the word monad, and it seems like it allows us to do the side effects. And what is a monad? And how does it help us do side effects and preserve ordering?

**Simon:**

One way to think about it that's very easy to understand and use is just to imagine that the do notation is somehow built into Haskell. So you can say do print x, semicolon, print y, and that has type IO unit. So a value of type IO unit means I do some input output and return a value of type unit. An expression of type IO int is an expression that when you run it will do some I/O and return an int. Okay, so do lets you combine I/O-performing computations together.

So print 3 has type IO unit. It does some I/O, namely printing 3. GetChar has type IO Char. It does some I/O, namely reading a character from standard input and returns a character. All right? Notice that's different from just Char. So quotes x quote has type Char. It's just the character pure, right? GetChar, the I/O-performing operation, has type IO Char. It does some input output and returns a character.

Okay, the do notation lets you combine together I/O performing computations. So if you could say do and then you say x left arrow getchar; putchar x, then that x left arrow getchar says run the getchar computation and get me the character. Call it x. The putchar x says run the putchar computation to put x, and we combine them together with the do notation that combines two computations to make one I/O performing computation.

But these things are completely first class. That's what's new about monads compared to just make it into C. x left arrow, getchar semicolon, putchar x. That's a computation whose type is I/O unit. Let me give it a name, so I can say let foo. We type I/O unit equals that do. Now I can pass foo as an argument to something. I could put foo in a data structure. I could return foo as a result; it's a value just as much as three or plus in particular.

For example, I could say do foo, foo that takes foo, uses it twice each time. Do foo; semicolon, foo says do foo and then do foo again, right? So I'll read a character and print it, and then read a character and print it again. So these values of type I/O for some type T are first class values, right? In C, I can't take X colon equals 3 semicolon, you know, Y plus 4 and pass that as an argument to something and expect it to happen wherever it's used, right?

It's not a first-class value.

**Ryan:**

When I first was learning this monad idea, it seems like you've said in a few places it's a way to do the side effects, but keeps the language pure. But when I saw it, my first thought was it's almost like this little place where we segregate the dirty things we want to do. But then how does that keep the language pure?

**Simon:**

Oh, because. Because we are lying. But look, if your function has type int to int, can it do any I/O? No, no. If it has type int to I/O int, it could do arbitrary I/O. So yes, so it's nice. Pure int to int function or dirty int to int function. So you may say, perhaps you're about to say, that's a bit of a blunt instrument. Either completely pure or completely dirty. Right. It gets you an awfully long way.

But nevertheless, it would be cool if you could say, oh, I am effectful, doing reading of files only. Right. So, in the type, you'd like to say, what kind of effects can it have? Can it throw exceptions? Can it spawn new threads? So you'd like to enumerate the effects this computation could have. Right. That would be cool. That's called an effect system. And there's a bazillion programming language papers about effect systems.

And it turns out that you can indeed, in the type system of Haskell, and indeed OCaml is rapidly becoming the same. You can express not just all or nothing, does it do I/O, game over, but rather which particular effects does it do, including no effects at all? That's pure. Right. A good place to start is a library called Bluefin, which my colleague Tom Ellis has designed. It's a very nice take on how to do effect systems in Haskell.

**Ryan:**

I guess the purity comes from that. This dirty stuff is signaled through the type system.

**Simon:**

Correct?

**Ryan:**

Okay, so we can do it. But here it is. And be aware.

**Simon:**

Yeah, and because you have to thread, you know, because the type system gets in your face, you were trying to map, say, no, map says I apply a function to every element of the list. Well, so it has type A to B to list of A to list of B. If you want to apply an I/O performing function, so the function you're applying has type like int to I/O of character, you could map that over a list, but you just get a list of I/O of chars that hasn't done any I/O yet.

Right. You want something that says, take a list of IO chars and perform those actions one at a time. So I want a function that goes from type list of IO char to IO of list, and you might want to perform all those actions top to bottom, or maybe bottom to top, who knows? That's what this function of type. Yes. So you could do it in various ways. So sometimes it gets in the way. Right. You say, oh, shit, can't I just use Map?

Well, in Haskell, no, sorry, you're going to have to do a little bit more work to tell me in what sequence you want your effects to happen. Because by default, Haskell does not specify sequence. So, adding monads to control effects does get in your face a bit. And that's the tax we pay. In effect, that's part of the big experiment that Haskell is doing: to say, suppose we upfront say we're willing to pay that tax.

How many followers can we get? And the more. But I will note that monads have infected quite a lot of other languages. Like F# is definitely a call-by-value impure language. And yet F# had these workflows that were definitely monad. And monads have appeared in Scala and in many other languages. So something that's very monad-like has appeared lots elsewhere. It's been a very unifying concept.

### 44:26 — Type systems

**Ryan:**

And so I kind of want to ask you, maybe just even on the highest level, what is a type system, in your words?

**Simon:**

Okay, so what does a type system do? It lets you reject silly programs upfront. So if I have a function that adds one to things and I apply it to a character or to an I/O computation, that's going to fail at runtime, right? Because I can't add one to a character. Or maybe you overload plus. Maybe I reverse a list or something. If I've got a list reverse function, and I give it something that just isn't a list, then it's a bit silly to allow that and only fail at runtime.

So fundamentally, type systems are about rejecting at compile time programs that you do not want to run because they will fail at runtime. Okay, now, we've had static type systems for a long time, going back to Pascal and earlier. But simple type systems are annoying because they get in the way. Imagine a function that reverses a list. In Pascal, you could write a function that reverses a list of integers.

But if you wanted to reverse a list of characters, sorry, you can't. That function that reverses a list of integers, it has type list event to list event, so you can't apply it to a list of characters. Game over. You have to write another copy of the code with a different type. That's a bit annoying. So what are we going to do? We need polymorphism. We need a more powerful type system. We want to give reverse the type for all a list of A to list of A.

So that upfront says, I work for any type A. You give me a list of integers. Fine, I'll produce a list of integers. You give me a list of characters. Fine, I'll produce a list of characters. Notice that's much better than just list to list. I want to keep the fact there's a list of integers so I know if I apply, when I look inside the list, I know I've got an integer. But also if I just list the list, I might get back a list of some completely different type.

But I know that reverse returns a list with the same type of things, right? So parametric polymorphism, super valuable, right? If you want a size of type system, it must have parametric polymorphism. The message is, if your type system is too simple, it gets in the way. Very important lesson, because it means that we cannot really say a type system is useful or not unless we say which one, because we know that weak type systems are very inconvenient.

It must at least have parametric polymorphism. And that is another idea that was born in the world of functional programming. It was born in ML, incidentally, Robin Milner's famous dictum: well-typed programs don't go wrong. ML was the first, I think, the first parametrically polymorphic functional programming language. But generics in Java and object-oriented programming more generally is exactly the same idea, right?

**Ryan:**

into the mainstream and you mentioned polymorphism, and so there's this parametric polymorphism in the type system. But in the example you mentioned where maybe you want to do an operation on a list and then the type of the input changes, I was just thinking, what about when people do polymorphism in the classes?

**Simon:**

Yeah, okay, but so now you're into a whole more complicated world, right? So as soon as you say class, you're talking static type system again, right? So object-oriented programming is another approach to polymorphism. So in an object-oriented language, we say if we have a Ford that is a car and a car is a vehicle, then anything that works on vehicles should also work on cars and should also work on Fords.

So the code that we write for cars works unchanged for vehicles and for Fords. Okay? Now that's a form of polymorphism, not parametric polymorphism. That's what you might call object-oriented polymorphism or subtype polymorphism. Okay, so now we have polymorphism in the sense that the same code, the same executable code, actually the same machine instructions work on values of different types. Okay. In both cases, both reversal lists, same machine instructions.

Code that works on vehicles works on things on Ford. Same machine instructions, right. Okay. That's what polymorphism in general means. Parametric polymorphism means this for all. A list of a to list of a stuff. Subtype polymorphism means if it works on vehicles, it works on any subtype of vehicles. Okay? Now the interaction of the two, which you get by adding generics to an object-oriented language, is pretty complicated.

Oh, and by the way, adding side effects as well. And so your question involving classes and superclasses and so forth is smack in that complicated world. I'm not sure it'll be very fruitful for us to get a lot more details of the type system sorted out to know what to say. But at this very high-level overview, the big point I'm trying to make is weak type systems get in the way.

Type systems are meant to reject programs that will go wrong. But my function that reverses a list of integers, it will also reverse the list of characters. So it's tiresome to be told, no, that is a bad program. I want to be able to write that it has type, for all a, list of a to list of a. So the idea of making the type system more complicated is to say programs that you want to run, you can still write in your static type system.

Now you might say, well, blimey, if that's all, why don't we just get rid of the static type system altogether? Now we could run all of those programs, but the trouble is, you can run too many programs now. You can run programs that will crash at runtime, and that's very, very, very bad. And we all know the costs of programs that crash in deployment, that you could have crashed before you even started to run them, before you even ran your first test, right before you even linked it into an executable.

That's really good. But the biggest benefit of a static type system, in my humble opinion, is maintainability. If you have a program written in, I don't know, Perl or Ruby or Lisp in its basic form, and it was written 15 years ago and the original author has left, and all of the people who were involved at the time it was written have left, then that program is very difficult to maintain, and it becomes almost immutable.

Nobody dares change it anymore. What they do is, it's an immutable piece of software, and you do stuff around the edges to impedance match what you really want to do to this now immutable blob. Now of course you have lots of tests, so test-driven development, I'm totally with it, I'll develop all of that. But still, GHC, for example, is itself written in Haskell. It's 35 years old, and yet I do large-scale systematic refactorings of it fearlessly because the type system keeps me safe.

In fact, often what I'll do is I'll change a few types and then start compiling, and then a sort of wave of changes propagate through, forced by—I just get type errors. So I know what to do. The thought was that I've changed the representation of this data structure a little bit. I've added a field to this data structure. Where in the entire compiler might that field be read, written, or freshly allocated?

I can't imagine how anybody maintains 30-year-old software and makes large-scale changes like that. Without a type system, it's unimaginable. So for me, the benefit of type systems is maintainability. Oh, and designability. Right. So I often write the types of my programs up front. The data types are super perspicuous. Novices say it's a bit like writing the classes of an object-oriented language, right?

But if you have no types, no classes, nothing, just I don't know, S expressions, types are my design language. They're the way that I start writing my designs.

**Ryan:**

I'm trying to understand the other mindset. Let's say C, for instance. I remember a lot of stuff when I was learning it in college, for instance, many times, right. I'd add a character to a pointer or something, and it just works because it interprets the character as a number. So is there any value to having that kind of type system, or is that just strictly unredeemable?

**Simon:**

Just use stronger, I think there's no benefit to weaker.

**Ryan:**

Just off the top of my head, one thing I think of is there is a set of programs that will work but don't satisfy the type system.

**Simon:**

Oh, yeah, that's why.

**Ryan:**

But those are. I mean, I don't know if they're good. That's subjective.

**Simon:**

Oh, no, they may be good. So we started, if you have Pascal and you write a function to reverse a list of integers, then if you apply it to a list of characters, the same machine instructions would work, but it is rejected, right? So we have rejected a perfectly decent program. Bad. Right. Our goal is to expand the collection of programs that satisfy the type system to include as many as possible of the programs we want to run without including any of the bad programs that we don't want to run.

Okay? Parametric polymorphism is a big step in that direction. Other type system innovations are a big step in that direction. But there will always be some programs that would run perfectly well that the type system rejects. Imagine a tree that contains integers at every node. But if you are 17 deep in the tree, or 34 or 51, if you're in a multiple of 17 deep, the integers can be characters instead, or the integers all turn out to be characters, right?

Now, you could write a program that generated such trees, and you could write a program that consumed such trees, knowing that every 17th layer we switched characters. But most static type systems would make it pretty hard for you to accept that program. And yet it will run. Now you might say, "Oh, but I really want to write that program, guys. Don't get in my way." Well, then we should provide a way for you to bail out into dynamic typing, right?

What I'd like to do is say, okay, so if all else fails, then at least you can, as it were, pair up a value with its type representation. There's one reason we don't want to interpret an integer as a double precision float, for example, is that they don't even have the same representation, which is just nonsense. One possible way untyped languages let you do this is to tag every integer and every double precision float.

With the fact I'm an integer, I'm a double precision float. But that has a lot of overhead. So one merit, I think it's not the biggest single merit, but it's a major merit of static type systems is you have no tags. You know that if it says it's an integer, it's going to be an integer. You know that if it's a double precision float, it's going to be a double precision float, right? But if you're not sure, maybe we could make a way to make a pair of a type representation.

And this value, the type representation, is now like a runtime tag. It's like a little runtime data structure that describes the type. And then in your program you could say, now I want to say, oh, I've got this type dynamic. We'll call this pair a value of type dynamic. Now when I want to take a value of type dynamic and treat it as a character, I want to say, ah, look, look at the type dynamic.

See if it says it's a character. If it is, return the character. If not, crash.

**Ryan:**

Right?

**Simon:**

Runtime failure. That's fine, you can do that. So Haskell has good support for dynamic typing where necessary. So my story would be static typing should expand to carry as much as possible, and where you absolutely cannot do it, sorry, then use dynamic typing. And we provide facilities to support that.

### 57:30 — How the Haskell compiler works

**Ryan:**

One thing I wanted to talk with you about is the compiler. How does GHC work on a high level?

**Simon:**

So GHC takes a string like any other compiler. The source code of the program parses it, and then it type-checks, it figures out, is this a type-correct program? Then it converts it to lambda calculus. Now Haskell, the Haskell AST, the original source tree, has 50 different data types, 50 different kinds of nodes, some of which have 30 or 40 different variants. So it's a really big, diverse, complicated data structure.

The AST lambda calculus has this variant of the lambda calculus. It has eight WANDA data, maybe two or three data with eight constructors. So it's like taking a gigantic language and squeezing it down into a tiny one. And that tiny one we can then optimize, right? That's what the optimizer works on. So the front end does parse, rename, type check, desugar into lambda calculus. That's the front end. The lambda calculus particular language is called GHC Core language.

I'm quite proud of it because it's been very, very stable. It's 35 years old, and it has barely changed since birth. That's amazing, right? Because Haskell has changed a lot. A lot. So almost all of the innovation in Haskell has been in the front end. Very little in core. Now the back end, the core optimizer, has changed a lot too. But all of the changes that were useful there would have been useful 30 years ago.

Right. So they're two completely separable things. So I'm quite proud about that. Core then. We do a lot of core-to-core passes that simply take core programs. We'll use core programs, lots and lots, long pipeline. Then we convert it to C, which is a prototypical imperative language. Think of it as a portable assembly code. So that bit is meant to be platform independent. So it's simply. That's the compiler that takes.

Remember I said if you take lambda calculus and compile it, that's that step. Right. I want to compile the lambda calculus into machine instructions, really. But I don't really mean machine, I mean portable machine instructions. That's called C. Then I want to convert C into actual machine instructions for various platforms. And there we could either do that directly with the native code backend or go via LLVM.

**Ryan:**

Interesting. I've never heard of C. Why not just go directly to it? I would have thought maybe assembly or something like that.

**Simon:**

Well, because. What happens in assembly? In which processor? Please?

**Ryan:**

Oh, I see. I guess it's the. I would have thought the lambda calculus part was already portable.

**Simon:**

So you just. It is, yeah. You could go straight, but, but, but. So there's work to go from lambda calculus. You could go all the way to x86, then throw all that away and now go from lambda calculus to PowerPC. Oh dear. I've just duplicated a lot of work by going from lambda calculus to C-- and then from C-- to x86, x C--. We've avoided duplicating the work that went from lambda calculus to C--.

When you see that, it's pretty obvious, isn't it? You got to. You want to make the platform-specific bit as small as possible. You would like to have, as it were, a generic architecture, one that can do addition and has a program counter and a stack and so forth. That's all C--. It's just a portable assembly language. And then you say, oh, the nitty-gritty of whether you have double-precision add and set, the floating-point bit here and there, that.

Well, that's platform specific. The core is itself statically typed, but in some ways it's surprising because no other compiler has this property. No other production compiler by core is statically typed. I don't just mean that the initial program was type correct. I mean that a core program, you could run a type checker on that. I might say, why do you need to? Because after all, if GHC is correct, it started with a type correct core program because it came from a type correct Haskell program.

Assuming the desugaring was right, and all the optimizations, if they're right, will generate a type-correct Core program. So why do you need to type check Core to discover bugs in GHC? Now, these are serious bugs, right? If you ever take a type-correct Core program and an optimization pass produces a type-incorrect Core program, what will happen if we don't have the type checker for Core? We'll generate machine code, and we'll run it, and we'll get a segfault.

Now we have to backtrack from a particular test program that now crashes all the way back up the pipeline. Up the pipeline, up the pipeline, up the pipeline. Oh, it was this pass of GHC that was faulty. That's super hard to do because you're getting out GDB on some runtime failure. That is an indirect and perhaps distant consequence of the fact you just generated a type. You just made a.

You had a bug in the optimizer. So it is amazing to have a type checker for Core. Now, why does nobody else do this? Well, it's because their intermediate language, typically, and this I really am talking typically, because I know of no other compiler that has this property, none. Production compiler, typically. Then they're complex syntax trees decorated with all sorts of pragma information and things hanging onto it here and there.

There's no type checker for it at all, and there's no hope of one. So I'm very proud of the fact that Core is statically typed. And I also think it's a. The most delightful thing is that the way that it is statically typed, it is an implementation of something called System F. So System F, when I said lambda calculus, lambda calculus, as Alonzo Church had, it was untyped, had no type system at all.

But Girard defines something called System F, which is a statically typed lambda calculus, a rather powerful one. And GHC Core is essentially System F. So he literally adopted something from the nerdy theoretical computer science, logic community, logic of mathematics community, and adopted it directly in a production implementation. So I'm very proud of that. I think GHC Core is. And the fact that we can do we have 35 years worth of development that has not just not been impeded, but actively aided by statically typed intermediate language is really a big marker in the ground.

### 01:04:35 — Why Haskell is talked about more than used

**Ryan:**

Watching all your talks, reading everything, one of the interesting data points that you brought up was that Haskell is talked about more than used. When you compared Stack Overflow volume and actually GitHub volume, like who's actually using the programming language, why do you think that is?

**Simon:**

So Haskell embodies one key idea: immutability changes everything. There's a quote from Pat Helland's talk that I think you also looked at or read. So it says programming with values changes everything about the way you think about programming. It's just mind changing. It's not necessarily better, but it is different. And so Haskell takes that idea and runs with it. Everything is driven by that one idea.

Everything else is incidental. In the early days, that meant we just said, well, guys, suck it up. We'll keep changing the language, and if it breaks your program, too bad. So it is a bit peculiar and therefore also it felt a bit academic because initially it was really not very powerful. It was taking the key idea, but you couldn't do very much with it. We talked about that. Right.

So over time, GHC and Haskell in general has become more and more powerful. The type system has become less and less in your way and more and more useful. All the obstacles that make functional programming harder become better. The compiler generates faster code, it can browse faster and so forth. So it has become less peculiar. So we've become more and more taking into account the needs of our users.

But in a way, the sort of cultural heritage is we never give up on the one core principle. We're just not going to give you unrestricted side effects. Sorry, you want to say unsafePerformIO and put up with the consequences. So we're going to stick to one core principle and then we'll do lots of work around the edge to make that better. Right. So that does limit our community somewhat. Right?

It does mean you really have to think in a different way. Immutability changes everything. That means you'd have to think a different way about programming. Maybe you don't want to think in a different way. That's fine. Then don't use Haskell.

So in a way, we started from a very small user community, a very sort of pure and nerdy one, and growing larger and larger. But all slowly, slowly, while all the time maintaining faithfulness to this core principle.

**Ryan:**

I thought that was very unique about Haskell because I feel a lot of the other programming languages are user-centric. I mean, if people want something, they work on it, they add it, whereas Haskell feels more principled. Or it's all starting from these ideas. And if you don't satisfy these ideas as a user, yeah, well, that's fine. For instance, in one of your talks, you mentioned somewhere that there was a release of the compiler where if a file wasn't type-correct, then the compiler would delete the file.

**Simon:**

Oh, wait, it reported the error message first.

**Ryan:**

Yeah, it reports there. But I thought that was absurd. I mean, very hostile, I guess, to the. I mean, well, if you're type safe, no problems. But.

**Simon:**

Oh, it was a mistake, right? It was a bug; it wasn't deliberate, and it only happened, you know, how did the bug get out? Because, of course, if it always did that, we'd have noticed. How did it get into a release? Well, it was because it was only on Windows and only when you compile a module that was not in the current directory. But at that stage, our users were very forgiving. And, you know, somebody wrote to us and said, well, by the way, Simon, you might like to know that, you know, GHC does this, but, hey, don't worry about it, you know, I just copy all my files somewhere else before I compile and then I copy them back.

So, of course, those days are long gone. We pay a lot more attention to our users and have much more rigorous CI testing than ever we did. Right. So that's a story from a long time ago, but it's a good cultural story because it suggests that we care about our users very much, but we care about users who want, in their hearts, want to be principled. We're trying to appeal to. One of the things I like best about Haskell is people often say, I just enjoy writing Haskell.

Right. It's fun, right? My boss doesn't allow me to because it somehow doesn't fit with my production shop. But for me, I would go for it. I love writing this stuff. Every time. Every time. Yeah, that's very rewarding to me.

### 01:09:07 — Avoiding success at all costs

**Ryan:**

There's also this interesting—I don't know if it's a cultural value—but it's a statement that you say often in the context of these older talks, that you say that you avoid success at all costs. Could you explain what you mean by that phrase?

**Simon:**

Oh, yeah, this was just a little play on words. It was in a retrospective on Haskell. I gave an invited talk at POPL a long time ago, probably 20 years ago. So it's a little play on words because you can read it as either avoid success at all costs. And that's what we've been discussing. Success at all costs means compromise your principles in order to satisfy your users or think that you're satisfying users, give them what they say they want, if we build it, they will come kind of deal.

So avoid success at all costs. Or if you parenthesize it the other way, it says, avoid success at all costs, at all costs. Avoid success. And that's saying, that's a little joke. But it says if you're too successful and have too many users, it becomes more difficult to make changes. And we experience that right now. So I devote many, many more of my personal cycles to backward compatibility issues than ever I did.

I've devoted hundreds of hours and hours, well, days and days, weeks and weeks in the last year or two to the following: what seems to be a very simple property. If you can compile a program, a package, a whole program with GHC 10.0 and we release GHC 10.2, you should be able to compile that same package unchanged with GHC 10.2. Seems reasonable, right? After all, 10.2 should just be better. But no, GHC has never had that property, and making it have that property has turned out to be very, very time consuming.

Previously we just never cared. Then we started to care, but thought it was a lot of work, and now we're investing the work.

### 01:11:12 — LLMs and programming languages

**Ryan:**

I guess that was from a long time ago. I think nowadays software engineering, there's been a major shift in the last year where a lot of code is being generated by these models or these LLMs. How do you see programming language design shifting to accommodate a world where a lot of the code is no longer written by humans?

**Simon:**

I think it may be the best thing that's happened to statically typed languages for a long time, because as we've been discussing with a static type system, you cut down the space of programs that the LLM can generate because it is perfectly capable of running the compiler and saying, "Oh darn, that was a bad program, better fix it," right? So a zillion iterations get done behind the scenes, whereas in an untyped language, the first one it coughed up, you'd have had to run it against a test suite or who knows what, but it dramatically tightens up that cycle.

Right. So I think that statically typed languages are a huge boon for LLMs because it's too easy to. And programs are just strings, right? It could just generate the next plausible word.

**Ryan:**

Away if there's a slider on, I guess, the strength of a type system. And the other side of the week, what do you see as the absolute strongest type systems among programming languages?

**Simon:**

Oh, Haskell. I think Haskell is exploring the bleeding edge. There is an exception, which is that module systems are a... And in particular, sort of functor-style module systems are explored much more deeply in the OCaml world and in the Haskell world. We've essentially never gone there. But otherwise, I think Haskell's right up there. Now, of course, a language like Scala is also as... So Scala has almost everything Haskell has, I think, not quite, but it also has subtyping and object orientation.

So that's a lot more complicated. A lot more complicated, I think. And they pay a price for it. I think Martin Odersky would agree that they pay a price for it. So in complexity, it's probably more complicated than Haskell's, and maybe in terms of power. So maybe I should have said Haskell and Scala are the two leading Haskell, Scala, OCaml, perhaps I'll just put them in an equivalence class for now.

They're not strictly comparable. They all have things which they're more powerful than the others, probably.

### 01:13:57 — New programming language design

**Ryan:**

What do you think are the important problems to solve in the future of programming languages today? What are the unsolved problems in the domain that are top of mind for you?

**Simon:**

I think it's actually hard to identify, to say, here's a problem we want to solve, let's try to solve it. Well, I think another way to tackle it is to say, what are interesting new languages out there that are exploring very different parts of the design space? And there I think I do have a candidate. So the language that is my day job. I work for Epic, and we're designing a programming language called Verse.

Now, Verse is a very exotic language. It's really a functional logic language, so it's yet more expressive than Haskell. It has a path-? type system, but a very different one to Haskell's. So if you like, the way I think of it is like this. If you look at C and Fortran, they look pretty different if you're an imperative programmer. But if you look at them, if you zoom out still, you can see functional languages.

Then C and Fortran are pretty close together, along with object-oriented languages. They're all in a clump, right? And then there's some functional languages, Haskell and ML. I know OCaml and Scala out here. If you zoom out still further, then the imperative languages and functional languages altogether, and Verse is way out here, right. So Verse is exploring a very new point in the design space.

But just like functional programming back in 1980, it seems sufficiently interesting and cool and unusual and weird that it's worth exploring. Right? So back in 1980, nobody would have said, we're definitely going to do functional programming and it's going to be useful for practical applications. They said, that's pretty weird. By all means, give it a try, guys. And that's kind of where I am with Verse.

One difference is that back in 1980 we were purely academics, and now, Verse is being developed by Epic Games, so we got much more muscle behind it than was behind functional programming to begin with. So we'll see. It's a very interesting intellectual endeavor, adventure, I should say.

### 01:15:59 — Should students continue to learn programming

**Ryan:**

Yeah. I think a lot of people, like students, are maybe worried about AI or studying computer science. Would you recommend people learn how to program today, given that AI is starting to write reasonable code now?

**Simon:**

Oh, yeah, yeah. So I think people are right to be worried in the sense that I think there's going to be considerable dislocation, right? Because if you were in the Industrial Revolution, then lots of people lost their jobs as spinners and weavers, and it wasn't easy for them to get a new job in the new economy. Now, the new economy had, in the end, had more jobs, but there was.

If you were one of the people who just lost their job, that was not a happy place to be. From our perspective, you know, from an Olympian perspective of a few hundred years later, we think, well, it's just a blip, right? If you're part of the blip, not a problem. So I think people are right to be worried. We don't know how things will shake out. I'm actually optimistic that in the medium term, if we don't destroy ourselves with some truly existential thing.

But from an employment market point of view, I'm optimistic that in the end we'll just be in a higher place, that AIs will just be a bigger power tool. I mean, everyone likes using compilers, right? We don't like machine code anymore. Compilers make us more productive. Maybe LLMs can make us more productive. That's what I hope. I sort of believe, modulo dislocation effects. Now, should we teach children or even undergraduates how to program?

So I think still yes. And the reason is because one way to say it is copilots who need pilots. I think Copilot was quite a good title that Microsoft gave their tools because it encourages you to believe it's your partner, not your boss. If LLMs spit out a pile of goop and we literally do not understand what it does, we just try it and it kind of works. That might be okay if we're just throwing up a quick visualization.

It might be less okay if the quick visualization is going to drive our policy choices about us a nation, whether to go into lockdown because of COVID or if this program is going to run my aeroplane or train signaling system. So now those are extreme ends of the spectrum from quick and dirty things. It really doesn't matter if it doesn't work, but it kind of does a lot of the time, absolutely fine too.

This is a 30-year code base. It's going to last a long time. I really want to make sure that it's like putting new stuff into GHC. If somebody sends me a pile of AI-generated code to put into GHC, I'm not going to put it in unless I've reviewed it or somebody's reviewed it. Because in 10 years' time, I'm going to want to change that code. How do I even know what it does? If it's simply a magic incantation that somebody's done that kind of worked on the test they did, but maybe won't work in deployment, that's no good.

So I really want long-lived, maintainable code to be well reviewed. Sorry. So. And to do that, I need reviewers who can write code, who know. Let me mention one other perspective. If you think about what every child should know. When I think about what every child should know about computing, I would include binary and bits, not, just as for physics, I would include atoms and molecules. Now it's not that in real life anybody manipulates atoms or molecules or takes decisions which are based directly on their knowledge about knowledge, but somehow knowledge that all matter is made up of atoms, you know, constituted of a finite number of elements that atoms.

That knowledge underpins everything we understand about the natural world. If you literally have never been told that, you are sort of emasculated as a citizen, let alone as a scientist. So if you literally do not know that everything is composed of bits, that words and music and text and LLMs and everything is all just bits, I think you're crippled. So I want every child to learn, you know, it's like I want you to learn the bottom.

It's all bits, nothing else. It's all just bits. I even have a talk. The talk is called Bits with Soul. It's so easy to grab for. It's a talk I gave to an audience that was not a computer science audience at all. It was a completely lay audience ranging from 14-year-olds to professors of quantum mechanics. Pretty difficult audience to address. And it was meant to be about codes and coding and bits.

So it tries to get at the essence of why I think it's important that every child, every person, every human being should understand something about the computational universe that surrounds them and that is founded in bits. Now, just to develop the analogy a bit further, I would then say, and it also, I think, I want them to also know about programming programs. I want them to know that computers fundamentally execute by following machine instructions blindly.

Right. That is not magic, it's not hocus pocus, it's just remorseless and very dumb. Right. It's incredibly empowering then. And also to learn the basics about how neural networks work. In the same talk I explain how a one neuron neural network works, and that's enough. Then it's actually true to say, not distorting, but that's to say ChatGPT is just a trillion of those wired together, and astonishingly, that very simple.

So all ChatGPT is, is a trillion floating-point numbers and a lot of floating-point arithmetic. That helps you make sense of a question like, can ChatGPT have feelings? Well, it gives you, I mean, of course that's a philosophical question, but it informs your discussion about if you know that all it is is trillion floats and a lot of floating-point arithmetic. That's all, nothing more.

Anyway, sorry, long answer to your question, but so I... So yes, basic programming, absolutely, yeah. Becoming fairly skilled in how to use, you know, Django framework, maybe not so much maybe. I think one thing that LLMs are very good at is knowing the arcane and complicated APIs that many of these frameworks present when there's just 10,000 functions you've got to know.

### 01:22:33 — Why Excel is is 2nd favorite programming language

**Ryan:**

You mentioned somewhere someone asked you, you know, what's your favorite programming language? And obviously Haskell's got to be number one. Yeah, but for your second favorite programming language, you said it was Excel at that time. Why was Excel your favorite programming language?

**Simon:**

Oh, because it's the world's most widely used functional programming language. The formula language is a functional language, isn't it? Doesn't have any side effects. You program entirely with values. So the formula language of Excel is a functional programming language, a very weak one. It doesn't even let you define new functions. And it has a very limited collection of data types, namely just flat arrays and numbers and strings.

So when I was working for Microsoft, I took it as my war cry to say, let's take that idea. Excel is the world's most widely used functional language by three orders of magnitude. And oh, it's the most widely used programming language by three orders of magnitude, not just functional language. Excel is used by many, many more programmers, users, domain experts than any imperative language.

Imperative language is a few million users. Excel, hundreds of millions of users. Even if you just restricted users who are using formulae. So how can we delight those users? Answer: take ideas from functional programming and use them to make Excel's formula language more powerful. It took me 20 years, but Excel did finally add Lambda to Excel. Look it up, there are blog posts about it and many YouTube videos about it.

So you can now program in Excel using full lambda as Alonzo Church originally defined it. You can write anything, because lambda is computationally complete. You can write any computation in Excel now. It would be a bit slow, but you can. And much more practically, you can take formulae that previously you just copy-pasted here and there and wanted to make reusable, wrap them up in a lambda, and now you can just call the lambda.

And now it is a proper grown-up functional language that is Turing complete. Just search for Excel LAMBDA, those two keywords will get you lots of raw material.

### 01:25:04 — Advice for his younger self

**Ryan:**

Last question for you is, knowing everything that you know now from your career, if you could go back to when you just graduated from college and give yourself some advice, what would you say?

**Simon:**

All of these people who you see very successful wandering around, looking as if they've made it, I guess you might class me among them. Now, they are all just making it up as they go along. They feel insecure, uncertain, not sure what to do next, not sure what their next steps are, not sure what next big problem they're going to tackle, unsure about whether what they're doing is going to be successful or not.

And so all of their confidence is, I mean, they project confidence. Maybe that's partly a life skill, but often they're not. And so the fact that, in those days, of course, I felt very not confident. I would say, since all of these successful people are making it up as they go along, it's fine for you to be as well. And they've been lucky. Moreover, they've been lucky. They've had.

But if you want to be lucky, you do need to put yourself in a position where accidents can happen to you, and that means taking risks. So if you want to be lucky, you need to put yourself in positions where lucky things could happen.

And that means taking some kind of risk. So if you're very conservative and never take any risk, then it's very unlikely that the accident that is life transforming will happen. That's a balance, of course. But it means that accidents are not so bad. And of course, dying is bad. But lots of accidents may change your life in a way that might be surprising to you, but turns out to be not so bad in retrospect.

**Ryan:**

Awesome. Well, yeah. Thank you so much for your time. I really appreciate it, Professor Jones. We will.

**Simon:**

Nice talking to you. Thanks, Ryan.

