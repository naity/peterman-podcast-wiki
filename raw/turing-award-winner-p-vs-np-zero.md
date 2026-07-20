---
type: raw-transcript
slug: turing-award-winner-p-vs-np-zero
title: "Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson"
guest: "Avi Wigderson"
date: 2026-06-01
url: https://www.developing.dev/p/turing-award-winner-p-vs-np-zero
fetched: 2026-07-19
complete: false   # transcript ends at 01:53:10; sections from 01:56:24 (Math vs computer science), 02:08:16 (Major breakthroughs), 02:12:31 (Advice for younger self) missing — source page truncated for fetch tool
---

# Episode Information

**Title:** Turing Award Winner: P vs NP, Zero-Knowledge Proofs, Quantum Computation | Avi Wigderson

**Guest:** Avi Wigderson

**Publish Date:** June 1, 2026

## Host's Introduction

Avi Wigderson is the only person in history to have won both a Turing Award (computer science) and Abel Prize (math). I interviewed him all about his field.

Check out the episode wherever you get your podcasts: YouTube, Spotify, Apple Podcasts.

## Timestamps

- 01:08 - P vs NP
- 14:51 - What if you relaxed correctness
- 25:38 - Why NP complete problems are equivalent
- 30:33 - Space vs time complexity
- 43:06 - Why people use SAT solvers
- 45:53 - Randomness is a resource
- 55:48 - Randomness depends on computational power
- 01:21:20 - Zero knowledge proofs and their significance
- 01:38:30 - Quantum computation and why it matters
- 01:56:24 - Math vs computer science
- 02:08:16 - Major breakthroughs and his experience
- 02:12:31 - Advice for his younger self

## Transcript

### 01:08 — P vs NP

**Avi:**

