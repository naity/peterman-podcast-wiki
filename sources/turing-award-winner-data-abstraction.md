---
type: source
updated: 2026-07-19
raw: ../raw/turing-award-winner-data-abstraction.md
guest: "Barbara Liskov"
guest_role: "Turing Award winner, MIT professor"
date: 2026-04-27
url: https://www.developing.dev/p/turing-award-winner-data-abstraction
---

# Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems | Barbara Liskov

Barbara Liskov is the Turing Award winner who invented data abstraction (via the CLU language), the Liskov substitution principle, and Viewstamped Replication — the consensus protocol equivalent to Paxos. In this episode she recounts being rejected from Princeton by postcard because "we do not admit women," how the 1970s software crisis led her to abstract data types, why [Python](../concepts/programming-languages.md) lacks the encapsulation that makes modularity work, [Dijkstra](../entities/edsger-dijkstra.md) stories, and why the internet questioned her Turing Award — which she reads as the ultimate compliment.

## Key takeaways

- Liskov got into computer science "by a happy accident": after her math degree at [UC Berkeley](../entities/uc-berkeley.md), Princeton returned her grad school application with a postcard reading "we do not admit women"; not ready for a math PhD, she took her best job offer — as a programmer.
- The 1970s software crisis: companies routinely spent millions of dollars and hundreds of person-years on systems they then threw away because they simply didn't work. The missing piece was real [modularity](../concepts/systems-design.md) — the only mechanism languages offered was the procedure, which can't model a file system or database ([programming-languages](../concepts/programming-languages.md)).
- Her breakthrough was seeing modules as data abstractions — hidden state accessible only through operations, the type could be a set or a sequence — turning vague "chunk of code" module talk into a designable concept; the 1974 paper with Steve Zilles sketched abstract data types, CLU embodied them, Ada was explicitly designed around them by government mandate, and Java carried them mainstream in the 90s. "There's sort of a time when an idea is ready and I happened to see it."
- What's wrong with Python: it has modules but no encapsulation — outside code can muck around with module internals, and "encapsulation is a crucial part of making modularity work."
- She entered [distributed systems](../concepts/distributed-systems.md) after reading Bob Kahn's dream of programs spanning networked computers; her language Argus (CLU-influenced, with "guardian" objects communicating by RPC) borrowed atomic transactions from the [database](../concepts/databases.md) field so distributed computations either complete entirely or have no effect.
- Viewstamped Replication (with PhD student Brian Oki) and [Leslie Lamport](../entities/leslie-lamport.md)'s Paxos are "essentially the same idea" developed independently — views are just incrementing numbers, no clocks involved. A former student consulting at [Google](../entities/google.md) recognized the Google File System's replication as Viewstamped Replication even though "the people at Google seem to think it was Paxos." Why Paxos got famous: per Lamport, "I went around giving all the talks and she implemented it" — plus the catchy name.
- The leader-failure step is the key advance both protocols share over transaction commit protocols; later, PBFT with her student Miguel Castro (prompted by a DARPA RFP) extended fault tolerance from crashes to Byzantine/malicious nodes.
- The Liskov substitution principle came from preparing a 1986 OOPSLA keynote: reading the Smalltalk papers, she saw the West Coast community describing subclasses by implementation deltas and unable to define "type hierarchy," while her MIT specification-first mindset (from the course with John Guttag) supplied the answer — a subclass must behave like its superclass wherever the superclass is expected. She only learned it had her name attached when a stranger emailed in the 90s asking for the correct interpretation.
- On Dijkstra: "Goto Statement Considered Harmful" was a letter, not a paper, and its deep point was that reasoning about code correctness is hard at a time when science dismissed CS as trivial; it was controversial because assembler required gotos, languages lacked structured constructs, compilers couldn't optimize, and skilled goto users were offended — "Dijkstra was not the most diplomatic person," but "clearly Dijkstra won the day" ([teaching-and-communication](../concepts/teaching-and-communication.md)).
- Why she stayed in academia: research freedom is "a gift and a curse — the gift is you can do whatever you want, the curse is you have to figure out what it is that you're doing"; she briefly worked at a startup in the late 90s and disliked it. Advice to grad students: don't do incremental work — find a good problem that's amenable to a solution and matches your skill set.
- On [career resilience](../concepts/non-linear-careers.md): with no good faculty offers post-PhD she returned to MITRE for four years, which let her switch from AI to systems without self-pity; then Title IX opened academia to women "and I was ready." Careers are doors opening and closing — "doors opened and then you have to decide, am I going to step through?"
- When online commenters asked why she deserved the Turing Award, she took it as "a huge compliment": data abstraction had become so fundamental that even her own grad students didn't realize there was a "before" — unlike a protocol you can point to, her contribution was the whole mindset of how programs are developed ([working-with-legends](../concepts/working-with-legends.md)).

## Notable quotes

- "I got this little card back. It was a postcard from Princeton saying, we do not admit women." — Barbara Liskov, ~1:00
- "So what Leslie says is, I went around giving all the talks and she implemented it." — Barbara Liskov, ~18:57
- "It's a gift and a curse. The gift is you can do whatever you want. The curse is you have to figure out what it is that you're doing." — Barbara Liskov, ~25:48
- "All that stuff was so fundamental that people thought there was no time when it hadn't already existed." — Barbara Liskov, ~32:13

## Connections

- [Turing Award Winner On Thinking Clearly, Paxos vs Raft, Working with Dijkstra | Leslie Lamport](turing-award-winner-on-working-with.md) — the other inventor of the same consensus idea (Paxos vs Viewstamped Replication) and shared Dijkstra stories.
- [Turing Award Winner: Postgres, Disagreeing with Google, Future Problems | Mike Stonebraker](turing-award-winner-postgres-disagreeing.md) — fellow Turing laureate; Liskov borrowed transactions from the database field Stonebraker built.
- [Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling](dropboxs-former-most-senior-eng-building.md) — Cowling did his MIT PhD in distributed systems in Liskov's group; industrial application of her replication lineage.
- [AWS Distinguished Eng: Learnings From 3000 Incidents And How Engineering Is Changing | Marc Brooker](aws-distinguished-eng-learnings-from.md) — modern cloud-scale practice of the replication/consensus techniques Liskov pioneered.
- [Turing Award Winner: TPUs vs GPUs vs CPUs, Computer Architecture, RISC vs CISC | David Patterson](turing-award-winner-tpu-vs-gpu-vs.md) — Berkeley-linked Turing laureate peer on foundational-abstraction contributions.
