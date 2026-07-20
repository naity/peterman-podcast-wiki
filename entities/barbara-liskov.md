---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [turing-award-winner-data-abstraction.md]
---

# Barbara Liskov

Turing Award winner and [MIT](mit.md) professor; inventor of data abstraction (CLU), the Liskov substitution principle, and Viewstamped Replication — "the beginning of cloud storage" ([episode](../sources/turing-award-winner-data-abstraction.md)).

## Career arc

Entered computing by accident: after a [UC Berkeley](uc-berkeley.md) math degree, Princeton rejected her grad application with a postcard reading "we do not admit women," and her best job offer happened to be as a programmer ([episode](../sources/turing-award-winner-data-abstraction.md)). Responding to the 1970s software crisis — companies burning millions on systems they threw away because languages offered only procedures as a modularity mechanism — she reframed modules as hidden state accessible only through operations. The resulting paper (with Steve Zilles) and the CLU language shaped Ada and, eventually, Java; she deliberately kept CLU a research artifact rather than productizing it at a company. Bob Kahn's vision of programs spanning networks pulled her into [distributed systems](../concepts/distributed-systems.md): her language Argus borrowed atomic transactions from [databases](../concepts/databases.md), leading directly to Viewstamped Replication (with student Brian Oki) and later PBFT (with Miguel Castro), which extended fault tolerance from crashes to Byzantine nodes. With no faculty offers after her PhD she spent four years at MITRE retooling from AI to systems — "I was ready" when Title IX opened academia to women — and stayed at MIT for the freedom ([episode](../sources/turing-award-winner-data-abstraction.md)).

## Key views & advice

- Viewstamped Replication and [Leslie Lamport](leslie-lamport.md)'s Paxos are essentially the same protocol invented independently; Paxos won mindshare because "I went around giving all the talks and she implemented it" (Lamport's own line) plus the catchier name. A former student even recognized [Google](google.md)'s GFS replication as Viewstamped Replication though Google believed it was Paxos ([episode](../sources/turing-award-winner-data-abstraction.md)).
- Python's flaw: modules without encapsulation — and encapsulation is the crucial part of making modularity work ([episode](../sources/turing-award-winner-data-abstraction.md)).
- The substitution principle came from her specification-first answer to a 1986 OOPSLA puzzle Smalltalk couldn't resolve: a subclass must behave like its superclass wherever the superclass is expected. She only learned it had her name via a random email in the 90s ([episode](../sources/turing-award-winner-data-abstraction.md)).
- Dijkstra's "Goto Considered Harmful" was a letter, not a paper; its real point was that reasoning about correctness is hard — "Dijkstra was not the most diplomatic person," but he won ([episode](../sources/turing-award-winner-data-abstraction.md)).
- Academia is "a gift and a curse": do whatever you want, but you must figure out what that is. Tells grad students to avoid incremental work — find a good, solvable problem matching your skills ([episode](../sources/turing-award-winner-data-abstraction.md)).
- On [non-linear careers](../concepts/non-linear-careers.md): careers are doors opening and closing; when internet commenters questioned her Turing Award she read it as a compliment — data abstraction is so fundamental people forget there was a "before" ([episode](../sources/turing-award-winner-data-abstraction.md)).

## Related

- [Episode: Turing Award Winner: Data Abstraction, Dijkstra, Distributed Systems](../sources/turing-award-winner-data-abstraction.md) — her interview
- [Leslie Lamport](leslie-lamport.md) — independently invented the same consensus idea (Paxos); shared Dijkstra experiences
- [Mike Stonebraker](mike-stonebraker.md) — fellow Turing laureate; she borrowed atomic transactions from his database field
- [Marc Brooker](marc-brooker.md) — modern industrial practice of the replication/consensus techniques she pioneered
- [working with legends](../concepts/working-with-legends.md), [programming languages](../concepts/programming-languages.md)
