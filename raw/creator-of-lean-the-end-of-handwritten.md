---
type: raw-transcript
slug: creator-of-lean-the-end-of-handwritten
title: "Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura"
guest: "Leonardo de Moura"
date: 2026-08-10
url: https://www.developing.dev/p/creator-of-lean-the-end-of-handwritten
fetched: 2026-08-10
complete: true
capture: verbatim
capture_note: >
  Unlike episodes 56 and 57, this one came back as a genuine word-for-word
  transcript with speaker labels and per-paragraph timestamp markers, in a
  single fetch pass covering all 12 timestamped sections from 00:28 through
  the 01:07:08 sign-off. A second targeted pass over 30:00-32:10 confirmed
  that the jump from 30:42 to 31:34 is a gap in the transcript AS PUBLISHED
  on developing.dev (roughly 50 seconds of audio with no published text),
  not a fetch truncation. No adversarial prompting was used.
---

# Episode Information

**Title:** Creator of Lean: Handwritten Math Will Change Dramatically | Leonardo de Moura

**Guest:** Leonardo de Moura

**Publish Date:** Aug 10, 2026

---

## Host's Intro

In 2024, AlphaProof from Google Deepmind broke through in competition math achieving a silver-medal in International Mathematical Olympiad (IMO). At the time, that was an impressive breakthrough by formalizing math problems in Lean and then having an LLM try to advance the proof. Lean was essentially the scaffolding for a "game" that AI could play.

More recently, frontier labs like OpenAI have been generating massive candidate proofs to unsolved problems in frontier math. Lean plays a critical role in formally verifying these proofs.

I wanted to learn more about Lean so I talked with the creator, Leonardo de Moura recently. He explained how Lean works and why LLMs plus Lean will fundamentally change how we write software and do math. Hope you enjoy this episode!

---

## Timestamps

- 00:28 - How formal verification works
- 05:21 - A new way of writing software
- 13:15 - Proof assistants vs programming languages
- 21:06 - How Lean has assisted in mathematical breakthroughs
- 32:03 - When is it worth formalizing software
- 33:29 - How Lean will impact handwritten math
- 38:55 - The Z3 theorem prover project he started
- 45:44 - The most technically challenging work of his career
- 51:10 - Lean vs its competitors
- 01:00:37 - The future of Lean
- 01:04:10 - Technical book recommendations
- 01:06:15 - Advice for his younger self

---

## Full Transcript

### 00:28 — How formal verification works

**Ryan:**

