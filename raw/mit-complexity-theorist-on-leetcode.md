---
type: raw-transcript
slug: mit-complexity-theorist-on-leetcode
title: "MIT Complexity Theorist: Why You Can Do Better Than 'Optimal' On Leetcode & SAT | Ryan Williams"
guest: "Ryan Williams"
date: 2026-06-29
url: https://www.developing.dev/p/mit-complexity-theorist-on-leetcode
fetched: 2026-07-19
complete: true
---
# MIT Complexity Theorist On Leetcode

**Guest:** Ryan Williams (MIT Professor, Gödel Prize Winner)
**Host:** Ryan Peterman
**Published:** June 29, 2026

## Host's Introduction

Ryan Williams is a professor at MIT and the winner of the Gödel Prize in theoretical computer science. This episode explores his groundbreaking work on complexity theory, fine-grained algorithms, and lower bounds in computer science.

## Timestamps

- 00:41 - Asking him a popular Leetcode question
- 03:54 - Doing better than the popular optimal solution
- 08:26 - Fine grained complexity
- 17:00 - A severe strengthening of P vs NP
- 24:38 - SAT problems and solvers
- 34:51 - Hot takes on famous open questions
- 46:57 - Simulating space with time
- 01:01:02 - Why he solves hard problems
- 01:02:35 - How to pick good research direction
- 01:07:14 - Technical book recommendations
- 01:08:31 - Advice for his younger self

## Transcript

### 00:41 — Asking him a popular Leetcode question

**Ryan Peterman:**

