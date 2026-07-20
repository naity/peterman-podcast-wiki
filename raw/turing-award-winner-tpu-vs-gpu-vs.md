---
type: raw-transcript
slug: turing-award-winner-tpu-vs-gpu-vs
title: "Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson"
guest: "David Patterson"
date: 2026-07-13
url: https://www.developing.dev/p/turing-award-winner-tpu-vs-gpu-vs
fetched: 2026-07-19
complete: true
---
# Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson

**Guest:** David Patterson  
**Host:** Ryan Peterman  
**Publish Date:** Jul 13, 2026

## Host's Intro

In college I briefly studied RISC vs CISC for my major but I forgot almost everything now. So it was great to talk to David Patterson about what happened there since he was one of the people involved in the historic RISC versus CISC debates.

Given his computer architecture expertise, I also was curious to hear his explanation of the differences about CPUs, GPUs and TPUs so we discussed that too. One of the things I enjoyed most about the conversation was reflecting on what was important looking back on his half a decade of experience. I hope you enjoy this episode.

By the way, I started to shoot my own episodes since it lets me record in scrappy locations and majorly cuts down on cost. Before when I got help, each onsite shoot would cost $2-3k minimum. Maybe one day I'll revisit this and get help if the podcast has more budget. For now though I've been enjoying learning video production and it's pretty simple. Lighting was rough on this episode though (lesson learned).

It's also fun bringing in equipment and trying to capture people in their natural environment like when I shot the Bjarne episode in front of his own library of C++ books.

Also, it's been ~6 months since I quit my job to work on the podcast full time. I've been meaning to write an update. I'll put something out in a week or two.

## Timestamps

- 00:42 - RISC vs CISC
- 12:51 - Compilers
- 17:38 - GPUs
- 23:07 - GPU vs TPU vs CPU
- 32:12 - Is Moores law dead?
- 38:04 - GPU benchmarks
- 41:40 - How to have a bad career
- 49:59 - Courage and optimism
- 55:56 - Advice for his younger self

## Transcript

### 00:42 — RISC vs CISC

**Ryan:**