[[00:28](https://youtu.be/KzdYKeAqWhY?t=28)] There's this famous Dijkstra quote I wanted to start the conversation with. It's that program testing can be used to show the presence of bugs, but never to show their absence. And my understanding is that Lean and formalizing proofs can be used to show the absence of bugs. And so in your words, what is Lean and how do people use it to show bugs can't occur in programs?

**Leo:**

[[00:59](https://youtu.be/KzdYKeAqWhY?t=59)] Lean is a programming language. You can write code, but you can also write proofs. You can reason about your code. You can write state properties about your code and prove them. Lean gives you machine-checkable proofs. You can check your proofs and get absolute assurance they are correct. You have many checkers, independent checkers, but you should view Lean as a platform. You can write code, you can write properties about your code, and you can prove them.

**Ryan:**

[[01:30](https://youtu.be/KzdYKeAqWhY?t=90)] So could you give a concrete example? Because when I think of a proof, I think of what I learned in math. But then how do you couple that with the software that we write?

**Leo:**

[[01:42](https://youtu.be/KzdYKeAqWhY?t=102)] Yeah, it's a great question. It's not that different from proof. Lean is actually very popular for math, but for software verification, there are two very different use cases. You can reason about Lean programs. Lean is a programming language. You can write programs in Lean itself. Then a Lean program is not that different from a definition you have in math. The techniques are very similar. But if you want to verify programs written in a different programming language, there are basically two different approaches.

[[02:20](https://youtu.be/KzdYKeAqWhY?t=140)] One of them, they translate, called shallow embedding. They translate for Rust. This happens today. We have a tool called Aeneas that maps Rust into Lean, and you can verify the Lean translation. There's another technique called deep embedding, where you have the semantics. You write a semantics of the programming language of C in. And now you have a data structure that represents a C program, and you can state properties about it, almost like your programs become Lean objects that you can reason about.

**Ryan:**

[[02:58](https://youtu.be/KzdYKeAqWhY?t=178)] To make it really concrete, to give someone a sense of, here's this thing I want to prove about a simple C program. Maybe no buffer overrun or something like that. What's the step by step where we could use Lean to prove that?

**Leo:**

[[03:13](https://youtu.be/KzdYKeAqWhY?t=193)] Yeah, yeah. Let's get an array. You're trying to access an array in C. You want to make sure the index is in bounds. You're not accessing elements that your array, for example, has 10 elements. You're not trying to access element 11, right? Basically, you can write that. You can write something that says the value of i at this point in your program is going to be greater than or equal to 0 and less than 10.

[[03:44](https://youtu.be/KzdYKeAqWhY?t=224)] You can write that as a mathematical statement. Another way to view it is that if you can express in math what you care about in your program, you can verify using Lean. That's another way to view it.

**Ryan:**

[[04:02](https://youtu.be/KzdYKeAqWhY?t=242)] So I have my C source files, and then somehow there's an equivalent Lean proof that's almost like metadata on top of the C program.

**Leo:**

[[04:11](https://youtu.be/KzdYKeAqWhY?t=251)] Yes.

**Ryan:**

[[04:12](https://youtu.be/KzdYKeAqWhY?t=252)] And that's a line-by-line proof. And Lean will go and check.

**Leo:**

[[04:16](https://youtu.be/KzdYKeAqWhY?t=256)] Exactly. People will build automation for automating the process. They're going to use techniques like Hoare triples, that says like we have a precondition, some mathematical facts that should be true before executing that statement, the statement and what is true after. Right. And they will have a lot of automation to process makes your proof modular. Right. I mean, complexity is a challenge in software verification.

[[04:48](https://youtu.be/KzdYKeAqWhY?t=288)] Handling the complexity is a big deal. And all these frameworks for verifying programs, they are trying to manage the complexity, make your proofs modular, even if AI. Now AI can prove things automatically for us, but they have to be modular, the proofs, if you want them to scale.

**Ryan:**

[[05:08](https://youtu.be/KzdYKeAqWhY?t=308)] And what you're saying sounds similar to software, where you have to write it cleanly. It needs to be easy to edit and reason about. So it's almost like a second software layer on top of the software.

### 05:21 — A new way of writing software

**Leo:**

[[05:21](https://youtu.be/KzdYKeAqWhY?t=321)] Yes, yes, you can view it this way. You can also flip it and imagine a future where you're writing what you want mathematically, precisely, and AI synthesizing the code and a proof that the code that was synthesized meets your specification. Right.

**Ryan:**

[[05:42](https://youtu.be/KzdYKeAqWhY?t=342)] Oh, interesting. So you could start by writing what you want to be true and then ask the AI, please.

[[05:50](https://youtu.be/KzdYKeAqWhY?t=350)] And AI is going to just go and hammer at it until the Lean proof says you're good.

**Leo:**

[[05:55](https://youtu.be/KzdYKeAqWhY?t=355)] Yes. It feels like science fiction. Six months ago, I would say this is science fiction. But for example, now a colleague of mine, Kim Morrison, a few weeks ago, she started a project I thought was, six months ago, I would say it's not possible at all. She said, we have zlib, this compression library written in C. She says she creates a very complicated prompt for AI saying I want you to translate to Lean.

[[06:28](https://youtu.be/KzdYKeAqWhY?t=388)] Ensure the Lean version passes the test suites for zlib. Then I want you to prove that if you compress data and you decompress, you get the original data back. It's a really strong property and, believe it or not, after one week, she succeeded doing the whole thing, and now it's just asking to optimize the code. But you cannot break the proofs. You have to keep still proved all the properties you care about.

[[07:02](https://youtu.be/KzdYKeAqWhY?t=422)] I mean compressing and decompressing, getting the data back is a really important property for a compression engine. Right? Yeah, this is rich now. I mean, surreal.

**Ryan:**

[[07:16](https://youtu.be/KzdYKeAqWhY?t=436)] I mean, it's crazy. And I hear in the industry, a lot of people use a really comprehensive test suite coupled with AI to do some really amazing rewrites because they have some more confidence that the rewrite is accurate and the AI can check itself. And it sounds like a specification is even better than a comprehensive test suite.

**Leo:**

[[07:45](https://youtu.be/KzdYKeAqWhY?t=465)] Yes, because your quote from Dijkstra captures it perfectly, right? With a test suite, you can show the presence of bugs, but not their absence. It's almost like with a good test suite, you may say, well, probably there are no bugs here, but you may have a really corner case that's not covered by your test suite. But with a proof, you're covering all possible cases. So property-based testing is really popular now.

[[08:19](https://youtu.be/KzdYKeAqWhY?t=499)] People are writing properties. They want to ensure they are true, but they are checking with testing. But now we can prove them. And you say, look, there's no point testing anymore.

**Ryan:**

[[08:32](https://youtu.be/KzdYKeAqWhY?t=512)] It seems like having a well-written specification is a superset of a test suite. But in terms of the human labor required to create a reasonable test suite versus a reasonable specification, how much more work is it to come up with a great specification? It varies a lot by the program.

**Leo:**

[[09:04](https://youtu.be/KzdYKeAqWhY?t=544)] In many cases, it's not uncommon for someone to start developing a piece of software, and they don't know exactly what the spec is. But properties are usually vaguely in your mind. Another thing that I tell people to keep in mind is that an inefficient program can be viewed as a specification. Usually, writing an inefficient program is way easier than writing the super efficient one that has many clever tricks.

[[09:35](https://youtu.be/KzdYKeAqWhY?t=575)] You can write a very, this is what I want, in a very naive way. And you ask the AI, look, generate the efficient version and optimize and prove that equivalence to my inefficient one. There are many scenarios. I mean, I will not say this. Specifications are always easy to come up with. But properties, usually the developers have good ideas about properties they care about. An inefficient program is a spec, right?

[[10:08](https://youtu.be/KzdYKeAqWhY?t=608)] You can view it as a specification, and the technology form of verification complements testing, right? I think your quote from Dijkstra captures...

**Ryan:**

[[10:19](https://youtu.be/KzdYKeAqWhY?t=619)] Perfectly, and I think I saw this on Twitter because Jane Street was more heavily investing in formal verification, and I read their post, and they talked about this. I think it was seL4 or some software that was entirely formally verified.

**Leo:**

[[10:37](https://youtu.be/KzdYKeAqWhY?t=637)] Yes.

**Ryan:**

[[10:38](https://youtu.be/KzdYKeAqWhY?t=638)] And the main drawback to why it wasn't. You know how much more time would it take writing a program versus verifying it?

**Leo:**

[[10:48](https://youtu.be/KzdYKeAqWhY?t=648)] Your example, seL4, is a great example. This was a major milestone. It's a microkernel they verified manually before AI. This project was done before AI was a big deal, and the cost is super expensive, right? At AWS, we have been using formal verification for decades, but only for the super-safe, critical components because it's expensive. Until now, right? With AI, it changes the game.

[[11:21](https://youtu.be/KzdYKeAqWhY?t=681)] You have to come up with a spec. But this is not the most painful part. The most painful part is developing the proofs manually. If you have tools before AI and maintain the proofs as you change the code, it's messing you up. I've seen people complaining that, "Oh, I changed the program. Right now I have a bunch of failures in my test suites, and I have to patch them one by one." Imagine with proofs, it's the same process.

[[11:50](https://youtu.be/KzdYKeAqWhY?t=710)] You have to fix the proofs. Sometimes you don't remember anymore why. What's the story behind this proof? It's a lot. But AI is extremely good at proving, writing formal proofs, maintaining formal proofs. For example, yesterday I was changing something. I want to modify some proofs for technical reasons. I didn't even know what the proofs were about. Someone else wrote. Then I said, look, I want you to—I asked AI to rewrite these proofs without using this feature because I'm going to change it.

[[12:31](https://youtu.be/KzdYKeAqWhY?t=751)] I don't want to break the libraries instantly. It came up with the new proofs for me. I mean, it's really good. And this is crucial for making formal verification mainstream because otherwise maintaining the proofs was almost like if your program took X amount of time to do the formal verification in the past, it would take 10x. That would be normal. But imagine if your program is changing. That's something that's really common now.

[[13:05](https://youtu.be/KzdYKeAqWhY?t=785)] You have to keep maintaining the proofs too. It's a lot of work. But AI eliminates this pain for us.

### 13:15 — Proof assistants vs programming languages

**Ryan:**

[[13:15](https://youtu.be/KzdYKeAqWhY?t=795)] You mentioned that Lean is a proof assistant, and then you also said it's a programming language. Is that typical for proof assistants to be both a programming language and a proof assistant?

**Leo:**

[[13:30](https://youtu.be/KzdYKeAqWhY?t=810)] Some of them, especially the ones that are based on dependent type theory, they are like Rocq and Lean — programming languages and proof assistants, right? You can write definitions like when you're defining concepts in math. But some of these definitions can be programs, and you have types, you have structures. It's a programming language, but it's in the family of what's called functional programming languages.

[[14:01](https://youtu.be/KzdYKeAqWhY?t=841)] I mean, is it a specific kind of programming language for people that are familiar with programming languages like Haskell? Lean is close to Haskell, but with the support for proofs. That's a way to view Lean.

**Ryan:**

[[14:16](https://youtu.be/KzdYKeAqWhY?t=856)] Are there major use cases where people use it as a programming language but not as a proof assistant?

**Leo:**

[[14:21](https://youtu.be/KzdYKeAqWhY?t=861)] Well, the first big use case is Lean is implemented in Lean. We have many of our tooling implemented in Lean. Like the documentation authoring system called Verso is implemented in Lean. The build system that's called Lake, like Lean make, is implemented in Lean. At AWS, we have a compiler for AI accelerators. It's half a million lines of Lean and using Lean as a programming language. They're proving some properties about the program using Lean.

[[14:54](https://youtu.be/KzdYKeAqWhY?t=894)] But the main goal is to use Lean as a programming language. In this project, the proofs are like a bonus that you can get the proofs and find problems in the design.

**Ryan:**

[[15:06](https://youtu.be/KzdYKeAqWhY?t=906)] I think most people are familiar with programming languages and the toolchains they have. But what are all the major components that you would need for a proof assistant?

**Leo:**

[[15:19](https://youtu.be/KzdYKeAqWhY?t=919)] It is not that different. I mean, if you're used to modern programming languages like Rust, the tooling, for example, Lake is our Cargo, right? I mean, you're going to open Visual Studio Code the same way. And I want to get all the IntelliSense. One big difference is that we have something called the Infoview in Lean. Your screen usually is going to be split in two. You have your file on the right-hand side, you have the Infoview that tells you information about your proofs, about your code.

[[15:55](https://youtu.be/KzdYKeAqWhY?t=955)] It's giving you constant feedback about your development. That's basically the main difference. But the tooling, VS Code, everything works the same way.

**Ryan:**

[[16:06](https://youtu.be/KzdYKeAqWhY?t=966)] I mean, it seems like the programming language is the fundamental layer, and then there's some additional layer on top that keeps track of that stuff.

**Leo:**

[[16:14](https://youtu.be/KzdYKeAqWhY?t=974)] Good question. In Lean you have definitions that show your program, but you have theorem statements. You're going to say, for example, factorial is always greater than or equal to zero, or something like that. Or if you add two even numbers, you get an even number. You can write statements like that, and immediately you can write actually a program that's the proof. But most people don't do that. They go into something called tactic mode.

[[16:47](https://youtu.be/KzdYKeAqWhY?t=1007)] You can view it as a domain-specific language for writing proofs. When you write "by," it switches to this domain-specific language, and you have steps like "simplify my goal," the state of my proof. You can say, "Oh, apply this rewriting step." Apply, for example, we know that x + 0 equals x. You can ask Lean to apply this rewriting, and you're going to see in the Infoview the state of the proof changing. You get immediate feedback, and you get this feeling that you said.

[[17:21](https://youtu.be/KzdYKeAqWhY?t=1041)] You keep telling it, applying transformations to your proof step by step. You can see what's happening until you get no goals left. You are done; the proof is complete. And some people view this process as a game. I have users that told me, "You built my favorite computer game." That's funny.

**Ryan:**

[[17:46](https://youtu.be/KzdYKeAqWhY?t=1066)] Is Lean itself verified in Lean?

**Leo:**

[[17:49](https://youtu.be/KzdYKeAqWhY?t=1069)] Lean is a massive program. You only have to trust the kernel, where the proofs are checked. Lean itself is the kind of program that, because there are so many new things we are adding, it's not even clear what the specification is. For example, what is the specification of a simplifier? You can write general ideas, but users want to be able to customize the behavior. They keep asking; they keep changing the specification all the time.

[[18:18](https://youtu.be/KzdYKeAqWhY?t=1098)] I want this, I want that. No, at this knob here. So it's really hard to have a full specification of Lean, but the kernel is possible to have a specification. We have a kernel. The kernel that comes with Lean is not verified. But there are other kernels that you can use. One of them is implemented by Mario Carneiro. It's called Lean for Lean, and it's implemented in Lean. And he's verifying, it's proving that this kernel has been verified with respect to the semantics of Lean.

[[18:52](https://youtu.be/KzdYKeAqWhY?t=1132)] This is a cool project, but for us, having multiple kernels is the best way to ensure that your results are correct. Some users implement their own kernels. We have kernels implemented in Rust in different programming languages.

**Ryan:**

[[19:10](https://youtu.be/KzdYKeAqWhY?t=1150)] And when you say kernel, what's the responsibility, or what's the input and output of that portion?

**Leo:**

[[19:16](https://youtu.be/KzdYKeAqWhY?t=1156)] Yes, in Lean, proof checking is type checking. These kernels, they are type checking your programs. Basically, you can export your Lean developments. You get a big blob, and you read this blob, and they're going to check it. When you say we have a proofing link, basically you have a term that has a type, and you're checking if the type of this term matches the type that you claim it has. For example, the example for the even numbers, this is a typing link saying that the sum of two even numbers is an even number.

[[19:57](https://youtu.be/KzdYKeAqWhY?t=1197)] You can view that it is exactly a typing link. And the proof, what the kernel is checking is whether the type of the proof matches the type you claim this term has. The kernel will check, you do this type checking. The kernels vary between high-performance kernel. It's like 5,000 lines of code. I mean, the goal of the kernel should be something you can write yourself. Of course, sometimes people put bells and whistles. One thing concerns people have is like, okay, but how do I know?

[[20:39](https://youtu.be/KzdYKeAqWhY?t=1239)] Suppose that I wrote Fermat's Last Theorem in Lean. How do you know that when you export it, it's really Fermat's Last Theorem? It's not 2 plus 3 equals 4. I mean, and people, some external kernels, they write print printers. I mean, it will print the statements that have been proved, all the dependencies. You can have all these fancy tools to make sure you're not being misled.

### 21:06 — How Lean has assisted in mathematical breakthroughs

**Ryan:**

[[21:06](https://youtu.be/KzdYKeAqWhY?t=1266)] Lean, obviously, it's so powerful, and I see on social media all these amazing results from formal verification. What are the top ones that you think of, or top examples more recently, that have impressed you that Lean was able to accomplish?

**Leo:**

[[21:25](https://youtu.be/KzdYKeAqWhY?t=1285)] Well, there are so many. I mean, I thought it was impossible. For example, getting a gold medal in the International Mathematical Olympiad a few years ago, everybody thought it was impossible. Now everybody use it as a benchmark of an easy problem. They say, oh, this is like an IMO problem. I mean, this is easy, but it's not. I mean, these are really challenging problems. The other conjectures that people close using AI with Lean also impresses me.

[[21:59](https://youtu.be/KzdYKeAqWhY?t=1319)] There is this unit distance conjecture for others. First, OpenAI proved using formal was not formal. And we have a system now in Lean. It's a website where we call Lean Eval, where we collect challenges. The same Kim Morrison saw this proof OpenAI, and she put on Lean Eval a challenge saying, okay, I want to see someone formalizing. We knew it was huge to formalize. It's serious math. It depends on.

[[22:38](https://youtu.be/KzdYKeAqWhY?t=1358)] And Boris Alexeev from OpenAI, he did, he made a 1 million line proof for formal proofing Lean for this conjecture. We estimate something though that background math that is needed for the proof. We knew it would take months, I mean for experts to do by hand.

**Ryan:**

[[22:58](https://youtu.be/KzdYKeAqWhY?t=1378)] I mean, how long did it take in that case? Like the time from when the proof came out to when the challenge was solved on Lean.

**Leo:**

[[23:06](https://youtu.be/KzdYKeAqWhY?t=1386)] I think it was one month, yeah. And after Kim was a few, I think less than two weeks. After Kim puts as a challenge only involved, it took I think two weeks to get the, or less. I mean, that's insane. Yes. Yeah, yeah.

**Ryan:**

[[23:24](https://youtu.be/KzdYKeAqWhY?t=1404)] We talked about verifying programs, but also there's using it just directly for mathematics, like in this case. How popular is Lean in terms of when you look at the users of Lean? What percent are using it for software engineering? What percent are using it more for just direct math?

**Leo:**

[[23:44](https://youtu.be/KzdYKeAqWhY?t=1424)] Well, historically Lean got popular first with math, right? I mean, with the beginning of the Lean mathematical library in 2017, we had a big project called Liquid Tensor Experiment. It started beginning of 2020. It was a big deal because it was to verify a result from a Fields Medalist, Peter Scholze. It was a result he was unsure about. He has not published it. He felt like this was one of the most important results in his career.

[[24:22](https://youtu.be/KzdYKeAqWhY?t=1462)] He wanted to be sure it was correct. It was done manually. The verification was a big deal because the team that formalized it, led by Johan Commelin, not only formalized the results without fully understanding it, they did not fully understand the proof. But having this Infoview helped guide them. Step by step, they formalized and simplified the proof without fully understanding the proof. It's mind boggling.

[[24:54](https://youtu.be/KzdYKeAqWhY?t=1494)] How can you simplify a proof from one of the greatest living mathematicians without fully understanding it? I mean, but they managed to simplify. It's almost like when people do refactoring code, you start changing the code. It's faster now, but the programmer doesn't really know why it felt like that. It's like you have a gut feeling, I mean, that you're going in the right direction. And this, for us at the time, lots of people got excited about Lean, the math community, because of this project. It's shown that it's not about verifying, but enabling people to work together in large numbers.

[[25:36](https://youtu.be/KzdYKeAqWhY?t=1536)] Because you can trust, you don't need to trust someone else's proof. Right. They can fill holes for you. This was, I mean, what attracts a lot of attention from the math community. Then came Terence Tao. He starts using Lean after this project. He has really cool projects with and without AI. He got addicted, actually. I think the first time he used it, he said, "I don't think I'm going to do it again." The formal proof, one week later he had another project using Lean, and he did a new result he had.

**Ryan:**

[[26:13](https://youtu.be/KzdYKeAqWhY?t=1573)] When you say addicted, you mean because of that game, that completion engine.

**Leo:**

[[26:17](https://youtu.be/KzdYKeAqWhY?t=1577)] Yeah. Some people, I feel, we feel like when I talk to professors that use Lean for teaching, they tell me that the class is more or less split. Some people love it, some people don't like it. But people that like problem solving, people that get medals in the IMO, they love Lean because you get this excitement of solving. It's like solving millions of really hard Sudoku problems, right? And you can keep solving one, and it's easy to get.

[[26:49](https://youtu.be/KzdYKeAqWhY?t=1609)] I mean, I'm a Lean developer, not a Lean user. But when you're developing Lean, I'm coding in Lean, and sometimes I have proved things. It's really easy to get addicted. You get lost proving things. You get this buzz every time you prove something.

**Ryan:**

[[27:07](https://youtu.be/KzdYKeAqWhY?t=1627)] You mentioned the IMO gold medals. How is Lean used in that kind of... I think maybe you're referring to AlphaProof by DeepMind, or maybe something else.

**Leo:**

[[27:17](https://youtu.be/KzdYKeAqWhY?t=1637)] Yes, DeepMind was. They got in 2024 was a big surprise. In 2024 they got a silver medal. And now we have gold medals from startups like Harmonic. ByteDance got a medal. I never imagined. ByteDance. They're behind TikTok. Right. I didn't even know they care about IMO math, but they have a 400 math team. They got medals. Also their prover is really good.

**Ryan:**

[[27:48](https://youtu.be/KzdYKeAqWhY?t=1668)] So how's it work? Let's say, I mean, there's a series of math problems. Lean is just used for verification, right? So I imagine there's other components there.

**Leo:**

[[27:57](https://youtu.be/KzdYKeAqWhY?t=1677)] Yeah, there's the AI. You can view it like we have Google. That was very popular with AI. The AI is playing the game. I told you that. Many people see Lean, I guess. It's the same. The AI is viewing Lean, I guess. They have the statements of what you want to prove. You have the by keywords. Now you have a blank field. Make sure that you have no goals left. It keeps applying steps in this game and seeing the state of the board.

[[28:30](https://youtu.be/KzdYKeAqWhY?t=1710)] That's the Infoview changing. In the AI, they use reinforcement learning to try to get to no goals left. It's a single-player game. Some people play together these days, but the AI is learning to play the game.

**Ryan:**

[[28:49](https://youtu.be/KzdYKeAqWhY?t=1729)] So before we were talking about that game, it kind of starts with the specification. So in that case, then the problem is kind of the specification, and then it hammers over the problem.

**Leo:**

[[29:00](https://youtu.be/KzdYKeAqWhY?t=1740)] Yeah. You have basically, for each problem in the International Mathematical Olympiad, someone translates the statements to Lean. It's super important to have the mathematical library because you want to be able to talk about the problems, right? For example, suppose the problem uses the real numbers. You need a definition in Lean, and we have it inside of mathlib, the Lean mathematical library. The first thing you have to do is be able to write the problems in Lean.

[[29:27](https://youtu.be/KzdYKeAqWhY?t=1767)] And this now because of mathlib, it's the easy part. And after that you have to provide the proofs. I mean, sometimes some problems you have to come up with a definition to some objects you have to create that has some property. But yeah, that's how it is.

**Ryan:**

[[29:47](https://youtu.be/KzdYKeAqWhY?t=1787)] I remember you said one of the first use cases of Lean was this Fields Medalist had this novel mathematics, and then we used Lean to verify it. But can Lean be used with LLMs to generate novel mathematics, or just verify existing?

**Leo:**

[[30:08](https://youtu.be/KzdYKeAqWhY?t=1808)] It's a good question. I mean, we don't see lots of evidence. We see no evidence it can find novel proofs, right? But coming up with new mathematical concepts is still at the limits, right? I mean, right now in this Lean Eval, we have challenges where the AI has to come up with the objects themselves, right? I mean, but this is. People will keep investing in this area. I would not bet against AI here.

[[30:42](https://youtu.be/KzdYKeAqWhY?t=1842)] I mean, but right now we don't have evidence they can come up with new math.

**Ryan:**

[[31:34](https://youtu.be/KzdYKeAqWhY?t=1894)] When I see on Twitter this major conjecture, they made headway on it. It's that they made headway on confirming something or disproving.

**Leo:**

[[31:43](https://youtu.be/KzdYKeAqWhY?t=1903)] They also have these 1 million lines. They showed the conjecture was false. They have a proof showing that it's false, but it's a formal proof. They did not come up with a new theory or anything like that. They are coming up with a proof, right?

### 32:03 — When is it worth formalizing software

**Ryan:**

[[32:03](https://youtu.be/KzdYKeAqWhY?t=1923)] And at what point would you say someone should evaluate formalizing something in Lean?

**Leo:**

[[32:12](https://youtu.be/KzdYKeAqWhY?t=1932)] I think if it's safety-critical or if you don't understand it really well, I mean this is an important part. I don't really understand. Anybody that went through the process of formalizing something understands the subject way better after that. I almost feel like I remember when I was in college, people would say, wow, after I implemented this algorithm, now I understand it much better. The next level is that you implement the algorithm, you prove the properties you expect, your level of understanding grows.

[[32:52](https://youtu.be/KzdYKeAqWhY?t=1972)] Another cool thing is that it enables you to be much more bold on your optimizations, because sometimes I've seen that all the time. People fear implementing optimization because they don't really understand why the piece of software works. They feel like if I do, that still works and it's faster. But they are not confident with proofs. You eliminate this discomfort, right? You can prove it again, or the AI can prove it for you or find a counterexample.

[[33:26](https://youtu.be/KzdYKeAqWhY?t=2006)] They are good at both things.

### 33:29 — How Lean will impact handwritten math

**Ryan:**

[[33:29](https://youtu.be/KzdYKeAqWhY?t=2009)] But if you were to speculate or draw into the future, maybe three to five years from now, if the cost of formalizing things goes down, how does that change software? How does that change handwritten math?

**Leo:**

[[33:46](https://youtu.be/KzdYKeAqWhY?t=2026)] Oh, I think it would change dramatically. We have to keep in mind the big labs, they only started training for formal verification and Lean very recently. Seriously, before that, it was like, oh, is in the data sets. I mean, you don't really have the reinforcement learning pipelines to optimize the behavior we see today. That is already amazing. Will get way better in the future. The costs will reduce. Programming languages like Lean and Rocq will become more mainstream.

[[34:23](https://youtu.be/KzdYKeAqWhY?t=2063)] Because of that, many people are not so, in the past, people say, "Oh, functional programming, I don't like it." But if I'm not the one that's writing most of the code anyway, it doesn't really matter. What matters? The specification level, right? It doesn't really matter how the code has been written. Yeah, I think you change a lot because of that. At least that's the direction we are pushing Lean to.

**Ryan:**

[[34:53](https://youtu.be/KzdYKeAqWhY?t=2093)] What about, let's say, 10 years from now? Lean is, everything's going really well with Lean. Could that be the end of handwritten math or handwritten proofs?

**Leo:**

[[35:07](https://youtu.be/KzdYKeAqWhY?t=2107)] I think there will always be aspects that are handwritten. Some people like to make a proof look. They want to use the proof as an artifact. You communicate ideas to others. I can't imagine there will always be people polishing, making them super easy to understand for another human to communicate ideas to other people. There will always be people like that. The same way today we have people that, we have machines that build furniture, but people, they like to create them by hand and polish them, make them perfect.

[[35:51](https://youtu.be/KzdYKeAqWhY?t=2151)] This will always exist, but it will be a mixture. I will be surprised if there is someone who's completely AI is not in their workflow somehow. Right. I mean, there'll be hybrids, many hybrids. Some people feel uncomfortable about this future, but for me, it's super exciting because I view developing software as a super painful process. And with AI, it's crazy how it brings you awareness of how many steps are just repetitive and there's no creativity, or just patching things.

[[36:37](https://youtu.be/KzdYKeAqWhY?t=2197)] And AI automates and removes lots of this pain, right? I mean, I cannot go back to that. I'm looking forward to this future you describe.

**Ryan:**

[[36:50](https://youtu.be/KzdYKeAqWhY?t=2210)] Yeah, I guess the thing that gives people. I mean, I'm guessing the discomfort is the worry that if it kept going, then we need less mathematicians or less computer scientists or something like that.

**Leo:**

[[37:05](https://youtu.be/KzdYKeAqWhY?t=2225)] People don't see that AI can bring more people. There's also the specification. I mean, I see people saying, oh, we are going to leave AI, we come up with new math. But if there's no connection to our world, this is some alien thing that's going by itself. You need an interface, for example. We want to build programs because we want to accomplish something. This something, whatever it is, has a specification.

[[37:39](https://youtu.be/KzdYKeAqWhY?t=2259)] There will always be humans in the loop saying this is what we know, this is what we want, writing this interface, interacting with the AI. The AI will have math libraries and everything to prove things about these programs we are writing, these artifacts, whatever we are trying to build. But we have to be able to interact with these libraries. We have to understand the abstractions that are there.

[[38:12](https://youtu.be/KzdYKeAqWhY?t=2292)] I don't see humans being eliminated. We are always going to be there. We are in the interface, we are telling them what we want. Specifications will be there. I can see people always writing code. Another thing is, a lot of people like to write this, and love coding. My interpretation is they love to write prototypes. This is fun. This is the fun part, to try a new idea. But to transform it into a product is never fun.

[[38:45](https://youtu.be/KzdYKeAqWhY?t=2325)] I can tell you it's never fun. And I can take over these parts. Nobody really likes doing outside of Lean.

### 38:55 — The Z3 theorem prover project he started

**Ryan:**

[[38:55](https://youtu.be/KzdYKeAqWhY?t=2335)] I know you worked on the Z3 SMT solver, and that sounds like a really difficult thing to build. So first, what is that solver in your words? And yeah, how does it differ from a SAT solver?

**Leo:**

[[39:10](https://youtu.be/KzdYKeAqWhY?t=2350)] Yeah, I started this really long time ago. It's going to be, yeah, 20 years ago I started Z3, I mean when I joined Microsoft Research. Yeah, Z3 is an SMT solver. Like I said, solver. But you have background theories, like you have support for arithmetic, for arrays. These are not random choices, right? This is because we use it for doing test case generation, software verification. Z3 is fully automated. It's a push button.

[[39:45](https://youtu.be/KzdYKeAqWhY?t=2385)] Although Lean and Z3 are called theorem provers, they are completely different beasts. Z3 is fully automatic. Lean is interactive. It has automation, but it's interactive. Z3 is not a programming language, it's more like a constraint solver. It turns out you can prove simple things about it. You cannot do advanced math with abstract math. You can solve constraints with Z3.

**Ryan:**

[[40:16](https://youtu.be/KzdYKeAqWhY?t=2416)] What's an example of the inputs to this SMT solver, and what do you get out of it?

**Leo:**

[[40:22](https://youtu.be/KzdYKeAqWhY?t=2422)] Oh, I can give you one. I mean that's even in the Z3 manual. You can encode a Sudoku problem as a set of constraints, and you can ask Z3 to solve it. It will give you back the answer instantaneously. For real applications, Z3 was used very successfully for finding bugs in software. People would convert. For example, suppose that you have a path in your code. You know that has a security vulnerability, but you don't know which inputs to the program allow you to execute this path.

[[40:58](https://youtu.be/KzdYKeAqWhY?t=2458)] You can convert that into a set of constraints that you send to Z3, and it will say unsatisfiable. It means it's impossible to execute this path and you are happy. Or it gives you back an example saying, look, with these inputs you're going to be able to do it. And people use it for doing software verification. But because the problem becomes undecidable at that level, you have many universal quantifiers for stating properties about your program, your pre- and postconditions.

[[41:35](https://youtu.be/KzdYKeAqWhY?t=2495)] The solver has heuristics, and this was all before AI. The heuristics were hand coded. They would always fail. And for simple things, people would be very happy with the fact that Z3 is push button. But when the property is not trivial, they would come back saying, "Come on, I know the proof. I mean, why can't Z3 find it?" That's why Lean started. I started Lean to make sure that we would have a system that's really good for software verification, right?

[[42:07](https://youtu.be/KzdYKeAqWhY?t=2527)] Z3 was successful for finding bugs, but not so much for software, for proving the absence of bugs. It was never super successful there. But Lean was born to fill this gap.

**Ryan:**

[[42:25](https://youtu.be/KzdYKeAqWhY?t=2545)] You said undecidable, but in practice, in the real world, if you run it, does it typically terminate?

**Leo:**

[[42:32](https://youtu.be/KzdYKeAqWhY?t=2552)] Yeah, great question. Z3 goes the whole complexity ladder, right? You have SAT solvers, you have NP-complete, PSPACE-complete, EXPTIME-complete, you have the whole two undecidable rights. I mean, surprisingly, even for SAT solvers, you can write really tiny SAT problems that are really hard to solve. No SAT solver will solve them. But in practice, the problems we get for hardware verification, especially if you bound everything, say, oh, I'm trying to look for a bug in the first 10 steps, right?

[[43:13](https://youtu.be/KzdYKeAqWhY?t=2593)] Everything's bounded. You're not trying to prove, but you're trying to capture a class, like a space of scenarios, right? They are very effective there. I mean, I think the lesson there is that programs and hardware, they are not correct for esoteric reasons, right? They are correct because for very simple reasons. I mean, that's why these tools are super effective there. Yeah, but when you get too undecidable and you're trying to prove, even if the property is not trivial there, I mean, it runs out of steam.

[[43:56](https://youtu.be/KzdYKeAqWhY?t=2636)] I mean, and they time out frequently. And sometimes there is a colleague of mine here at Amazon, Iminator chose the name proof instability because sometimes if you change the problem, you just flip. You have A and B, you write B and A, where B and A are complicated formulas, you may fail to prove. And when she was just trying to maintain things, proofs would break if using this kind of technology.

[[44:28](https://youtu.be/KzdYKeAqWhY?t=2668)] But with Lean, she switches to Lean, and it's super smooth, right? Because you're controlling the proof in the Lean case.

**Ryan:**

[[44:40](https://youtu.be/KzdYKeAqWhY?t=2680)] Why is it so much more efficient?

**Leo:**

[[44:43](https://youtu.be/KzdYKeAqWhY?t=2683)] Your proof is basically, you can view the sequence of steps for solving the problem. In Z3, you can view that you have only one proof step, solve, right? I mean, you're saying you have options to solve goals, but you have very little. You cannot influence what Z3 is going to do. It's much harder to influence this kind of system. In Lean, if you want to give a step, super detailed, step-by-step proof, you can. You can use proof automation like is available in Z3, but you can also break it down step by step.

[[45:25](https://youtu.be/KzdYKeAqWhY?t=2725)] And the fact you can do that, humans can do it. But the happy surprise is that AI can do it because now you can say step by step why something is true. The AI can convince Lean that it can provide a proof.

### 45:44 — The most technically challenging work of his career

**Ryan:**

[[45:44](https://youtu.be/KzdYKeAqWhY?t=2744)] When you were working on Z3 and Lean, what was the most technically challenging part that you had to build for either project?

**Leo:**

[[45:55](https://youtu.be/KzdYKeAqWhY?t=2755)] I underestimated how much harder Lean is in comparison to Z3. It's always a magnitude harder. I mean, I talked to many colleagues about that, why I felt like this Lean was so much harder. I think it's the surface. The interface for humans is way fuzzier. You have a defined language for it. It's called SMT-LIB. It's a very simple language. It's not meant for humans; it's meant for tools. I mean, Z3 is used as the backend of many different tools.

[[46:32](https://youtu.be/KzdYKeAqWhY?t=2792)] Someone generates some program generating input for Z3, and people expect a counterexample or saying it's impossible, it's unsatisfiable to come up with a counterexample. The interface is really, really simple, right? You can view Z3 as a command-line tool that you pass this file on this very low-level language that's super easy to parse, and you come back with yes or no. And Lean is a programming language.

[[47:04](https://youtu.be/KzdYKeAqWhY?t=2824)] You have libraries, you have mechanisms, you have interactivity, you have user interface, you have LSP, you have build system, you have GitHub. You have, it is so vast. That's another challenging part for me. As I mentioned, Z3 was a backend. The Z3 users are very sophisticated software developers, people that speak the same language I speak. It's way easier to talk to people that speak the same language.

[[47:41](https://youtu.be/KzdYKeAqWhY?t=2861)] With Lean, it's completely different. The first users are all math people. They have a completely different background, different expectations, different everything, and different community. And then you have people that want to choose Lean as a programming language. I'm not a programming language person. My background is automated reasoning. And yeah, it's a different language, different expectations.

**Ryan:**

[[48:11](https://youtu.be/KzdYKeAqWhY?t=2891)] Was there a singular component that was just really technically challenging?

**Leo:**

[[48:18](https://youtu.be/KzdYKeAqWhY?t=2898)] I told you that Lean's implemented in Lean. Of course, it was not always like that, right? I mean, it had to be implemented in something else at the beginning. The switch from originally was C++. The switch from C++ to Lean was extremely painful. Really? Really. I remember I literally wanted to cry when I managed to compile Lean 4. I was just... Sebastian Ulrich and I at the time were building Lean 4 together.

[[48:56](https://youtu.be/KzdYKeAqWhY?t=2936)] But this was before we had a nonprofit for Lean. I remember calling him and I said, wow, man, insane. Say, are you not excited? He said, yes, I am. I mean, super excited.

**Ryan:**

[[49:13](https://youtu.be/KzdYKeAqWhY?t=2953)] What made that switch hard?

**Leo:**

[[49:16](https://youtu.be/KzdYKeAqWhY?t=2956)] The first thing is, imagine you're going to implement the language in itself. The first thing you want is to minimize the number of features as much as possible, is that you want to implement Lean using bare-bones features. Because you're going to have to be able to compile it with itself then. Now you have like 100,000 lines, more or less. I don't know the exact number, but it was around 100,000 lines.

[[49:48](https://youtu.be/KzdYKeAqWhY?t=2988)] And you start trying to compile, you fail the first. You can't even compile the first file in the pipeline, the one that more than 1,000, and the first one fails, then you fix the bug, you can compile the first one, then you can compile the second, and you keep moving, and you are always finding discrepancies between the new and the old one. And you're trying to reconcile, make things easier for the new one because you want to replace the old one.

[[50:22](https://youtu.be/KzdYKeAqWhY?t=3022)] This process and Lean is a complicated language because of these dependent type theory and so on. The proofs, for example, when you're implementing Lean, you still need some proofs there. There are some basic proofs you need, but you have to construct these proofs with no interactivity, nothing. Bare bones. You have to provide the proof too. It's almost like programming in assembly. The proof. This was also super painful.

[[50:55](https://youtu.be/KzdYKeAqWhY?t=3055)] Thank God. Yeah. But it took. Yeah. Many people thought we were going to fail. Sebastian, I would not be able to do it.

**Ryan:**

[[51:05](https://youtu.be/KzdYKeAqWhY?t=3065)] 100,000 lines is a lot, like all human written.

**Leo:**

[[51:07](https://youtu.be/KzdYKeAqWhY?t=3067)] Yes, all human written. Yeah.

### 51:10 — Lean vs its competitors

**Ryan:**

[[51:10](https://youtu.be/KzdYKeAqWhY?t=3070)] We talked a lot about Lean, and I know there are competitors to Lean. What are the pros and cons of the different proof assistants? In what scenarios is one preferred over the others?

**Leo:**

[[51:23](https://youtu.be/KzdYKeAqWhY?t=3083)] For instance, the first disclaimer: I'm a completely biased person here, right? But I can tell you what users tell me about. For example, one thing users love is the fact that Lean is super extensible. Because Lean is implemented in Lean, you can add extensions. So imagine you're doing your math proof. In the middle of this math proof, you say, oh, I want this fancy automation here. You can write in the same file, or the AI can write for you, the extension for automating a proof.

[[51:57](https://youtu.be/KzdYKeAqWhY?t=3117)] And it will do it. I mean, even the AIs, they know about the fact that Lean is extensible. If I ask the AI to isolate an issue in Lean, I give the AI a Lean file. It will start writing a Lean metaprogram, a program about Lean tunnels to validate the conjecture it has about why it doesn't work. It's crazy. It keeps writing Lean meta extension there. The fact that Lean's extension is popular, really popular with so many people.

[[52:33](https://youtu.be/KzdYKeAqWhY?t=3153)] For example, there is Patrick Massot. He's a French mathematician. He wrote something called Lean Verbose. Lean Verbose you can use for teaching. We have this language for writing the proofs, but he made the language look like English, and he has the Infoview now. You can click there. It gives you suggestions about the next move that's written in structured English, like you find in a textbook.

[[53:07](https://youtu.be/KzdYKeAqWhY?t=3187)] You see, the student has a really good idea on how to write informal math proofs. And he did that without asking me any questions. I mean, all this stuff, the point and click, the new language, the new interactivity, he did all by himself. He's not a computer scientist. He has a math degree and he does all this stuff. And it's for English and French. I mean, you can choose, you can write the proofs in French and it looks like textbook proof.

[[53:41](https://youtu.be/KzdYKeAqWhY?t=3221)] I mean, there are people that write visualizations. You're trying to prove something about a math object. You can write extensions that visualize these objects in your Infoview. The people that write new domain-specific languages embedded in Lean for different purposes. For example, for protocol verification there is a language called Veil. It's a Lean file. You open Veil, you feel like it's a different system for protocol verification, but it's just a Lean file with these extensions for protocol verification, the language for writing protocols in a very convenient way.

[[54:25](https://youtu.be/KzdYKeAqWhY?t=3265)] These folks wrote the whole thing without ever talking to us. They all talked to us after they had done it, said, "Look, I want this part of Lean to be faster." That was the only interaction we had. And so interactivity is a big deal. Another big deal now is the mathematical library. It's vast. I mean, for stating problems, open conjectures, you need a library with the concepts to even state the problem.

[[54:56](https://youtu.be/KzdYKeAqWhY?t=3296)] So Lean has a massive library and a massive community. The community also plays a big role. Before AI, I think now most people ask questions about Lean to AI. But in the past, people would go to the Lean Zulip channel, ask a question about Lean. They would get an answer in five minutes. People would say human beats AI. I mean, people would be writing answers instantaneously to your problems. The community played a big role.

[[55:29](https://youtu.be/KzdYKeAqWhY?t=3329)] Another one was we listen to our users. I mean the math. I mean if you talk, for example, Jeremy Avigad was the first user. I mean he has math backgrounds. You ask him, look, he said, look, I could ask anything, any new feature, I would get back the same day. I mean fix the new feature same day. And this attracts people, right? I mean, because you're making people improvements, making sure the system does what they want, they come back for more.

[[56:10](https://youtu.be/KzdYKeAqWhY?t=3370)] I mean, this also has a huge impact in growing the community.

**Ryan:**

[[56:16](https://youtu.be/KzdYKeAqWhY?t=3376)] When I was doing some research, there was this idea I think you mentioned in this conversation too. There's this dependent type theory proof assistant, and then there's higher-order logic. What is that difference there?

**Leo:**

[[56:29](https://youtu.be/KzdYKeAqWhY?t=3389)] At the beginning when I started Lean, I won't choose higher-order logic because it's much easier to implement. I mean, dependent type theory is way harder. But the math community, I mean, Jeremy is the one that convinced me that I would never be able to attract serious mathematicians like Fields Medal-level math people with higher-order logic. Right? His point is that higher-order logic is good for concrete math.

[[57:01](https://youtu.be/KzdYKeAqWhY?t=3421)] But if you want to talk about abstract objects, dependent type theory is way more powerful, and it's beautiful. It's easy to explain. Why is it called dependent? For example, you can have a structure in Lean when you have several fields, like X and Y are natural numbers or integers, let's say integers. You can have another field. The type of the field is a proof that X is greater than Y. The type of these fields is X.

[[57:32](https://youtu.be/KzdYKeAqWhY?t=3452)] Let's call it greater colon. You say X greater than Y. The type depends on the value of the previous fields. That's why it's called dependent type theory. You can have types that depend on the values of other parameters, other fields, and so on. But the beautiful thing about that is that you have this very small language that is so expressive. For example, this field, now that's a proof. You have to provide a proof.

[[58:05](https://youtu.be/KzdYKeAqWhY?t=3485)] You can view it as an invariant. I can only build elements of this type if I give the X and Y, like in other programming languages. But I have to give a proof that X is greater than Y. It's impossible to construct elements without providing this evidence, right? You can view this as an invariant. You don't have to invent invariants, right? The language is just the fact you have these dependencies; you can express them in the functions.

[[58:37](https://youtu.be/KzdYKeAqWhY?t=3517)] You can have a function, for example, that says it takes X, a Y, and a proof that Y is different from zero, right? I mean, it's impossible to call the function if you do not provide evidence that Y is different from zero. This was always cool, but in the past people would say, wow, providing these proofs is really annoying. But with AI now, the AI can synthesize the proofs for you, and it's really cool.

**Ryan:**

[[59:07](https://youtu.be/KzdYKeAqWhY?t=3547)] In higher-order logic, though, could you express the same?

**Leo:**

[[59:10](https://youtu.be/KzdYKeAqWhY?t=3550)] No, no, that's... You cannot. You don't have that. You lose the dependencies. For example, one thing that you cannot do in higher-order logic in Lean. In serious math, people have a bunch of structures they manipulate. You have something, a field, I mean a ring, a group. You can write a function in Lean that takes a group and turns it into a new group, a new structure. You're not manu.

[[59:43](https://youtu.be/KzdYKeAqWhY?t=3583)] You don't really care about the elements of the structure. You are viewing the structure as a first-class citizen. That's something that dependent type theory can do easily; in higher-order logic, you have to play encoding tricks. It's a mess. I mean, some people say, "Oh, it works for me." None of the mathematicians agree with this statement. None. I mean, you talk to Terence Tao, to Alex Kontorovich, Jeremy Avigad, Kevin Buzzard, Patrick Massot, they would say, no, no, you have to do dependent type theory.

[[01:00:18](https://youtu.be/KzdYKeAqWhY?t=3618)] I mean, that's another example for me that listening to your users is important. If you want to appeal to this community, it's totally okay to say I don't care about this community. But if you care, listening to what they really want is important.

### 01:00:37 — The future of Lean

**Ryan:**

[[01:00:37](https://youtu.be/KzdYKeAqWhY?t=3637)] So when we think about the future of Lean, I'm curious to hear your thoughts on where you think Lean is going, things you're excited about in the future. What might it look like in a few years?

**Leo:**

[[01:00:51](https://youtu.be/KzdYKeAqWhY?t=3651)] Yeah, I think we have these nonprofits behind Lean since 2023. I mean, Lean is 13 years old. The first 10 years was a such project, right? I mean, only when we got the nonprofits behind Lean that it became, you can view it as a product. You have a team of engineers, and we managed to do it because of the impact on math. But Sebastian Ullrich and I, we co-founded this nonprofit. What we are really excited about is Lean as a programming language.

[[01:01:29](https://youtu.be/KzdYKeAqWhY?t=3689)] A programming language where you can prove things about your programs, right? That's a direction we are pushing really hard. Lean 4. We are super grateful for AWS, Amazon. They're making the largest donations so far to these nonprofits, where the goal is to accelerate this path. I mean, Lean is doing super well in the math path. But let's make Lean a programming language, Lean a system for software verification, hardware verification.

[[01:02:01](https://youtu.be/KzdYKeAqWhY?t=3721)] Let's push to the extreme. Let's give some love to these people, to this path that's right. Now we do not really have funding to push seriously this path. That's the nonprofits, right? For me to be in a world where you can reason about your code is part of my life. I'm not writing unit tests anymore. I'm writing properties and proving them. The AI is proving most of them. For me, this is the direction we are pushing hard.

[[01:02:37](https://youtu.be/KzdYKeAqWhY?t=3757)] And one thing that people don't realize is that when you have proofs, it enables optimizations for free. You can ask the, for example, today, if you ask the AI to optimize, you have to inspect the code to make sure no bugs were introduced in the process. But if the AI is telling you, look, I optimized it, it still computes the same thing. Here's the proof. Game changer in my point of view.

**Ryan:**

[[01:03:10](https://youtu.be/KzdYKeAqWhY?t=3790)] Yeah, I've heard multiple people say this decade will be the decade of formal verification of software. And yeah, maybe Lean will be a huge part of that.

**Leo:**

[[01:03:23](https://youtu.be/KzdYKeAqWhY?t=3803)] Yeah, for sure. We're super excited to make it happen. Scalability is super important, right? Because there is a big difference between math and software verification. In math, the statements are usually really tiny or small. I mean, Fermat's Last Theorem is an example. I mean, super small. But the proof's insanely cheap. For software verification, it's the opposite, right? The statements are big.

[[01:03:59](https://youtu.be/KzdYKeAqWhY?t=3839)] I mean, but the proofs are shallow. The reason why this is shallow, but you have to manipulate these big objects, right?

### 01:04:10 — Technical book recommendations

**Ryan:**

[[01:04:10](https://youtu.be/KzdYKeAqWhY?t=3850)] So for someone who wants to learn more about formal verification or learn more about Lean, do you have a top technical book recommendation in the Lean websites?

**Leo:**

[[01:04:18](https://youtu.be/KzdYKeAqWhY?t=3858)] I mean, we have several books there that introduce Lean Functional Programming, Lean Theorem Proving, Lean Mathematics, and Lean: The Mechanics of Proof is great for educational purposes. We have a collection of proofs. If people go to lean-lang.org, you find all these books there. But one thing I tell people these days is that learning Lean using AI is super efficient. I mean, you keep talking to AI in natural language, asking what do you want?

[[01:05:03](https://youtu.be/KzdYKeAqWhY?t=3903)] Asking it to write examples. Many people split the screen in three now, right? We had the Lean code, the Infoview, and on the bottom. Now many people use an AI agent there that's writing the code and explaining in natural language what's going on there. It's a super effective way. I mean, Terence Tao, he told me when he learned Lean, he uses the old version. It was before agents. He would have ChatGPT on one window and Visual Studio Code in the other window, and he would copy and paste between them.

[[01:05:41](https://youtu.be/KzdYKeAqWhY?t=3941)] And that's how he learned. But now it's even more effective with the AI agents. It's easy to pick up. I mean, just talk to the agents. Sometimes people say, how do I start? Start talking to the agents. It will help you, it will customize. Right? You can explain what you know already, right? I mean, what's your background? And for example, if you tell, oh, I know Haskell, it's so much easier, right?

[[01:06:12](https://youtu.be/KzdYKeAqWhY?t=3972)] You can customize the process.

### 01:06:15 — Advice for his younger self

**Ryan:**

[[01:06:15](https://youtu.be/KzdYKeAqWhY?t=3975)] And then last question for you is, if you could go back to the beginning of building C3, building Lean, and give yourself some advice, knowing what you know now, what would you say?

**Leo:**

[[01:06:28](https://youtu.be/KzdYKeAqWhY?t=3988)] I'll keep it a secret. I mean, I think eagerness is bliss. I mean, you don't know how hard things are, and when you start the adventure, maybe I'll keep secrets. What I would tell, I think one thing, especially before starting Lean, I'm super introverted. And I would tell, look, you should work on your people skills because it helps a lot. I mean, when you have to interact with a community, with people.

[[01:06:58](https://youtu.be/KzdYKeAqWhY?t=4018)] For me, it was hard to learn that, and I would tell myself, I think it's really important to have people skills, too.

**Ryan:**

[[01:07:06](https://youtu.be/KzdYKeAqWhY?t=4026)] Well, thank you for your time today.

**Leo:**

[[01:07:08](https://youtu.be/KzdYKeAqWhY?t=4028)] Thank you. Thank you.