[[00:41](https://youtu.be/AaK1SL2i_4Y?t=41)] Okay, I want to start by asking you the most popular [LeetCode](https://en.wikipedia.org/wiki/LeetCode) question. So the question is [3SUM](https://en.wikipedia.org/wiki/3SUM): given a list of numbers, we want to find three numbers such that they sum to zero.

[[00:58](https://youtu.be/AaK1SL2i_4Y?t=58)] And so what are your thoughts on the brute force solution for this? We can start there.

**Ryan Williams:**

[[01:04](https://youtu.be/AaK1SL2i_4Y?t=64)] So the obvious brute force solution takes, if you've got n numbers, N cubed time, just try all the triples of numbers, sum them up, see if they sum to zero. There is a faster solution. So one way to get an order N squared time algorithm for [3SUM](https://en.wikipedia.org/wiki/3SUM) is to first start by sorting the numbers. And then you go through the numbers one by one. Say you're looking at a number A, and you want to know, is there a B and a C in the rest of the list whose sum with A is going to be zero?

[[01:45](https://youtu.be/AaK1SL2i_4Y?t=105)] Okay, so the way this works is after you sort the numbers, you do what's called a finger search. So you put the finger from your left hand on the minimum element and a finger from your right hand on the maximum element. So you start there and you check, okay, are these my B and C? Right? So you add them, min and max, and check if adding that with A gets you zero.

[[02:17](https://youtu.be/AaK1SL2i_4Y?t=137)] And if you're lucky, then you're done. But typically you're not lucky. And so this sum of the min and the max is either larger than your target value minus A, or it's smaller. If it's larger, then you need to decrease the larger number. So you take your right finger, which is sitting on the maximum element, and you move it to the left one slot. So you decrease the larger one. All right?

[[02:47](https://youtu.be/AaK1SL2i_4Y?t=167)] If the sum is smaller than your target, you need to take the smaller number and make it a little bit bigger. So you move your left finger, sitting on the minimum, over one slot. Okay? And you keep doing this. You keep checking whether your left finger and right finger are pointing at a solution. And if they aren't, then you adjust it. If they do, if they ever do sum up to exactly what you want, you're done.

[[03:14](https://youtu.be/AaK1SL2i_4Y?t=194)] And so after each comparison, right, one of your fingers moved, okay? If the fingers ever cross, then you don't have a solution. There just can't be a solution. And so the number of times you move your fingers in total is like N. So you have order N solution for finding that extra pair. And you do this for each of the numbers A, okay? So then you get an order N squared solution overall, you do it N times.

[[03:46](https://youtu.be/AaK1SL2i_4Y?t=226)] Each finger search takes order N time.

**Ryan Peterman:**

[[03:50](https://youtu.be/AaK1SL2i_4Y?t=230)] And that is the popular solution.

**Ryan Williams:**

[[03:53](https://youtu.be/AaK1SL2i_4Y?t=233)] That's the popular solution.

### 03:54 — Doing better than the popular optimal solution

**Ryan Peterman:**

[[03:54](https://youtu.be/AaK1SL2i_4Y?t=234)] A lot of people know when we're in these algorithmic [LeetCode](https://en.wikipedia.org/wiki/LeetCode) interviews, and I know a lot of your research is kind of about pushing lower bounds. So maybe we can start that conversation off by asking: can you do better than N squared for this?

**Ryan Williams:**

[[04:10](https://youtu.be/AaK1SL2i_4Y?t=250)] Yeah, you actually can do better than N squared. And this is not at all obvious. In fact, it stems from taking this finger search idea and pushing it in a different direction. So what you do is you take your sorted list, okay, and you break the sorted list up into little groups of contiguous elements. So let's say your little group is like log n size or square root log n. It's like a really small little group, okay?

[[04:42](https://youtu.be/AaK1SL2i_4Y?t=282)] So you've got either n over log n groups total or n over square root log n groups total, depending on how you break up your groups. And then the idea is you're going to perform the same kind of finger search, but you're going to set things up so that you're comparing two pairs of groups. Your finger's always pointing at an entire group. So the left hand and right hand are pointing at two groups.

[[05:08](https://youtu.be/AaK1SL2i_4Y?t=308)] And you want to know if there's a [3SUM](https://en.wikipedia.org/wiki/3SUM) solution in that group. And you can set up a kind of fast data structure to check a small group, okay? This data structure will take much less than the number of elements in the two groups squared. So you set up some kind of fancy data structure. And because you set your group size so small, it's like a preprocessing that you do over all the possible inputs you could send from a pair of groups.

[[05:40](https://youtu.be/AaK1SL2i_4Y?t=340)] And so you have some data structure, and it will, let's say it takes you \(n^{1.5}\) time to prepare this fancy data structure. But now when you're looking at a pair of groups, you can look up the answer much faster than what finger search would have taken. I guess finger search through a group of length \(g\) and another group of length \(G\) would take about \(O(G)\) time, and you can do actually faster by this kind of lookup, this kind of table lookup.

[[06:08](https://youtu.be/AaK1SL2i_4Y?t=368)] I think it is kind of like you take this list of length n and you kind of shrink it into like N over group size number of things. And these are more complicated objects. And then you do, and now you're trying to speed up the check over these small, complicated objects for like, should I move my finger to the right? Is there nothing in this group? Would finger search just go straight through this group or not is basically what you're asking.

**Ryan Peterman:**

[[06:45](https://youtu.be/AaK1SL2i_4Y?t=405)] So the unit that you're operating on is not a single integer, it's a group.

**Ryan Williams:**

[[06:49](https://youtu.be/AaK1SL2i_4Y?t=409)] Yeah, it's a group of them. So you use some kind of table lookup. Well, it's much fancier than a table lookup. Actually, it goes through some other model called the linear decision tree model. So it's like in some weird model where you can actually get a faster [3SUM](https://en.wikipedia.org/wiki/3SUM) solution. You can get it into the 1.5 solution. It's a really interesting and sophisticated solution.

[[07:11](https://youtu.be/AaK1SL2i_4Y?t=431)] But what I want to emphasize is that it starts from the finger search solution and sort of figuring out how to process finger moves faster, sort of do preprocessing so that finger moves can go faster.

**Ryan Peterman:**

[[07:26](https://youtu.be/AaK1SL2i_4Y?t=446)] Yeah, I saw the time complexity of this. It's N squared divided by log n divided by log log n, divided by all raised to the 2/3. What is there any intuition behind that? I mean, that's just crazy.

**Ryan Williams:**

[[07:40](https://youtu.be/AaK1SL2i_4Y?t=460)] So there are several algorithms of this kind, and they all work by doing some modification on what I was talking about because you can sort of reduce to a different model, like a different kind of lookup table, a different kind of set of tricks. And maybe there are some savings you can do here and there by sort of compressing things a little differently. So yeah, there are several algorithms that beat the n squared running time bound, and they all, to my knowledge, kind of work in a similar type of way.

[[08:14](https://youtu.be/AaK1SL2i_4Y?t=494)] They're taking this n-squared time algorithm, finding little ways to preprocess and then optimize based on the preprocessing, like make finger searches faster and things like this.

### 08:26 — Fine grained complexity

**Ryan Peterman:**

[[08:26](https://youtu.be/AaK1SL2i_4Y?t=506)] Yeah, a lot of your research is on this topic of fine-grained complexity, or kind of lowering lower bounds. So maybe you can explain what is lowering lower bounds.

**Ryan Williams:**

[[08:40](https://youtu.be/AaK1SL2i_4Y?t=520)] The idea behind fine-grained complexity is we have a variety of problems, canonical problems, that we teach to undergrads. We have canonical algorithms for these problems. These algorithms have resisted any major improvements in decades. And so we wonder, are these algorithms optimal? And what does the theory of optimality look like in terms of time complexity? So what if we just focus solely on the time complexity of a problem, like the fastest algorithm that will solve that problem?

[[09:22](https://youtu.be/AaK1SL2i_4Y?t=562)] What does complexity look like then? Because P versus NP is not about time. I mean, it's about time complexity. But on a coarse-grained level, where P is just polynomial time, that polynomial could be n to the 10, n to the billion, whatever. And so showing that something's not in P is showing that it needs some superpolynomial amount of time. Whereas here we are concerned with there's a canonical problem, it takes N cubed time.

[[09:53](https://youtu.be/AaK1SL2i_4Y?t=593)] With some very elegant canonical algorithm, we want to know, could you do any better? Could you improve that exponent to n to the three minus epsilon for some epsilon? And then you ask, well, suppose I have a problem over here and it has a quadratic time algorithm, and I want to know if I can improve that quadratic time algorithm by a little bit. Then you start asking questions like, well, suppose I improve this algorithm by a little bit.

[[10:25](https://youtu.be/AaK1SL2i_4Y?t=625)] Can I improve this algorithm over here by a little bit? And this is naturally a notion of reduction, like saying that I want to have some reduction from problem A to problem B, so that if I can improve the algorithm for problem B just a little bit, then I can also improve the algorithm for problem A by just a little bit. This actually leads to a different notion of complexity. You can even take an NP-complete problem and a P problem and reduce the NP problem to the P problem, and the question still makes sense.

[[11:00](https://youtu.be/AaK1SL2i_4Y?t=660)] So, for example, you could talk about the [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem, okay? So the [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem, you've got n numbers and a target value, and you want to know if there's a subset of those numbers that sum to a particular target value. Okay, now you've got 2^n possible subsets. The obvious algorithm takes 2^n time. Okay? But you can actually do better than this. And the way you do better than this is to reduce to a polynomial-time solvable problem.

[[11:41](https://youtu.be/AaK1SL2i_4Y?t=701)] So you can get an algorithm which runs in square root of 2 to the N time. For the [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem, you can avoid enumerating over all the possible subsets in a substantial way. And this is, in fact, known as commonly used in [cryptanalysis](https://en.wikipedia.org/wiki/Cryptanalysis) by, I guess, a [meet-in-the-middle](https://en.wikipedia.org/wiki/Meet-in-the-middle_attack) type approach. So people do this sort of thing all the time. The idea is you partition the set of all the numbers into two halves, like n over two, n over two.

[[12:16](https://youtu.be/AaK1SL2i_4Y?t=736)] You enumerate all the subset sums on the two halves. So you have 2 to the n over two possible sums for the first half, two possible sums for the second half. Then you want to know, is there a number from the first half, from this huge list, plus another number from the second half, this huge list, that sums to the target. Now this is the 2SUM problem. This is really nothing more than a 2SUM problem, which you can solve by sorting and binary search.

[[12:51](https://youtu.be/AaK1SL2i_4Y?t=771)] And this is a reduction. We have shown how to solve a [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem, which would normally take 2 to the n time, in square root of 2 to the N time, an NP-complete problem, by reducing it to a problem like 2SUM. The obvious algorithm there takes n squared time, trying all the pairs of numbers to see if they sum to a target, and using an n log n time algorithm for that. So fine-grained complexity can relate problems that would not be relatable at all in the traditional P vs NP theory.

[[13:28](https://youtu.be/AaK1SL2i_4Y?t=808)] Like, one problem should be complete, the other problem's not, so they should not have a polynomial-time reduction between them in general. Right. But if you just look at the time complexity and you focus on, okay, I have an algorithm, 2 to the n algorithm, is it the best possible? And then I have an n squared algorithm, is it the best possible? And then you can relate the two problems, and this is a general phenomenon that you can relate problems that look like they should have nothing to do with each other.

**Ryan Peterman:**

[[13:58](https://youtu.be/AaK1SL2i_4Y?t=838)] So you talked about reducing a [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) to 2SUM, but [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) is arbitrary integers that sum to the target sum, right?

**Ryan Williams:**

[[14:11](https://youtu.be/AaK1SL2i_4Y?t=851)] Yeah. So the idea is, nobody said I had to use a polynomial-time reduction or something like that to reduce one problem to another. So what happened? The trick was I took this [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem that had n numbers and then I blew it up to an instance of this 2SUM problem. But that 2SUM problem has about square root of 2 to the n numbers. Now I can solve 2SUM in linear time, so solving that instance gives me a square root of 2 to the n time algorithm for the original problem.

[[14:49](https://youtu.be/AaK1SL2i_4Y?t=889)] But yeah, in the meantime, going from one problem to the other, I blew it up. But by blowing it up, I'm able to improve the time complexity of the obvious algorithm for [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem).

**Ryan Peterman:**

[[15:01](https://youtu.be/AaK1SL2i_4Y?t=901)] I get it. Okay. So the reduction, it's kind of like if you solve the [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem), you have some time complexity, and if you translate it to the other problem, you lose a little bit of time complexity, but less than the aggregate.

**Ryan Williams:**

[[15:17](https://youtu.be/AaK1SL2i_4Y?t=917)] So all you want to make sure is when all the dust is cleared and settled, you want to be able to say, look, if I can improve the obvious algorithm for 2SUM, then I can improve the obvious algorithm for [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem). And that's what this thing achieves, because I know how to get a faster algorithm for 2SUM. I can get one for [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem). So you just want your reduction between two problems to have this property.

[[15:43](https://youtu.be/AaK1SL2i_4Y?t=943)] If I can improve one problem by a little bit in running time, I can improve the other problem by a little bit.

**Ryan Peterman:**

[[15:49](https://youtu.be/AaK1SL2i_4Y?t=949)] In one of your talks, you mentioned preserving magic between.

**Ryan Williams:**

[[15:54](https://youtu.be/AaK1SL2i_4Y?t=954)] Right.

**Ryan Peterman:**

[[15:54](https://youtu.be/AaK1SL2i_4Y?t=954)] Okay, so this is that.

**Ryan Williams:**

[[15:55](https://youtu.be/AaK1SL2i_4Y?t=955)] Yes, this is exactly like preserving magic because once you see the 2SUM solution, it's not so magical anymore. But imagine that you didn't know about sorting and binary search and the like, and someone just says, find a pair of things with a certain property and there are N things. And you're like, well, all the number of possible pairs is about N squared, so maybe it'll take me N squared in this particular case, because they're numbers and you're summing them.

[[16:28](https://youtu.be/AaK1SL2i_4Y?t=988)] There's an n log n time algorithm. It is a surprise when you first see that. No, you don't have to try all of the pairs of numbers. There is a shortcut. There is a clear shortcut that lets you find a pair much faster. And then you can use that surprise, or magic, if you will, and get something for [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem). Get an algorithm for [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) that avoids trying all of the subsets.

### 17:00 — A severe strengthening of P vs NP

**Ryan Peterman:**

[[17:00](https://youtu.be/AaK1SL2i_4Y?t=1020)] So I understand one of the driving motives for pursuing this, I guess, lowering of lower bounds is the Strong Exponential Time Hypothesis, or SETH. Could you explain that and its significance?

**Ryan Williams:**

[[17:18](https://youtu.be/AaK1SL2i_4Y?t=1038)] SETH is like a severe strengthening of the P vs NP question. So P vs NP is asking whether the SAT problem has a polynomial-time algorithm or not.

**Ryan Peterman:**

[[17:37](https://youtu.be/AaK1SL2i_4Y?t=1057)] Right.

**Ryan Williams:**

[[17:38](https://youtu.be/AaK1SL2i_4Y?t=1058)] And SETH is basically saying that for the SAT problem, you cannot solve it much faster than 2 to the n. So there's no 1.999 to the n time algorithm for every string of nines. There is no 1.9999 to the n time algorithm, to say the hypothesis totally precisely. It has to do with the k-SAT problem. And you're looking at clauses of length k for arbitrary k, but those details don't matter.

[[18:21](https://youtu.be/AaK1SL2i_4Y?t=1101)] So much. It's a canonical NP-complete problem. SAT is solved all the time. In practice, it's extremely useful for verification. Nowadays it's an engine for verification. So it can be solved fairly well in practice. However, in the worst case, we still don't know how to solve it significantly faster than 2^n. So the hypothesis that it needs, say, 1.9999^n time for all strings of n is a very strong exponential time hypothesis.

[[19:00](https://youtu.be/AaK1SL2i_4Y?t=1140)] And so it's stronger than P versus NP. It says, no, no, no, it says not superpolynomial. It's actually darn near the end time that you need.

**Ryan Peterman:**

[[19:09](https://youtu.be/AaK1SL2i_4Y?t=1149)] Right. And so do you think that hypothesis is true? And why or why not?

**Ryan Williams:**

[[19:15](https://youtu.be/AaK1SL2i_4Y?t=1155)] I think I'm on the record as not believing this hypothesis. Yeah, yeah. Why don't I believe this hypothesis? Well, I started thinking about this hypothesis maybe already as an undergrad, but certainly starting in grad school. Early in grad school, I was thinking about this. So before it was even called SETH, I guess that shows how old I am, I was trying to think about how to solve this so-called CNF-SAT problem faster than 2^n.

[[19:52](https://youtu.be/AaK1SL2i_4Y?t=1192)] And well, at the time there were a number of other NP-complete problems that had faster algorithms, like [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem). So I thought, well, there's not, I mean, what's so special about SAT? If all these other problems have faster algorithms, why not SAT as well? If you restrict to the 3-SAT problem, this is where you have an AND of these clauses. Each clause is an OR of three variables.

[[20:30](https://youtu.be/AaK1SL2i_4Y?t=1230)] Some of the variables may be negated. You want to know if there's a way to set all the variables to make all the clauses simultaneously true. There is a faster algorithm for that, but this is a more general version of SAT. So at first I just thought, well, there's no good reason to think in a lower bound. These other related problems have upper bounds, so why not? But then over time I would have different attacks on SETH, like trying to refute it, always trying to refute it in different ways. These attacks would fail in some completely catastrophic and ridiculous way.

[[21:13](https://youtu.be/AaK1SL2i_4Y?t=1273)] They would have no chance of actually solving the original problem. But by sort of staring at my failure and trying to think, well, there's something interesting happening here. What can I do with this? There's something interesting, yeah, it doesn't refute the Strong Exponential Time Hypothesis thing. What does it do? So by trying to pivot and figure out, okay, what can I do with my failure, I was able to solve a variety of other problems instead.

[[21:47](https://youtu.be/AaK1SL2i_4Y?t=1307)] And so after a while, I realized that the truth value of SETH to me is almost irrelevant because if I believe that it's false, then I get good ideas. I get good ideas. And so by trying to think about, okay, what would an algorithm that breaks 2-SAT look like? What could it look like? I sort of force myself to think in a different way. I have to discard other natural algorithmic possibilities because we know they won't work, and I have to think in a different direction.

[[22:32](https://youtu.be/AaK1SL2i_4Y?t=1352)] And so because it kind of sends my brain in a different direction, sends me thinking a different way, it's very useful for research. I mean, even though I still haven't refuted it or whatever, it's very useful for me to believe that it's false operationally.

**Ryan Peterman:**

[[22:55](https://youtu.be/AaK1SL2i_4Y?t=1375)] I believe this is a minority opinion, right? Why would they go against it?

**Ryan Williams:**

[[22:59](https://youtu.be/AaK1SL2i_4Y?t=1379)] I mean, I think, for example, Russell Impagliazzo, a good friend of mine who helped propose this. I mean, he always emphasizes to me, well, this is a hypothesis. We explicitly did not name it a conjecture. We wanted to sort of put forth some lower bound that would get you to think about it, like something that's maybe a little more controversial than the other types of things like P vs NP or whatever, or other things that people more normally believe.

[[23:34](https://youtu.be/AaK1SL2i_4Y?t=1414)] So, hypotheses which are at the edge of our understanding can be enlightening to think about, like where we truly don't know what the answer might be based on our intuition. So this is, I guess, one reason why it was proposed. But one reason why you might believe that SETH is true is because believing it implies a lot of other lower bounds for you. Conveniently, because you can reduce the SAT problem to a bunch of other problems that seem totally unrelated, like edit distance, various pattern matching problems.

[[24:18](https://youtu.be/AaK1SL2i_4Y?t=1458)] They have natural polynomial-time solutions. If you can improve on the algorithms for any of those, you would improve the one for SAT as well. You would get something better than 2^N. So believing in it sort of makes a convenient worldview. It shows that all these different textbook algorithms are indeed optimal.

### 24:38 — SAT problems and solvers

**Ryan Peterman:**

[[24:38](https://youtu.be/AaK1SL2i_4Y?t=1478)] We've talked about SAT, or we've mentioned SAT so many times in this conversation. I know there are so many forms of that problem. What are all the different forms? And I know there's clause width, also this idea of depth, too.

**Ryan Williams:**

[[24:51](https://youtu.be/AaK1SL2i_4Y?t=1491)] The most common representation of a SAT formula is a conjunctive normal form, so-called CNF representation. And this is what modern SAT solvers get as input. They get their file in so-called DIMACS CNF form. And this is just every line of my file. I give you a list of variables, possibly with negations, and each one is a clause. And I'm supposed to take the OR of those variables or negations. These are variables or negations.

[[25:30](https://youtu.be/AaK1SL2i_4Y?t=1530)] They're often called literals. Okay? So I take an or of these literals, and the width of that clause is the number of literals in it, okay? And I'm supposed to take the and over all those lines, each line in my DIMACS CNF file. So it's an and of a bunch of ors, and each or has some small number of literals in it, call it k. So usually the width is called k. And so the k-SAT problem is to find an assignment to all the variables that satisfies all the clauses.

[[26:09](https://youtu.be/AaK1SL2i_4Y?t=1569)] When each clause has width k or at most K, it could be smaller. So that's the most popular version. That's what SAT solvers churn on. And that's what is behind SETH. That's the representation there. But there are other ways to represent a Boolean formula. You could just simply represent it as some arbitrary expression made up of ors and ands and negations. It could just be some arbitrary expression with nested parentheses and all that mess.

[[26:51](https://youtu.be/AaK1SL2i_4Y?t=1611)] You could ask, given a formula in this representation with a bunch of variables, is there a way to set the variables to make this true? That's Formula-SAT. You could also look at circuits of bounded depth, as you mentioned. So there is this class of circuits that people study called AC circuits for alternating circuits. It doesn't mean alternation in terms of electricity; it means alternation in terms of ors and ands.

[[27:28](https://youtu.be/AaK1SL2i_4Y?t=1648)] So these circuits are made up of ORs and ANDs, in layers. So the CNF representation is a special case where I have an AND of ORs, like an AND of a bunch of clauses and ORs of the literals. But you can go further. You can have an AND of OR of ANDs of variables with negations and things like that. And so these are constant-depth AC circuits. And because the idea is you only have some constant number of layers of these ANDs and ORs.

[[28:05](https://youtu.be/AaK1SL2i_4Y?t=1685)] And you can look at the SAT problem on circuits like that as well. For example, those are two other versions that people look at.

**Ryan Peterman:**

[[28:13](https://youtu.be/AaK1SL2i_4Y?t=1693)] Yeah, SETH is on k-SAT. And I saw on 2-SAT, 3-SAT, 4-SAT, 5-SAT, there exist solutions that are asymptotically better than 2 to the N. So I guess the larger K can be, the more difficult the problem.

**Ryan Williams:**

[[28:33](https://youtu.be/AaK1SL2i_4Y?t=1713)] That's the intuition. That is the intuition.

**Ryan Peterman:**

[[28:36](https://youtu.be/AaK1SL2i_4Y?t=1716)] I'm curious, have you ever plotted that curve? Does it drop off exponentially, or...

**Ryan Williams:**

[[28:41](https://youtu.be/AaK1SL2i_4Y?t=1721)] Yeah, yeah, yeah. That's what's so interesting about the current state of the art in k-SAT algorithms. As K increases, all of them, all of the different types of algorithms you might try to run, they all approach a 2 to the n exponent. Like as K grows and grows and grows, they get 1.99, 1.999, and so on. And yeah, it drops. In other words, it goes toward two pretty quickly, actually. So we understand how the exponent behaves pretty well for the known algorithms we have.

**Ryan Peterman:**

[[29:24](https://youtu.be/AaK1SL2i_4Y?t=1764)] And then for something like 3-SAT, what is the intuition behind speeding up an exponential time search?

**Ryan Williams:**

[[29:32](https://youtu.be/AaK1SL2i_4Y?t=1772)] Yeah, so for 3-SAT, let's just look at a single clause. Okay. A clause that's got three variables in it. Okay. We know that if we set all those three variables wrong, it's going to be false. Okay. So we have to avoid one of those assignments. Okay, well that means that there are seven out of the eight possible assignments. So there's three variables, 2 to the 3, eight possible assignments.

[[30:01](https://youtu.be/AaK1SL2i_4Y?t=1801)] Seven of them could be a satisfying assignment. They could be part of a satisfying assignment. We don't know. But one of them is definitely not. So one easy way to see that 3-SAT can be solved in less than 2^n time is just take any clause, try one of the seven possible assignments and plug them in, and then recurse on the remaining formula. Now let's think about what we did. If we were just trying all the possible 2^n assignments and we would like plug in one of eight possible assignments for each of those three variables.

[[30:43](https://youtu.be/AaK1SL2i_4Y?t=1843)] And so we'd have seven recursive calls. Well, instead, because we're clever and we looked at the clause, we have seven recursive calls, and that's the difference. So we reduced by three variables at the cost of seven recursive calls, as opposed to eight. And this gets you a slight improvement. This gets you about 1.92 to the N. Something slightly better than to the N. Okay, but you can do better than this.

[[31:17](https://youtu.be/AaK1SL2i_4Y?t=1877)] But this is sort of like the idea you try to look at ways to plug in variables that will force constraints so you can rule out a large portion of the possible assignments.

**Ryan Peterman:**

[[31:30](https://youtu.be/AaK1SL2i_4Y?t=1890)] When I was thinking about circuits and the different widths and depths, I don't know if this is an unusual question, but it reminds me of neural nets. But the operators are different and the space of the literals is different. So instead of booleans, it's maybe floating points. And so it just made me wonder about the algorithms that you might apply on a neural net. Is there analogs between these two spaces?

**Ryan Williams:**

[[32:01](https://youtu.be/AaK1SL2i_4Y?t=1921)] Yes, yes. If we look at, say I want to model a neural network, so I want to compute, say it's still a Boolean function, but I want to do it with a neural network. So I want to use, let's say ReLU or sign activation functions or what have you. There is a slightly more general gate that we can use instead of ORs and ANDs that turns out to basically be equivalent. So if instead of using ORs and ANDs, we use a so-called majority gate, which outputs one if and only if at least half of its inputs are one, using this and negations, we can actually simulate neural nets, like the usual types of neural nets that you think of with the usual types of activation functions.

[[33:03](https://youtu.be/AaK1SL2i_4Y?t=1983)] So if they have a constant number of layers of neurons, we can get a constant number of layers of majority gates and negations. So this is so-called TC circuits for threshold circuits.

**Ryan Peterman:**

[[33:19](https://youtu.be/AaK1SL2i_4Y?t=1999)] Yeah.

**Ryan Williams:**

[[33:19](https://youtu.be/AaK1SL2i_4Y?t=1999)] So once you allow threshold circuits, you can start to model neural networks still using Booleans. We're still looking at Boolean inputs though. Yes. So once you allow your input space to be larger and have floating points, then you can prove a lot more in terms of lower bounds. You can find things that take depth 3 in the neural net that can't be done in depth two and so on. So yeah, once you go past that and you start looking at just arbitrary real domain, it becomes a totally different picture from a discrete domain.

### 34:51 — Hot takes on famous open questions

**Ryan Peterman:**

[[34:51](https://youtu.be/AaK1SL2i_4Y?t=2091)] One topic I thought might be fun to go over is you wrote this paper about the likelihoods of these various conjectures and complexity theory.

[[35:00](https://youtu.be/AaK1SL2i_4Y?t=2100)] And I pulled a few of these that were kind of minority opinions, or maybe less common takes. Curious to hear your rationale. Okay, one of them, the well-known one, P not equal to NP, or P vs NP, you assigned an 80% confidence that they're not the same. Yes, and I think most people say much higher confidence. So why would you assign such a low confidence that they're not the same?

**Ryan Williams:**

[[35:32](https://youtu.be/AaK1SL2i_4Y?t=2132)] It's interesting because I think I originally had something like 75%, but then my college classmate Scott Aronson was like, how dare you? Kind of. He sort of called me out. I'm like, okay, fine for you, 80% fine. I guess my point is that we really don't understand polynomial-time computation as deeply as we think we do. And there are surprises, like all the time, in the power of algorithms. There are very few surprises in terms of lower bounds.

[[36:13](https://youtu.be/AaK1SL2i_4Y?t=2173)] When we are able to prove a lower bound, typically it's something we very much expected to be true. But it was hard to prove. Somehow we pulled it off, we got what we expected to be true. But all the time in algorithms, people are finding algorithms where it's just surprising. Just wait, what? How do you get something that fast? Right? So this just happens over and over.

[[36:47](https://youtu.be/AaK1SL2i_4Y?t=2207)] When I was younger, when I was first thinking about P versus NP, I had an intuition for what should be. And what I've understood over the years is that my intuition for what should be is often just wrong. And I'm having to revise my intuitions all the time. So when something like this happens often enough, you start asking yourself, what do I really understand? Do I really understand P versus NP?

[[37:26](https://youtu.be/AaK1SL2i_4Y?t=2246)] I mean, I understand that the statement, right? It's just one of those problems where somehow it is not so difficult to make formal, to write down mathematically, but to actually know what the answer is is just orders of magnitude more difficult than it is to phrase the problem. And complexity theory in particular is littered with statements like this, where the space of algorithms is just that vast.

[[38:01](https://youtu.be/AaK1SL2i_4Y?t=2281)] So if you just keep getting surprised over time, you're like, well, what do I understand? Maybe it was just misplaced confidence.

**Ryan Peterman:**

[[38:10](https://youtu.be/AaK1SL2i_4Y?t=2290)] Okay, what about this one? So EXP not equal to NEXP. Or would you say NEXP?

**Ryan Williams:**

[[38:16](https://youtu.be/AaK1SL2i_4Y?t=2296)] Oh, NEXP. Yeah, X versus NEXP. So this is like the exponential time of P versus NP for EXP not equal to NEXP.

**Ryan Peterman:**

[[38:22](https://youtu.be/AaK1SL2i_4Y?t=2302)] Or NEXP, you gave it a 45% chance. And if this is the P vs NP equivalent, but for exponential time, why is it so low?

**Ryan Williams:**

[[38:39](https://youtu.be/AaK1SL2i_4Y?t=2319)] Oh, because exponential time algorithms are even more powerful. Did I really say 45%? I mean for NEXP versus EXP or NEXP versus coNEXP?

**Ryan Peterman:**

[[38:49](https://youtu.be/AaK1SL2i_4Y?t=2329)] Yeah, NEXP not equal to EXP, 45%. It's in this table.

**Ryan Williams:**

[[38:55](https://youtu.be/AaK1SL2i_4Y?t=2335)] So in other words, I believe NEXP equals EXP more than I believe they're different. Right? So, yeah, let me try to explain why. So you can think of the NEXP vs. EXP question as some special case of P vs. NP where instead of looking at the arbitrary SAT problem, I'm looking at a SAT problem which is extremely compressible. So there's a really small little computer that is exponentially smaller than the length of the instance, and it just outputs the character on the line number and the column number for the DIMACS CNF, like the CNF file.

[[39:44](https://youtu.be/AaK1SL2i_4Y?t=2384)] Okay? So it's like an extreme compression of some file. So it's like you zipped it down to something like exponentially smaller than its original length. Okay, so it's like some super compressed, extremely highly regular SAT instance. So I give you that and I ask you, when you unpack this thing, decompress it, is the result going to be satisfiable or not? And I want you to solve this in time polynomial in the decompressed representation.

[[40:20](https://youtu.be/AaK1SL2i_4Y?t=2420)] Okay. So the point is that this is SAT, but in some very special case where the thing is extremely structured. So the idea, one conjecture for why SAT solvers work in practice, like one, I mean, this is, I mean, conjecture may be overkill because, I mean, this is just. This is not even a well-formed mathematical statement. So one hypothesis for why SAT solvers work in practice is because the real world is highly structured.

[[40:58](https://youtu.be/AaK1SL2i_4Y?t=2458)] The real world is governed by physical laws that are not random, they're not arbitrary. From a very small number of rules, we can recreate so much of science. So what arises in practice from designs of hardware and things like this are often extremely compressible. They have to be extremely compressible. And so maybe it's true that every sentence which has a highly compact representation can just be solved efficiently.

[[41:35](https://youtu.be/AaK1SL2i_4Y?t=2495)] This is the idea of whether in P vs NP that when it's really, really structured like that and super compressible, there is some advantage. It's not like something completely random. And since it's not like something arbitrary, it's, in fact, very, very special.

**Ryan Peterman:**

[[41:51](https://youtu.be/AaK1SL2i_4Y?t=2511)] The other one is 80% likelihood on NEXP equal to coNEXP. And you wrote, "Why would a self-respecting complexity theorist do that?" Yeah, I was curious why that's such a contentious statement.

**Ryan Williams:**

[[42:08](https://youtu.be/AaK1SL2i_4Y?t=2528)] So NEXP versus coNEXP. Let's first talk about NP versus coNP. So coNP is like the class of complements of NP-complete problems like UNSAT, like checking whether something is UNSAT. Now from the time-complexity point of view, there's no difference between checking SAT and UNSAT. You can always flip the answer from the complexity point of view. If I ask you, does coNP equal NP? What I'm asking you is could you prove to me that a formula is unsatisfiable with a short proof when it's satisfiable?

[[42:50](https://youtu.be/AaK1SL2i_4Y?t=2570)] I can give you a short proof. I can just give you the satisfying assignment, you plug it in, check that it works. But if it's unsatisfiable, if no assignment works, we're saying for all assignments the formula is not true. Can you flip that to an existential statement and say, oh, there exists this little proof that makes it work? So people don't believe that NP is equal to coNP, and in fact NP different from coNP implies P different from NP.

[[43:21](https://youtu.be/AaK1SL2i_4Y?t=2601)] But so this is the exponential time version of P vs NP. So it's coNEXP versus NEXP. The reason why I think these are likely to be equal is that if a little birdie sat on a NEXP machine's shoulder and gave it a little bit of advice about what the coNEXP thing is doing, then the NEXP algorithm can actually solve coNEXP problems. And so let me explain, let me explain why. What's the little birdie?

[[44:02](https://youtu.be/AaK1SL2i_4Y?t=2642)] What the heck is the little birdie saying? So because NEXP problems can run in 2 to the n time and 2 to the n squared time and things like that, running an exhaustive search over all possible inputs of length n is no problem for NEXP. So what a little birdie can do is say, okay, suppose I want to verify that this particular instance, let's say we can talk about an UNSAT, but some compressible UNSAT problem or something.

[[44:38](https://youtu.be/AaK1SL2i_4Y?t=2678)] Suppose I want to prove that this compressible UNSAT instance is a yes. Okay, how am I going to do that? With NEXP, the little birdie will tell me the total number of inputs of length N which are a yes. Okay, so it will just tell me some string which says, "Here's the total number of inputs of length N. You gave me a length-N input. Here's the total number of inputs of length N that are a yes."

[[45:09](https://youtu.be/AaK1SL2i_4Y?t=2709)] Okay. So this advice, this little bird's advice doesn't take very much to encode count. It's like order in bits to encode a count of things. So what does the NEXP thing do to prove a coNEXP thing? What it does is it guesses the things which are a no. So I'm trying to prove UNSAT. So UNSAT means yes, SAT means no. So the NEXP thing guesses those things which are no.

[[45:45](https://youtu.be/AaK1SL2i_4Y?t=2745)] The no things it can answer, right? If it's a SAT thing, it can just guess the answer to each of the no's. Okay, so it guesses the answer to each of the no's, it verifies all those answers, and then it checks the number of things it guessed is what the birdie told it. Once it's done that, all the no's have been covered, so everything else must be a yes. So it can actually prove a yes by just exhaustively finding all the no's and ruling out any other no's.

**Ryan Peterman:**

[[46:21](https://youtu.be/AaK1SL2i_4Y?t=2781)] But the big question in my mind is, where do you get the little birdie?

**Ryan Williams:**

[[46:24](https://youtu.be/AaK1SL2i_4Y?t=2784)] Where do you get the little birdie advice from? Yeah, yeah. So, yeah, so this I've studied. Yeah, this is what the little birdie gives you. And it seems to me that it's possible that this little birdie itself can be constructed in NEXP. And if so, then we'd just be done. In NEXP, you figure out what the little birdie would tell you and then use that to just flip the answer. So, I guess let's sort of guess all the things which are no.

[[46:55](https://youtu.be/AaK1SL2i_4Y?t=2815)] So what remains must be a yes.

### 46:57 — Simulating space with time

**Ryan Peterman:**

[[46:57](https://youtu.be/AaK1SL2i_4Y?t=2817)] And we talked a lot about time complexity, and you mentioned a little bit this advice, I guess, kind of space complexity. And I know you had a major result relating space and time complexity. You're basically simulating time complexity with space complexity, but lower than it's been done prior. Could you explain what it was before your breakthrough result and then maybe the intuition behind your breakthrough result?

**Ryan Williams:**

[[47:25](https://youtu.be/AaK1SL2i_4Y?t=2845)] In general, the problem is the following. I give you an algorithm that runs in time T, and I want to know, is there another algorithm that uses space much less than T, uses an amount of memory much less than T, and still solves the problem completely, still completely simulates the thing perfectly. One intuition for why you might think this question just can't be solved.

[[48:01](https://youtu.be/AaK1SL2i_4Y?t=2881)] For some problems, there's just no way to improve on the space. If you think of a lot of problems in dynamic programming, let's say I have some logic circuit that I want to evaluate, and all the gates are provided to me in a row, and all the wires sort of flow from left to right, and I start with information on the left. I want to compute the information on the far right, and all the bits are flowing left to right by wires.

[[48:36](https://youtu.be/AaK1SL2i_4Y?t=2916)] The natural way to evaluate such a circuit is you start with, say, the inputs on the left. For each gate in turn in the line, you look at its inputs. Its inputs have been determined. There are some bits. You use that to compute the value of that gate. You pass the values of the output of that gate forward. But if that circuit has T gates in it, it will take about T time to solve, but it will definitely also take about T space in general.

[[49:10](https://youtu.be/AaK1SL2i_4Y?t=2950)] Right? Like the circuit could be wired up in some wild way, and there just might not be a way to save space for an arbitrary circuit. But already in 1975, people were studying this kind of question and finding counterintuitive answers to it. So Hopcroft, Paul, and Valiant, based on work of Paterson and Valiant, showed that time T algorithms, at least in this so-called multi-tape Turing machine model, a very powerful model, can be simulated in space t divided by log of t.

[[49:54](https://youtu.be/AaK1SL2i_4Y?t=2994)] It's like you get some space savings, but it's only a log T factor. Okay. And the way this is done is quite counterintuitive. Even though there's only a log factor, it was pretty shocking that development was extended to random access models of computation later and more general models of computation. So, in the late 70s and early 80s, it was known for pretty much any reasonable model of computation that time T can be simulated in space about T over log T.

[[50:42](https://youtu.be/AaK1SL2i_4Y?t=3042)] But there was a hidden, maybe not so hidden, gotcha. In the space-efficient simulation, it needs an exponential amount of time to run. So there's a time-space tradeoff. Okay. If you really want to save some space, you got to blow up the time by a lot. Nevertheless, yeah, it was kind of commonly conjectured that this T over log T space was about the best you could do and that you were probably not going to get T to the 0.

[[51:17](https://youtu.be/AaK1SL2i_4Y?t=3077)] 9 space or something much more efficient. So, yeah, it was a big surprise to me that you can actually put time T in space about square root of T. Again, there's an exponential running time just to give the full caveat out there. But it's still very surprising. This holds for any kind of time T algorithm, including something that might be outputting something pseudorandom, something from cryptography.

[[52:00](https://youtu.be/AaK1SL2i_4Y?t=3120)] It's not at all obvious that every such process could be compressed to only need square root of t space and still get the job done, still compute whatever function was being computed.

**Ryan Peterman:**

[[52:13](https://youtu.be/AaK1SL2i_4Y?t=3133)] I mean, I know it's probably super involved, but if you could just, at a high level, what's the trick? How'd you do it?

**Ryan Williams:**

[[52:19](https://youtu.be/AaK1SL2i_4Y?t=3139)] Well, the trick for me was to read James Cook and Ian Mertz's paper on tree evaluation very, very carefully, and just know the landscape around P versus PSPACE and know what Hopcroft, Paul, and Valiant did. Yeah. But I can give you a very high-level idea of kind of what's going on and how what they did is useful. So Hopcroft, Paul, and Valiant, the way they were modeling space-bounding computation was in a particular way that seemed pretty general at the time, but turned out to be restrictive in ways that we just didn't anticipate.

[[53:10](https://youtu.be/AaK1SL2i_4Y?t=3190)] So the way they thought of it was I'm gonna take certain, I'm gonna break the computation up in little pieces, and I'm gonna write pieces of the computation, little bits, into the memory, but I'm only gonna do that over blank space. I mean, this is something that sounds natural, right? So I'm gonna erase pieces of memory and then I'm going to overwrite that blank space with a piece of memory.

[[53:43](https://youtu.be/AaK1SL2i_4Y?t=3223)] So I'm being very destructive in a certain sense. But this is a natural thing you do, right? If you want to replace, swap something with something else, you often just erase. But there are ways to swap without erasing, right? So there's a common little trick that is taught in CS courses. So if you require everything to be written into a blank register, then if you want to swap the contents of two variables like X and Y, then you've got to have a temporary register.

[[54:23](https://youtu.be/AaK1SL2i_4Y?t=3263)] You move one into the temp, you erase it, you move Y into there, and so on. Right. But if you don't want a temp, you can achieve the same thing with just XORing the registers bitwise, or if you've got numbers, you can add and subtract. Okay. In three instructions, clever instructions, adding, subtracting, or XORing, you can actually swap the contents of two registers without needing a third. Okay.

[[54:54](https://youtu.be/AaK1SL2i_4Y?t=3294)] This is kind of the starting point for thinking about, well, why does it matter if you're always writing into erased memory? So what James Cook and Ian Mertz showed at a very high level was they were studying a certain problem called Tree Evaluation Problem, whatever that is. And the problem had an algorithm where you had a little stack and you were always sort of popping and pushing on the stack, but you were always writing computation contents into erased memory.

[[55:42](https://youtu.be/AaK1SL2i_4Y?t=3342)] Okay. What they realized was that if you allow computations to XOR bits of memory into existing memory, then you can save a lot of space. So if you're really, really careful about how you XOR things, you can basically recover what's in your memory without storing all of it at once. You sort of offload things to computation, and you XOR on top of things very, very cleverly. You can get nice cancellations of things you don't want and keep around things you do want.

[[56:18](https://youtu.be/AaK1SL2i_4Y?t=3378)] Yeah. So that is a high-level idea of how this stuff works.

**Ryan Peterman:**

[[56:24](https://youtu.be/AaK1SL2i_4Y?t=3384)] And then going to square root, is it just an extension of that, or is it completely different?

**Ryan Williams:**

[[56:29](https://youtu.be/AaK1SL2i_4Y?t=3389)] So the way it works with square root is square root just happens to be kind of like the optimal tradeoff in this Tree Evaluation Problem business. So what you do is you break the computation into square root of t time intervals. And each time interval has about square root of t steps in it. And what you do is you give a particular way of simulating this thing so that you're only kind of holding about a constant number of blocks of these time intervals in memory at any point in time.

[[57:09](https://youtu.be/AaK1SL2i_4Y?t=3429)] Like you're only holding a small number of these time intervals, records of time intervals, in memory at any point in time, which is entirely not obvious how you would do it, but it's some sort of sweet spot to set the square root of T. It's like the minimum setting of tradeoff. Say I want to break the computation into intervals, and the intervals have a certain number of steps. If I set it to be square root of T, then the number of intervals and the number of steps in each interval is about the same.

**Ryan Peterman:**

[[57:44](https://youtu.be/AaK1SL2i_4Y?t=3464)] So I mean, that was a long-held result. I mean, you mentioned it was 1975, that's maybe almost 50 years. If you come up with something like that, and I guess you're writing it out, you're thinking through, and then you see it, what is that moment like?

**Ryan Williams:**

[[58:00](https://youtu.be/AaK1SL2i_4Y?t=3480)] So I've been around long enough to have been deceived by myself many, many times. So, yeah, I guess the first two or three times I thought about this, I just thought, this is another one of those ideas that can't possibly work. There's no way. There's just no way this works. So I would just kind of leave it and then come back to it sometimes when I was bored of whatever else I was working on.

[[58:35](https://youtu.be/AaK1SL2i_4Y?t=3515)] It was a pretty slow process of convincing myself that this could possibly be true. I thought there was either a bug in what James and Ian was doing somewhere, or there was a bug in my interpretation of what's happening. I thought there had to be a mistake for a long time. And the only way I got over that was just writing it down over and over and over in different ways, sort of writing and rewriting and writing and rewriting and adding more detail and then maybe finding a different way of explaining it and erasing and writing something shorter and just sort of re.

[[59:23](https://youtu.be/AaK1SL2i_4Y?t=3563)] Explaining it to myself over and over and over. And even then, when I submitted it to the STOC conference where it appeared, I wasn't entirely confident that it was correct. I was just exhausted from thinking about it for so long and just thought, maybe someone else will find the mistake for me. I got at this point, I was just desperate.

[[59:49](https://youtu.be/AaK1SL2i_4Y?t=3589)] I had actually sent it to two colleagues that I trust privately and asked them, "Can you help me find the mistake? Or whatever? Can you help me understand this?" And one of them just said, basically, they just didn't read past the abstract. They're like, "I'm not. I'm sorry, I'm not going to." I'm like, they just didn't believe it, period. Just like me. I mean, they didn't believe it.

[[01:00:17](https://youtu.be/AaK1SL2i_4Y?t=3617)] And another one said, after a long time, "Well, I didn't quite follow it, but there was a footnote that you put, like, in the bottom of some page. After that, after that footnote, then I began to believe it."

So then what I did was I just took that footnote and elaborated it in a later revision, sort of made it what I called the warmup, because I was like, yeah, I've got to do. I've got to write this thing in a way that is airtight so that other people will actually believe this.

[[01:00:56](https://youtu.be/AaK1SL2i_4Y?t=3656)] Because, yeah, it took me a long time to get used to it, to believe it. Yeah.

### 01:01:02 — Why he solves hard problems

**Ryan Peterman:**

[[01:01:02](https://youtu.be/AaK1SL2i_4Y?t=3662)] Wow. What motivates you to solve these hard problems? I mean, what keeps you driven? Because you kind of sound like you gotta just bash your head against the wall, and maybe you get there, maybe you don't.

**Ryan Williams:**

[[01:01:20](https://youtu.be/AaK1SL2i_4Y?t=3680)] I try not to bash my head against the wall. And if I'm going to do it, it's gonna be a comfortable wall. It's gonna be one that's high-end and luxurious or something. I'm gonna enjoy the process, is what I mean. If I don't enjoy the process of really grinding and trying to understand something, I'm not going to do it. So I think, if anything, one thing that I like, I like to involve myself in working on problems where the grind is actually joyous and fun.

[[01:02:07](https://youtu.be/AaK1SL2i_4Y?t=3727)] Yeah. For the other things, they're just mainly opportunistic. They're mainly me just taking something new that I see and fully integrating it with everything I know and following everything to the logical conclusion and just seeing what happens. And not trying to get emotional, trying not to whatever, just trying to follow everything one step after another. Yeah.

### 01:02:35 — How to pick good research direction

**Ryan Peterman:**

[[01:02:35](https://youtu.be/AaK1SL2i_4Y?t=3755)] How do you pick a good research direction?

**Ryan Williams:**

[[01:02:37](https://youtu.be/AaK1SL2i_4Y?t=3757)] The best kind of research direction, which is very hard to come across, is a direction where you've set yourself up in a way that you can't lose. I have a hypothesis H, and one of two things is going to happen. Either I prove H is true, or I refute H, prove not H. What I would like to have is a situation where if H is true, then good things happen. If not H is true, good things still happen.

[[01:03:16](https://youtu.be/AaK1SL2i_4Y?t=3796)] Other good things. I like to look at things where H. Yeah, it's a win-win kind of. If you can find opportunities like this, this is important. I think often I'm not looking at a specific problem, I'm looking at a method. I'm looking at the technique. I'm looking at not the specific proof, but the space of ideas. And I'm trying to understand what else can be done in this space of ideas.

[[01:03:54](https://youtu.be/AaK1SL2i_4Y?t=3834)] So often I solve problems just by taking some idea and putting it somewhere else.

**Ryan Peterman:**

[[01:03:59](https://youtu.be/AaK1SL2i_4Y?t=3839)] Do you have a concrete example of where you've pursued something knowing that if you succeed, good. If you succeed in the other direction, also good.

**Ryan Williams:**

[[01:04:09](https://youtu.be/AaK1SL2i_4Y?t=3849)] I have some particular research program for which, if it materializes, would actually show that something called the orthogonal vectors problem can be solved in nearly linear time. Okay. Now, if that's true, then the SAT problem can be solved in about the same time as [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem). It could be solved in like square root of 2 to the N. So this would truly break SETH in a radical way.

[[01:04:43](https://youtu.be/AaK1SL2i_4Y?t=3883)] Okay. And I did a lot of work in the past showing how if you can improve on the running time of SAT, then you can somehow use that to prove circuit complexity lower bounds. You can take an algorithm for analyzing circuits that's nontrivial and interesting and turn that into a limitation on what those circuits can compute. Okay, so this hypothesis, maybe I won't exactly say what it is, it's a pretty technical statement, but the point is that if the hypothesis is true, then I get this fantastic algorithm for this orthogonal vectors problem.

[[01:05:34](https://youtu.be/AaK1SL2i_4Y?t=3934)] I get this algorithm for SAT, I get circuit complexity lower bounds. From that I get to somehow prove limitations on what circuits can do if the hypothesis is false. I can use that hypothesis to actually show another circuit complexity lower bound of a different flavor. So regardless of whether or not the hypothesis is true or false, I'm going to make progress in complexity theory. I'm going to prove a new limitation one way or the other.

[[01:06:04](https://youtu.be/AaK1SL2i_4Y?t=3964)] Right. So sometimes, I mean, this can be difficult to do, but usually what has happened instead of something so clean is that I have, I read about some idea or whatever, I try to apply the idea, I read about some magical algorithm, I try to apply the magical algorithm to solve something like SAT. It doesn't work, but I look at my approach, I stare really hard at it, I try to pivot, I try to just extract what I can, and then I get some other type of algorithm.

[[01:06:41](https://youtu.be/AaK1SL2i_4Y?t=4001)] I mean, this is essentially how I proved the circuit complexity lower bounds that first got me a job at [Stanford](https://en.wikipedia.org/wiki/Stanford_University) was I was trying to solve SAT faster with some algorithm. It didn't work, but then I realized that that algorithm worked for a large class of circuits, including ones we didn't know lower bounds for. So then I used that to prove a lower bound. Yeah. So I mean, this is just a general principle that I've had.

### 01:07:14 — Technical book recommendations

**Ryan Peterman:**

[[01:07:14](https://youtu.be/AaK1SL2i_4Y?t=4034)] What would be your book recommendation if someone wants to learn more about complexity theory?

**Ryan Williams:**

[[01:07:19](https://youtu.be/AaK1SL2i_4Y?t=4039)] Yeah, so it sort of depends on how deep you want to go. There's Avi's book. Yeah, Avi's book is really nice. If you're looking for something a little more gentle of an introduction, I would say you could read the early chapters of Lance Fortnow's The Golden Ticket, trying to imagine what a world would be like if P equaled NP. I like that imagination exercise that Lance did. On a more technical level, if you're looking for something slightly more technical, you could look at The Nature of Computation by Mertens and Moore, I think.

[[01:08:05](https://youtu.be/AaK1SL2i_4Y?t=4085)] So this is still not very technical, but it is a textbook, right? Yeah. And then, of course, Sipser's Introduction to the Theory of Computation is a fairly concise and very well-written textbook. Yeah.

### 01:08:31 — Advice for his younger self

**Ryan Peterman:**

[[01:08:31](https://youtu.be/AaK1SL2i_4Y?t=4111)] Last question for you is, if you could go back to the beginning of your career, knowing what you know now, what advice would you give yourself?

**Ryan Williams:**

[[01:08:38](https://youtu.be/AaK1SL2i_4Y?t=4118)] So I guess one thing that I did by accident, which I think people should keep in mind, is that you don't need permission to work on very tough problems. In fact, the tougher the problem, like in complexity theory, there are all these problems where nobody has a very good clue of what to do beyond a few simple structural results. So that kind of levels the playing field a bit.

[[01:09:15](https://youtu.be/AaK1SL2i_4Y?t=4155)] And yeah, you just, you don't need permission to think about these problems. You don't need anybody's say-so or whatever. I mean, that's one thing that I would like younger people to keep in mind, that this knowledge is open to the world and it's open to you. And you can just go learn it and think about it. And yeah, you don't need anybody's permission, especially not mine.

[[01:09:43](https://youtu.be/AaK1SL2i_4Y?t=4183)] Yeah. Another thing I think is to avoid inertia in the sense that if you don't think about and reflect, where am I going and what am I doing? You can just end up coasting in a certain direction. And I think it's important for people to sit down and truly reflect and think from time to time. Okay, if I keep going in this direction, is this going to lead to a place that I want to be?

[[01:10:27](https://youtu.be/AaK1SL2i_4Y?t=4227)] And this sort of advice is good for all aspects of life, really. If I keep just allowing things to be the way they are, am I going to be okay with that, or do I need to do something? Do I need to? So it's like little interrupts in your life and reflection, just sort of like, okay, do I need to be coasting here? I think in research for me, I was always reevaluating, like, okay, what did I do last year and what did I do the year before, and could, you know, like, what do I know now that I didn't know then?

[[01:11:11](https://youtu.be/AaK1SL2i_4Y?t=4271)] And, am I progressing? I think that sort of self-evaluation is crucial when you're in grad school because once you're in a PhD program, there are no more easy metrics to gauge how good or bad you are doing. And the truth is, there just isn't such a metric. So all you can really do is evaluate your past self with your present self and compare and contrast to see if you're making progress with whatever it is you want to do.

**Ryan Peterman:**

[[01:11:49](https://youtu.be/AaK1SL2i_4Y?t=4309)] Thank you so much for your time, Professor Williams. I really appreciate it.

**Ryan Williams:**

[[01:11:52](https://youtu.be/AaK1SL2i_4Y?t=4312)] Yeah, I appreciate you having me here. It's been fun. Thanks.

---

