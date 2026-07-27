---
type: raw-transcript
slug: creator-of-ocaml-functional-programming
title: "Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy"
guest: "Xavier Leroy"
date: 2026-07-20
url: https://www.developing.dev/p/creator-of-ocaml-functional-programming
fetched: 2026-07-27
complete: true
---

# Creator of OCaml: Functional Programming, Formal Verification, Programming Languages | Xavier Leroy

**Guest:** Xavier Leroy (Creator of OCaml)
**Host:** Ryan Peterman
**Publish Date:** Jul 20, 2026

## Host's Intro

Professor Leroy (Creator of OCaml) is incredibly knowledgeable. I felt like a student at his office hours asking away at a bunch of my curiosities. His answers off the top of his head brought a lot of clarity.

For instance, I have seen people talking about Lean and formal verification on Twitter/X but never really had a good mental model for how it worked. Part of the conversation we dive into that and he shared examples that made the topic a lot more concrete.

He's one of the best people to speak on the topic since he led a project called CompCert to formally verify (using the Rocq proof assistant) that the compiler always generates faithful machine code from the source code it is given.

We also talked about programming languages comparing OCaml to popular languages (e.g. Rust and Javascript) and how interesting language features like type inference work. Hope you enjoy the episode!

## Timestamps

- 00:43 - What sets OCaml apart
- 04:39 - OCaml vs Rust
- 07:57 - Why is manual memory management more performant
- 11:21 - Javascript vs OCaml
- 14:00 - Famous Rob Pike quote
- 16:05 - Type inference and how it works
- 22:12 - What is formal verification and how does it work
- 40:07 - What made multicore support difficult for OCaml
- 50:17 - How programming languages interface and call each other
- 57:41 - The danger of almost-correct LLM code
- 01:05:39 - How LLMs will change programming languages
- 01:10:26 - Industry vs academia
- 01:15:05 - Most interesting unsolved problems
- 01:18:30 - Top book recommendations for engineers
- 01:21:17 - Advice for his younger self

## Transcript

### 00:43 — What sets OCaml apart

**Ryan:**

