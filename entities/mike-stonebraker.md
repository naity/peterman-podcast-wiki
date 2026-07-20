---
type: entity
entity_kind: person
updated: 2026-07-19
sources: [turing-award-winner-postgres-disagreeing.md]
---

# Mike Stonebraker

Turing Award winner, creator of Ingres and Postgres, [UC Berkeley](uc-berkeley.md) and [MIT](mit.md) professor, and serial founder (most recently DBOS) ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).

## Career arc

Started building Ingres at Berkeley in 1972 — one year after Ted Codd's relational paper — knowing nothing about [databases](../concepts/databases.md); it earned him tenure by 1976 and ran at ~100 universities as the free DBMS on Unix. He founded Ingres Corporation in 1980 because academic software couldn't be commercially adopted (Arizona State abandoned Ingres partly because Unix had no COBOL). Postgres followed, with an extendable type system as its core innovation, motivated by GIS types and a bond trader who wanted to overload date subtraction with 30-day "bond time." He chose academia plus [startups](../concepts/startups-and-founding.md) over big tech because big companies impose bosses, rules, and politicking — even part-time at 2000-person Informix felt bureaucratic and impact-free. His latest company DBOS (2023, with Matei Zaharia) grew out of replacing the upper half of Linux with a database and sells durable transactional workflows; ~2/3 of customers are doing agentic AI, which he predicts becomes a distributed-database problem once agents go read-write ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).

## Key views & advice

- Oracle won partly by over-promising: Larry Ellison "made present tense and future tense indistinguishable," shipping broken software and documenting unimplemented features while Ingres actually shipped them ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).
- "One size fits none": stream engines, column stores, and vector stores each beat general RDBMSs ~10x in their domain; Postgres is the right low-end default but lacks a column store and multi-node support for large warehouses ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).
- Vindicated against [Google](google.md): the 2011 DeWitt/Stonebraker paper showed distributed databases beat Hadoop, and eventual consistency fails basic integrity constraints — Google abandoned both with Spanner ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).
- Told [AWS](aws.md) that supporting ~15 database systems is "about 12 too many"; graph databases should be a UI layer over a relational engine — a direct critique of the portfolio [Marc Brooker](marc-brooker.md) works on ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).
- On [AI-era engineering](../concepts/ai-era-engineering.md): LLM text-to-SQL scores ~85% on academic benchmarks but 0% on his real-world warehouse benchmark Beaver (~10% with RAG), because real queries run ~100 lines of SQL over messy, non-mnemonic schemas absent from training data ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).
- Career advice: he wouldn't necessarily recommend CS to 18-year-olds today (healthcare and building trades look safer); PhD grads should take the most prestigious job, find a mentor, and pick an against-the-flow area ([episode](../sources/turing-award-winner-postgres-disagreeing.md)).

## Related

- [Episode: Turing Award Winner: Postgres, Disagreeing with Google, Future Problems](../sources/turing-award-winner-postgres-disagreeing.md) — his interview
- [Barbara Liskov](barbara-liskov.md) — fellow Turing laureate; borrowed transactions from his field
- [Leslie Lamport](leslie-lamport.md) — the consistency/transactions theory behind the eventual-consistency debate
- [Marc Brooker](marc-brooker.md) — AWS databases insider on the other side of his "12 too many" critique
- [Bryan Cantrill](bryan-cantrill.md) — fellow systems contrarian building companies in Oracle's shadow
- [distributed systems](../concepts/distributed-systems.md), [regrets and advice](../concepts/regrets-and-advice.md)