[[01:08](https://youtu.be/5GUcvSAJcJw?t=68)] Well, in the simplest way, and I will talk at a high level, we are interested in various problems in life, in all sorts of problems: mathematical problems, scientific problems, medical problems, personal problems, intellectual problems. We are in the business, in computer science, of solving problems by computers. Now we would like to somehow classify those problems that we can solve, to know what we can know.

[[01:43](https://youtu.be/5GUcvSAJcJw?t=103)] The problems we can solve are the things we will know, we will understand. There are all these problems that we want to understand. There are many of them, and there are problems that we can understand but can't solve. In a very basic way, the first class is NP. All the problems we want to solve are really NP problems. It's a class of problems, and a subset of it is the problems we can solve.

[[02:13](https://youtu.be/5GUcvSAJcJw?t=133)] They are the problems we can currently solve, but we are interested in all the problems we can solve in principle. The question of P versus NP is whether we can solve all the problems we want to solve, whether we can know everything we want to know. This is basically about the limits of our knowledge. Of course, I have to justify why these classes, which are mathematically defined, are actually captured by the intuitive meanings I'm giving them.

[[02:52](https://youtu.be/5GUcvSAJcJw?t=172)] P is very easy to justify. What we can solve is what we can solve in our lifetime using whatever we have, let's say all computers that we have using efficient algorithms. Problems we can solve are problems you see in our apps, in our phones. If there's a navigation app, it means somebody invented an algorithm that's efficient enough to solve any shortest path problem between any two places in any kind of map. All the problems we want to solve are NP problems.

[[03:32](https://youtu.be/5GUcvSAJcJw?t=212)] What is NP? NP is a class of problems in mathematical definition, problems such that we don't know whether they are easy or hard to solve. But if somebody hands us a solution, then we can easily check that indeed it is a good solution. Now, why are all problems humanity is interested in of this nature? You can think there's no limit to what we may want to know. But I claim that essentially, in any human endeavor, if you are embarking on any problem, if you really seriously want to solve a problem, the least you want to know is that when you hit upon a solution, you will recognize it as a solution.

[[04:19](https://youtu.be/5GUcvSAJcJw?t=259)] Why would you ever start looking for something if you will never recognize it as what you looked for? So you think mathematicians are looking for proofs of theorems? Certainly, if somebody gives a proof and writes a paper about it, we can verify it. If a scientist wants to explain data about the planets or about bacteria or whatever, they want to develop a theory. So that's what you are searching for in this case.

[[04:54](https://youtu.be/5GUcvSAJcJw?t=294)] And yeah, again, scientists write papers about their theories. They have to be consistent with the data. We have a way of recognizing that this is a good solution. Engineers are usually tasked with creating something, like a bridge or a phone, under some constraints. It can be monetary constraints, physical constraints, all sorts of limitations, such as what you can use but not this, and so on.

[[05:24](https://youtu.be/5GUcvSAJcJw?t=324)] But anyway, if an engineer designs something, whoever gave them the task can look at it and say, "Well, you violated some constraints," or "No, it's good, you really delivered what we were looking for." So I'm giving you examples. I mean, I can give many more. Detectives are supposed to solve crimes, and we know from detective books they eventually provide solutions. So these are examples of very fundamental human endeavors that encompass almost everything I can think of in all of them.

[[05:58](https://youtu.be/5GUcvSAJcJw?t=358)] What people are searching for has the property that when a solution is found, it is easily recognized. Repeating in the beginning, NP are all problems that we can honestly say we really want to solve. NP are those that we can solve. If they are equal, then everything we would want to know, a cure for cancer, anything you can imagine, can be just the very fact that a solution can be easily recognized, which would imply that it can be efficiently found.

[[06:38](https://youtu.be/5GUcvSAJcJw?t=398)] That means that we can know everything we ever want to know. It's a fundamental question about human knowledge.

**Ryan:**

[[06:44](https://youtu.be/5GUcvSAJcJw?t=404)] So I know this is one of those Millennium Prize problems. There's a million-dollar prize if you can provide a proof for this. I can imagine you could prove that they're equivalent. You could also prove that they're not. If you had to guess when and if a proof comes, which direction would your intuition say it goes? And why?

**Avi:**

[[07:07](https://youtu.be/5GUcvSAJcJw?t=427)] I think that my intuition, and that probably holds for almost all members of the theoretical computer science community, is that they are different. I think there are several reasons for that, and I will already tell you now that they are not that convincing. One is the intuition that most of us have that finding something is really hard and just checking that it's there.

[[07:37](https://youtu.be/5GUcvSAJcJw?t=457)] If you lost your keys or your phone and have no idea where to look, but if somebody points out, "Oh, you left it on the windowsill," you might say, "Ah, yeah, I did." We have this experience from life that finding something is typically a harder task than just checking that it is what we look for. Another reason is that real NP problems occur all over the place. They occur in optimization, in logic, in other aspects, in mathematics, and in verifying that algorithms, protocols, and security systems actually work.

[[08:22](https://youtu.be/5GUcvSAJcJw?t=502)] All sorts of. In this generality, these optimization problems that are NP problems, maybe NP-hard problems, people try to solve for completely egocentric reasons to make their company richer. There are thousands of these, and they manifest themselves in many different forms. Over the last 50, 60, or 70 years, people have seriously looked for algorithms for these very different ones and couldn't find any.

[[09:02](https://youtu.be/5GUcvSAJcJw?t=542)] This may seem like there's no such solution. Getting a bit more technical, NP problems, NP-complete problems in particular, seem to require search over an exponentially large space, like all the possible solutions to some system of equations. Somehow, a solution is about having a general method for cutting down this exponentially large search space into searching over something much smaller in a clever way.

[[09:48](https://youtu.be/5GUcvSAJcJw?t=588)] And this should apply to all these problems. So that would be equal. And people don't think that there is such a way. But as I said, these are intuitions that are maybe pretty strong. And I think that's the only, tomorrow somebody finds an efficient algorithm for NP-complete problems using some new idea that nobody ever thought of.

**Ryan:**

[[10:22](https://youtu.be/5GUcvSAJcJw?t=622)] That would change the world. In software engineering, we use algorithms all the time, and they often have these very satisfying properties where the solution we use takes something where the brute force is much larger down to something that's polynomial time or something very reasonable. But in all these NP problems, it's pretty unsatisfying that the best we could do is brute force.

[[10:55](https://youtu.be/5GUcvSAJcJw?t=655)] Am I understanding that correctly?

**Avi:**

[[10:57](https://youtu.be/5GUcvSAJcJw?t=657)] Yeah, you're understanding it perfectly correctly. I think that maybe what you are getting at is that NP-complete problems are, a particular NP-complete problem is really a family of instances. I mean, you want to find a Hamiltonian cycle, some Traveling Salesman Problem through some map. There's this map and that map and this network and other network. And there are many, many instances when we talk about an algorithm for them.

[[11:32](https://youtu.be/5GUcvSAJcJw?t=692)] Typically, we say an algorithm is efficient if it's efficient and correct on all of them. In software engineering and many aspects of optimization in real-world problems, the instances are a much more restricted set. They come from trying to verify a particular protocol or, I know, protein folding. If you want to think about the biological example, the way it is phrased as an NP problem is that you want to minimize the energy of a system under various constraints that have to relate to the chemistry of the various molecules and atoms that appear in the protein.

[[12:25](https://youtu.be/5GUcvSAJcJw?t=745)] And this kind of optimization problem one can easily prove is NP-hard. Nevertheless, our body folds proteins all the time, extremely efficiently. Now why is that? Of course, I don't really know why that is. But it would seem that evolution designed proteins in such a way that this, you know, folding them, only them, we don't have that many proteins. There are not exponentially many proteins in the body.

[[12:57](https://youtu.be/5GUcvSAJcJw?t=777)] There are only a few that may be more prone to efficient energy minimization. More generally, I think in software engineering, at least in verification and testing, you often want to check that something meets the specifications. You usually translate it into a satisfiability question of Boolean formulas. The formulas that you get, the instances that you get out of these have some structure, and maybe for them, various greedy approaches or clever methods can be applied.

[[13:38](https://youtu.be/5GUcvSAJcJw?t=818)] Not just greedy, but clever and efficient methods work. In other words, making it short. Instances that come up are not the worst-case instances. We have many examples of this that we can actually prove. For example, early on it was recognized that the Simplex method, which is an algorithm to solve linear programming problems, on the one hand, requires exponential time for the worst-case system of inequalities.

[[14:16](https://youtu.be/5GUcvSAJcJw?t=856)] But in practice, it seems to run in linear time. Evidently, the set of linear systems that we tackle in real life has some extra structure that allows this particular algorithm to solve them efficiently. Of course, today we know an algorithm that's efficient for all linear programs, but it's much more complicated, and I don't know how much it's used in practice. But the Simplex method is very simple to run, and usually, it works.

### 14:51 — What if you relaxed correctness

**Ryan:**

[[14:51](https://youtu.be/5GUcvSAJcJw?t=891)] You mentioned protein folding, and that's an interesting one because it's an NP problem, but it was solved to an acceptable extent. When I was reading about it, I found that it wasn't solved for 100% of cases. It provides a solution and a confidence score, but it doesn't give you the answer that is 100% accurate and fully computed. So when you think about these NP problems, what if you relaxed the criteria of being correct?

[[15:27](https://youtu.be/5GUcvSAJcJw?t=927)] Could the asymptotic complexity be less than the exponential that we're talking about?

**Avi:**

[[15:33](https://youtu.be/5GUcvSAJcJw?t=933)] Yeah, it's a very natural and good question. So in the protein folding, you are talking about AlphaFold, which is an algorithm or heuristic that was learned from existing proteins and works very well on instances it didn't see but are still proteins coming from the body. Even if it did perfectly on these, that would still be following the discussion I mentioned before because the instances it is trying to solve come from real life and probably have extra structure that allows efficient solutions.

[[16:13](https://youtu.be/5GUcvSAJcJw?t=973)] But you are right that one of the things that people naturally do when they cannot solve an optimization problem exactly because it's NP-complete or NP-hard. Maybe I should say NP-complete and NP-hard problems are those problems in NP that are as hard as all problems in NP. If you solved one efficiently, you solved all efficiently. If you prove one hard, then you prove all of them hard. So they somehow capture the complexity of the class.

[[16:46](https://youtu.be/5GUcvSAJcJw?t=1006)] The Traveling Salesman Problem is an example. Portraying folding in this framework of energy minimization is one, and Boolean satisfiability and so on. Okay, so you want to optimize something, and it's NP-complete or NP-hard. That's a sign that you shouldn't try to find an algorithm that works always. But one thing you can do is an approximation. That's a very natural relaxation. You don't want the optimum.

[[17:16](https://youtu.be/5GUcvSAJcJw?t=1036)] You are willing to live with a factor of 2 from optimum or 10% from optimum or some factor away from optimum. NP-completeness was discovered in the early 70s. In the early 90s, there was a breakthrough called the PCP theorem. The PCP theorem allows you to argue hardness of even approximation problems. For example, you can show that satisfiability of Boolean formulas—it's not just, so you want to, let's say, find an assignment to a bunch of constraints, let's say Boolean constraints, let's say on three variables, for simplicity.

[[18:06](https://youtu.be/5GUcvSAJcJw?t=1086)] So you want to satisfy all of them. The relaxation would be okay, I want to satisfy 90% of them, or as good a fraction as I can if I cannot get 100% of them. The PCP theorem, one way to phrase it, and suddenly one of the major consequences is that we know that you cannot even achieve a very good approximation. To illustrate how tight this understanding is for some problems, when there are only three variables per constraint, if you just guess at random the values to the variables in the assignment, you will satisfy 7 or 8 of the constraints.

[[18:55](https://youtu.be/5GUcvSAJcJw?t=1135)] This is because each particular constraint, usually the disjunction of three variables, will be true with probability seven-eighths. So if you randomly assign values to the variables without thinking or looking at the formula, you can satisfy seven-eighths of them. The PCP theorem, along with a significant strengthening by Johan Håstad, tells you that if you want to satisfy seven-eighths plus epsilon, that's already NP-hard.

[[19:30](https://youtu.be/5GUcvSAJcJw?t=1170)] So we know today to argue the difficulty not only of finding the perfect solution, the optimal solution, but even how close to optimal you can get for lots and lots of problems, large classes of problems, in particular constraint optimization problems, you know, of the type of satisfiability.

**Ryan:**

[[19:56](https://youtu.be/5GUcvSAJcJw?t=1196)] So even if you solve just the slightest epsilon for any trivially small epsilon, it's just as hard as doing.

**Avi:**

[[20:06](https://youtu.be/5GUcvSAJcJw?t=1206)] It's as hard as finding the optimum source.

**Ryan:**

[[20:09](https://youtu.be/5GUcvSAJcJw?t=1209)] You mentioned NP-hard, NP-complete, and P. I know there are other complexity classes. Maybe you could give some more context on the whole space of complexity classes.

**Avi:**

[[20:22](https://youtu.be/5GUcvSAJcJw?t=1222)] Yeah, so I'll just remark that we have a zoo of complexity classes. In fact, there's a website called the Complexity Zoo, which has in it hundreds and hundreds of complexity classes of all types. The website was started by Scott Aaronson. Once we realize that there's a whole zoo out there, we want to know the relationship between these classes. Okay, so what is the point about these classes like P and NP?

[[21:02](https://youtu.be/5GUcvSAJcJw?t=1262)] We want to classify problems by the amount of resources they take. So P (polynomial time) is a class of problems that can be solved in an amount of time that relates polynomially to the size of the data. Of course, you expect that as the data grows, the instance grows, and you'll spend more time. But if it's linear time, quadratic time, or cubic time, you say, let me call it at least theoretically efficient.

[[21:35](https://youtu.be/5GUcvSAJcJw?t=1295)] And NP, you classify not the time to solve, but the time to verify a solution if it was given. You want this to be polynomial time. So it's very different. But first of all, there are many more time functions than just polynomial, exponential, and doubly exponential. And you can go to finite, and one fundamental result, starting with Turing's paper, is that there are problems that are simply unsolvable by computers.

[[22:16](https://youtu.be/5GUcvSAJcJw?t=1336)] So really, the first complexity class is a class of solvable problems, decidable problems. Turing shows that these are not all problems. There are natural problems that are not decidable at all. But time is only one resource, and we are interested, both from practical and theoretical reasons, in lots of other resources. Memory is a costly resource, and we want to minimize the space invested in a computation.

[[22:47](https://youtu.be/5GUcvSAJcJw?t=1367)] In problems with several parties, you are interested in the amount of communication exchange, not the internal computational effort that they exert themselves, but how much. If you talk to a satellite, you want to minimize the communication. You can think about energy; there are plenty of other resources, like parallel time. How much can you speed up the computation of a problem if you work on it not with one computer, but with n computers?

[[23:21](https://youtu.be/5GUcvSAJcJw?t=1401)] If your data is of size, then does it allow it to solve it immediately? Or maybe it doesn't help at all? Complexity classes classify problems according to how much resources they need. There are many of these, and one important part of that is a major theme in the methodology of complexity theory. Coming with it are attempts to understand complexity classes as problems that relate to each other, even if you don't know their complexity.

[[24:02](https://youtu.be/5GUcvSAJcJw?t=1442)] So, for example, NP is a class, and we don't know the complexity of all problems in this or NP-complete problems. We don't know whether they are all easy or hard, but we do know we have efficient algorithms to translate one into the other. It's not obvious that if you want to solve a satisfiability problem, you don't know how. But you have an algorithm to solve Sudoku problems, not just three by three, but also four by four. If you had an efficient method to solve Sudoku problems, P equals NP, because you can efficiently take an instance of satisfiability, the Traveling Salesman Problem, or factoring integers, and from the solution of the Sudoku problem, you can translate back and get the best solution for your original Traveling Salesman Problem.

[[25:04](https://youtu.be/5GUcvSAJcJw?t=1504)] So we are interested in efficient reductions between problems whose complexity we don't know, but we want to relate them to each other. We build some kind of partial order of the hardness of different problems. There are really, you don't want to know how many problems we have summarized for constraints that real-world technology may impose or cause for. Some are naturally arising mathematically because they are interesting.

### 25:38 — Why NP complete problems are equivalent

**Ryan:**

[[25:38](https://youtu.be/5GUcvSAJcJw?t=1538)] You mentioned that these NP-complete problems are all equivalent in some way. What's the proof to equate a SAT solving problem to a graph coloring problem or something like that? Are they all similar in nature? Are they kind of bespoke to the problem you're going to and from?

**Avi:**

[[25:59](https://youtu.be/5GUcvSAJcJw?t=1559)] That's a very good question. You will find that in most of these, they call them reduction algorithms to translate one problem to another. Most of them are relatively simple, but not all. I talked about the PCP theorem before, showing that approximation is hardest is very highly non-trivial. But most NP-complete problems prove equivalence, like between graph coloring and satisfiability. This goes both ways; they are both complete.

[[26:32](https://youtu.be/5GUcvSAJcJw?t=1592)] So it goes both ways. It is simple. The first one was the satisfiability problem. The original papers of Steve Cook and Leonid Levin, defining NP-completeness and proving that NP-complete problems exist, both focused on this. The first problem they proved complete was satisfiability. Why is this so? Why can all these other problems be reduced to satisfiability? The reason is really that computation is local. Computation is local.

[[27:10](https://youtu.be/5GUcvSAJcJw?t=1630)] I mean that if you think about your computer, your laptop, or any computational device, usually it manipulates bits by some local operations. You look at these two registers and you add them, or you take these two bits and exclusive OR them or AND them or something, and you do a sequence of simple operations and you arrive at a conclusion. This locality can be translated to a bunch of constraints or what would be a consistent sequence of states of your machine.

[[27:48](https://youtu.be/5GUcvSAJcJw?t=1668)] If you look at the time evolution of any computation, memories in some states and in another state change locally. If you could guess, and that's the NP part, if somebody provided you the table of computation, you could check that it's consistent by writing a bunch of local constraints or some conjunction of very few variables all over this table of computation and write down a satisfiability problem.

[[28:25](https://youtu.be/5GUcvSAJcJw?t=1705)] I want this to be true, this to be true, and this to be true for some assignment. What the assignment has to satisfy should be a table like this. All these constraints should be satisfied, should be true, and it has to be consistent with the input given, right? Some of the inputs have to match the first time zero content of the machine. This locality allows for many of these translations.

[[28:56](https://youtu.be/5GUcvSAJcJw?t=1736)] If you realize this, you will quickly find a reduction from coloring to satisfiability. It's also not clear why coloring is an evolution of computation, but it starts already with local constraints. You want a few colors and that every constraint is satisfied. In some cases, it's even easier. But the reduction from any NP computation—that's what NP-complete means. Anything in NP can be translated to satisfiability.

[[29:29](https://youtu.be/5GUcvSAJcJw?t=1769)] NP is just a computation of a Turing machine, say only that you don't know what the computation is. If somebody guessed it or showed it to you, then all you need is to verify this verification is local. And that's the source of many simple NP-completeness reductions. Let me give you a really simple example. Why is factoring integers reducible to satisfiability? Because if I gave you factors of an integer, you could just multiply them and check that they equal the input.

[[30:15](https://youtu.be/5GUcvSAJcJw?t=1815)] This multiplication is a simple algorithm, right? I mean, we know how to do it from second grade or something.

### 30:33 — Space vs time complexity

**Ryan:**

[[30:33](https://youtu.be/5GUcvSAJcJw?t=1833)] You really, the factors you mentioned, time complexity and space complexity. Intuitively, in software engineering, we often trade those off for each other. Is there general theory on that, on how these two trade off?

**Avi:**

[[30:50](https://youtu.be/5GUcvSAJcJw?t=1850)] Yeah, we have all these questions. They are natural questions for complexity theorists. How do two resources relate to each other, and can they trade off? Or maybe you can minimize them both at the same time. It depends on the problem. There are problems for which we know results, like multiplying time and space. It has to be at least the square of the length of the input. So you can either do it with very small space, like logarithmic space, but you need to pay maybe quadratic time.

[[31:32](https://youtu.be/5GUcvSAJcJw?t=1892)] And if you want linear time, you have to pay linear space or close to linear space. There are results of this type in various models of computation. That's another thing you play with. Not all of them are equivalent in principle, but if you care about exact time or exact space, they are not equivalent. So there are problems for which there is a trade-off. There are problems where you can solve them in linear time and logarithmic space.

[[32:05](https://youtu.be/5GUcvSAJcJw?t=1925)] One very important general result that is the breakthrough from last year is a result of Ryan Williams. I'll tell you what it is, but first, I need to describe what we knew about time and space. There's a clear inequality, right? If you run in time T, you will never use more than space T, because you will never visit so many cells or registers in your machine. So space is at most time. Fifty years ago, Valiant, Paul, and Pipin improved this a little bit.

[[32:41](https://youtu.be/5GUcvSAJcJw?t=1961)] They said that if you run in time T, there's an equivalent computation that will do this in slightly less space than T over log T. That was a big result. The running time, of course, will blow up. It will be very, very expensive time-wise, but at least you can save on space a little bit. This was believed for almost 50 years to be the best you can do. In fact, we had arguments that in certain models, in stylized models, models of computation, you cannot improve that.

[[33:19](https://youtu.be/5GUcvSAJcJw?t=1999)] I will not describe this restricted model, but in some way, natural restricted models, you cannot beat this. What Ryan Williams found out last year is that, in fact, much better can be done. Any computation that runs in time T can be simulated by another algorithm that uses only the square root of T space, far less than before. The algorithm is quite sophisticated and uses an earlier result of James Cook, the son of Steve Cook, known for defining NP-completeness, and Ian Meltz, which was an essential technical ingredient.

[[34:07](https://youtu.be/5GUcvSAJcJw?t=2047)] But anyway, there's a really interesting way to save space. A very non-trivial way to save space. Again, this algorithm will run in a lot of time, but at least you have a sense that the two parameters are related in a highly non-trivial way.

**Ryan:**

[[34:29](https://youtu.be/5GUcvSAJcJw?t=2069)] Is this for a general problem?

**Avi:**

[[34:31](https://youtu.be/5GUcvSAJcJw?t=2071)] General problem for Turing machines? Okay, it may not work on random access machines or.

**Ryan:**

[[34:37](https://youtu.be/5GUcvSAJcJw?t=2077)] Yeah, what's the trick? If you could explain intuitively, or is it too deep to explain?

**Avi:**

[[34:45](https://youtu.be/5GUcvSAJcJw?t=2085)] It is really technically explaining it. It's too deep. But I'll give you a much earlier result which indicates that really mysterious things can be done in small space. Again, it's probably over 40 years ago, people discovered the following. Dave Barrington discovered the following really interesting phenomenon. So suppose all you want is to count. I give you a sequence of bits, and you want to count.

[[35:20](https://youtu.be/5GUcvSAJcJw?t=2120)] Say you want to know whether there are more zeros than ones, like the majority problem. Who wants the vote, zeros or ones? Okay, well, you can count. You can just add them up, and this takes logarithmic space; it seems the best you can do. You want to count up to N. To represent N takes log N bits, right? Any number between 1 and N takes log N bits. It seems essential. It turns out that there's an algorithm I have to define exactly how it works.

[[35:58](https://youtu.be/5GUcvSAJcJw?t=2158)] I will not define exactly how it works, but it solves this problem. In constant space, it seems like you can count arbitrarily high. All you need is access to whatever bit you like, whenever you like. I want the 17th one, I want the 81st one. If you can have random access to the bits, even if you have constant space, you can tell whether there are more zeros than ones or ones and zeros, regardless of how long the input is.

[[36:33](https://youtu.be/5GUcvSAJcJw?t=2193)] The trick is that somehow you use noncommutative algebra. Noncommutative algebra is not something everybody's familiar with. I mean, we usually put the cars behind the horse and not in front of the horse. It matters. In software engineering, we do this before that; it's very important that the order of things matters. So you can think about applying permutations one after the other.

[[37:10](https://youtu.be/5GUcvSAJcJw?t=2230)] If I rotate a circle and then take a mirror image, it will give me the... So these are two permutations, right? I mean, say I have endpoints in a circle. I can shift it by one, or I can, let's say, flip it around some diameter. There are two permutations, and they don't commute. If I first flip and then rotate, I'll get something else than if I first rotate. Think of all the points as colored, so they don't commute.

[[37:45](https://youtu.be/5GUcvSAJcJw?t=2265)] Barrington is using permutations to encode the bits in the input, specifically permutations of size five. When he sees a one, he may rotate, and when he sees a zero, he flips. The non-commutativity of these operations allows him to carry out a general formula, a formula of ANDs, ORs, and NOTs. Any formula of some size S enables him to simulate the ANDs, ORs, and NOTs in this formula through rotations and flips of these five-sided pentagons.

[[38:45](https://youtu.be/5GUcvSAJcJw?t=2325)] And so just to remember the configuration of this pentagon, you need five bits, right? So you need constant space. How this captures the computation, I can tell you one more sentence. Maybe it will not be clear to everybody, but these non-commuting things allow you to do the following type of operation: do a rotation, do a flip, then rotate back and flip back. This is called the commutator, and it can simulate an AND gate.

[[39:33](https://youtu.be/5GUcvSAJcJw?t=2373)] I can. It's too much to describe in words without how it does it. But there's a very famous analogy, which is a riddle that captures this NP-complete problem. You want to hang a painting in the following way: you have a painting, it has a string connecting the two sides, but you want to hang it not on one nail, but on two nails.

[[40:08](https://youtu.be/5GUcvSAJcJw?t=2408)] Okay. There are two nails on the wall, and you can do with the string whatever you want. The property you want is that if the two nails are there, it's hanging, and everybody's happy. If you pull out one nail, it doesn't matter which, the picture falls to the floor. How would you loop the string around these nails so that this happens? Clearly, this is an AND gate or an OR gate. Right? If one... Yeah. And this has to do.

[[40:43](https://youtu.be/5GUcvSAJcJw?t=2443)] I mean, if anybody finds a solution, they realize what non-commutativity I'm talking about. It's a nice fiddle. Anyway, this type of trick, where you can really do this type of result in small space, is something you wouldn't imagine possible. It's a striking example. When I heard this result for the first time, I was a postdoc, and somebody told me, and I just didn't believe it was possible.

[[41:18](https://youtu.be/5GUcvSAJcJw?t=2478)] You cannot count arbitrarily high with. The trick that Cook and Mertz have in their algorithm is a solution to a natural problem in much less space than you would think. It uses some sense tricks of this nature.

**Ryan:**

[[41:44](https://youtu.be/5GUcvSAJcJw?t=2504)] If you're counting arbitrarily large, that is information. You're saying maybe the intuition is that information is encoded in the sequence of operations.

**Avi:**

[[41:55](https://youtu.be/5GUcvSAJcJw?t=2515)] It is encoded. Of course, you are not delivering the final count. You just say whether there are more zeros than ones. If you have to write it down, and if the answer takes some number of bits, then you need this number to write it down. If you have a decision problem, say like yes or no, like are there more zeros than ones? Then you can do it for any size input in constant space.

**Ryan:**

[[42:26](https://youtu.be/5GUcvSAJcJw?t=2546)] That's incredible.

**Avi:**

[[42:28](https://youtu.be/5GUcvSAJcJw?t=2548)] Pretty incredible, yeah. And by the way, this highly applicable result used in cryptography in fundamental ways is used in various places, and it's an extremely useful result here. Unlike the Ryan Williams result, if you have a formula of size S, you can do it in constant space. The time of this algorithm does not blow up really a lot; it's just quadratic. So it's quadratic time.

[[43:00](https://youtu.be/5GUcvSAJcJw?t=2580)] So this is something actually doable, useful, efficient, and magical.

### 43:06 — Why people use SAT solvers

**Ryan:**

[[43:06](https://youtu.be/5GUcvSAJcJw?t=2586)] We talked about the equivalence between these NP-complete problems. In practice, a lot of people solve other problems using SAT solvers. I would have thought that would be less efficient, though, because you have to translate it and then you're doing it in almost like a different problem space.

**Avi:**

[[43:25](https://youtu.be/5GUcvSAJcJw?t=2605)] Yeah, you usually also enlarge the instance. In translation, you enlarge the instance. So what your question is, why do people use SAT solvers? I would say that there's no problem other than satisfiability that people thought so hard about really optimizing the heuristics that efficiently work on many instances. There are very clever ways in which you can try to start. I mean, you are not going to guess all the N bits, but you want to start by guessing some bits that seem more pivotal. If you like in dominoes, maybe when you set them to one value, they force many other values to be set.

[[44:22](https://youtu.be/5GUcvSAJcJw?t=2662)] And if that happens, you cut down your subspace. There are many heuristics of this type and also more clever than this that allow solving such satisfiability problems if they have such structure. Again, in the worst case, it will not help you. There is, in fact, a conjecture that is much stronger somehow than NP-completeness, you know, NP-complete problems taking exponential time. It says that we don't expect any savings.

[[44:56](https://youtu.be/5GUcvSAJcJw?t=2696)] We expect satisfiability problems to require really true to some constant times N. It's not going to be two to the square or N to the log N or something like this. The worst case may be hard, but people optimize attacks on many such formulas that somehow have all sorts of structural properties arising maybe in practice. I think that's the main reason they are used. It's also convenient.

[[45:33](https://youtu.be/5GUcvSAJcJw?t=2733)] I mean, it's very common. People do it for testing specifications that programs or protocols meet. The specifications are usually easily translated into simple constraints, and that's almost a satisfiability problem.

### 45:53 — Randomness is a resource

**Ryan:**

[[45:53](https://youtu.be/5GUcvSAJcJw?t=2753)] We talked about all the different types of resources in an algorithm, and in one of your talks, you said something where you consider randomness another resource for an algorithm. What do you mean when you say randomness is a resource for an algorithm?

**Avi:**

[[46:10](https://youtu.be/5GUcvSAJcJw?t=2770)] In the early 70s, of course, randomized algorithms existed since antiquity, and everybody was tossing coins for a lot of reasons. Statisticians do sampling and use randomness. But when algorithmics, designing efficient algorithms, became big—once we had computers—people realized that it can really enhance all sorts of computation. For example, we had no idea how to test the primality of a number.

[[46:46](https://youtu.be/5GUcvSAJcJw?t=2806)] And in the 70s, both Michael Rabin and Sulwin Slauson found probabilistic algorithms, which are fast to test primality. Okay, so what does it mean, a probabilistic algorithm? It's an algorithm that's allowed to make random choices. You can think that there is an internal little person or device inside that tosses coins. Of course, that's not what happens. There's no little person sitting in your laptop.

[[47:15](https://youtu.be/5GUcvSAJcJw?t=2835)] So the question is, where do you get these random bits? It's very important to stress that in all these probabilistic algorithms, the underlying assumption is that the bits you get are perfect. They are half, half each one and independent of each other. It's like a uniform distribution on all possibilities. Now, where do you get this? I mean, where seriously do you get this? If you run a public algorithm on your laptop, since it doesn't have this person inside tossing coins, it does something well.

[[47:52](https://youtu.be/5GUcvSAJcJw?t=2872)] High-quality randomness of this type costs money, time, and memory. What do I mean by "cost money"? You can have a very cheap solution. You can just measure the thermal noise in your computer or use one of the Intel chips. You can measure Internet traffic and sample it, believing it's random, and all of these things are used. You can do something mathematical, have some simple procedure that is actually deterministic, like a linear congruence generator or something like this, and believe it's random.

[[48:32](https://youtu.be/5GUcvSAJcJw?t=2912)] Or you can take the digits of π. It also looks random in some sense. There are many things you can use, but you don't know they are random. If you want them to be random, one source— even this is not a perfect source— but we have quantum mechanics. People believe it works in life. It seems like a true theory of nature. There are all sorts of arguments about it, but let's put them aside.

[[49:01](https://youtu.be/5GUcvSAJcJw?t=2941)] They predict. If you measure photons coming out from some source and you measure their spin, whether it's up or down, the prediction is that each one is half, half, and it's independent of each other. That's very nice. But if you are going to build this device, it's going to cost you a lot of money, and let alone that it will not be perfect. But let's leave this aside. Anyway, since you want high-quality randomness, you have some way of guaranteeing, I mean, you are running it really on your laptop.

[[49:34](https://youtu.be/5GUcvSAJcJw?t=2974)] It's not okay. The paper was written; we can test primality with a probabilistic algorithm. Now we want to run it. What do you use? It makes sense to ask lots of questions about randomness. What guarantees the quality of the randomness? Maybe you can minimize the use of randomness. By the way, another issue with randomness is that the outcome is a random variable, and it's not always correct. Right?

[[50:02](https://youtu.be/5GUcvSAJcJw?t=3002)] The whole point, in most of these algorithms, is that you just have some small probability of error. If you have a deterministic algorithm, there's no error, so you also don't like the error. Treating it as a resource is simply a convenient, complex theoretic way of saying how do we understand the amount of this resource we have to invest, or the number of bits we have to invest, their quality, and so on.

[[50:30](https://youtu.be/5GUcvSAJcJw?t=3030)] So it's almost automatic. If you think like a complexity theorist, how do we minimize for a particular algorithm, like primarily testing? Do you really need this? Do you need them to be independent? Maybe you can generate them in a, you know, maybe you need n bits, but you can start from squared n bits or from log N bits that are truly random and make from them in some deterministic way, a sort of pseudo-random sequence you can call it, which is a good name actually, that will, for the purpose of this algorithm, look as if it was random.

[[51:13](https://youtu.be/5GUcvSAJcJw?t=3073)] If you could do that, you don't need all these bits; you can use much fewer. This whole theory of reducing randomness, derandomization, and removing randomness is a huge field, and there are many problems and many ways of doing it. The story with primality is actually fascinating. I mentioned these two algorithms that were invented, and people were wondering about the deterministic algorithm for primality.

[[51:45](https://youtu.be/5GUcvSAJcJw?t=3105)] It's a problem that has been articulated already by Gauss in the most complex theoretic way you can. Back in his days, hundreds of years ago, and maybe 150, I don't know, he was asking for an indefatigable calculator. Calculator, of course, is a person. But he wanted this to be efficient. That's basically what he was looking for, a primality test for large numbers. Because they really wanted to know about numbers, maybe only a few tens of digits.

[[52:23](https://youtu.be/5GUcvSAJcJw?t=3143)] They wanted to know whether the numbers are prime or not. There was no efficient algorithm. You can wonder about the Miller-Rabin or Solovay-Strassen algorithms; maybe you can use less randomness or structures, randomness that you can generate from fewer bits, but nobody has any good idea. Then, in the early 2000s, Agarwal, Kayal, and Saxena devised a different probabilistic primality test, and it's different.

[[52:55](https://youtu.be/5GUcvSAJcJw?t=3175)] So the analysis of randomness in it is different. Once you understand how randomness is used, you can say, "Ah, we don't need to have totally independent bits. It's okay if it has some structure." They found, using number-theoretic methods, a tool to generate pseudo-randomness from very few bits. That's how it works. Sometimes, deterministic versions of probabilistic algorithms are discovered simply by understanding how the algorithm uses randomness, analyzing the algorithm, and realizing it doesn't use all that much.

**Ryan:**

[[53:49](https://youtu.be/5GUcvSAJcJw?t=3229)] You mentioned a few times the quality of the randomness. How do you quantify the quality of random bits?

**Avi:**

[[53:56](https://youtu.be/5GUcvSAJcJw?t=3236)] This is basically a question about what pseudorandomness is. The general answer is that it depends. You want to fool a particular algorithm, let's say, for primality. You want the randomness to fool this algorithm; you want it not to notice that you switched from perfect randomness to something that's really far less random, has far less entropy, but the analysis works nonetheless. For another algorithm, maybe you need a completely different type of pseudorandomness for it.

[[54:35](https://youtu.be/5GUcvSAJcJw?t=3275)] There are a set of examples of algorithmic problems for which, when you look at the analysis, they are much simpler than this primality testing. It seems to use not the independence of all the n bits. You really need only every pair of them to be independent, or every triple. Spaces of random variables that have this property are much smaller. You can generate them from log N bits, and so you can fool them with this.

[[55:08](https://youtu.be/5GUcvSAJcJw?t=3308)] So the quality of randomness is a phrase. I like that. The quality of randomness is in the eye of the beholder or in the computational power of the beholder. You really need it to be just as good as the tests that are applied to it. You just want to be completely pragmatic. You don't care whether it's random or not. You just care that an observer of a particular structure or particular computational power will not distinguish the pseudo-random distribution, which may have much less randomness in it than the perfect one.

### 55:48 — Randomness depends on computational power

**Ryan:**

[[55:48](https://youtu.be/5GUcvSAJw?t=3348)] In one of your lectures, actually, you mentioned that, and you gave a good example. I was wondering if you could give the intuitive example of why randomness is a function of the observer's computational power.

**Avi:**

[[56:00](https://youtu.be/5GUcvSAJcJw?t=3360)] Yeah. So if you watch this talk, the example I give is taken from this fundamental paper of Manuel Blum and Silvio Micali. They tell you to consider three experiments, and the experiments go as follows. They are always between you and me. You are the observer, I am the cause. I have a coin on my finger, and I toss it. Just as it leaves my finger, you are supposed to predict what the value will be when it falls on the floor, like in two seconds.

[[56:38](https://youtu.be/5GUcvSAJcJw?t=3398)] You have to immediately say, heads or tails, okay? Before you have to predict, before it falls. Well, this is the first experiment. And you know what I ask and what they ask? What do you think is a success, your success? What are your chances of predicting it? And the obvious answer is, you know, one half. You know what, how can it help? You know, what can you do? The second is when you sit there, but you have a laptop like you have now.

[[57:10](https://youtu.be/5GUcvSAJcJw?t=3430)] And, yeah, what can you do? I don't know how fast you type, but the coin will be on the floor in a second. The third experiment is where your laptop is connected to a Cray supercomputer, and the Cray supercomputer is connected to a bunch of sensors and cameras and whatever devices you want. They are all trained on my finger, okay? And so as it leaves my finger, the coin. This apparatus certainly is more than enough to calculate all the angular momentum of the coin and the distance to the floor and the humidity in the air and whatever parameter that completely determines its motion.

[[57:57](https://youtu.be/5GUcvSAJcJw?t=3477)] In particular, how it will land in a split second, far less than the time needed. So the real point in this example is that the experiment, the random coin toss, did not change in all of them. It is the same what masses of people in math, physics, and philosophy have defined randomness in various ways. There are many definitions of randomness, and they all focus on this event, on the chronos or sequence of coin tosses.

[[58:37](https://youtu.be/5GUcvSAJcJw?t=3517)] We in computational complexity theory, starting from this paper, don't care about this event. The event stays the same, and all it focuses on is the observer. The only thing that changed in these three experiments is the computational power. We want to know how much entropy is in the coin. If you don't have enough computational power, it seems to be full entropy. It's half. Half. You don't know what it will be; if you have enough computational power, you can predict it completely, and then it has zero entropy.

[[59:12](https://youtu.be/5GUcvSAJcJw?t=3552)] So what changed is the observer. The observer is this algorithm we talked about before. Any test that's applied to a distribution to test the quality of randomness, depending on the test, you want to make sure to use as little true randomness in a way that the observer will not notice. This is the source of many of the important theorems that show you can remove randomness or reduce randomness in probabilistic algorithms with or without assumptions.

[[59:55](https://youtu.be/5GUcvSAJcJw?t=3595)] And really, they are behind this understanding that we have today. Randomness in algorithms is not as powerful as we thought. It's like if you know that P is different from NP or you have a Traveling Salesman Problem that is exponentially hard or sustainable. If you know that, then in fact, I can give you a pseudorandom generator that will derandomize any. We know that under this assumption, we have what we call P equals BPP.

[[01:00:28](https://youtu.be/5GUcvSAJcJw?t=3628)] Anything that has an efficient probabilistic algorithm also has an efficient deterministic algorithm. You just need to know that there is a hard function somewhere. Under what assumptions do we know P equals BPP? The very natural assumption is that one of these NP-complete problems, or in fact even problems in higher classes, requires a lot of hardware and requires exponential size circuits to solve. We believe that it's like the P versus NP problem in strength, and you cannot count down the exponential subspace.

[[01:01:14](https://youtu.be/5GUcvSAJcJw?t=3674)] And so maybe people are happier with this assumption, but this assumption about time complexity has no randomness in it. At first, it's shocking that it's actually related to the problem of removing randomness from algorithms. So that's one fundamental connection in this hardness versus randomness paradigm. But we know even more. We know that it goes both ways. We know that if you are trying to remove randomness from some algorithms, if you can do that, then you've found the hard function.

[[01:02:02](https://youtu.be/5GUcvSAJcJw?t=3722)] So there's really an almost. It's not an exact if and only if, but again, there are many variants of this. In some variants, if and only if it's stronger, but we really know that it's one or the other. Since it's hard to believe that all these hard problems are easy, or the seemingly hard problem like P versus NP, we tend much more to believe the other alternative, which is that randomness in algorithms is weak and you can remove it.

**Ryan:**

[[01:03:20](https://youtu.be/5GUcvSAJcJw?t=3783)] Is there an intuitive explanation for the relationship between problem hardness and randomness?

**Avi:**

[[01:03:25](https://youtu.be/5GUcvSAJcJw?t=3805)] Yeah, there's almost always an intuitive explanation for this. So what's the hard problem? I give you the input. You are a limited computer. You are a polynomial time algorithm. I give you the input. Let's say it's a Traveling Salesman Problem, or you don't know the answer. So there's some entropy in the answer, right? In the same sense we discussed before, there's some entropy, a tiny entropy, maybe exponentially small entropy, because if the input is random, maybe only a few instances are hard, and all the others you can solve. But at least you see a hint of a relationship between hardness and entropy.

[[01:04:12](https://youtu.be/5GUcvSAJcJw?t=3852)] This, of course, is not satisfactory because we want half. We want the answer to be like a coin toss, not like a very biased coin toss. So we need to find ways to amplify this uncertainty for you. Amplify the hardness. We want not just that some instances will be hard, but since they are random instances, whether the answer is yes or no, for polynomial time, the observer will be half and half.

[[01:04:46](https://youtu.be/5GUcvSAJcJw?t=3886)] It will not be able to gain an epsilon advantage over a random guess. For this, we developed all sorts of methods that amplify randomness. Now, this doesn't solve the problem at all because I managed to take n bits of a random instance of a problem and manufacture one bit. That's hard for you to guess. But I could have taken the first random bit I picked.

[[01:05:20](https://youtu.be/5GUcvSAJcJw?t=3920)] What you want to do is the opposite. You want a method that will take a few and generate many. That's a pseudorandom generator. The pseudorandom generator starts with a few truly random bits and generates many. For this, we need other tools. There's something that I developed with Noam Nisan called the NW generator. I like to say that people say making the first million dollars is easy, and afterwards, you can make many more millions.

[[01:05:57](https://youtu.be/5GUcvSAJcJw?t=3957)] You can think of it this way. The hardness in the way I describe it allows you to make $1 million. But once you can make one, there are methods to make many more, in fact, more than the number of bits you started with. But still, their quality depends on the hardness of the function you use. We still use this and your limitation of being in polynomial time. So you can also solve this hard instance.

[[01:06:30](https://youtu.be/5GUcvSAJcJw?t=3990)] You build many instances from a short seed. You start from maybe a logarithmically long seed. You take many subsets of this, like N. You will need n of them. I ask you for the value of the solution to each one. Each one is hard, but we want to say that they are simultaneously hard. You cannot tell them apart. There is no correlation that you can detect between them, even though they are extremely correlated.

[[01:07:00](https://youtu.be/5GUcvSAJcJw?t=3920)] So, we have methods to do that as well. The connection you embed, having a hard problem to a limited observer, means there's some uncertainty about the answer. That's the key. That's a starting point.

**Ryan:**

[[01:07:14](https://youtu.be/5GUcvSAJcJw?t=4034)] So when you say that the quality of the randomness is a function of the computational power of the observer, one thought that comes to mind is, imagine I have maybe infinite compute. Then nothing is truly random. Is that accurate to say? Like, you know, if I had infinite compute, the weather is not random. Nothing is random.

**Avi:**

[[01:07:42](https://youtu.be/5GUcvSAJcJw?t=4062)] Okay. So it points to the fact that you have to really be careful about what question you are asking about randomness. If you want to apply this to probabilistic algorithms, then it's really important that you are limited computationally. If you have infinite compute time, you will be able to distinguish a distribution with full entropy from one coming from a generator with low entropy.

[[01:08:19](https://youtu.be/5GUcvSAJcJw?t=4099)] So you could do that. But one thing you cannot do with infinite compute is something that's information theoretic. There are many other things we need to do with random bits than just run probabilistic algorithms. For example, we want to generate passwords for our cryptography for security systems. The very demand is that they are random, right? I mean, Shannon's theorem tells you the quality of your password is as good as the entropy in it.

[[01:08:58](https://youtu.be/5GUcvSAJcJw?t=4138)] So the notion of a secret rests on the true randomness of the bits. If I ask you to produce a random bit, or you ask me to produce a random bit, whether you have infinite computational power or not doesn't matter. To generate this random bit, it has to be random. Your demand is not that it will succeed in some test; you really want the probability of heads to be half and tails to be half.

[[01:09:34](https://youtu.be/5GUcvSAJcJw?t=4174)] Then this definition or this task of producing randomness is not related to your computational power. Lucky or unlucky, I don't know. For us, many times we do have implicit or explicit tests for this randomness. You say, "I can break this system or something." Then you can maybe use pseudorandomness. But if your very demand is to have a random event, then you need to produce a random event.

**Ryan:**

[[01:10:08](https://youtu.be/5GUcvSAJcJw?t=4208)] I saw in my research that there are ways to create higher quality randomness by aggregating weaker sources. How does that work?

**Avi:**

[[01:10:22](https://youtu.be/5GUcvSAJcJw?t=4222)] Well, it's another theory I talked about before, the theory of pseudorandomness. There's a whole different theory. They are related in nontrivial ways, but it's called the theory of randomness extraction or randomness purification, maybe. And this is exactly what you asked about. We imagine that the world may not give us perfect randomness, but we have all these events we cannot predict, like the weather, various quantum phenomena, or sunspots. We cannot predict the stock prices, right? Otherwise, the market will be.

[[01:11:04](https://youtu.be/5GUcvSAJcJw?t=3530)] But these are not, even though these are unpredictable events, they are somewhat predictable. I mean, the weather tomorrow is more likely to be similar to the weather today than the opposite. So there are correlations. If you sample this weather, for example, there are also biases. I mean, sometimes in the spring it's more, or in the summer it's more likely to be hot than cold.

[[01:11:33](https://youtu.be/5GUcvSAJcJw?t=4293)] So there are biases and correlations. These are called weak random sources, and there's a mathematical quantification of how weak they are. Basically, we talk about the amount of entropy in them. You have N bits; potentially, you can have entropy N, but maybe they were generated from a generator or they came from some source. It has some entropy in it, but you have no idea where. Maybe half of them are fixed and half of them are chaotic, and you don't know which half.

[[01:12:10](https://youtu.be/5GUcvSAJcJw?t=4330)] Maybe they are each half, three-quarters zero and one-quarter heads or tails, have a virus that also has lots of entropy, but not full. The correlations may be even more complicated. You can imagine all sorts of situations like this, and you mathematically model it by saying, okay, there are N bits. It's a probability distribution of N bits which has some entropy, let's say the square root of N.

[[01:12:39](https://youtu.be/5GUcvSAJcJw?t=4359)] You don't know where, and you want to use it in a probabilistic algorithm. So it's a basic question: can we use physical events, weak sources coming from nature, maybe in probabilistic algorithms? It's certainly not obvious. I mean, just feeding them to the algorithm as is is not going to work. There are very simple algorithms that will succeed on perfect randomness and will fail, making an error.

[[01:13:14](https://youtu.be/5GUcvSAJcJw?t=4394)] But the theory of randomness purification wants to take this sample of n bits with some amount of entropy, which is not full, and massage it to create from it maybe a shorter string that is of higher quality. Ideally, it would be perfect random bits. So, ideally, you can imagine that if I have n random bits and I have entropy root N, maybe I can massage out of there square root N, or maybe just the fourth root of n bits that will be essentially uniformly distributed.

[[01:13:59](https://youtu.be/5GUcvSAJcJw?t=4439)] Then if I have an algorithm that just needs this amount, that's what I feel. Turns out you cannot do that; it's impossible. But what you can do is not produce one string of length, let's say, the square root of N, but you can produce N to the hundred of them, okay? And what you are guaranteed is that this randomness purification device is an official algorithm that takes any distribution with entropy in it and produces many blocks, polynomially many blocks, of the length roughly the entropy.

[[01:14:41](https://youtu.be/5GUcvSAJcJw?t=4481)] What you would hope to be perfect and what you are guaranteed is that 99% of them are truly perfect. So you have many, 99% of them are as good as perfect. And there's 1% that is bad. You don't know which it is. But this already solves your problem because you can run your algorithm on each one of them and take a majority vote. Doing this is extremely complicated. There are many ways of doing it. There are variants of various assumptions you can make about the entropy.

[[01:15:21](https://youtu.be/5GUcvSAJcJw?t=4521)] Maybe you have several weak sources that are not related to each other. There are various variants, and this theory is very well developed. But we know that the statement I made essentially is accurate. If you have one source with some entropy in it, you can generate polynomially many samples of the length of almost the entropy, and most of them will be perfect. So that's as useful as having one.

**Ryan:**

[[01:15:55](https://youtu.be/5GUcvSAJcJw?t=4555)] Yeah, I vaguely remember skimming a bunch of papers, and one of the papers had this figure with a two-dimensional array of numbers. I think they were drawing rectangles or something like that. Is that one of the ideas?

**Avi:**

[[01:16:11](https://youtu.be/5GUcvSAJcJw?t=4571)] So it's a notion of pseudorandomness, which is related to one particular variant of this extraction problem where you have several weak sources, not just one. One is the hardest because that's... Yeah, but maybe you have a few that are independent, and each of them has some entropy in it. I think what you are referring to is this sum product theorem. I cannot draw the pictures of that, but you don't really need to.

[[01:16:45](https://youtu.be/5GUcvSAJcJw?t=4605)] So let's just think about this problem. You have three sources of randomness; they are each weak, so each has just a little bit of entropy in it. All you want to produce is one source with somewhat larger entropy. You are losing the number of sources, but you are gaining entropy. If you can repeat this, you eventually get to full entropy. So that's the idea. What combination of which sources would you take?

[[01:17:17](https://youtu.be/5GUcvSAJcJw?t=4637)] It's not obvious. And the solution? Yeah, there certainly is one. Maybe you mean this one. There's a paper I have with Barack and Impagliazzo about this particular problem, and we are using a result in what's called arithmetic combinatorics. I can explain it very simply. I think that we learn about addition in second grade and about multiplication in third grade, maybe. The only motivation for multiplication is that it's a way to shortcut repeated addition.

[[01:17:56](https://youtu.be/5GUcvSAJcJw?t=4676)] And that's all we talk about. Then if you go to college, you learn that sums and products are the basic operations of fields. You can do it with integers, rational numbers, complex numbers, and finite fields. And so you remember these are the basic operations. But how do they relate to each other? It's not clear. Maybe there are many ways to ask this question. But one way to ask this question that was suggested by Erdős and was solved for the first time by Erdős and Semerédi, and then in a much more applicable form we really need by Bourgain and Katzentau, said the following.

[[01:18:38](https://youtu.be/5GUcvSAJcJw?t=4718)] Just think of a set of integers and add all pairs. So you start with, let's say, K integers and add all pairs. How many new integers do you get? This you should think of as entropy increase. If you get many more somehow. So you have K integers. Well, it depends on what they are. I mean, if they are the first K integers and you add all pairs up, you get the numbers between 1 and 2K. That's not much larger; that's a factor of 2 larger.

[[01:19:11](https://youtu.be/5GUcvSAJcJw?t=4751)] If you want to increase entropy, you want to get some power of K bigger than one. Of course, if you take a random set of integers, you'll get K squared. They'll all be distinct because K squared integers. So somehow you want to say, it would be great if, for any set, when you take all pairs, you group. But it's not true. By this example of the interval, you cannot take sums; you can take products, but also products don't always increase.

[[01:19:48](https://youtu.be/5GUcvSAJcJw?t=4788)] If you take 1, 2, 4, 8, you take a geometric progression, you multiply all pairs, you just get twice as many as you started with. So that's also not good. The magic in this sum-product theorem is that sums and products are orthogonal to each other. Somehow, if one of them fails to grow a set, then the other will grow this set. This is an amazing result. In this context, you think of the outcome of your sources as numbers.

[[01:20:31](https://youtu.be/5GUcvSAJcJw?t=4831)] You multiply the first pair and add them to the third. You mix the sum and product. This guarantees growth. This is not obvious, but if you do this, it guarantees that you grow. The number of different values you get is significantly more than K. Maybe it's K to the 1.5 or something. Entropy does increase, and that's the source. You need to prove it. Distributionally, it's not just the size.

[[01:21:03](https://youtu.be/5GUcvSAJcJw?t=4863)] The entropy is not just size; it's more than that. Anyway, this is behind one solution to one of the problems about purification. It does not solve the one source problem. For this, you need other tools.

### 01:21:20 — Zero knowledge proofs and their significance

**Ryan:**

[[01:21:20](https://youtu.be/5GUcvSAJcJw?t=4880)] I saw that you had done some work in zero-knowledge proofs. I was wondering if you could explain what a zero-knowledge proof is. Maybe we can talk about its significance.

**Avi:**

[[01:21:30](https://youtu.be/5GUcvSAJcJw?t=4890)] Sure, zero-knowledge proof. It's pretty amazing that it became a household word. I mean, it was in the domain of theorists for a long time. The original definition of zero-knowledge proof came in a seminar paper by Goldwasser, Micali, and Rakoff, which also contains the definition of interactive proof. So even before zero-knowledge, they conceived of the notion that proofs don't have to be written down like in mathematical papers.

[[01:22:06](https://youtu.be/5GUcvSAJcJw?t=4926)] People can have a discussion, a randomized discussion, in which I try to convince you of something I want to prove to you. Something like, I know the proof of the Riemann Hypothesis, or I can solve this Sudoku puzzle, and we can do it interactively with the random. We are randomized. In particular, you, the verifier of my claim, are allowed to be randomized. So it's like in randomized algorithms. But now there's a prover.

[[01:22:37](https://youtu.be/5GUcvSAJcJw?t=4957)] It's not just an algorithm; it's a prover, like in NP. Someone who knows the solution. But the convincing has this interactive form. This model was suggested in this paper and also in a paper of Babai, parallel at the same time from different motivations. Basically, it offers a generalization of the notion of NP. NP is just when I send you a message, and it convinces you; you verify it and it convinces you.

[[01:23:09](https://youtu.be/5GUcvSAJcJw?t=4989)] Now, we allow an interaction and we allow a small chance because you are randomized. We allow a small chance that I will convince you of a false claim. But this error can be reduced, like in probabilistic algorithms. You want one in a billion? You can get one in a billion, whatever. Anyway, so there's a notion of an interactive proof. In the Goldwasser-Micali-Rothblum paper, they suggested another notion of interactive proof, which is more restricted.

[[01:23:46](https://youtu.be/5GUcvSAJcJw?t=5026)] You want to prove something, but the zero-knowledge proof means that you want the verifier to learn nothing, absolutely nothing about the proof except that it's true. Now, this sounds really totally ridiculous. I mean, if you think about the last time you convinced somebody to change their mind about anything without providing them any knowledge, any new things they didn't know, say, what are you talking about?

[[01:24:17](https://youtu.be/5GUcvSAJcJw?t=5057)] Such proofs don't exist for anything. There's no zero-knowledge proof for anything. They were not thinking about convincing someone of a political opinion; they were thinking about cryptography. Of course, they've created the foundation of cryptography in many other papers, but they are imagining cryptographic protocols in which you have secrets. You use these secrets in your computation, and the protocol tells you to do things that, if you don't, then you're violating the protocol.

[[01:25:00](https://youtu.be/5GUcvSAJcJw?t=5100)] So the others don't want you to cheat. They want to make sure you perform the right operations on your secrets. For example, you are supposed to pick a public key by multiplying two prime numbers. If you multiply three or something else, then you are violating the protocol, and maybe security is not guaranteed. So I would like to convince you that the number I give you is actually a product of two primes.

[[01:25:30](https://youtu.be/5GUcvSAJcJw?t=5130)] I certainly don't want to give you the two primes. What I really want to convince you of is that I computed this number by multiplying two primes. You learn from this interaction absolutely nothing except that you are convinced with very high probability that I did multiply two primes and not any other number, and I didn't do anything else that I shouldn't. You can think about lots of other cryptographic protocols where people are doing things like multiparty computation, very complex things.

[[01:26:06](https://youtu.be/5GUcvSAJcJw?t=5166)] They are confused with their secrets and don't want to reveal them, whereas the others want to make sure that they did what they should. There are many applications for this idea. The only problem is that it sounds ridiculous because it seems impossible in mathematical terms. If someone came here and said that they proved P versus NP, I would want to see the proof and then tell me, okay, I'll prove it to you in zero-knowledge proof.

[[01:26:40](https://youtu.be/5GUcvSAJcJw?t=5200)] How can anybody convince me that they have a proof of P versus NP? I come out congratulating them and amazed by them, and nevertheless, I know absolutely nothing about the way they proved it. I just know that they did this. So it really sounds ridiculous. And yeah, certainly one of my favorite papers, maybe my favorite, is the zero-knowledge proof paper, which came a year later, co-authored with Omer Goldreich and Silvio Micali.

[[01:27:17](https://youtu.be/5GUcvSAJcJw?t=5237)] Well, we showed that it's not only not ridiculous, it's universal. Namely, anything that has a mathematical proof also has a zero-knowledge interactive proof. Anything like P versus NP or that I multiply two primes, or anything that you can prove revealing your secret, you can prove without revealing your secret and be convinced beyond any reasonable doubt. So that's possible.

**Ryan:**

[[01:27:46](https://youtu.be/5GUcvSAJcJw?t=5266)] What's the intuition behind that? Let's say I have a proof for P versus NP, and we want to convert it to a zero-knowledge proof. How does that work?

**Avi:**

[[01:27:55](https://youtu.be/5GUcvSAJcJw?t=5275)] How does this work? Well, first of all, it assumes cryptography. We assume we have some one-way functions. We assume that some problem, like factoring integers or discrete logarithms, or any number of one-way functions believed to be one-way, exists. One-way functions, if people don't know, are functions that are easy to compute in one direction but hard to invert. For example, multiplying numbers is easy. Finding the factors of a number, which is the inverse problem, is believed to be hard.

[[01:28:32](https://youtu.be/5GUcvSAJcJw?t=5312)] Of course, we can never know any hard problems. That's the pre-first entry question. We don't know, but we believe many problems are hard, and this belief is actually shared by the whole world because the entire world is using cryptographic systems that rest on this assumption. All electronic commerce assumes this. So, we assume we have one-way functions. One-way functions allow you to create basically garbled message commitments.

[[01:29:06](https://youtu.be/5GUcvSAJcJw?t=5346)] I have a number in my head. I don't want to tell you what the number is. It's a number between 1 and 100. I can write down another number that looks like a random number to you. On the one hand, you have no idea. I claim this encodes my secret, okay? This commitment scheme, which is built very simply for one-way functions, guarantees two properties. A) You cannot tell what my secret is, even though you can see this other number I gave you.

[[01:29:48](https://youtu.be/5GUcvSAJcJw?t=5388)] And on the other hand, I cannot change my mind about my secret. It really commits me to it. So I can later provide you with a certificate that I was thinking about 17, and I can only do it for 17. I cannot do it for any other number. In fact, a very simple example is really using factoring in some sense the product of two primes. This number commits to its factors.

[[01:30:27](https://youtu.be/5GUcvSAJcJw?t=5427)] It uniquely defines its factors, right? The only problem is this is not exactly random products of primes. Yeah, but you can do it, so you can do this. Okay? So now that we have to take commitments, that are possible, that's very important. I'm describing very high level; I'm hiding lots of things. Even the definition of zero-knowledge proof, the formal definition, is quite intricate. The intuition is obvious, and I said it.

[[01:30:58](https://youtu.be/5GUcvSAJcJw?t=5458)] But actually, formally defining it is non-trivial. At a high level, I'll give you some idea about how a zero-knowledge proof looks. Now we have to think about what theorems I am proving to you. It was very important for us to figure out what problem to think about. Even though today you can do it for others, we were thinking about theorems of the type where, in the graph, we can color it in three colors.

[[01:31:27](https://youtu.be/5GUcvSAJcJw?t=5487)] It's also a formal mathematical statement; either it's doable or not, right? We simply focus on proving zero-knowledge claims of this type. The graph we both know, I claim I can color it with three colors. You don't believe me. You want to be convinced of this fact, and you don't want me to cheat you. You don't want me to be able to provide an interactive proof. Moreover, I want it to be zero-knowledge.

[[01:31:58](https://youtu.be/5GUcvSAJcJw?t=5518)] I don't want you to have the slightest idea of what my coloring is or what anything you didn't know before is. Okay, so roughly the way it works. The honor is proof for this particular set of claims that are certainly not all claims. They are very structured claims. We look like the following. We iteratively repeat the following procedure. I put commitments for the coloring on every vertex. I tell you, you know, I don't tell you it's green, red, or blue, but I put a commitment to one of them.

[[01:32:38](https://youtu.be/5GUcvSAJcJw?t=5558)] On each vertex, you will choose at random an edge of the graph and ask me to open these two envelopes to decommit. You will check that the colors you see are in this set. They are not gray or orange; they are either red, green, or blue, and they are different. This should give you some slight advantage or support to the belief that maybe I'm not cheating you.

[[01:33:13](https://youtu.be/5GUcvSAJcJw?t=5593)] Of course, it's a very limited one because I can cheat you in some corner. We have to establish two things. We will repeat this again and again. We have to establish that it's a proof, an interactive proof that I cannot cheat you. And we have to argue that zero-knowledge part. Okay, so let's do one at a time. The correctness that I cannot fool you is very simple, is the following.

[[01:33:49](https://youtu.be/5GUcvSAJcJw?t=5629)] If the graph is not three-colorable, whatever I commit for there is one place which is an arrow. Either it has the wrong color and not allowed color, or two colors are equal. You have some non-trivial chance of catching this with your random guess. It's one over the number of edges. It's not so small. It's a graph with a hundred edges. It's one in a hundred if thousands.

[[01:34:16](https://youtu.be/5GUcvSAJcJw?t=5656)] If we repeat it, not a thousand, but 10,000 times, the probability that you don't catch me in any of them drops exponentially to zero. So, of course, this establishes that I cannot fool you. The zero-knowledge proof is a more serious problem because if I keep using the same coloring, you will ask me about this edge and this edge, and then eventually you'll know the coloring of all colors.

[[01:34:50](https://youtu.be/5GUcvSAJcJw?t=5690)] Here's something that's really special to the coloring that is being used. If I have one coloring of the graph, I really have six because I can permute the names; I can replace red and green, and it's another valid coloring. So what I do in each one of these iterations is not use the same coloring, but use a random one of these possible six. They are all legal, and I just use one of these six.

[[01:35:21](https://youtu.be/5GUcvSAJcJw?t=5721)] What's the advantage of this? When you open a pair of vertices under this distribution, one of the six, what you will see, if I do have a coloring—and that's the only thing I want to stress—is that we only have to establish zero-knowledge proof if I really can prove the theorem. So if I do know the solution, the proof, I want to protect my knowledge. What happens when I reveal to you two of these colors on the adjacent vertices of the graph?

[[01:35:52](https://youtu.be/5GUcvSAJcJw?t=5752)] It will be true in this distribution. When you are given two vertices, it will simply be two different random colors. This is what you get by all permutations in this experimentation. What did you learn from this? Nothing. You could have picked two random different colors. You didn't need me for that. So you didn't learn anything. In each iteration, you learn nothing. This is the idea of the proof.

[[01:36:20](https://youtu.be/5GUcvSAJcJw?t=5780)] Well, this is the end of the proof that I can show there are zero-knowledge proofs for all graph coloring, three-coloring problems. What about all the Riemann Hypotheses and the P versus NP problem and factoring and all these other things? I want to claim to you and prove with zero-knowledge. Here it's very simple. You use NP-completeness. This is an NP-complete problem. Anything that can be proved is really something in NP, right?

[[01:36:52](https://youtu.be/5GUcvSAJcJw?t=5812)] This is the definition. So you reduce it to three-coloring, proving it in zero-knowledge. The main point about reductions in NP is that they don't only convert the yes/no answer in a consistent way—if this is solvable, then this is solvable. But actually, if you have a witness, if you have a proof for, I don't know, whatever, it will become a legal three-coloring of the graph you generate. So if you have a proof, you can also have the three-coloring.

[[01:37:26](https://youtu.be/5GUcvSAJcJw?t=5846)] It's very important that the reduction also provides translation not just between the instances, but also between the proofs. NP-completeness theory gives you for free that if you solve the problem for Hamiltonian cycle instances, you solve it for any. You can prove anything in zero-knowledge proof.

**Ryan:**

[[01:37:47](https://youtu.be/5GUcvSAJcJw?t=5867)] So with the zero-knowledge proofs, you can never be 100%.

**Avi:**

[[01:37:52](https://youtu.be/5GUcvSAJcJw?t=5872)] No.

**Ryan:**

[[01:37:53](https://youtu.be/5GUcvSAJcJw?t=5873)] Okay, but practically, I mean exponentially approaching.

**Avi:**

[[01:37:58](https://youtu.be/5GUcvSAJcJw?t=5878)] You can make the completeness 100%. Namely, if I do have a proof, you will be. Yeah, there'll be no error in your proof. But there is a slight possibility that the graph is not three-colorable, and you will not catch me. You can make this exponentially small. You cannot make it zero.

**Ryan:**

[[01:38:18](https://youtu.be/5GUcvSAJcJw?t=5898)] When I think of cryptography and one-way functions, there's this idea of quantum computing that's kind of changed complexity theory.

**Avi:**

[[01:38:27](https://youtu.be/5GUcvSAJcJw?t=5907)] bit and big time.

### 01:38:30 — Quantum computation and why it matters

**Ryan:**

[[01:38:30](https://youtu.be/5GUcvSAJcJw?t=5910)] And I wanted to ask your thoughts on how quantum computing, or that model of computation, is changing complexity theory. What are the big takeaways?

**Avi:**

[[01:38:42](https://youtu.be/5GUcvSAJcJw?t=5922)] Okay, let me say what it is. First of all, quantum mechanics is a theory of nature that seems to be universally accepted. So, like with randomness, we can ask, why not enhance computers with this physical knowledge? We allow our computers to operate in the ways that quantum mechanics dictates, namely, manipulate bits in superposition using unitary operations, whatever this means.

[[01:39:16](https://youtu.be/5GUcvSAJcJw?t=5956)] But according to the rules of quantum mechanics, really strange things happen. I'm sure many people know about the interference patterns. Basically, you are working with probability theory. With negative numbers, events cannot aggregate; they can only cancel each other. Okay, so it's a model of computation.

[[01:39:51](https://youtu.be/5GUcvSAJcJw?t=5991)] It's a generalization of Turing machines. In fact, it's a generalization of randomized Turing machines. It's very easy to see that a quantum computer is at least as strong as a probabilistic computer. How do you see it? You just measure the quantum bit before you start. You measure them. This is what I mentioned about the photons in the beginning. If you have some basic superposition on a quantum bit, if you measure it, you get a random bit.

[[01:40:23](https://youtu.be/5GUcvSAJcJw?t=6023)] So because of that, quantum computers are at least as strong as probabilistic computers. Okay, so it's a model of computation. It was suggested in the 1980s. Richard Feynman, along with others, suggested letting algorithms use these quantum mechanical operations, mainly originally for simulating quantum systems rather than building bigger parallel systems, like we simulate other things, such as turbulence. I don't know what the power of quantum algorithms is, again, let's say running into polynomial time or efficient ones.

[[01:41:08](https://youtu.be/5GUcvSAJcJw?t=6068)] Can they do more than efficient classical ones, deterministic or probabilistic? It wasn't clear for a while. There were a few examples that were very stylized but were not for concrete natural problems we care about. Then in 1994, Peter Shor sort of created an earthquake or avalanche. He found quantum algorithms that are efficient, that factor integers and also compute discrete logarithms, the two most basic underpinnings of all security systems that exist.

[[01:41:48](https://youtu.be/5GUcvSAJcJw?t=6108)] And this sets the world on fire. Right. So lots of people try to do a lot of things. Of course, people want to have these algorithms they implement; maybe they want to break other people's cryptosystems. Since then, billions were invested by companies, by governments, by lots of people trying to build the technological infrastructure. This is extremely complicated. Holding bits in superposition is extremely complicated.

[[01:42:25](https://youtu.be/5GUcvSAJcJw?t=6145)] These things are called noise. When people built classical computers like von Neumann, noise was one of the serious problems because the bits were really in vacuum tubes, and they had to contend with it. In fact, it built a nice theory of classical computers that have errors. They have to cope with errors; some of their components can be faulty. But today's hardware has no errors to speak of.

[[01:43:02](https://youtu.be/5GUcvSAJcJw?t=6182)] We don't, there are error-correcting mechanisms, but we don't need them for classical computing. Intel chips don't have error correction in them. Hardware is very reliable. When you move to quantum, there is this decoherence noise in quantum mechanics. Everything depends on everything. The world can influence the computation in your laptop, and protecting from this is very hard.

[[01:43:33](https://youtu.be/5GUcvSAJcJw?t=6213)] There are quantum error correcting codes, and that's part of the solution. That's only one of the problems. Just holding bits in superposition is hard, and there are many hard technological issues, and there's progress on that. So this is one line of huge investment. The other line comes from cryptography because, of course, everybody should be worried. Forget quantum computers.

[[01:43:59](https://youtu.be/5GUcvSAJcJw?t=6239)] If tomorrow, I mean really tomorrow, somebody finds even a classical factorization algorithm in polynomial time, I think there'll be chaos in the world because nobody can do any transactions since most security systems still rely on factoring. Of course, we want to change this. We want to change the underlying assumptions of security. The whole revolution in cryptography was that we risk cryptography on computationally hard assumptions.

[[01:44:38](https://youtu.be/5GUcvSAJcJw?t=6278)] And with this, we build all the wonderful public key systems and all the magical things you can do by assuming that players are computationally limited. But now, if the adversary is a quantum computer, suddenly they can break this assumption. You want to find other mathematical problems, computational problems that are somehow hard even for quantum computers. So that's a whole field, this change in complexity theory and cryptography.

[[01:45:19](https://youtu.be/5GUcvSAJcJw?t=6319)] There is an army of people who are just trying to invent problems. I maybe should stress one-way functions are easy to find. Most problems, most processes in nature are not easily reversible. You make an omelet from an egg. Reversing this doesn't take the same amount of time; that's the usual example of a physical one-way function. But trapdoor functions, like factoring problems, are what you can use to build public key systems.

[[01:45:55](https://youtu.be/5GUcvSAJcJw?t=6355)] And that's the most really basic thing for electronic commerce. We don't know many. So we know this. I mentioned factoring and discrete logarithm. In the 90s, Itay and Roark created another type of trapdoor function from problems on lattices in high dimensions. I will not describe it, but it's another problem. Then people refined and got a few more of similar nature. It turned out when Peter Shor discovered this, people immediately tried to solve other problems with quantum computers.

[[01:46:31](https://youtu.be/5GUcvSAJcJw?t=6391)] In fact, even today we cannot solve too many other problems with quantum computers. These are special. The special thing about them is that somehow you can reduce them to finding periods in a signal. Periods are like fluorescence form. A Fourier transform turns out to be in exponential space. But you can somehow perform a Fourier transform with quantum computers using interference with lattice problems and problems related to it.

[[01:47:02](https://youtu.be/5GUcvSAJcJw?t=6422)] Some call it learning with errors. Similar to this, to this day, nobody has found an efficient quantum algorithm for them. So there's not even a theory. Forget building quantum computers; we don't know how to solve them. The world is not just complexity theory. The whole physical world of security systems and also governments like the NSA is supporting or asking the world to produce assumptions that may be resilient to quantum attacks.

[[01:47:44](https://youtu.be/5GUcvSAJcJw?t=6464)] And so this is a huge change. There is a major change in the interaction between computer scientists and physicists, which grew tremendously since its discovery. It's rich in many ways that are not the influence of algorithmic thinking on physical theories, including today's theories in quantum gravity, black holes, and so on. The impact is immense. We have new sources of problems, new models, and new complexity classes, et cetera, et cetera.

[[01:48:19](https://youtu.be/5GUcvSAJcJw?t=6499)] And there's a fantastic interaction. It's also enormous complexity theory in that it turns out you can discover quantum algorithms and maybe then dequantize them in special cases. Like I mentioned factoring before, de-randomizing. Sometimes it's a way, it's a road to discover new algorithms. There are connections between problems. It's extremely rich. But one of the most amazing consequences is that we, being what we are, make up models and study them.

[[01:49:05](https://youtu.be/5GUcvSAJcJw?t=6545)] And the interactive proofs I mentioned before, it turns out that even before quantum, they were generalized to interactive proofs not with one prover, but with many provers, which seems weird but turns out to be very important in itself because it led to this PCP theorem. Then people said, okay, let's allow quantum verifiers, quantum provers, and see what they can do. So one amazing result, which is about five years ago, is the acronym MIP* = RE.

[[01:49:40](https://youtu.be/5GUcvSAJcJw?t=6580)] Of course, we have acronyms for all these complexity classes: MIP*, RE. You may have seen them, maybe you didn't, and they look weird, but I'll tell you what they say. It says that there is a really weird proof system with quantum provers trying to convince efficient verifiers. And it turns out, you know, you ask for which problems can they do it? Forget their own knowledge, just convince.

[[01:50:12](https://youtu.be/5GUcvSAJcJw?t=6612)] And it turns out they can do it for the halting problem, for problems that are not computable. But things that are not computable are verifiable by efficient verifiers if the provers are quantum and they are entangled. It's a weird proof system, very weird, but it does something that looks totally ridiculous. Things that are uncomputable by any classifiable component are verifiable in this interactive probabilistic sense by efficient verifiers.

[[01:50:51](https://youtu.be/5GUcvSAJcJw?t=6651)] So what I like to say in talking about this is that it seems the best hypothetical reaction of anybody who hears this is, "Okay, you complexity theorists, you play in your sandbox and you build all these sandcastles and make up all these models that have nothing to do with anything just because you can." Once you get weird enough, you get weird enough consequences.

[[01:51:20](https://youtu.be/5GUcvSAJcJw?t=6680)] So one message which I think is very powerful is that this result has absolutely fundamental impact on mathematics and physics. It turns out that it implies, and this was already done in the initial paper, resolution of well-known conjectures in mathematics and physics. It turns out that, weird as it is, it's a new mathematical technique to solve problems that nobody had any idea about. Famous problems, important problems that fields were dedicated to, are resolved by this result, by the techniques of this result.

[[01:52:05](https://youtu.be/5GUcvSAJcJw?t=6725)] So you ask about the impact of quantum computing. The impact spans many generations with different motivations and developments, but all of them following the methodology of complexity theory, understanding the power of computational models, proof systems, and so on, has magically led to such a consequence. We are just at the beginning of this, right? This type of proof technique is now being explored and used, and there are more results using this type of technique to address long-standing problems.

[[01:52:44](https://youtu.be/5GUcvSAJcJw?t=6764)] Pretty amazing.

**Ryan:**

[[01:52:45](https://youtu.be/5GUcvSAJcJw?t=6765)] That's incredible. Yeah, I mean, in complexity theory there are these Venn diagrams of all possible problems. The implicit assumption in this picture is that these are decidable problems.

**Avi:**

[[01:53:02](https://youtu.be/5GUcvSAJcJw?t=6782)] Yeah, yeah.

**Ryan:**

[[01:53:03](https://youtu.be/5GUcvSAJcJw?t=6783)] In some of these diagrams, there's a little in the corner. Undecidable.

**Avi:**

[[01:53:09](https://youtu.be/5GUcvSAJcJw?t=6789)] Yes, unreachable.

**Ryan:**

[[01:53:10](https://youtu.be/5GUcvSAJcJw?t=6790)] Yeah, right. And it's just, I


[TRANSCRIPT GAP: content after 01:53:10 unavailable — the page content available to the fetch tool was truncated at this point. Missing sections: 01:56:24 Math vs computer science; 02:08:16 Major breakthroughs and his experience; 02:12:31 Advice for his younger self.]