[[00:43](https://youtu.be/9Cswiqrq6So?t=43)] What sets OCaml apart from other programming languages?

**Xavier:**

[[00:47](https://youtu.be/9Cswiqrq6So?t=47)] It is a fine functional language. You can write functions by case over inductive types and recursion and combine them with combinators and higher-order functions and everything. So it's really a fine functional language, but it's also a fairly decent systems programming language. So it has full imperative power. It has lots of interesting control structures, exceptions, threads, handlers for user-defined effects, which we added recently.

[[01:25](https://youtu.be/9Cswiqrq6So?t=85)] And it has a very predictable cost model, execution model. So when you write your code, you have a pretty good idea what will take time and what will be fast and what will be slow. And that's not the case for all functional languages. Some are pretty unpredictable, and then the implementation is also pretty performant. So there's a fairly decent compiler, not the best in its class, but the code is pretty efficient.

[[01:52](https://youtu.be/9Cswiqrq6So?t=112)] There's a very good allocator and garbage collector with low latency, so you don't have much pause. You don't have long pauses. And that's quite important when you do things like network programming. And so you can write systems applications in a mostly functional style and with all the benefits of functional programming. So initially OCaml wasn't designed for those kinds of applications. It was more for things like theorem proving or implementing domain-specific languages.

[[02:30](https://youtu.be/9Cswiqrq6So?t=150)] And then we got some of our first users who were from the systems community, in particular the Ensemble project in the late '90s at Cornell University. So it was a network protocol stack for reliable multicast and those kind of collaborative distributed applications, like collaborative editing or multiplayer video games. And their first code was in C, of course. They were systems people, right?

[[03:03](https://youtu.be/9Cswiqrq6So?t=183)] And it worked, but it was unmaintainable and they couldn't extend it anymore. And someone had the idea to try OCaml. And so first the code became a lot nicer and easier to evolve, and the performance was about as good as C code. And in particular they had this brilliant trick of running the garbage collector while packets are in flight. Once you've sent a packet, you're idle for a few microseconds, and so you can run some GC.

[[03:35](https://youtu.be/9Cswiqrq6So?t=215)] It costs nothing. So they were very happy with that. And then there were some other projects like this using OCaml for systems applications, like the MirageOS unikernels. Another benefit or consequence of this Ensemble project is that one of the PhD students working on that was Yaron Minsky, who then went to Jane Street and implemented their trading infrastructure in OCaml. So that is still today one of our big users.

[[04:15](https://youtu.be/9Cswiqrq6So?t=255)] And again, they do automatic trading, so it must be fast and reliable, and no long pauses. But they also want the allegory of functional programming. They want non-programmers to be able to read their code, like financial engineers or quantitative analysts. OCaml is a fairly good match for those kinds of applications.

### 04:39 — OCaml vs Rust

**Ryan:**

[[04:39](https://youtu.be/9Cswiqrq6So?t=279)] I thought it might be interesting to ground some of the conversation here by making comparisons across programming languages, maybe ones that people know more. When you think about Rust versus OCaml, what are the big differences and the pros and cons of the various design decisions in those languages?

**Xavier:**

[[04:59](https://youtu.be/9Cswiqrq6So?t=299)] The big dividing line between Rust and OCaml is, well, OCaml has automatic memory management, garbage collection, and Rust is definitely a language for manual memory management. It's the finest language that I know for manual memory management. It manages to make it mostly safe with the discipline of borrowing, et cetera, and tracking ownership and so on. So it's infinitely safer than C or C++. But it's still a language where you allocate and free memory yourself.

[[05:42](https://youtu.be/9Cswiqrq6So?t=342)] And on the one hand, it gives more control over what the program is doing. On the other hand, it's still a big responsibility. It's significantly harder to write programs when you have to manage your memory, even with the help of Rust types. For me, that's kind of the main dividing line. Otherwise, Rust has many of the high-level features of functional languages, in particular in data structures and ability to do pattern matching and so on.

[[06:21](https://youtu.be/9Cswiqrq6So?t=381)] So it's a very interesting design because they really managed some kind of fusion between C or C++-style low-level programming and some of the high-level facilities of functional programming. But still, that divide, garbage collection versus manual memory management, remains.

**Ryan:**

[[06:43](https://youtu.be/9Cswiqrq6So?t=403)] So it sounds like this is a performance trade-off where you give more to the programmer in exchange for higher performance.

**Xavier:**

[[06:53](https://youtu.be/9Cswiqrq6So?t=413)] That's mostly true. They said manual memory management is not always faster, or you need to be a very good programmer so that it's always faster. There's been some mostly C code, for instance, that does a lot of copying of objects just because you're not quite sure you're the only owner. So you make a copy, and now you're the only owner. But the copying is quite costly in time and in memory bloat. And for those kinds of applications, a garbage-collected language is better.

[[07:32](https://youtu.be/9Cswiqrq6So?t=452)] And likewise with GC you can work with shared data structures. It's perfectly safe, while sharing is kind of limited. With Rust's ownership discipline there are more constraints, and so you may end up unsharing and using more memory.

### 07:57 — Why is manual memory management more performant

**Ryan:**

[[07:57](https://youtu.be/9Cswiqrq6So?t=477)] It is surprising to me that manual memory management would in many cases be more performant than automatic, because, for instance, in other patterns in computer science, let's say, letting the compiler optimize things for you instead of optimizing things yourself, I would have thought that letting some system manage memory for you rather than manually managing it would also be better. So why is there a difference there?

**Xavier:**

[[08:26](https://youtu.be/9Cswiqrq6So?t=506)] Well, because garbage collection takes place at runtime, so from time to time the program is no longer executing what you wrote. It is actually scanning memory, trying to find memory that is no longer used. So there is runtime overhead, and it can be, depending on applications, 10%, 20%, maybe sometimes 30%. But again, that doesn't mean the whole program is 30% slower than if you had written it with manual memory management.

[[09:07](https://youtu.be/9Cswiqrq6So?t=547)] Because there may have been other costs, as you said, of manual memory management. But yes, there's been a lot of research on trying to do more, let's say, compile-time automatic memory management, and you can do that to some extent. But for some programming styles where it's easy to track the lifetime of objects and data blocks, but in general you still have quite a bit of work to do at runtime.

**Ryan:**

[[09:41](https://youtu.be/9Cswiqrq6So?t=581)] I think a lot of people, for garbage collection, might think of it as a binary thing, or it's either you have it or you don't. But I wonder, in OCaml, is there some way to turn down the memory management and do some manual, kind of like a mixture, to have the benefits of both?

**Xavier:**

[[10:01](https://youtu.be/9Cswiqrq6So?t=601)] So that's one of the things that the Jane Street people are looking at. So they have the OxCaml variant, which is kind of OCaml with some inspiration from Rust. So it's still very experimental. But yeah, they've been playing with things like stack allocation of some data structures so that they're automatically deallocated when the function returns, which is quite cheap. Yeah, there are a few things you could try, but I'm not sure they are going to make such a big difference.

[[10:31](https://youtu.be/9Cswiqrq6So?t=631)] I remember doing with a student some experiments with stack allocation of data structures a long time ago, and you don't win as much as you would think. Garbage collection or heap allocation is pretty cheap for objects that have a very short lifetime. If they die before the next garbage collector, they will cost very little in garbage collection time. But it's more expensive for long-lived data structures because those will be scanned and analyzed multiple times.

[[11:08](https://youtu.be/9Cswiqrq6So?t=668)] And stack allocation works for the first kind of objects, things that have short lifetime anyway, so you don't win as much as you think.

### 11:21 — Javascript vs OCaml

**Ryan:**

[[11:21](https://youtu.be/9Cswiqrq6So?t=681)] One of the most popular programming languages, JavaScript. Curious, when you think about the difference between JavaScript and OCaml, what's the main thing that comes to mind?

**Xavier:**

[[11:30](https://youtu.be/9Cswiqrq6So?t=690)] Yeah, I'm not a big fan of JavaScript. Well, JavaScript is very dynamic. Type checking is entirely dynamic, but it's more than that. I mean, pretty much everything can be redefined at runtime, including, I don't know, the semantics of method invocation, for instance. So really some pretty fundamental aspects of the language are very flexible. So some people say, oh, that's great, we can do lots of metaprogramming, et cetera.

[[12:02](https://youtu.be/9Cswiqrq6So?t=722)] And to me, it's a big weakness. I mean, it makes programs that can be very fragile and also have some security issues. So JavaScript is the ultimate dynamic language, in my opinion. While OCaml is very static, static typing, static binding, pretty much everything is fixed at compile time. Well, I guess it's kind of a different data model. JavaScript is a little more object-oriented in the way it presents data.

[[12:37](https://youtu.be/9Cswiqrq6So?t=757)] Maybe that's not that important. And to say one good thing about JavaScript is that it also contains a decent functional language. Inside there's a little core of JavaScript, which is basically Lisp and can be used to do functional programming if you want. And actually the designer of JavaScript, I think, was a former Lisp person. I can't remember his name, but Brendan Eich maybe. Yeah, Brendan Eich.

[[13:08](https://youtu.be/9Cswiqrq6So?t=788)] Yeah, there's a little bit of heritage from Lisp to JavaScript, but a very dynamic kind of Lisp.

**Ryan:**

[[13:17](https://youtu.be/9Cswiqrq6So?t=797)] You said you weren't the biggest fan. Is that just because of the dynamics, or is there some other aspect?

**Xavier:**

[[13:22](https://youtu.be/9Cswiqrq6So?t=802)] Yeah, mostly the dynamics. I think they really went overboard with that. This kind of meta object protocol where you can really find the semantics of very basic operations like method invocation, the fact that a method can. There's a lot of introspection. A method can look at its own call stack, look at callers, look at the code of its callers, which is a security nightmare. All those things, I think, are completely unnecessary and not conducive to good programs.

[[13:57](https://youtu.be/9Cswiqrq6So?t=837)] Easily abused. Easily abused.

### 14:00 — Famous Rob Pike quote

**Ryan:**

[[14:00](https://youtu.be/9Cswiqrq6So?t=840)] I think on the topic of functional languages, compared to imperative languages, there's this thought that functional languages are kind of harder to learn or maybe they have more perceived complexity. And actually, when I research, there's this popular quote from the designer of Go, Rob Pike, and he's talking about what they intended to do with Go. And he said, the key point here is the programmers are Googlers.

[[14:30](https://youtu.be/9Cswiqrq6So?t=870)] They're not researchers; they're young, fresh out of school. They're not capable of understanding a brilliant language. And I think that thought of a brilliant language is often attributed to functional languages. What do you think about—is a language like OCaml harder for programmers to grasp than imperative languages?

**Xavier:**

[[14:51](https://youtu.be/9Cswiqrq6So?t=891)] I think functional programming is not fundamentally harder, especially if you have a little bit of mathematics background. So, coming back to the quote by Rob Pike, I think it describes very much how they go about hiring at Google. They hire a lot of engineers who are fresh out of college. Some of them have master's degrees, and then they train them internally. Other companies, I think, tried to hire people with more education and perhaps more diverse backgrounds.

[[15:29](https://youtu.be/9Cswiqrq6So?t=929)] So Jane Street, for instance, and some others use OCaml as a filter on who they want to hire. Yes, they have fewer applicants, but in general they have more interesting backgrounds. And perhaps one last thing I would like to say, Python is 50% functional language. Okay? A lot of good Python code looks like functional code with comprehensions. So I think people are already halfway through functional programming when they are comfortable with Python.

### 16:05 — Type inference and how it works

**Ryan:**

[[16:05](https://youtu.be/9Cswiqrq6So?t=965)] Yeah. When I was learning OCaml in college, I think one thing that really stood out to me and I thought was interesting was this concept of type inference, where the compiler knows the types of everything implicitly in the way that the code is written. Can you explain type inference and what the advantages are?

**Xavier:**

[[16:27](https://youtu.be/9Cswiqrq6So?t=987)] Well, the basic idea is that you don't have to declare the type of every variable. You introduce every function parameter, every local variable, because quite often the type can be deduced from the uses of the variable. Like if you do, I don't know, X equals string length of S, then you kind of know that S is a string and X is an integer, right? Because that's what the string length function, that's the type of string length, and it tells you that.

[[17:00](https://youtu.be/9Cswiqrq6So?t=1020)] So that's a basic idea. Now, the actual realization is a little more complicated. Basically, the compiler needs to collect a number of constraints and then try to solve them. Well, if there's no solution, then it's a type error. But sometimes there are several solutions, and you must find good criteria to choose one. Otherwise, it also needs to be predictable for programmers, and often you can still put type annotations.

[[17:33](https://youtu.be/9Cswiqrq6So?t=1053)] As a programmer, you can still put type annotations if that makes code clearer. So I think the main advantage is precisely to have less verbose code. Less verbose code where you don't need to put types everywhere, but only where they help documentation and make the code easier to read. But quite often for small local functions, for short-lived temporary variables, the type is obvious from the context, so let's just omit it.

**Ryan:**

[[18:12](https://youtu.be/9Cswiqrq6So?t=1092)] If I'm trying to figure out how this type inference works, the intuitive example you said makes sense, but you mentioned it seems to be some sort of system of equations that you solve or something like that. Can you give a concrete example? What does that look like to the compiler?

**Xavier:**

[[18:29](https://youtu.be/9Cswiqrq6So?t=1109)] Okay, well, for a slightly more complex example, say you have a function with two parameters, X and Y, and then you do if X equals Y. So that tells you that X and Y have the same type, but that still doesn't tell you which type it is, assuming polymorphic equality comparison. So you've learned something about X and Y, that they have the same type, but you still don't know what the type is. And later maybe you will learn something about the type of X, and now you will have determined the type of Y as well.

[[19:02](https://youtu.be/9Cswiqrq6So?t=1142)] So that's the kind of constraints you accumulate and solve, a little bit like Sudoku or those kinds of puzzles. And then there's the interesting case where you don't have enough constraints to find a unique type. So maybe in the end X and Y will be, they have the same type, but it's still unconstrained. And then that's where you automatically get polymorphism for free. The type checker said, okay, those types are unconstrained, so it can work for any type.

[[19:35](https://youtu.be/9Cswiqrq6So?t=1175)] So my function can take an X of any type and a Y of the same type, again any type, and it's a polymorphic function. So there's this beautiful, I think, phenomenon that polymorphism can be discovered just by running type inference and noticing that there are no constraints, so it must be polymorphic. And that was a guiding insight by Robin Milner, the British computer scientist pioneer who invented this ML family of languages and this kind of type inference in the '70s. Polymorphism was not very well understood at the time.

[[20:16](https://youtu.be/9Cswiqrq6So?t=1216)] And so the fact that he could introduce polymorphism so easily in his language just as a consequence of typing rules was a beautiful discovery.

**Ryan:**

[[20:28](https://youtu.be/9Cswiqrq6So?t=1228)] So for type inference, it seems like the benefit is the code is going to be a lot more concise because we don't need to write out all of the types, which seems nice, but what are the trade-offs of adding type inference to a programming language?

**Xavier:**

[[20:43](https://youtu.be/9Cswiqrq6So?t=1243)] Well, as I said, type error messages can be very confusing because they don't always point to the actual source of the type error. Okay. The system may have done some wrong inferences and will report some of those inferences instead of reporting the source, the actual source of the type error. So it's been the subject of much research, and there's no very well-defined idea of the source of a type error, basically.

[[21:21](https://youtu.be/9Cswiqrq6So?t=1281)] So errors can be an issue. Some features of type systems are easy to combine with type inference, and some are harder. For instance, when it comes to genericity, so I mentioned parametric polymorphism, which is very well handled. But subtyping, the kind of thing you have in object-oriented languages, is actually harder to combine with type inference for super technical reasons that I'm not going to go into.

[[21:54](https://youtu.be/9Cswiqrq6So?t=1314)] So sometimes you have to make a choice. Either you have type inference, but it is less powerful, or you have full type inference but a more restrictive type system, and that choice is part of the language design.

### 22:12 — What is formal verification and how does it work

**Ryan:**

[[22:12](https://youtu.be/9Cswiqrq6So?t=1332)] Actually, you mentioning this solver kind of reminds me of the topic of formal verification. Could you explain what formal verification is?

**Xavier:**

[[22:25](https://youtu.be/9Cswiqrq6So?t=1345)] Well, the idea is that for some programs, you want strong guarantees that the program is correct, and guarantees that are hard to get just with testing and code reviews. There's this famous quote by Dijkstra, the Dutch computer pioneer, which goes something like testing can only show the presence of bugs, but not their complete absence. Because in general, there's infinitely many inputs to your program, and you cannot test them all.

[[23:02](https://youtu.be/9Cswiqrq6So?t=1382)] So you're only testing a sample. And sometimes you have surprises. So what if you want to make sure your program is correct for an infinite number of inputs? And that's where you need to turn to those so-called formal methods. So you're using mathematical reasoning, you're using static analysis algorithms on your program to really analyze all possible executions of a piece of code and make sure that it matches a specification.

[[23:35](https://youtu.be/9Cswiqrq6So?t=1415)] The specification can be very simple, like the code will never crash given well-formed inputs. So that's a fairly simple property, but still extremely useful because code that crashes is always code that can be attacked. It's often a security hole. So, for instance, all accesses within all array accesses are within bounds. That's a very simple property, and it's very hard to ensure just by a type system or just by testing.

[[24:09](https://youtu.be/9Cswiqrq6So?t=1449)] So that's where you need some more advanced formal verification. And then there are much more precise specifications that you may want to check that can be where the program always terminates. It can be the program doesn't leak confidential data. It can even be, well, the program computes this mathematical function with an error, floating point error, I don't know, 10 to the minus six. Okay, something like that, something very precise like that.

[[24:42](https://youtu.be/9Cswiqrq6So?t=1482)] And so it's been a really hot topic in software sciences since at least the seventies, I would say. There's lots of techniques. Some are just fully automatic, like static analysis, but they're already pretty good at finding bugs and making sure that some bugs, like out of bounds, are not there. And some are a lot more interactive and require a lot more programmer assistance to write specifications and then do so-called program proofs.

[[25:16](https://youtu.be/9Cswiqrq6So?t=1516)] So proving mathematical statements about the program.

**Ryan:**

[[25:19](https://youtu.be/9Cswiqrq6So?t=1519)] I hear about it a lot more now, which is Lean and these theorem provers. What are those in this context, and how are they used?

**Xavier:**

[[25:31](https://youtu.be/9Cswiqrq6So?t=1531)] Lean is an instance of the so-called provers, or proof assistants. So originally, those were developed to do mathematics on the computer. So nothing to do with formal verification of programs, but they can also be used for formal verification of programs. But the initial motivation was really to do mathematics with the help of the computer. Well, originally everyone focused on automatic theorem proving.

[[26:04](https://youtu.be/9Cswiqrq6So?t=1564)] So having the machine find proofs all by itself, but that's very, very difficult and not necessarily what mathematicians need. And so those proof assistants are more like formal languages, like programming languages, but where you can write mathematical definitions, mathematical statements, and they will help you prove. So some small proof steps they will do automatically. And for others, the user still has to guide the provers through the major steps.

[[26:43](https://youtu.be/9Cswiqrq6So?t=1603)] But the good thing is that the proof is recorded also in a format that the machine can understand and recheck. When you complete a proof in Lean or Isabelle or one of those tools, and it is rechecked, the computer makes sure that all inferences are justified, that you didn't forget any case, that you didn't use a conclusion as a hypothesis, all kinds of problems you can have with pencil-and-paper proof.

[[27:13](https://youtu.be/9Cswiqrq6So?t=1633)] And so in the end you get proofs that are extremely reliable, extremely credible. And those tools have been used a little bit for some big mathematical results where the proofs are so big that they can't be done just by humans. You really need computer assistance. I think there's a recent example with the weak Goldbach conjecture. So part of the proofs involved checking a whole lot of inequality, maybe a thousand inequalities involving several real variables, and blah, blah, blah.

[[27:55](https://youtu.be/9Cswiqrq6So?t=1675)] And so computer assistance was really needed to make sure that everything was checked and there were no human mistakes left. And maybe we'll talk about generative AI later. But there's also now a lot of interest in conjunction with generative AI. AI is pretty good at coming up with plausible proofs, but then they have to be checked by humans, unless AI writes a proof in one of those formal languages like Lean, in which case it can be checked by a machine, and that's much more effective.

[[28:38](https://youtu.be/9Cswiqrq6So?t=1718)] So, yeah, so it's the idea of using the machine to help you write proofs and recheck proofs that you've written yourself, or maybe with some help from an AI. And now those tools can also be used to prove properties about programs. And so I spent many years proving the correctness of a compiler, C compiler, using one of those tools, the Coq proof assistant. So basically, what I'm hoping about the compiler, so it takes C code, it produces assembly code, and proving that the assembly code is faithful to the C code.

[[29:21](https://youtu.be/9Cswiqrq6So?t=1761)] So there's no miscompilation. The compiler didn't introduce a bug in the program that wasn't there originally. And it's a fairly big proof because compilers do complicated things about programs. And then you have to define exactly what it means to preserve the semantics of a program. So you have to define the semantics of your programming languages. And so it's all a very good use of those machines, of those proof assistants.

[[29:49](https://youtu.be/9Cswiqrq6So?t=1789)] The same work could be done on paper, but this would be a proof of several thousand pages, and nobody would want to read it, nobody would trust it. It's just too big, and it would be very hard to evolve. One good thing about those mechanized verifications of programs is that it can also help you evolve the program. You can add new features and so on and adapt your proofs and be really sure that you haven't introduced a regression or things like that.

[[30:23](https://youtu.be/9Cswiqrq6So?t=1823)] So, yeah, so it's really programming taken to a higher level today. It's quite expensive. It takes a lot more time to prove a program than to write it in the first place. But maybe this is getting a little better. I should also mention another great example of verified software. It's a microkernel, the seL4 microkernel developed in Australia, which is used as an hypervisor in some applications. And so it's really like 8,000 lines of extremely technical C code that manipulates processes and capabilities and security tokens and so on.

[[31:14](https://youtu.be/9Cswiqrq6So?t=1874)] And it's been proved correct. Every line has been proved correct. And that's a very big achievement.

**Ryan:**

[[31:20](https://youtu.be/9Cswiqrq6So?t=1880)] When you mentioned the example of verifying a mathematical proof, that makes sense to me. When you talk about proving something about a program, it's a little bit more abstract to me, or I'm having some trouble visualizing. Could you give a concrete example, maybe some trivial program, and we're trying to prove something about it and how that theorem prover would work?

**Xavier:**

[[31:46](https://youtu.be/9Cswiqrq6So?t=1906)] Let's say you have a function that takes three numbers X, Y, Z and returns the average of those numbers. Okay? And maybe you're using a not completely obvious formula, like T equals X plus Y, and then T equals T plus Z, and then T equals T divided by three, and then return T. Okay? So not exactly the formula for the average. And you want to prove that this function is correct, so you want to prove that it returns X plus Y plus Z divided by three.

[[32:33](https://youtu.be/9Cswiqrq6So?t=1953)] And maybe you will have to make it clear whether you're rounding up or rounding down. If you're using integers or floating-point numbers, it's not exact arithmetic. So yeah, you'll have to say exactly what you mean by divided by three. And then if you're in a language like C++, you can have arithmetic overflows. When you compute X, Y, or Z, you can overflow the range of representable integers. And in C++, it's a bug; it's undefined behavior.

[[33:07](https://youtu.be/9Cswiqrq6So?t=1987)] So typically you will want to put a so-called precondition on your function saying, okay, if you call me, call me with numbers that are between, I don't know, 0 and 1 million, for instance, but no bigger than that. And then the prover will check that no overflow can occur in this case. Okay? And so basically you have the precondition that says, okay, these are safety warranties that must hold of the parameters; otherwise anything can happen.

[[33:40](https://youtu.be/9Cswiqrq6So?t=2020)] And then there will be a little bit of symbolic execution of the function body that says, okay, when you do t equals x plus y, then t plus equals z, then t slash equals 3, then in the end t is x plus y plus z divided by 3, provided no overflow occurred. And then you put that with a precondition that says there cannot be any overflow, and you get your final result. Okay, so basically you're stating a contract for your function, hypothesis on the arguments, guarantees on the results, and you want to prove.

[[34:18](https://youtu.be/9Cswiqrq6So?t=2058)] Analyze the function body to show that this contract is respected. I hope it's a little more concrete.

**Ryan:**

[[34:25](https://youtu.be/9Cswiqrq6So?t=2065)] So it sounds like Lean will help you basically take in some invariants about a program and kind of propagate them through line by line and uphold them. And so you can say something about, yes, maybe not Lean by itself.

**Xavier:**

[[34:42](https://youtu.be/9Cswiqrq6So?t=2082)] Well, a program prover will do exactly what you say. And for Lean to be able to do it, you still need to teach it a little bit about the semantics of your programming language. Okay, what does plus mean? What does assignment mean? Okay, Lean is mathematics. You don't assign. In mathematics, you don't say X equals X plus one, or you're just comparing X and X plus Y, and it's always false.

[[35:11](https://youtu.be/9Cswiqrq6So?t=2111)] There's no assignment in mathematics. There's assignment in many programs. So you need to make it explicit that there are actually three different states for the T variable, three different values, and relate those values to, well, the program defines what those values are, and then a prover like Lean can reason about those three successive values. Because now you're in mathematics, and that kind of bridge between programs and their mathematical meaning is called semantics.

[[35:48](https://youtu.be/9Cswiqrq6So?t=2148)] That the field of semantics of languages, it's been a big topic in PL research since the '60s at least.

**Ryan:**

[[35:56](https://youtu.be/9Cswiqrq6So?t=2156)] Am I understanding then that a pure functional programming language, the gap between mathematics and the actual symbols is much smaller than an imperative?

**Xavier:**

[[36:08](https://youtu.be/9Cswiqrq6So?t=2168)] Absolutely. You're absolutely right. And that's one of the reasons why people who do formal methods don't like assignment, don't like imperative features. Purely functional style is much, much closer to mathematical style. So much easier to reason about. There can still be a few discrepancies between the program and the math. For instance, functional programs may not terminate, they may loop forever.

[[36:36](https://youtu.be/9Cswiqrq6So?t=2196)] Mathematics doesn't like that. So you need a way to reason about termination. And also sometimes, for instance, the arithmetic you get in the programming language is not integer arithmetic, or it's not real numbers, it's floating point. So you still have to account for that gap. But you're absolutely right that the gap is much shorter for functional programming. And in the experience of CompCert, my verified compiler, I think the first decision was to write it in a purely functional style so that it would be easier to reason about it later. You mentioned the specifications that we could prove, and one of them was proving that the program terminates.

**Ryan:**

[[37:22](https://youtu.be/9Cswiqrq6So?t=2242)] But I thought that's a famously difficult or impossible. I forgot exactly the halting problem. Right, so how is that something that you could prove?

**Xavier:**

[[37:38](https://youtu.be/9Cswiqrq6So?t=2258)] Okay, so what computability theory says is that there is no algorithm that can always say this problem terminates or this program doesn't terminate. So there will always be some very weird programs for which your analyzer, your automatic termination analyzer, will produce a wrong result or will not terminate itself. So it will not work. But still, for many programs, you can succeed. You can write automatic termination analyzers that will work for a large class of programs.

[[38:21](https://youtu.be/9Cswiqrq6So?t=2301)] And then the termination analysis, termination proof can also be done by hand by a mathematician. Okay, so perhaps a human can see through those weird Turing programs that are hard to prove terminate and recognize the trick. But anyway, yeah, it's a hard problem. And program verification tasks are difficult problems. They are pretty much all undecidable. So there is no static analyzer that will always find all problems in all programs.

[[39:03](https://youtu.be/9Cswiqrq6So?t=2343)] But still you can try, okay, you can try for specific problems or specific programs and get some very useful results out of that. You only need to be able to do it for the cases that are of interest to you, the programs you really care about.

### 40:07 — What made multicore support difficult for OCaml

**Ryan:**

[[40:07](https://youtu.be/9Cswiqrq6So?t=2407)] One thing I saw when I was researching OCaml is that in 2022, OCaml added multicore support. But from my memory, I remember multicore processors became standard much earlier than that.

[[40:20](https://youtu.be/9Cswiqrq6So?t=2420)] And so I figured there might be some unique engineering challenge in adding that support. So, yeah, what happened there, and what made it difficult? Well, there were engineering challenges, that's for sure.

**Xavier:**

[[40:33](https://youtu.be/9Cswiqrq6So?t=2433)] There were also some language design issues. But let's talk about the engineering challenges first. So it's true that when you have a language with a runtime system, memory allocator, or garbage collector, at least the one for OCaml was really designed with sequential executions in mind. So if you had shared memory concurrency, then you need a garbage collector and a memory allocator that can work concurrently.

[[41:04](https://youtu.be/9Cswiqrq6So?t=2464)] And that's actually quite difficult, at least if you want them to be fast. Of course, you could always take a lock at every operation in the heap, but then you would sequentialize your programs. Basically, they would run as slowly as on a single processor. So that's not interesting. So, yeah, there were engineering challenges. And yeah, I was at least initially quite reluctant to basically reimplement a complete garbage collector and memory allocator on large parts of the runtime system.

[[41:40](https://youtu.be/9Cswiqrq6So?t=2500)] That's what we did eventually. Well, it was done mostly by the team at OCaml Labs at Cambridge University. But yes, it was a really big rewrite. But then I said there's also a language design issue, which is that for the longest time, well, now when you say multicore processors and so on, pretty much everyone, and language support for multicore processors, everyone thinks about language support for shared memory concurrency.

[[42:19](https://youtu.be/9Cswiqrq6So?t=2539)] This model where you have several threads of control and they access the same memory, and basically the threads communicate by modifying the memory and someone else is going to notice. I've never liked this model of communication. I mean, it's a bit like if you want to communicate with your neighbor, then you break into their house and move the furniture around, and then when they are back they say, "Oh, something was moved."

[[42:51](https://youtu.be/9Cswiqrq6So?t=2571)] So it's probably Ryan who's trying to tell us something. Maybe you could just meet your neighbors, and that would be things like message passing, which is a completely different form of communication, much higher level. So for the longest time I was really interested in message passing concurrency. And there's, for instance, a functional language called Erlang that was built on those ideas that I found quite interesting.

[[43:22](https://youtu.be/9Cswiqrq6So?t=2602)] However, I never got to have a decent language design, and everyone was saying, no, but it's too costly, it's not effective, there's too much copying of data. With shared memory, you can share some kind of huge database in memory. If you don't modify it too much, then basically the concurrency is free. While with message passing, we'll have to exchange a lot of data, so to get the same effect. So you will pay more for it anyway.

[[43:56](https://youtu.be/9Cswiqrq6So?t=2636)] Okay, so starting with Java, I guess, and then C++11, there was this idea that, okay, we need to expose shared memory concurrency to the programmers. But then comes the problem of the memory model, which is that what happens when there's a race, for instance, when two sides want to access the same location and maybe they want to modify it in different ways. And so sometimes parts of the C++ standard says it's undefined behavior, anything can happen, but still you need to give a little more guarantees.

[[44:34](https://youtu.be/9Cswiqrq6So?t=2674)] At the other end of the spectrum there are so-called sequential consistency, which says, well, what happens is an interleaving of reads and writes of your program. You don't know which interleaving, but there is an interleaving. But that doesn't work with modern processors; multicore processors reorder memory accesses in very clever ways to get more performance. And so, viewed from the program, it's very hard to predict what they are actually doing.

[[45:01](https://youtu.be/9Cswiqrq6So?t=2701)] And so you need to give your programmers, when you're designing a language with shared-memory concurrency, you need to give your programmers some guarantees about the ordering of reads and writes, concurrent reads and writes, while not constraining the hardware too much. And it's very difficult. So Java went through five different iterations of the memory model. Some were too strict, some were too lax, some were inconsistent.

[[45:28](https://youtu.be/9Cswiqrq6So?t=2728)] We're making predictions, impossible predictions, where the past depends on the future. Crazy, really crazy stuff. Then C++11 did a little better, but still an extremely complex memory model. And so when we wanted to add, when the, especially the OCaml Labs people wanted to add shared memory concurrency to OCaml, we had to also agree on a memory model that would be exposed to the program rules. And that also took quite a bit of design, quite a bit of time to come up with a good design.

[[46:03](https://youtu.be/9Cswiqrq6So?t=2763)] And I think it's better and easier to understand and use than the one in Java. But the OCaml memory model is still quite complicated, and sometimes I feel sorry our users are exposed to that. Okay, so that explains why it took so long, solving the engineering challenges but also agreeing on a memory model and what kind of guarantees we are going to give to programmers. Oh yeah, I forgot to say one thing, which is that in C++ and C++ there's a lot of things you can say, oh, it's just undefined behavior, or anything can happen.

[[46:46](https://youtu.be/9Cswiqrq6So?t=2806)] In type-safe languages like Java and OCaml, you want to give stronger guarantees. Maybe many things can happen, but your data should remain well typed. Typically, you don't want to expose an object to another thread before it's been fully initialized, for instance, and that's actually very hard to guarantee in your memory model. And then you have to implement that memory model. So your compiler also needs to take extra precautions to guarantee this.

[[47:19](https://youtu.be/9Cswiqrq6So?t=2839)] So yeah, type safety in the presence of shared memory concurrency is not obvious at all. So that's why it took so long.

**Ryan:**

[[47:30](https://youtu.be/9Cswiqrq6So?t=2850)] So in Python, I know this is the famous GIL, or the global interpreter lock. What is that lock protecting? Is it the cleanup of objects on the heap, or is it something else?

**Xavier:**

[[47:41](https://youtu.be/9Cswiqrq6So?t=2861)] Among other things, yes. So yeah, we had the same thing in OCaml before multicore OCaml was merged in. So yeah, basically the idea that when your runtime system is not site safe, as we said, you can protect the non site safe functions by a lock so that they will never be executed concurrently. But if you take the lock at every allocation and release it, you take and release the lock for every allocation, that is just too slow anyway.

[[48:12](https://youtu.be/9Cswiqrq6So?t=2892)] And so the idea is that you take the lock when you enter Python code, let's say, and you start executing Python code, but you can still release it when you do input output, for instance, when you're going to block for a long time, or when you're calling into C code that is thread safe and is not going to use your runtime system, then you can release the lock and some other Python thread can take it and execute.

[[48:42](https://youtu.be/9Cswiqrq6So?t=2922)] So you get a little bit of concurrency. You can overlap computations in your high-level language with I/O or computations in a low-level language in another language, but you still have mutual exclusion between two threads running Python or running OCaml before multicore OCaml. So you get some benefits like concurrent I/O, but you don't get any parallelism. Okay, you don't get a speedup for computations.

[[49:14](https://youtu.be/9Cswiqrq6So?t=2954)] And so, yeah, so we used to have this GIL in OCaml as well, and so you can get rid of it, but in general you need to redesign at least a garbage collector and memory allocator. There's probably a few places in the OCaml runtime system that still use locks to ensure mutual exclusion, like in the I/O subsystem and some phases of the garbage collector. I think there's a phase which is kind of stop the world.

[[49:50](https://youtu.be/9Cswiqrq6So?t=2990)] You need to make sure that everyone, no OCaml code is running for a short time. You need to make sure that everyone is stopped and then do a little bit of work to finish the GC, and then you can restart everyone. So, yeah, these are tricky things, and I don't know what the Python people are up to with their GIL, if they finally manage to remove it or they're still working on it, but I've heard they are making progress.

### 50:17 — How programming languages interface and call each other

**Ryan:**

[[50:17](https://youtu.be/9Cswiqrq6So?t=3017)] Yeah, you mentioned Python calling into C, and I've seen that pattern before, of a higher-level language interfacing with a lower-level one. How does that binding typically work?

**Xavier:**

[[50:31](https://youtu.be/9Cswiqrq6So?t=3031)] Oh, it's another kind of worm. Well, there are two aspects there: the control flow and the data. So the control part is not that hard. So yes, you need a mechanism so that your Python interpreter or your OCaml compiled code will actually jump to the C function. So for OCaml, basically you tell the OCaml compiler that this function is not implemented in OCaml; it's actually implemented by a C function, and you give its name, and then the compiler will emit a call to the C function using the C calling conventions, which are not exactly the same as the OCaml calling convention. But the compiler knows about that, and so it will call the C function, maybe through a little bit of glue code, whatever, and then the C function will execute and return back to the OCaml code.

[[51:30](https://youtu.be/9Cswiqrq6So?t=3090)] That's relatively easy. Now the hard part is data like function arguments and function results, because OCaml and C have different data representations. For instance, a floating-point number in OCaml is generally boxed, so it's allocated in the heap and handled through a pointer. So it's more like a double star in C. It's not a double, which is not allocated, just sits in a register. So typically the C code needs to use a so-called foreign function interface.

[[52:08](https://youtu.be/9Cswiqrq6So?t=3128)] So some C functions and macros are provided by OCaml to access the OCaml data. The OCaml arguments extract the part that it needs, the numbers. Another example is arrays. In OCaml, when you have a two-dimensional array, it's actually an array of arrays. So viewed from C, it's an array of pointers to arrays, while in C, an array of arrays has no intermediate pointers, so it's not the same representation. And so you have to explain to C or give C some functions and macros to access elements in OCaml arrays. It's not exactly the same code that you would do to access a C array from C.

[[52:52](https://youtu.be/9Cswiqrq6So?t=3172)] Okay, so you need accessors. But now if your C code wants to return some complex results, like a list, an array, and so on, it needs to allocate it in the OCaml heap. So it needs to ask the OCaml runtime system to do some heap allocation and then fill the heap blocks correctly, and then this allocation can trigger a garbage collection. So the C code might also kind of cooperate with garbage collection with root registration mechanisms, et cetera, et cetera.

[[53:26](https://youtu.be/9Cswiqrq6So?t=3206)] So there's quite a bit of work to be done, and then different foreign function interfaces arrange this work differently. So there's a base FFI for OCaml. Basically, it's a C code that must do all the work, but then it can be very fast and quite optimized. But there are other FFIs like the ctypes FFI in OCaml, where most of this data conversion and mediating between two data formats is automated. You start basically with a description of the C type of the C function, and you can automate some of those conversions.

[[54:05](https://youtu.be/9Cswiqrq6So?t=3245)] But sometimes it can be expensive. For instance, you may end up copying a whole array while your C code only needs to access two or three elements in it. Okay, so there's lots of trade-offs and, quite frankly, it's a dirty part of programming language implementation. The OCaml FFI is not that clean, but if you get the Java FFI, for instance, it's also quite complicated. And for Python I never tried, so I don't know what it looks like, but yeah, it's a necessity.

[[54:42](https://youtu.be/9Cswiqrq6So?t=3282)] But it can be quite hard because the data models are different between the two languages.

**Ryan:**

[[54:49](https://youtu.be/9Cswiqrq6So?t=3289)] So to kind of get the big picture, on the OCaml side, there's an interpreter, which is a program running in application space that is interpreting your OCaml code. And then at some point in the OCaml code it says, "Do some, load this C++ program." And the C++ program is a binary somewhere, and the OCaml interpreter then starts to load those instructions and execute them.

**Xavier:**

[[55:18](https://youtu.be/9Cswiqrq6So?t=3318)] Okay, so actually this is the third aspect that I didn't touch. There's an interpreter mode, but in general we compile, we compile to assembly code and then machine code. And so in compiled mode what you say is how you put together the OCaml code and the C code is done by the linker, the C linker. So basically someone else is doing that for us. And it's not that different from linking together two object files produced by C or two object files produced by OCaml, but for more interpreted languages there's also the question of how you load the C code.

[[56:07](https://youtu.be/9Cswiqrq6So?t=3367)] Generally, you use a dynamic loading interface, dlopen, for instance in Unix. And then there's a little bit of introspection. So at runtime, the interpreter queries C libraries: where is the address of a function named foo, and then it will find the address and use that to manufacture a call. So yeah, if you're in an interpreted setting or bytecode-compiled setting like Python, there's this additional level of complexity on top of it.

**Ryan:**

[[56:44](https://youtu.be/9Cswiqrq6So?t=3404)] I see, I see. Okay, so if I had a mixed OCaml program on my computer, it's just one binary or one blob in the simplest case.

**Xavier:**

[[56:57](https://youtu.be/9Cswiqrq6So?t=3417)] Yes, there are also dynamic loading facilities in OCaml, but I don't want to get into that because I'm a firm believer in static linking. I think programs should be statically linked so that there's no surprise when you run them, like, oh, where is this DLL or DLL not found, for instance, problem? But of course you lose a little bit in flexibility. But yeah, I think static linking has a lot to it. It's actually quite useful in that it warrants a lot of things. It checks a lot of things at link time that you don't have to check again at runtime.

### 57:41 — The danger of almost-correct LLM code

**Ryan:**

[[57:41](https://youtu.be/9Cswiqrq6So?t=3461)] We mentioned earlier in the conversation talking a little bit about LLM-generated code. I thought that might be interesting to cover. And in one interview you talked about the danger of almost-correct code, so plausible code, but it's wrong, that an LLM can produce. What are your thoughts on how to address that kind of problem?

**Xavier:**

[[58:05](https://youtu.be/9Cswiqrq6So?t=3485)] It's a tough problem globally. I'm a little bit skeptical about generative AI. Of course, they can do amazing things that were unthinkable a few years ago, but there's always some errors. You can't really trust what's being produced by generative AI. In principle, humans should be there to check the output and fix errors, or ask the LLM to fix its own errors until the result is actually usable.

[[58:52](https://youtu.be/9Cswiqrq6So?t=3532)] But of course it's very hard because there's a slop problem. AI produce so much, it's so easy to produce large quantities of text, of code, pictures, whatever, that in the end there's no human time to check it all. So yeah, recently I heard someone working in an AI startup who was enthusiastic about AI-generated code saying that thanks to generative AI, the cost of programming is dropping to zero.

[[59:35](https://youtu.be/9Cswiqrq6So?t=3575)] Well, the cost of writing code maybe, but what about checking it, making sure it is correct, that it does what we want? Well, that cost is not zero at all. For me, every new line of code is a liability. You have to test it, you have to check it, maybe you have to do formal verification, you have to evolve it, maintain it later. No, I don't want huge amounts of code, okay? I want 50 lines of code that have been thought through, that have been published over the years.

[[01:00:14](https://youtu.be/9Cswiqrq6So?t=3614)] So anyway, I'm not getting that with AI, and I think that's a problem. And this idea that humans will be there to check the output of generative AI is just wrong. No, they are not available for that. There's too much of it, and it's not pleasant either. Okay. I mean, I don't think it's a good way to split the world between machines and humans. So anyway, so maybe there will be some societal solution like a big no to AI slop movement.

[[01:00:53](https://youtu.be/9Cswiqrq6So?t=3653)] So we're trying to see that in some open source projects that refuse generated contributions because there's just too many. I know that, well, for OCaml and especially for CompCert have received issues that were obviously generated by AI. And there was maybe one good issue among 10 reports, and each report was several pages long, with very detailed explanations and repro case that in the end doesn't repro anything or reproduces something else.

[[01:01:31](https://youtu.be/9Cswiqrq6So?t=3691)] But it takes time to go through all those things. And maybe at some point I will say no to AI-generated contributions. Okay, but maybe there's also a bit of a technical solution, which is, as we said earlier, to have AI produce proofs, so evidence that its creation is correct. So, as I said, this is starting to work for mathematical proofs. Some generative AIs are able to produce proofs both in English and in the formal language of the Lean prover, for instance.

[[01:02:08](https://youtu.be/9Cswiqrq6So?t=3728)] And so you can get Lean to recheck the proof and get some confidence. You still need to be very careful about the statement because sometimes AIs will change the statement or the definitions to make the proof easier. That happens. And also you should be careful about so-called self formalizations, where the AI also comes up with some definitions and some statements by parsing a PDF file or whatever.

[[01:02:45](https://youtu.be/9Cswiqrq6So?t=3765)] And sometimes it introduces errors at that point. So anyway, there's still a need for human review, but on smaller quantities of text and mathematical text. And maybe one day it will also work for program proof. So when an AI generates a program, it might be able to generate some Lean proof or whatever that the program satisfies some specification. So I think it is possible. But now the question will be, where does the specification come from?

[[01:03:20](https://youtu.be/9Cswiqrq6So?t=3800)] For formal methods, that's always been a big issue. It's not just that verification is hard, but agreeing on the spec can be difficult too. And where mathematicians have a lot of experience in stating, finding definitions that they find interesting and stating theorems that they believe should be true or that will mean something, computer programmers are less good with that, and it's fairly easy to come up with specifications that are inconsistent or impossible.

[[01:04:02](https://youtu.be/9Cswiqrq6So?t=3842)] So remember this average function where there was a precondition of the three numbers, three arguments saying they must not be too big, but say maybe you can end up with a precondition that just cannot be satisfied. And at this point the body of the function will always be verified, even if it's completely wrong, because the assumption says basically this function cannot be called. And so you get a false sense of confidence: you verify something, but it's actually unusable.

[[01:04:43](https://youtu.be/9Cswiqrq6So?t=3883)] And that's a fairly delicate point where I'm not sure LLMs are going to help much. But it's a problem with formal methods in general, and some possibilities include the ability to test specifications, for instance. So instead of using your test suite to see if your code works out, you can also use it to see if your spec checks out, those kinds of things. But yeah, we are kind of moving some of the difficulties from the programming phase to the specification phase, but we still have some problems anyway, so that might be a way to deal with the AI-generated code and develop some confidence in it.

### 01:05:39 — How LLMs will change programming languages

**Ryan:**

[[01:05:39](https://youtu.be/9Cswiqrq6So?t=3939)] LLM-generated code is becoming extremely popular, and I think there's a lot of potential downstream consequences on the programming language landscape. And I thought it might be interesting to hear your thoughts on speculating. Imagine 10 years from now, if you took LLM-generated code and turned it up, how might you think that the programming language landscape might change?

**Xavier:**

[[01:06:08](https://youtu.be/9Cswiqrq6So?t=3968)] Yeah, a couple of years ago someone asked me about that, and there was a concern that the training data would be. There wouldn't be enough training data in OCaml for an LLM to really learn how to program in OCaml. And it's true that there's less OCaml code in the wild than JavaScript code, for instance, but apparently contemporary LLMs do well with the amount of OCaml code they have. Maybe because there's enough, maybe because learning has become a little more efficient, maybe because, well, there's less OCaml code than JavaScript code, but maybe the OCaml code is better quality on an average, I don't know.

[[01:07:00](https://youtu.be/9Cswiqrq6So?t=4020)] Anyway, maybe LLMs are getting better also at transferring knowledge that they've learned from one language to another. That could be. I have no idea how those things work. But yeah. So the latest feedback I've got about LLMs and generative AI and OCaml is that the OCaml code generated is quite decent and quite similar in quality to more popular languages. And one thing that seems to help the generative AI is a type system.

[[01:07:35](https://youtu.be/9Cswiqrq6So?t=4055)] So the fact that there's some static checking just of the type, it's already effective in avoiding some errors and maybe encouraging the LLM to declare types first. So give some type structure to the program. All right. And now from 10 years from now, it's difficult to guess. So will it be the more popular languages of today that will be even more popular because of generative AI? Will it be the safer languages of today that will be more popular with AI because.

[[01:08:22](https://youtu.be/9Cswiqrq6So?t=4102)] Well, because there's fewer errors. In the end, I'm hoping it will be the safer languages, but I really don't know.

**Ryan:**

[[01:08:31](https://youtu.be/9Cswiqrq6So?t=4111)] I've seen in the industry there's a few cases where because it's so easy to generate code, massive rewrites are something that would have been very infeasible in the past, but are very realizable now. So if there's an existing project where they chose a programming language for whatever reason in the past, they could translate the entire thing into another language with reasonable confidence. Given that kind of environment, which programming languages would you expect more people would switch to because they want to switch to it, but they weren't able to in the past, but now it's cheaper so they can?

**Xavier:**

[[01:09:13](https://youtu.be/9Cswiqrq6So?t=4153)] Well, so today it seems. Well, I've heard mostly about C and C++ to Rust translations, hoping that the generated Rust code will be safer. He said, I've seen at least one project when the generated Rust code is entirely in unsafe blocks. So it's really kind of line-by-line translation of the C code, but maybe it can still be used as a starting point for making it safer later.

[[01:09:46](https://youtu.be/9Cswiqrq6So?t=4186)] So, yeah, I would say today I can imagine significant efforts being done with Rust as a target language in the functional world. I'm not quite sure. Well, maybe a functional language to one of those proof assistants like Lean or Coq, because they also have programming languages, functional programming languages in them, much more restricted, but much more amenable to proof. So maybe for a few projects that could be interesting again as a first step towards a formal proof.

### 01:10:26 — Industry vs academia

**Ryan:**

[[01:10:26](https://youtu.be/9Cswiqrq6So?t=4226)] As we said earlier, when you compare industry versus academia today, where would you say most of the innovation in programming languages comes from? And also, has that changed over time?

**Xavier:**

[[01:10:41](https://youtu.be/9Cswiqrq6So?t=4241)] Well, I think most of the innovations have come from industry lately. And that wasn't the case in the early days of computer science if you think of the truly innovative languages like ALGOL, Lisp, Prolog, Smalltalk were developed in mostly academic settings. Smalltalk was Xerox PARC, which was an industrial research lab but very, very far away from industrial customers. And then there were much more practical languages and uglier languages developed typically at IBM like Fortran, COBOL, PL/I, et cetera.

[[01:11:32](https://youtu.be/9Cswiqrq6So?t=4292)] And then, so really the idea that the nice ideas come from academia, and then, well, the nice ideas from academia started to be transferred by industry much more quickly. I'm thinking of, well, C, and especially C++, and then Java, which really took ideas like object orientation and garbage collection, automatic memory management. In industry before Java, it was just crazy academics in the ivory tower that were using garbage-collected languages.

[[01:12:15](https://youtu.be/9Cswiqrq6So?t=4335)] It was completely impossible to have that in enterprise computing. And Java came, and two years later everyone was doing garbage collection and being very happy about it. And there were, well, Java also popularized type safety, bytecode verification, some pretty advanced techniques of the '90s. And if you look at further developments, I don't know, Swift for instance, popularized the idea of algebraic data types and pattern matching.

[[01:12:46](https://youtu.be/9Cswiqrq6So?t=4366)] And then Rust, well, Rust is even more spectacular, I would say, because algebraic data types, garbage collection, et cetera, those were already present in academic languages like Caml, for instance. But Rust really took very recent research results of the 2000s on safe low-level programming that were basically never implemented in any language and managed to do a consistent whole from that.

[[01:13:17](https://youtu.be/9Cswiqrq6So?t=4397)] And so I'm really admirative, and I have the impression that, well, I would have loved if Rust came out of academia, but I'm not sure it would have been possible because it's also a huge effort, and you really need the backing of a big company. But still, I'm not sad because I think it's also a very good sign that industry is interested in new programming languages. At some point in the '90s, well, pretty much when I was hired at Inria on a research position, someone who had developed first versions of OCaml, well, predecessor of OCaml, and who was working on type systems for programming languages and so on.

[[01:14:08](https://youtu.be/9Cswiqrq6So?t=4448)] But then some people told me, "There's no future in programming language research. Industry has decided it will be C forever, so deal with it. Maybe you could do software engineering and not PL research." Then Java came a few years later, showing that no, industry hasn't decided on a particular programming language. Industry is still interested in new programming languages. Industry still thinks that a new programming language can be part of the solution to software problems, and I find it extremely encouraging.

[[01:14:47](https://youtu.be/9Cswiqrq6So?t=4487)] We are not stuck with bad languages from the past where there's a lot of legacy code, of course, but there is still real interest in better languages. And I think this will continue, and I think it's good for the computing field.

### 01:15:05 — Most interesting unsolved problems

**Ryan:**

[[01:15:05](https://youtu.be/9Cswiqrq6So?t=4505)] In 2018, there was an interview that you did, and they asked you, what are the most interesting and important problems to focus on in the coming years? And you called out the difficulty of programming GPUs because they were using dialects of C, shoddy tools, and also the challenges in verifying machine-learned code, basically. And that sounds pretty relevant today, but what would you say your answer is today?

**Xavier:**

[[01:15:35](https://youtu.be/9Cswiqrq6So?t=4535)] So, yeah, I think, well, for the question of how we program massively parallel hardware, I think we've made a little bit of progress recently with things like the MLIR initiative around LLVM or some domain-specific languages like Halide, which are pretty good. Those tensor domain-specific languages for tensor computations are getting a little better, but still I find it a little bit frustrating that I cannot do, I don't know, theorem proving on a GPU.

[[01:16:10](https://youtu.be/9Cswiqrq6So?t=4570)] Absolutely no idea how to go about that, and in part by lack of an appropriate language. Okay, so I'm not ready to program the GPU pipelines at a very low level myself. And I think it's more general. I think we are not using all these GPU and highly parallel hardware as much as we could. Yeah, so verifying applications that have been learned or generated by AI or so on is still a pretty hot issue.

[[01:16:50](https://youtu.be/9Cswiqrq6So?t=4610)] Back in 2018, I was more thinking of verifying simple neural networks like those used for, I don't know, computer vision, self-driving cars, or some numerical computations like weather prediction and so on. So specialized LLMs, but you still want some guarantees about what they produce, that they cannot produce completely inconsistent outputs. For instance, there were some attempts in the last years at using static analysis tools and basically program verification tools applied to LLMs, but.

[[01:17:28](https://youtu.be/9Cswiqrq6So?t=4648)] Well, it doesn't scale. LLMs are big. Sorry, neural networks are big. And for LLMs, there is also a distinct lack of specification. You don't really know what's a good answer from an LLM. Well, you know it when you see it, but you cannot write a mathematical specification of it. So that part is probably over. What I would say are the big problems for today? Yeah, probably maintaining software quality despite AI slope, despite a lot of pressure to throw away traditional software development.

[[01:18:09](https://youtu.be/9Cswiqrq6So?t=4689)] Techniques using LLMs and AI as much as we can to do mechanized proofs, so proofs that can be checked by machines. Maybe this will be the decade of formal verification of software. We've been waiting for that for 50 years. Maybe it will finally take off.

### 01:18:30 — Top book recommendations for engineers

**Ryan:**

[[01:18:30](https://youtu.be/9Cswiqrq6So?t=4710)] What's your top book recommendation for software engineers, and why?

**Xavier:**

[[01:18:36](https://youtu.be/9Cswiqrq6So?t=4716)] This is an old one, Programming Pearls by Bentley. I think I read it when I was a PhD student, but I think it's nice as showing how very talented programmers work, how they think about their programs. It's a combination of choosing the right algorithms, expressing them clearly, knowing when to stop, when to use a simple algorithm when a more complicated one is not needed, having a sense of elegance in the code you write, having a feeling for where the problem is when the code misbehaves.

[[01:19:19](https://youtu.be/9Cswiqrq6So?t=4759)] So all those kinds of things that are hard to communicate, and I think those pearls are a very easy to read and don't use any complicated data structures, don't use any complicated language. I mean, it's kind of timeless. I think those pearls are a good illustration of that. So if you haven't read it, it's a classic, but I think it's a nice reading, nice read. The second one is a little more controversial, I guess.

[[01:19:51](https://youtu.be/9Cswiqrq6So?t=4791)] So, in How to Design Programs, which is a fairly ambitious title as well. And this comes from the Scheme community, okay. Matthias Felleisen, Robert Bruce Findler, Matthew Flatt, and Shriram Krishnamurthi. And those people have developed. Well, the Scheme community is famous for having developed pedagogical resources that are, I mean, ways to teach programming that go beyond teaching functional programming, basically. And so there were the MIT course Structure and Interpretation of Computer Programs, which was quite famous.

[[01:20:27](https://youtu.be/9Cswiqrq6So?t=4827)] And this is kind of a more modern twist on similar ideas. And I find this book interesting because, well, it really teaches you the way of functional programming or a way to functional programming. It can be very irritating sometimes, very opinionated, very almost mystical sometimes. But it's also another great attempt at trying to communicate how experienced programmers go about designing a program even before writing the first line, and then how, given a language like Scheme, which is pretty flexible, how the code kind of follows naturally, knowing what you know.

### 01:21:17 — Advice for his younger self

**Ryan:**

[[01:21:17](https://youtu.be/9Cswiqrq6So?t=4877)] Now, if you could go back to when you just started your career and give yourself some advice, what would you say?

**Xavier:**

[[01:21:27](https://youtu.be/9Cswiqrq6So?t=4887)] Sometimes I got the feeling that I specialized a little too early in programming language research, or maybe. Well, there are some topics that I didn't learn because I didn't feel like it and that I had to relearn later, or I still have to learn now that I'm almost 60 and maybe not as quick as I was back in the day. So, yeah, maybe I did specialize a little bit too early. And so I would encourage everyone who's serious about working in computing to get a fairly diverse computer science background, even for topics that look super theoretical and not very relevant to everyday jobs.

[[01:22:28](https://youtu.be/9Cswiqrq6So?t=4948)] Where we mentioned computability, for instance, the halting problem and so on, you're not going to run into that very often, but it still gives interesting perspectives, I think. And then it also helps understanding new problems, like with quantum computing. What can you do with a quantum computer that you cannot do with a normal computer? And it's time to revisit all of the classic basic complexity theory I learned earlier when I was young.

[[01:23:06](https://youtu.be/9Cswiqrq6So?t=4986)] And so, yeah, I think it's good to have this kind of background, even if it's not obvious you will be using it every day. And sometimes I wish I had taken time to accumulate a little more of this background before specializing in primary languages.

**Ryan:**

[[01:23:25](https://youtu.be/9Cswiqrq6So?t=5005)] Awesome. Well, thank you so much for your time, Xavier Leroy. I really appreciate it.

**Xavier:**

[[01:23:28](https://youtu.be/9Cswiqrq6So?t=5008)] Thank you, Ryan. That was nice.

---

LAST POINT REACHED: 01:23:28