[[00:42](https://youtu.be/Pn4ZwlEh5nw?t=42)] Maybe you could explain RISC versus CISC, kind of like what that debate was and why it was controversial.

**David:**

[[00:49](https://youtu.be/Pn4ZwlEh5nw?t=49)] What happened is, in the 1970s, the microprocessor was invented. But in the beginning, it was basically a toy. It'd be something that would go in microwaves and things like that. Those of us who believed in Moore's Law believed eventually the microprocessor would be the way we did all our computing, with the doubling of transistors every year or two. Eventually, there'd be enough transistors that one of these microprocessors would be a serious computer.

[[01:19](https://youtu.be/Pn4ZwlEh5nw?t=79)] So the people who are designing microprocessors, like Intel and Texas Instruments, weren't really computer architects, so they just imitated what the big companies did. So leading companies, like IBM, where at the time Digital Equipment Corporation, IBM for mainframes, Digital Equipment for what were called minicomputers, they kind of drove the architecture, the instruction set design. So what they were doing with Moore's Law was building more and more sophisticated instructions.

[[01:49](https://youtu.be/Pn4ZwlEh5nw?t=109)] They had many computers be the size of a refrigerator or a couple of refrigerators, and mainframes would be the size of many of those. That's what they were doing with more hardware resources. The philosophy at the time was that by having a more sophisticated instruction set, you raised the level of abstraction closer to the software. So that had some inherent benefits over having something at a lower level.

[[02:16](https://youtu.be/Pn4ZwlEh5nw?t=136)] Now, from some of us who were in that area, like my friend John Hennessy at Stanford and I, we thought that wasn't necessarily the right thing to do. Compilers would go from programming languages down to the instruction set. So why couldn't compilers hold that? And then the question is, what's the right instruction set for this emerging microprocessor? And the prevailing wisdom of these more sophisticated instruction sets, complex instruction sets, and if we think of it like vocabulary, it was like having lots of polysyllabic words in your vocabulary.

[[02:52](https://youtu.be/Pn4ZwlEh5nw?t=172)] And the alternative was going to be what we call the reduced instruction set computer, was having lots of reduced instructions, like monosyllabic words. So you might guess that for a program to execute these instructions, if they're simpler, they take more of them, and if they're sophisticated, they take fewer. But the sophisticated ones might take longer to run. So the question came down to what was that ratio?

[[03:18](https://youtu.be/Pn4ZwlEh5nw?t=198)] And in the beginning, in the 1980s when these debates were happening, there was this kind of very vociferous debates partly about what those ratios are going to do, but a big part was kind of philosophical. Weren't you doing damage to the software industry by lowering the instruction set level so the gap between the programming languages and the instruction set was larger? That was kind of the ferocity of the debates.

[[03:43](https://youtu.be/Pn4ZwlEh5nw?t=223)] Well, after the dust settled a few years later and we started getting numbers, it turned out you needed maybe 30%, 40% more simple instructions to execute in a program. But you could run them 4 or 5 times faster. So the net was 3 or 4x speedup was the potential for RISC over CISC.

**Ryan:**

[[04:05](https://youtu.be/Pn4ZwlEh5nw?t=245)] You mentioned that philosophical difference, that gap. Why would that be controversial?

**David:**

[[04:12](https://youtu.be/Pn4ZwlEh5nw?t=252)] I mean, unfortunately, I'd say computer architecture in the 1970s and even 1980s, a lot of it was kind of people designed this by using their intuition or using their gut, their feelings, was this the right thing to do. And even the textbooks of the time were like catalogs. Here is a computer and just list all its features. And here's another computer listing all its features. So it's pretty dissatisfying what was going on.

[[04:41](https://youtu.be/Pn4ZwlEh5nw?t=281)] Because these debates, it would seem like we ought to be able to decide this scientifically with numbers that are there. But, absent that, it was more like a philosophical debate, like how many angels on the head of a pin, right? You could have arguments qualitatively, but you couldn't settle the arguments. And because there weren't ways to settle the arguments quantitatively, people would just argue about it.

**Ryan:**

[[05:06](https://youtu.be/Pn4ZwlEh5nw?t=306)] Would you say that, you know, RISC versus CISC, did one side win the war?

**David:**

[[05:13](https://youtu.be/Pn4ZwlEh5nw?t=313)] Yeah, I was just reading. There's some guy online who revisited it and he said, "CISC? Well, that's a pretty myopic view. It's in the PC era because of the importance of distributing software in binary." So once x86 was established and PCs would ship software in binaries, that was very hard to overcome. That was a huge impediment to changing the instruction set. So PCs are defined largely by the x86 architecture.

[[05:46](https://youtu.be/Pn4ZwlEh5nw?t=346)] But also in the 1980s, there was this company in England that wanted to do a personal computer. They called it the Acorn personal computer. And they decided they wanted to have their own instruction set architecture to do that, their own chip they run satisfactorily. The chips they had available at the time they were doing it weren't fast enough. And they were influenced by the papers that we did at UC Berkeley.

[[06:09](https://youtu.be/Pn4ZwlEh5nw?t=369)] And so they built what they called the Acorn RISC Machine. And then one of the benefits of this kind of reduced instruction set is that it could be simpler. It would take less resources and take less energy to execute. And then several years later, when Apple was looking for a microprocessor that could power one of their personal devices, this one was called the early forerunner of the iPhone called Apple Newton.

[[06:35](https://youtu.be/Pn4ZwlEh5nw?t=395)] They came to this company and said, "Boy, I really like it. Let's get rid of the Acorn name." So they renamed it the Acorn RISC Machine, ARM, and they rechristened it the Advanced RISC Machine to get rid of the Acorn. And then Apple used it in the Newton. Now, the Newton wasn't a commercial success, but it demonstrated the benefits for RISC architecture for mobile devices. So Nokia came along just a few years later with their GSM cellular phone, which is one of the first popular ones, and they embraced ARM.

[[07:10](https://youtu.be/Pn4ZwlEh5nw?t=430)] And so ever since, ARM has dominated all the mobile devices. So I think I just checked, there's been 350 billion ARM processors, microprocessors with ARM technology in it today. So it's like today 99% of all processors and computers are RISC, even in personal computers. Apple switched over to ARM from the x86 architecture. So even PCs, there's RISC architecture is significant and it's starting to get in the cloud.

[[07:47](https://youtu.be/Pn4ZwlEh5nw?t=467)] The cloud's largely been defined by the x86 server architectures. But Amazon, Microsoft, and Google all have their own development of ARM processors. So ARM is becoming a RISC processor, becoming more popular in the cloud. So right now I'd say the x86 architecture market is shrinking while the RISC architecture market is growing leaps and bounds.

**Ryan:**

[[08:12](https://youtu.be/Pn4ZwlEh5nw?t=492)] Well, how could someone say CISC when you mentioned 99%?

**David:**

[[08:17](https://youtu.be/Pn4ZwlEh5nw?t=497)] Yeah, well, that's just if they're doing something in history and they define computers as personal computers and maybe servers, and they go up through around 2000. If the story ended then, you could—well, it looks like a CISC architecture, but once we get into this post-PC era, I don't understand how somebody would reach that conclusion.

**Ryan:**

[[08:43](https://youtu.be/Pn4ZwlEh5nw?t=523)] You mentioned the energy expenditure. So RISC makes sense in places, or maybe on mobile devices, things like that.

**David:**

[[08:52](https://youtu.be/Pn4ZwlEh5nw?t=532)] Well, even in the cloud, everybody cares about.

**Ryan:**

[[08:55](https://youtu.be/Pn4ZwlEh5nw?t=535)] We're.

**David:**

[[08:56](https://youtu.be/Pn4ZwlEh5nw?t=536)] Everything is energy bound now. So if these days, of course you're not dealing with millions of transistors, but billions of transistors. So it matters somewhat less today. There's so many things going on that you can hide that. I mean, even what the x86 architecture did to compete is that it translated the x86 instructions in hardware into RISC instructions. And so you had to pay that extra overhead of that translation step to get RISC instructions.

[[09:26](https://youtu.be/Pn4ZwlEh5nw?t=566)] And then you could take any good ideas that the RISC people had that x86 could do. But it was worth it financially for that extra overhead because of the value of the PC software base. So it made a lot of sense for Intel to do that. And they did that in the early 2000s. It was a great commercial idea.

**Ryan:**

[[09:49](https://youtu.be/Pn4ZwlEh5nw?t=589)] Is there any niche use case where CISC makes sense? Is there any engineering trade-off, or is CISC objectively worse?

**David:**

[[09:57](https://youtu.be/Pn4ZwlEh5nw?t=597)] Yeah. So if you want to, if we want to go kind of one level deeper into all of this, what was actually going on in designing computers, the hard part is the control. And so what happened is, in the beginning, control was kind of ad hoc. You would figure out, you put the gates together to make it work. One of the computing pioneers, Maurice Wilkes, figured out a more elegant way to design control.

[[10:27](https://youtu.be/Pn4ZwlEh5nw?t=627)] And he said, well, we could just list all the control signals as the output of a memory, and we could have something that would keep track of where we were in the memory and issue those control signals. And he called this effort the instruction, the control signals. You could think of instructions. He called that a microinstruction, and he called the programming of these instructions microprogramming.

[[10:54](https://youtu.be/Pn4ZwlEh5nw?t=654)] Where technology was in the 1960s, that made a fair amount of sense. IBM built these so-called microprogram computers. It was basically an interpreter with very simple instructions that would interpret this much more sophisticated instruction set above it. But you would pay this interpretation overhead. And classically in computer science, interpreting versus compiling is something like a factor of five or ten.

[[11:23](https://youtu.be/Pn4ZwlEh5nw?t=683)] But given the latencies of the memory technologies and the possibility of doing this out of read-only memory, it made sense up until the '60s and '70s. But then the question came up around 1980: Is this still a good idea? Should we have this microcode interpreter inside there? And so the alternative is to think of, well, rather than having this microcode interpreter in there, why don't we just compile directly into those instructions?

[[11:52](https://youtu.be/Pn4ZwlEh5nw?t=712)] And that's pretty close to the RISC ideas. The microinstructions themselves used to be like 100 bits wide and really complicated. So if you make them not quite so long, you make them kind of more natural still. We could skip the interpretation step. So, going one level deeper, the question today would be: would people invent an instruction set that was so sophisticated it needed a microcode interpreter?

[[12:21](https://youtu.be/Pn4ZwlEh5nw?t=741)] And probably they wouldn't do that. I mean, you could do it; nothing prevents you from doing it. But you wouldn't want to design an instruction set that was forced to use a microcode interpreter. It might make sense in some very tiny applications, possibly where you have tens of thousands of transistors. Maybe this microcoded interpreter would work. But I think nobody today—I don't think anybody's invented an instruction set in the last 20 years that has anything that would need a microcode interpreter.

### 12:51 — Compilers

**Ryan:**

[[12:51](https://youtu.be/Pn4ZwlEh5nw?t=771)] You mentioned the compiler multiple times here, and it seems like that's a critical piece that kind of makes RISC work so well. Can you explain the role of the compiler and how it manages the relationship between software and hardware?

**David:**

[[13:06](https://youtu.be/Pn4ZwlEh5nw?t=786)] Well, you're writing in a programming language like C or C++, or maybe Python, but the quality of the code that gets generated is up to the compiler. And a specific example is that it's useful when you construct computers to have registers. And those registers are actually kind of visible in the assembly language or the machine language programming. There can be 8, 16, or 32 of these registers for the people programming to use.

[[13:37](https://youtu.be/Pn4ZwlEh5nw?t=817)] Well, it used to be very difficult for compilers to allocate registers efficiently. Computers just weren't fast enough. We didn't have the algorithms that we could look at a section of code or a subroutine or something and say, how can we most efficiently do register allocation? In fact, the C programming language, which was invented to do systems programming in C. Before that, to write an operating system, people wrote them in assembly language, believe it or not.

[[14:08](https://youtu.be/Pn4ZwlEh5nw?t=848)] But the Unix people showed, Ken Thompson, Dennis Ritchie showed that if we had a low level language, a pretty low level language, we get the benefits of writing in something that's much easier for humans to understand and debug because register allocation by the compilers was so poor, they had to put in the ability for the programmer to give hints of what variables should go in registers. It was just easier for them to have the programmer step in and say if the machine had eight registers, I want these six variables to be in these registers.

[[14:40](https://youtu.be/Pn4ZwlEh5nw?t=880)] Don't leave them in memory because it runs so much slower; registers are so much faster. So a big part of the RISC argument was the compiler algorithms were getting better. They could handle these low-level instructions; they could allocate registers efficiently. And that was another reason in these debates about why it made sense to have a simpler architecture. What we did in the RISC architecture is, well, if registers are really important, register allocation is really important.

[[15:10](https://youtu.be/Pn4ZwlEh5nw?t=910)] One way to make it easier for the compiler was just to have a lot more of them. So typically the CISC architectures at times would have eight or maybe 16 registers. So we put in 32. And that was one of the arguments, right? If it's hard to efficiently use a small number, let's give them plenty. So even if it wasn't that good, there'll be enough registers most of the time. And registers weren't that much more expensive to include in machines because of Moore's Law.

**Ryan:**

[[15:38](https://youtu.be/Pn4ZwlEh5nw?t=938)] I saw somewhere in one of the talks that he had given that somehow the compiler, it's easier for it to optimize the code for RISC. But in CISC, there were these complex bigger ones, and it almost never used them. Is that a shortcoming of the compiler?

**David:**

[[15:56](https://youtu.be/Pn4ZwlEh5nw?t=956)] So what happened, if we go back to the compiler days, there's this argument that by having more sophisticated instructions, this would raise the level of abstraction. There'd be a smaller gap, and they'd make it easy to compile. But that was a philosophical argument. It wasn't something that necessarily compiler people could. Compiler people weren't making that argument; it was the architects who were making that argument.

[[16:20](https://youtu.be/Pn4ZwlEh5nw?t=980)] And as it turned out, when we looked at the programs, when we were doing the early research on CISC versus RISC, the compilers didn't really use those instructions. Often the compiler writers, the architects, would come up with a sophisticated instruction, and the compiler writers would say, well, we don't need that. In fact, we found examples where, like for a procedure entry, there'd be a special instruction built in to do all this work.

[[16:44](https://youtu.be/Pn4ZwlEh5nw?t=1004)] That's what the architects thought the compilers were going to do, and the compiler designers said, well, we don't need that. It's faster. It's actually faster for you to use separate instructions than to use your sophisticated instruction. And so we found a bunch of examples like that. So you pay the extra overhead of the microcode interpreter to have these sophisticated instructions, and then the compiler doesn't even use them.

[[17:05](https://youtu.be/Pn4ZwlEh5nw?t=1025)] Right. So this is kind of a nonsensical situation that we're in. And, you know, this is kind of like, you know, why, why, why are there startups or why are there scientific, you know, breaking points like that? As we looked at all the technologies with Moore's Law, you know, ideas like caches, with where compilers were using sophisticated instructions, the ability to allocate registers more efficiently, it made sense to change the directions away from these microcoded instruction set architectures to these simple architectures.

### 17:38 — GPUs

**Ryan:**

[[17:38](https://youtu.be/Pn4ZwlEh5nw?t=1058)] When we talk about instruction sets, I mean we're kind of assuming that we're talking about these general-purpose computers or these CPUs. And I know GPUs are kind of talked about a lot, and maybe there's other forms of computing. Are there instruction sets for those types of machines as well?

**David:**

[[17:55](https://youtu.be/Pn4ZwlEh5nw?t=1075)] So what happened is around 2000 is when GPUs came along, and these were what we call domain-specific architectures. So a GPU is a graphics processing unit. It had one job. It didn't need to do everything that a general-purpose processor needs to, didn't have to support virtual memory, it didn't have to support a compiler, which is a pretty radical idea for architectures. It was just for graphics. And so around 2000 is when NVIDIA and the other GPUs out there, because they were trying to give you the graphics for games and give you the graphics for movies.

[[18:32](https://youtu.be/Pn4ZwlEh5nw?t=1112)] So it was a niche product. So what happened kind of in the computer industry is it was driven by Moore's Law, which I've mentioned many times, and also this lesser known law called Dennard scaling, which raises kind of an interesting question. Well, if Moore's Law puts a lot more transistors on a chip, how come they're not getting hotter and hotter as we double the number of transistors every year?

[[18:56](https://youtu.be/Pn4ZwlEh5nw?t=1136)] And the reason was this observation made by Robert Dennard, that as you added more transistors, people would also lower the threshold voltage, which is the distinction between a 0 and 1. And that had a squared effect. So you would end up doubling the transistors, but you'd lower the threshold voltage. So microprocessors stayed at like 20 or 30 watts. In fact, we did a John and I eventually did a textbook, and I was just checking, and it came out in 1990.

[[19:28](https://youtu.be/Pn4ZwlEh5nw?t=1168)] And we didn't even talk about power as an issue for the first three editions. The third one came out in 2000. Power wasn't even a topic because Dennard scaling was going on. And so microprocessors stayed in the tens of watts even as they got faster and faster. What happened is about 2005 or so, Dennard scaling stopped working. And that was a shock. And Intel actually had a microprocessor that failed one of their generations because they just couldn't get the power down enough.

[[20:00](https://youtu.be/Pn4ZwlEh5nw?t=1200)] It was too hot to do that. So then what that forced us to go to multicore is that before that, it was easiest for the programmer, for everybody, if there was one very sophisticated processor that did everything, but we couldn't do that anymore. So it went from one sophisticated processor to two, and then four, and then eight simpler processors. Then it was up to the programmer to deliver on the potential of Moore's Law by parallelizing their code.

[[20:29](https://youtu.be/Pn4ZwlEh5nw?t=1229)] So we stayed that way for about another 10 years. And then Moore's Law started slowing down so that the general-purpose microprocessor was barely improving. It got a little better, but it wasn't getting dramatically better. In the 1980s, 1990s, 2000s, you have a laptop and your friend's laptop would be like four times as fast as yours. And you were jealous. So you would throw away perfectly good hardware because your friend's thing was so much faster because of the rapid change in performance.

[[21:05](https://youtu.be/Pn4ZwlEh5nw?t=1265)] Well, that all ended in the 2010s, where you wouldn't throw away a laptop because the new ones were hardly that much faster than the old ones. You'd throw them away when they break and slow down. Nevertheless, programmers were used to this dramatic improvement in performance every few years because they could add more features to their software and stuff like that. So what were architects going to do?

[[21:27](https://youtu.be/Pn4ZwlEh5nw?t=1287)] They'd already done the multicore trick in 2005 or so. So in around 2015, the idea was we would do domain-specific architectures like the GPUs. So if you tell me I only have to run a narrow class of programs and I don't have to necessarily run all the operating systems, everything else, well, yes, I could shuffle those resources and do something much more efficient for something. Well, so you could do some things well, and there's other things either you do poorly or not even at all.

[[21:59](https://youtu.be/Pn4ZwlEh5nw?t=1319)] So then the question is, okay, what domain? So just coincidentally, where we were technologically, right around 2012, 2015 is when machine learning AI burst on the scene. And so that was, it was evident what domain should we do? And the domain was machine learning AI. So just coincidentally, where we were technologically, this new domain came along. And then I would say I work for Google, but I think it's fair to say Google was the one who really saw it was certainly the first big company who understood the potential of machine learning AI and bet that they or feared that they were going to be swamped with demand and needed to do custom hardware.

[[22:46](https://youtu.be/Pn4ZwlEh5nw?t=1366)] So the tensor processing unit, or GPU, that Google debuted in 2016 really kind of shocked the world and got people to realize that we should be designing hardware for machine learning, and we could continue to improve performance dramatically for that one domain.

### 23:07 — GPU vs TPU vs CPU

**Ryan:**

[[23:07](https://youtu.be/Pn4ZwlEh5nw?t=1387)] What's the high-level difference between a CPU, a GPU, and a TPU?

**David:**

[[23:14](https://youtu.be/Pn4ZwlEh5nw?t=1394)] The CPU has got to be this general-purpose thing. And basically even today they have these general-purpose cores that each core is very similar to what the instruction sets used to be like 20 years before that. It's not a surprising design, and it's just got lots of cores, and the modern ones today could have 50 or 100 cores in there. So that's the feature for graphics. What they decided to do to do the graphics job is they need to get a lot of performance out of the memory system.

[[23:46](https://youtu.be/Pn4ZwlEh5nw?t=1426)] So they went to multithreading. They have hardware threads that you would send a memory request out and the hardware would switch over to do something else while memory is coming up. So this highly threaded architecture, and that's what they developed, and it could run well for graphics. And graphics, it turns out, doesn't need very, doesn't need a powerful floating point. It doesn't need wide floating points.

[[24:15](https://youtu.be/Pn4ZwlEh5nw?t=1455)] So 32-bit floating point is plenty for graphics, even 16-bit. So they were doing, pushing graphics with 16- and 32-bit floating point in this multithreaded kind of architecture. And because it was kind of its own unique thing, it has its own set of terminology all to itself. It wasn't kind of out of the main branch of computer architecture. So when you look at our textbooks, we have kind of like a Rosetta Stone which says here's the terms that NVIDIA uses to describe GPUs.

[[24:45](https://youtu.be/Pn4ZwlEh5nw?t=1485)] This is what it means in kind of normal, well, normal in the mainstream processor design. So there was this niche product that happened to do pretty fast single-precision floating point and even half-precision floating point, and they were pretty cheap. They were like hundreds of dollars. So when people, so kind of, but some people were thinking, boy, for some applications, if I could turn my program into, like, pretend that it was doing, creating an image, if I could turn my problem into image generation, I could use these pretty cheap GPUs, which had very good floating-point performance per dollar compared to anything else.

[[25:31](https://youtu.be/Pn4ZwlEh5nw?t=1531)] And so people started playing around with that. And the founder and CEO, Jensen Huang, really liked that idea. So in 2006 he funded an effort to create a programming language that would handle this multithreaded hardware architecture for graphics to make it easier to program. And so that led to the invention of CUDA, which I can't remember its acronym, but it's really a proprietary programming language for the multithreaded GPU architecture to make it easier to program.

[[26:07](https://youtu.be/Pn4ZwlEh5nw?t=1567)] It was a C-like language, but you can't just compile C programs and run it. But it was C-like, but people actually liked it. It was certainly much better than trying to turn your program into image generation, but people liked it. But Jensen Huang, his vision was try to get these teenagers in the basement who are playing the games to learn how to program these things. And he had a couple of markets that he was interested in, like some of the Department of Energy labs, like fluid flow and some of the things, like, some.

[[26:38](https://youtu.be/Pn4ZwlEh5nw?t=1598)] And he would build special-purpose libraries that could handle that domain and then use his GPUs to do that kind of special-purpose computing, but breaking out of graphics. But that's kind of the heritage there now for the TPU program. And so what's happened, people started right from the very beginning, people started using GPUs because they had much better single-precision floating-point performance than the CPUs.

[[27:04](https://youtu.be/Pn4ZwlEh5nw?t=1624)] They had a lot more processors on them, so they had potentially much more performance. So one of the breakthrough moments was in 2012, when within the machine learning community, this neural networking piece, which had a few advocates but a lot of people didn't believe in, went into a competition to see who could do the best image recognition. In 2012, the so-called AlexNet beat all the competition.

[[27:33](https://youtu.be/Pn4ZwlEh5nw?t=1653)] This was this historic moment in machine learning and neural networking. And once they did it, and the guy who did that had taken a CUDA course at the University of Toronto to learn how to use it. And so he says, well, as long as I'm doing this, I'll do it on a GPU. He was able to explore a lot more space on this cheap, fast GPU. So he entered it in the competition in 2012, and he was the only one using neural networks.

[[28:00](https://youtu.be/Pn4ZwlEh5nw?t=1680)] And he crushed the competition. And within a few years, everybody switched over, and not only were they doing neural networks, but they were using GPUs. So GPUs have this heritage of being graphics engines, but more programmable, and started getting used in machine learning. When Google came along, they decided it was a clean slate. They didn't care about graphics. So at the heart of neural networking is a matrix multiply.

[[28:31](https://youtu.be/Pn4ZwlEh5nw?t=1711)] That's the thing. So they designed a processor. At the time, the microprocessor had a giant matrix multiplying unit. That was the main thing. And then they threw a bunch of stuff out that they didn't need. So a lot of general-purpose computing is what's on the chip is maybe three levels of caches to try and have so you don't spend all your time going to the relatively slow memory.

[[28:54](https://youtu.be/Pn4ZwlEh5nw?t=1734)] Well, for machine learning they knew when their memory accesses were, so they could schedule that. So a hardware cache didn't make any sense. They would just have a memory the software understood would transfer in time. Those are some of the innovations. Also, they innovated on the floating point format you didn't need. Scientific computing cares a lot about precision. Most of it's done in 64-bit floating point, where the exponent is less than 10 bits and most of it is the precision.

[[29:27](https://youtu.be/Pn4ZwlEh5nw?t=1767)] The fraction can be 50-some bits. Well, what they realized for machine learning and AI, they don't need all that precision; they needed the range. So Google did the first floating-point format where the exponent was bigger than the fraction. That was a radical idea, the so-called bfloat16. The part of Google that was doing this was the Google Brain research group. So they brought out this architecture.

[[29:51](https://youtu.be/Pn4ZwlEh5nw?t=1791)] They had this narrow floating point format. They had a big matrix multiply unit. It only had one processor in it. Unlike the other ones, it was just dedicated machine learning. And it just kind of blew the doors off of everybody in the field. It was like 30 times better at inference than the contemporary GPU and 80 times better than CPU by having this dedicated one. So when Google made this announcement at their annual retreat a year or so after they had deployed it inside, it just shook everybody up.

[[30:26](https://youtu.be/Pn4ZwlEh5nw?t=1826)] Intel started buying companies, NVIDIA started modifying the design to be much more focused on machine learning. And then a bunch of other competitors, hyperscalers, started doing their own efforts. So I think that was the watershed. I think the TPU announcement was the watershed moment there.

**Ryan:**

[[30:48](https://youtu.be/Pn4ZwlEh5nw?t=1848)] So it's almost like levels of specialization, like the CPU is the most general.

**David:**

[[30:53](https://youtu.be/Pn4ZwlEh5nw?t=1853)] Yeah. If we still had Dennard scaling, Moore's Law and Dennard scaling, where would we be today? With general-purpose processors, we should have 100 TL microprocessors. If we could build 100 TL microprocessors, that's what we'd do. GPUs would still be a niche. If we could do that, it raises all boats. That would be fantastic if we could do that. But that's long in the history.

[[31:22](https://youtu.be/Pn4ZwlEh5nw?t=1882)] We haven't been able to do that for 20 years. And so there were probably two or three gigahertz microprocessors in 2005, and that's kind of where they are, barely improved today. So we can't do that. So there's still areas where it's important to have CPUs. They're the right—you need operating systems, compilers, and things that they're the right solution. But things have been specialized.

[[31:47](https://youtu.be/Pn4ZwlEh5nw?t=1907)] And then now, in terms of industry terms, a huge emphasis is being put into the AI accelerators, or just AI in general, is where the money is being invested. And so the question for any processor designers was, how does my processor design fit into this AI universe, and what should I do? How should I change it for this important application?

### 32:12 — Is Moores law dead?

**Ryan:**

[[32:12](https://youtu.be/Pn4ZwlEh5nw?t=1932)] So you mentioned that Moore's Law is slowing down. And I watched this other talk from Jim Keller saying that Moore's Law isn't dead. But is it controversial to say that it's?

**David:**

[[32:25](https://youtu.be/Pn4ZwlEh5nw?t=1945)] No. I mean, not, not to real engineers. Moore's Law is very simple. It says in a chip the number of transistors will double. Originally said every year, and then he changed it to every two years. Just look. Do the chips, the number of transistors doubled? No. Now I think what people assume that means is if we are no longer on Moore's Law, that technology is not improving.

[[32:52](https://youtu.be/Pn4ZwlEh5nw?t=1972)] That's not the same thing. It's not improving at the rate that Moore's Law projected. And what was amazing about Moore's Law, which lasted 50 years, is that guided the investment of semiconductor manufacturing. We need to deliver on doubling transistors every year or two. How are we going to do that? How are we going to build the equipment to do it? So it was a guideline for the whole industry, which was kind of remarkable.

[[33:17](https://youtu.be/Pn4ZwlEh5nw?t=1997)] So what we are doing now is there's pieces of the technology that get better and there's pieces that don't improve at all. So one of the big pieces, important pieces on a chip, is the static random-access memory. So that's hardly improving at all. Logic gates still continue to improve. The gates are getting better. So if you're doing adders or multipliers, those are getting there. So it's not uniform improvement anymore.

[[33:46](https://youtu.be/Pn4ZwlEh5nw?t=2026)] And we're also going to more exotic packaging to be able to deliver it. So people now, you know, forever. It was a single chip, was the best way to package everything fits on one chip. And that's what we're going to build. And now there's these ideas of chiplets or packaging multiple chips together. The latest GPUs, and I think the latest TPUs, has actually two what are called full reticle design dies packaged, put into a package.

[[34:18](https://youtu.be/Pn4ZwlEh5nw?t=2058)] And so a full reticle design is the maximum you can build on a semiconductor. Well, on a semiconductor they have a step-and-repeat motor, and in the old days you'd have many chips inside that. Now there's just one. So two maximum reticle designs form a node. So they're using packaging. So if you look from outside, you can say, well, look how many transistors. Moore's Law is continuing.

[[34:43](https://youtu.be/Pn4ZwlEh5nw?t=2083)] But if you see what's inside the chip, that has tapered off. And I think part of it is for a fair amount of the industry, if you were in a semiconductor manufacturer and people ask you what you do, it's I make Moore's Law, I sustain Moore's Law, that's what I do. And if you've been doing that for decades and somebody says Moore's Law is over, it's like my career is over. So I think there's an emotional side of it.

[[35:09](https://youtu.be/Pn4ZwlEh5nw?t=2109)] But just look at the data, the data doesn't back up with. Keller says, but I also didn't say that the technology is not improving. The technology is continuing to improve and specifically domain-specific architectures. But if you look at the general-purpose architectures or even other memory technologies, it used to be the DRAMs would improve by a factor of four in density every three years, like clockwork.

[[35:34](https://youtu.be/Pn4ZwlEh5nw?t=2134)] And now it's maybe 10 years between factors. So you can see plenty of evidence that Moore's Law no longer applies.

**Ryan:**

[[35:41](https://youtu.be/Pn4ZwlEh5nw?t=2141)] Is there some new version or some analog to Moore's Law that is kind of guiding microprocessor design and architecture these days?

**David:**

[[35:54](https://youtu.be/Pn4ZwlEh5nw?t=2154)] I guess the question is both NVIDIA and Google are continuing to deliver much faster processors for machine learning, tremendously better. What are they doing? Well, part of it is what I said about packaging, to be able to get more transistors, and you keep them closer together because distance matters. Part of it is innovating on the floating-point formats. So unlike the supercomputers of 64-bit, it's not even 64-bit, not even 32-bit, not even 16-bit, but 8-bit and 4-bit floating point is going on.

[[36:33](https://youtu.be/Pn4ZwlEh5nw?t=2193)] So narrowing of the data types, having kind of what's called the matrix multiply instructions. So these powerful units that are put in there that can do special purpose applications that are very important, making those bigger and faster. So those are the three things that are going on. But we don't have this simplifying guideline kind of underlying all this. You have to be aware of each piece of the technology, gauge how fast it's improving, whether they can deliver on what's going on, and then you assemble that together and make your bets.

[[37:15](https://youtu.be/Pn4ZwlEh5nw?t=2235)] There's a paper that we've just got approved that I think we're going to put on arXiv soon, which is talking about the Google TPU line. And pretty remarkably, the Google TPU line, particularly for training, has stayed pretty constant in the basic architecture design. Things have gotten bigger and faster. But if you look at the design of it going back to the first training TPU, that block diagram still works all these a decade later.

[[37:47](https://youtu.be/Pn4ZwlEh5nw?t=2267)] So the people who designed that in, whatever, 2015 or 2016, did a really great job.

### 38:04 — GPU benchmarks

**Ryan:**

[[38:04](https://youtu.be/Pn4ZwlEh5nw?t=2284)] Blocks are still there. I think in your career with the CPU benchmarks were huge. They played a huge role in measuring which computer architectures were performant and not in this new space of floating point operations for AI. Is there a benchmark that people use for GPUs, and can you also apply it for TPUs?

**David:**

[[38:27](https://youtu.be/Pn4ZwlEh5nw?t=2307)] I and some friends were involved in the MLPerf effort. So it was inspired by the SPEC CPU effort, with the SPEC benchmarks, where there were these competing companies and they'd all make claims that theirs was better than the others, and they realized that wasn't good for the industry. So they agreed on a set of benchmarks. So the MLPerf effort is this run now, but what's called MLCommons is an attempt to do that.

[[38:55](https://youtu.be/Pn4ZwlEh5nw?t=2335)] If we're going to do these comparisons, let's not argue about what the benchmarks are. So that's a serious effort in that kind of. Interestingly, what's happened, I'd say, is because there's two pieces to design. There's the machine learning libraries that are to implement a lot of features that you need for these applications, and the libraries will even be rewritten for specific applications, rather than just having general libraries.

[[39:29](https://youtu.be/Pn4ZwlEh5nw?t=2369)] This has turned out to be a big advantage for NVIDIA because they have a large corporation with lots of people that are available, lots of engineers who could build these libraries for them. So it's turned out not quite a... It's not a neutral evaluation, right? It's the architecture plus the libraries that go with it, and the compiler too, but specifically the libraries that you tailor each time. So NVIDIA brings out, when they announce a new architecture, they create a new set of.

[[40:04](https://youtu.be/Pn4ZwlEh5nw?t=2404)] They modify the libraries to run that really well or to run applications really well. So that's a powerful combination. Kind of in business terms, people refer to NVIDIA as having this CUDA moat, and part of it is CUDA, the programming language, but a big part of it is the libraries that NVIDIA makes. So this has made it difficult for startups to be able to compete with NVIDIA, partly because they didn't put enough emphasis in the software and partly because NVIDIA just has many more engineers than they do to be able to tailor the libraries.

[[40:42](https://youtu.be/Pn4ZwlEh5nw?t=2442)] So it's the libraries plus the architecture. There's this powerful advantage why most people do things on GPUs. Now Google has been able to develop their own libraries. They don't have as many engineers. They use compilers more than I think NVIDIA does. So they have a set of libraries that they can use. But up until recently, Google's, it's all been internal. It's just for Google to use, or you could use it via the cloud.

[[41:13](https://youtu.be/Pn4ZwlEh5nw?t=2473)] But these startups have to have a difficulty as a result. That's why MLPerf hasn't been as popular. Not everybody runs them because NVIDIA runs them really well, really better than everybody else. And the startups have a hard time showing off what they can do, given they don't have the engineering effort going into the libraries that you need to do well in MLPerf.

### 41:40 — How to have a bad career

**Ryan:**

[[41:40](https://youtu.be/Pn4ZwlEh5nw?t=2500)] You gave this popular talk about how to have a bad career, and it's kind of the negation of advice for how to have a good career. And I was just wondering if you could summarize maybe the top three things that people should take away.

**David:**

[[41:58](https://youtu.be/Pn4ZwlEh5nw?t=2518)] Yeah, well, there's been a few things. So the story is early in my career, my friend, a good friend, and I said, how can we teach grad students how to give a good talk? And we thought it'd be funny to explain how to give a bad talk. And then if you didn't want to give a bad talk. So this is how to do it badly. And if you don't, here's the things you do not to do it badly. And so then I later did how to have a bad career that's pretty much focused toward academia.

[[42:23](https://youtu.be/Pn4ZwlEh5nw?t=2543)] So for researchers to be able to do that. I later did a How to Have a Bad, How to Build a Bad Research Center, how to build a bad research lab. And then recently I've been giving how to give AI a bad carbon footprint. That's my latest one. But I think the thing that might be more relevant is at the end of my talks, I would kind of reflect on my career and talk about lessons learned. So I've written a paper called Lesson.

[[42:49](https://youtu.be/Pn4ZwlEh5nw?t=2569)] I think it's "Lessons, Life Lessons from the First Half Century of My Career." I wrote that recently. And so those are divided up into kind of career advice and personal advice. There, on the personal side, I'd say, if you have a family, make sure your family's first. Keep your family first. The technology we've invented makes it really easy for your, you know, to take your work home with you and not pay attention to your family.

[[43:17](https://youtu.be/Pn4ZwlEh5nw?t=2597)] I had a. When I was first here at UC Berkeley, I gave a senior faculty member a ride home, dropped him off late at night, coming up from Silicon Valley. And he said, well, Dave, if I had to do it over again, I wish I'd spent more time with the family. And I never wanted to say that. And nobody on their deathbed says, you know, I wish I spent more time in the office. So, so you got to, you know, whenever it's easy to kind of, you know, let the.

[[43:44](https://youtu.be/Pn4ZwlEh5nw?t=2624)] Let your career overcome the needs of your family, but you just got to remember that. I would say, in my life, growing up in the 50s, the idea was that to be happy, you had to be wealthy. But those are actually two different goals, wealth and happiness. So I always made decisions toward happiness versus wealth, and I felt very good about that. And even now, why would I pick something that made me wealthy and unhappy?

[[44:15](https://youtu.be/Pn4ZwlEh5nw?t=2655)] Why would you do that? And in the field that we're in, it turned out there was a lot of wealth to go with it. So optimizing happiness didn't mean you had to suffer. Beyond that, I think it's important to have fun personally. I think when you're a kid, you don't have to tell kids to play, but as you get adult, you get so busy you don't think you have time to have fun. But you only get to do this once.

[[44:43](https://youtu.be/Pn4ZwlEh5nw?t=2683)] So right now I play soccer, I rode my bicycle to the interview, I lift weights, I body surf, do things with my wife and family and my son. So it's important to have fun. I think on the career side, one of the pieces of advice is by Stephen Covey. He wrote this book, The 7 Habits of Highly Effective People, I think, and he has a little quadrant, and he divides it into urgent and not urgent, and important and unimportant.

[[45:20](https://youtu.be/Pn4ZwlEh5nw?t=2720)] There are so many things in our technology, like email and texting, for you to focus on the urgent things, but you really shouldn't be spending a lot of time on the unimportant urgent things. And it takes self-discipline to set aside time for the important, non-urgent things. But if you don't block that out, you can just not have time to do anything. I get to see other people's calendars at Google, and there's managers that every half hour from eight to six, five days a week, are scheduled.

[[45:49](https://youtu.be/Pn4ZwlEh5nw?t=2749)] And I don't see how you have time to think and reflect on things like that. Other career advice thing is I remember I kind of woke up one morning and it was like God spoke to me. I was like thunderstruck. And it said it's not how many things you start, it's how many things you finish. It seems relatively obvious, but that's not the way I was acting. I had many things going on, but after that it's like there's one main thing I'm doing at times.

[[46:19](https://youtu.be/Pn4ZwlEh5nw?t=2779)] So when John Hennessy and I wrote a textbook, that was the main thing. When I was department head here, that was the main thing I did. I would do some other little things there. And John Hennessy, he wrote a kind of career advice book based on his presidency. And one of the things he said in there, you're only going to be remembered for the five or six things you've done in your life, not for the hundreds of little things.

[[46:44](https://youtu.be/Pn4ZwlEh5nw?t=2804)] So to give yourself a chance to have some things you're really proud of, it's better to concentrate on a few of them, hoping that some of them will turn out to be a big deal rather than scatter yourself to many things. But if you're interested, you can. Yeah, if you look for life lessons, David Patterson, first half century, you can see the whole list of. I think there's 16 lessons altogether.

**Ryan:**

[[47:11](https://youtu.be/Pn4ZwlEh5nw?t=2831)] You mentioned that you didn't want to reflect back on your life and feel like you didn't have enough family time. Yeah, I've— I don't think I've ever heard anyone say the opposite. Why do you think that is? Why is it that everyone looks back on their life and they never regret a lot of family time? I imagine there's got to be at least one person that says, "I spent too much time with my family; my career suffered."

**David:**

[[47:39](https://youtu.be/Pn4ZwlEh5nw?t=2859)] Yeah, well, what's, what's, it's pretty philosophical. I mean, what's life all about? What's success? Right. You have to figure out what that means for you. I mean, if you have, I don't know, if you have financial goals of being a millionaire, a billionaire or something like that, and that's how you judge your life. Okay. Good luck.

[[48:04](https://youtu.be/Pn4ZwlEh5nw?t=2884)] You know, it's pretty hard to make it. It's pretty hard to do, but I think it's the... When I was finishing my PhD, I read this book by Studs Terkel called Working, where he interviewed all these people in his careers, and they looked back at what they liked and what they didn't like, what they felt about their careers, and what I got out of it. The people who worked with people like ministers or teachers or doctors felt really good about what they do with their careers.

[[48:30](https://youtu.be/Pn4ZwlEh5nw?t=2910)] And the people who did more ephemeral stuff, like technology things or airplanes or something like that, are long gone, didn't feel as good about it. It was the people that they worked with that they really cared about. And I went out with a retired engineering dean here, and he— and to a meeting who I knew, and he said, "You know, Dave, as I think my career, it wasn't the projects, it was the people that I worked with that mattered."

[[48:54](https://youtu.be/Pn4ZwlEh5nw?t=2934)] And I thought I knew that from a long time ago. So that's, I mean, this is kind of senior persons offering advice. I think you're going to care more about the people you've worked with, the people you've helped, will be a bigger deal. That's part of, one of the other things about personal happiness is they studied happiness. Psychologists used to just study crazy people, but they started like, why are people happy?

[[49:17](https://youtu.be/Pn4ZwlEh5nw?t=2957)] And they know what the reasons are. Have a job that you like, have friends and family. Helping other people makes you happy. They know this. Having something kind of either a religious side of it, it doesn't have to be a formal religion, but contact with nature, the grandeur of nature, but the list of things you need to do to be happy is well understood.

[[49:42](https://youtu.be/Pn4ZwlEh5nw?t=2982)] And our world is filled with unhappy billionaires. Right. If money was the thing that made you happy, why are these people, very wealthy people, so mad about things? So, yeah, this is me passing on advice.

### 49:59 — Courage and optimism

**Ryan:**

[[49:59](https://youtu.be/Pn4ZwlEh5nw?t=2999)] In one of your talks, it said what worked well for me, and it was kind of some reflections. And one of the things in there I thought was unique and interesting. You mentioned that courage was a big part of your career, and I don't hear that too often. I was curious why you say courage is so important in a career.

**David:**

[[50:19](https://youtu.be/Pn4ZwlEh5nw?t=3019)] Yeah, I think that's, I mean, that might be partially my personal makeup, but I was kind of the youngest kid in my class and kind of small. It took me a while to grow despite age, so I was always small. But my parents encouraged me to go out for wrestling. And wrestling gives you physical self-confidence because you spend years doing that. I did it in high school and college. And so I think partly technically, having courage to do things kind of goes along with the advice is fortune favors the bold.

[[50:59](https://youtu.be/Pn4ZwlEh5nw?t=3059)] That goes. That's advice is 2,000 years old. It's hard to figure this out. Helen Keller wrote, even trying to play it safe, you still get caught. So it turns out you might as well. You might fail no matter what. And if you take a big chance, you can succeed. If you don't take the chance, you probably won't succeed if you play it safe. So fortune favors the bold. And I think it takes courage to do that.

[[51:28](https://youtu.be/Pn4ZwlEh5nw?t=3088)] I think also it just, for me, intellectually, I feel like if there's something not right, I need to stand up and confront it. And I think that kind of, ironically, comes from the wrestling side of my personality, where if I see something, somebody getting picked on or something like that, I'm going to stand and try to stop it. And I feel that same responsibility. Intellectually, if people are making bad arguments or doing something, we need to stand up and do it.

[[51:57](https://youtu.be/Pn4ZwlEh5nw?t=3117)] And I feel good about that. The cautionary part about that is, because I guess one of my senior faculty members saw this nature of me, and he said one of the sayings is friends come and go, but enemies accumulate. This is an old saying. So if you think about it, you kind of, people you went to high school with, while friends, you kind of forget. But somebody who you really dislike, you never forget that you dislike that person.

[[52:22](https://youtu.be/Pn4ZwlEh5nw?t=3142)] So standing up when it's important, but be careful when you make enemies because they're going to stick around for a long time.

**Ryan:**

[[52:29](https://youtu.be/Pn4ZwlEh5nw?t=3149)] When you say something's gone bad, technically, do you mean someone was incorrect?

**David:**

[[52:35](https://youtu.be/Pn4ZwlEh5nw?t=3155)] Yeah, when they're weak, either politically or technically, when it's a weak argument. Right. I think of this, I really like there to be a marketplace of ideas, and we hone the ideas by arguing them. And so if it's a specious argument, even if a person is a leader of a company and it just doesn't make sense, I feel it's kind of the responsibility.

[[53:03](https://youtu.be/Pn4ZwlEh5nw?t=3183)] It's better for the company if somebody stands up and points that out than to just let them get away with it. And then it's a little bit confrontational. But as long as people all agree that this is for the greater good, we're gonna, we need to get the right ideas out there. And so let's argue about the ideas just to see, polish them to make them stronger. I think that's important in science and engineering and kind of in life too.

[[53:36](https://youtu.be/Pn4ZwlEh5nw?t=3216)] There's a lot of stuff going on right now in the country that is worrisome. And I certainly stood up and wrote op-eds about things that I think are wrong and need to be corrected. And if people are afraid to do that, it's hard to be optimistic about the future. If people are afraid to stand up when there are wrongs and try to stop them.

**Ryan:**

[[54:02](https://youtu.be/Pn4ZwlEh5nw?t=3242)] You also mentioned optimism in the talk, and you had this story. I wonder if you're willing to share.

**David:**

[[54:08](https://youtu.be/Pn4ZwlEh5nw?t=3248)] So I would say in engineering, it's hard. It's hard to know, right? But I think you need to be kind of optimistic or positive, have a positive outlook because so many things could go wrong. And then my personal story that illustrates this goes back to high school when I'm 16. I'm dating this very attractive girl, and I screw up my courage and ask her if we would be exclusive. At the time, the phrase we used was going steady.

[[54:35](https://youtu.be/Pn4ZwlEh5nw?t=3275)] And she looked at me and said, and, you know, she was 16. She had dated other guys and thought we were pretty young. And she said, "Well, Dave, you're such a nice guy, I don't know how to say no." For me, as a logical person, a no sounded like a yes. And so I hugged her and said, "Great." And so she, in her mind, thought, "Well, I'll let him down gently later." But we've been married 59 years now, and she hasn't let me down yet.

[[55:04](https://youtu.be/Pn4ZwlEh5nw?t=3304)] So that was a case where optimism paid off.

**Ryan:**

[[55:07](https://youtu.be/Pn4ZwlEh5nw?t=3307)] I think everyone that hears about a healthy relationship for that long might wonder how you did it.

**David:**

[[55:13](https://youtu.be/Pn4ZwlEh5nw?t=3313)] I used to tell people, if you go to weddings, the marriage vows are really great, right? But nobody can remember their wedding vows. I used to say, remember your wedding vows, but nobody remembered that. So we boiled it down to nine magic words, and it's just three sentences. And they start: "I was wrong, you were right. I love you." Okay?

[[55:35](https://youtu.be/Pn4ZwlEh5nw?t=3335)] Those are the nine words. And this applies to both partners in a relationship, not just one partner. But, yeah, if you can say them all, and no substitutions— I was wrong. You're right. You're a jerk. You know, you can't do that. If you can remember those nine words, that can help you have a long relationship, like my wife and I have.

### 55:56 — Advice for his younger self

**Ryan:**

[[55:56](https://youtu.be/Pn4ZwlEh5nw?t=3356)] And then last question for you: knowing everything you know now from your career, if you could go back to yourself when you had just entered the industry and give yourself advice, what would you say?

**David:**

[[56:09](https://youtu.be/Pn4ZwlEh5nw?t=3369)] I mean, I think when I got here, because the imposter syndrome. I was a UCLA graduate student, and suddenly I'm a UC Berkeley professor. So that just doesn't seem like— That was very intimidating. But after a while, I just thought, well, I'm probably not going to get tenure, so I should just have a good time. So I think I already had the right attitude about it. I think that first year, I think it was very stressful while I was trying to handle the imposter syndrome and be a UC Berkeley professor.

[[56:40](https://youtu.be/Pn4ZwlEh5nw?t=3400)] But I think after that, I handled it pretty well. I did all the things with the kids and stuff. So there's a version of that question is, like, is there anything I would do over again? There's one thing I would have. I was chair of this, of the architecture community, ACM SIGARCH, as it's called. And they have an annual conference of the year. And I was in, this was in the 1990s, I think I was the chair.

[[57:06](https://youtu.be/Pn4ZwlEh5nw?t=3426)] And what I wasn't aware of is that at these conferences, there were men who were harassing young women at this conference. I just didn't think people like young people, people like me, nobody would do that. Only an idiot would do that. That can't possibly be happening. But it was happening, and I wish somebody had said something to me about it, because I would have straightened it out.

[[57:33](https://youtu.be/Pn4ZwlEh5nw?t=3453)] Any man would have threatened his life if he were to do that. Today, the only comforting thing is Sarita Adve, who's a famous computer architect. She said she also was not aware that that was going on. It became clear later, you know, five or 10 years later, it became more clear that this was going on. And there are mechanisms. Sorry, but that's the one thing I wish. You know, if I could go back in time, I would have figured that out, and I would have straightened men out who were doing that, and they wouldn't.

[[58:05](https://youtu.be/Pn4ZwlEh5nw?t=3485)] That would have stopped. I believe that would have stopped them.

**Ryan:**

[[58:08](https://youtu.be/Pn4ZwlEh5nw?t=3488)] Yeah. Thank you so much for your time today. I really appreciate it.

**David:**

[[58:12](https://youtu.be/Pn4ZwlEh5nw?t=3492)] All right. Thanks for the interview.

