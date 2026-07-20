---
type: raw-transcript
slug: dropboxs-former-most-senior-eng-building
title: "Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling"
guest: "James Cowling"
date: 2026-05-25
url: https://www.developing.dev/p/dropboxs-former-most-senior-eng-building
fetched: 2026-07-19
complete: false   # transcript ends ~1:21:58; sections from 1:23:23 (mentoring Senior Staff+) through 1:56:36 (younger self advice) missing — source page truncated for fetch tool; text after ~1:18:37 may be lower fidelity
---

# Episode Title, Guest, and Date

**Dropbox's Former Most Senior Eng: Building Great Systems and Advice for the AI Era | James Cowling**

Guest: James Cowling

Publish Date: May 25, 2026

---

# Host's Intro

James Cowling is the CTO at Convex and was previously the most senior engineer at Dropbox. We discussed technical details of his past projects, simplicity vs complexity, and career advice given where AI is today.

Check out the episode wherever you get your podcasts: [YouTube](https://youtu.be/3XkmNSuHFmY), [Spotify](https://open.spotify.com/episode/1Xt2SfdlM8huFQERnsknqP?si=qU-6R9T4QTiwYlpMeppmzg), [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-peterman-pod/id1777363835).

---

# Timestamps

[0:53 - Systems work during his PhD](https://www.developing.dev/i/198900303/053-systems-work-during-his-phd)

[13:05 - Dropbox technical deep dive](https://www.developing.dev/i/198900303/1305-dropbox-technical-deep-dive)

[21:57 - Why Dropbox migrated from AWS](https://www.developing.dev/i/198900303/2157-why-dropbox-migrated-from-aws)

[36:40 - How to do massive migrations](https://www.developing.dev/i/198900303/3640-how-to-do-massive-migrations)

[44:31 - Simplicity vs complexity in promos](https://www.developing.dev/i/198900303/4431-simplicity-vs-complexity-in-promos)

[49:23 - What technical teams should be focused on](https://www.developing.dev/i/198900303/4923-what-technical-teams-should-be-focused-on)

[1:00:25 - Doing the right thing vs promo hypothetical](https://www.developing.dev/i/198900303/10025-doing-the-right-thing-vs-promo-hypothetical)

[1:08:13 - Why he dipped into management sometimes](https://www.developing.dev/i/198900303/10813-why-he-dipped-into-management-sometimes)

[1:11:36 - Why you shouldn't lead by example](https://www.developing.dev/i/198900303/11136-why-you-shouldn-t-lead-by-example)

[1:23:23 - How to mentor Senior Staff+ engineers](https://www.developing.dev/i/198900303/12323-how-to-mentor-senior-staff-engineers)

[1:27:30 - Career advice for the AI era](https://www.developing.dev/i/198900303/12730-career-advice-for-the-ai-era)

[1:37:21 - Why he started his own company](https://www.developing.dev/i/198900303/13721-why-he-started-his-own-company)

[1:46:05 - The most technically challenging work of his career](https://www.developing.dev/i/198900303/14605-the-most-technically-challenging-work-of-his-career)

[1:48:10 - How he got involved in Silicon Valley](https://www.developing.dev/i/198900303/14810-how-he-got-involved-in-silicon-valley)

[1:52:16 - Career regrets](https://www.developing.dev/i/198900303/15216-career-regrets)

[1:55:54 - Top technical book recommendation](https://www.developing.dev/i/198900303/15554-top-technical-book-recommendation)

[1:56:36 - Younger self & permanent underclass advice](https://www.developing.dev/i/198900303/15636-younger-self-permanent-underclass-advice)

---

# Transcript

### 0:53 — Systems work during his PhD

**Ryan:**

[[0:53](https://youtu.be/3XkmNSuHFmY?t=53)] Here's the full episode. First off, your PhD thesis was huge. It's 156 pages. I didn't know theses were that long; I thought papers were maybe 10 pages or something like that. It's its own book.

**James:**

[[1:12](https://youtu.be/3XkmNSuHFmY?t=72)] It's very similar to [Spanner](https://en.wikipedia.org/wiki/Spanner_(database)) ultimately. What's funny is I did that work; it came out a little bit before [Spanner](https://en.wikipedia.org/wiki/Spanner_(database)), so I got a citation in the [Spanner](https://en.wikipedia.org/wiki/Spanner_(database)) paper. But then [Spanner](https://en.wikipedia.org/wiki/Spanner_(database)) came out, and everyone kind of forgot about my paper.

**Ryan:**

[[1:27](https://youtu.be/3XkmNSuHFmY?t=87)] You know, about the research. If you could kind of describe the problem that [Granola](https://www.usenix.org/system/files/conference/atc12/atc12-final118.pdf) was solving and how it solved it, those types of things. We can talk about that.

**James:**

[[1:38](https://youtu.be/3XkmNSuHFmY?t=98)] Yeah, absolutely. So my interest in my career has been two parallel threads. One has been abstractions in general, the idea about how to build simple models for complex problems. I find that a very difficult and intellectually stimulating design exercise—how to design APIs, basically. The other has been large-scale transactional systems. I'm a big fan of transactions. A transaction is doing a bunch of things at once, and I think transactions are just one of the most incredible abstractions we've invented because they allow us to manage probably the most difficult problem in computer science, which is concurrency.

[[2:22](https://youtu.be/3XkmNSuHFmY?t=142)] [Granola](https://www.usenix.org/system/files/conference/atc12/atc12-final118.pdf) was an algorithm for how to do distributed transaction coordination, particularly for transactions that I described at the time as one-shot transactions. I'm not actually sure if that was a standard term at the time or whether I made it up. A one-shot transaction means you send some code to the server and say, "Run this function, all these reads, all these writes on two, three, whatever nodes at once."

[[2:55](https://youtu.be/3XkmNSuHFmY?t=175)] And how to make sure this commits atomically across multiple shards in a distributed system. That was my PhD thesis, and my master's thesis was on Byzantine fault tolerance, a consensus protocol in the presence of malicious nodes. It focused on how to achieve agreement in state across multiple parties when there are malicious entities. I guess the most well-known work I did as part of grad school was on a paper called View Stamp Replication Revisited.

[[3:27](https://youtu.be/3XkmNSuHFmY?t=207)] And that was a paper on redefining a protocol called View Stamp Replication Revisited, which predated [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)). It's a very similar algorithm. [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)), [Raft](https://en.wikipedia.org/wiki/Raft_(algorithm)), and View Stamp Replication are all based on virtual synchrony; they're all basically the same thing. That was a paper I wrote at the time, which ended up being influential to a few really great companies like Tiger Beetle.

**Ryan:**

[[3:53](https://youtu.be/3XkmNSuHFmY?t=233)] You mentioned transactions, and I saw in the paper there's this idea of an independent transaction. If I'm understanding correctly, a lot of the efficiency in a distributed system is lost by needing to get consensus and to vote for consensus. In your research, you found a way to avoid needing to vote to reach consensus. How did you do that?

**James:**

[[4:20](https://youtu.be/3XkmNSuHFmY?t=260)] Yes, I mean a lot of people think about performance maybe from the wrong angle because I think of performance as a factor of just this raw horsepower, how fast are your disks, how fast is your network, etc. No one has particularly faster disks or memory than anybody else. What really matters to performance in a large-scale system is eliminating points of coordination. So it's how to allow systems to progress without having contention between parties.

[[4:53](https://youtu.be/3XkmNSuHFmY?t=293)] Where you're basically reducing parallel throughput to serial throughput across large numbers of transactions. In [Granola](https://www.usenix.org/system/files/conference/atc12/atc12-final118.pdf), we had this idea called an independent transaction. Again, that was the terminology at the time where there were two entities basically processing pure functions. They have independent state and they'll both come to the same conclusion as a result.

[[5:16](https://youtu.be/3XkmNSuHFmY?t=316)] And all they need to do then is serialize those transactions. They have to decide if it was to happen atomically across multiple nodes, what timestamp should it get. [Granola](https://www.usenix.org/system/files/conference/atc12/atc12-final118.pdf), the paper, was mostly about how to exchange these timestamps very efficiently. So, how to have multiple parties each propose a timestamp and then choose the maximum of these, basically so you could safely serialize the transaction.

[[5:42](https://youtu.be/3XkmNSuHFmY?t=342)] And there's a lot more complexity that goes into this. But really the focus there was about how to maximize throughput in a large distributed system without resulting in the alternative, which is two-phase commit and two-phase locking. Two-phase commit with two-phase locking is basically the standard approach for when you want to have multiple nodes agreeing on the same thing, where they both agree to lock their state, not process any other data, and then commit a transaction.

[[6:09](https://youtu.be/3XkmNSuHFmY?t=369)] Two-phase commit can be quite low performance because you're blocking basically the systems for the duration of the transaction. It can be high risk too because you are taking a dependency on another node; you're basically blocked waiting for another node to return. And so that was what [Granola](https://www.usenix.org/system/files/conference/atc12/atc12-final118.pdf) was. Now, it's funny you asked about [Granola](https://www.usenix.org/system/files/conference/atc12/atc12-final118.pdf) because I forgot about it.

[[6:33](https://youtu.be/3XkmNSuHFmY?t=393)] That's so far in my history, I kind of forgot about that work. I even forgot the phrase "independent transactions," to be honest. It's great to hear you bring it up again. But I guess all this stuff does feed into all the work you do later on in interesting ways.

**Ryan:**

[[6:48](https://youtu.be/3XkmNSuHFmY?t=408)] When I think about distributed systems, I think about you're at a big company and you got a bunch of machines. But when you were at MIT building this thing, how did you build and test it? Were there spare machines that the college had, or was this in the cloud?

**James:**

[[7:05](https://youtu.be/3XkmNSuHFmY?t=425)] Yeah, this was a long time ago. Now I'm showing my age. This is pretty early in the days of Amazon Web Services. We had a rack of servers in our office that we could use. I was fortunate enough to be at MIT where we could afford a rack. There was also a service called Planet Lab, which was a big communal set of nodes that academics could use to run tests. But Planet Lab was a communal system.

[[7:34](https://youtu.be/3XkmNSuHFmY?t=454)] And so it was continually having problems. It's just a free for all. For the longest time, I would just sleep next to my desk and wake up whenever. Planet Lab was free. Because you need to run some benchmarks these days, you just spin something up on Amazon Web Services. But then I would sleep next to my desk, and I would wake up in the middle of the night or at random times and check Planet Lab status and then kick off a benchmarking job.

[[7:58](https://youtu.be/3XkmNSuHFmY?t=478)] Now this was right at the cusp of when, in some respects, Google ruined systems research. I say that with affection and respect to Google because before then, most of the research was coming out of academia. A lot of distributed systems research was done on smaller scales, and a lot of the value proposition was the ideas. So, like, hey, I wrote a paper, here's an interesting new idea, and yeah, it's all in theory.

[[8:28](https://youtu.be/3XkmNSuHFmY?t=508)] And so the value that came out of it was the idea. Around this time, you started seeing papers out of Google, Amazon, and these various companies where it wasn't necessarily a paper about an idea; it was a paper about a system. Hey, I built this giant system, it has a whole bunch of features, some of which are interesting, some of which are not, and by the way, it powers Gmail or whatever. That kicked off a pretty interesting transition because at that point, program committees reviewing papers started to expect to see realistic benchmarks that, frankly, grad students were not able to produce at least at the time.

[[9:08](https://youtu.be/3XkmNSuHFmY?t=548)] I mean, I wasn't running Gmail on my system, and I think it did, in some respects, obscure intellectual ideas. I'm more for papers about systems. But I think there's also value in a paper about an idea. It's not just, "We built this big thing, and it works, and it's up to you to figure out what's interesting about it." Instead, it's, "Here's a new thing." There's a paper, an old paper just called Leases, where someone invented the idea of a time-based lock.

[[9:37](https://youtu.be/3XkmNSuHFmY?t=577)] And it's just a paper called Leases. That was a cool era of systems research. I think a lot of it now has shifted towards industrial research, where people are building stuff for practical purposes. Whereas I think it's hard for academia to compete on pragmatism. Academia is really a great place to do impractical work.

**Ryan:**

[[9:59](https://youtu.be/3XkmNSuHFmY?t=599)] When you look back on getting the PhD in academia, being enabled to completely explore an idea versus going into industry, maybe working on [Spanner](https://en.wikipedia.org/wiki/Spanner_(database)) at Google or something like that, which path do you think would be better and why?

**James:**

[[10:18](https://youtu.be/3XkmNSuHFmY?t=618)] I think that's a bit of a misconception a lot of folks have about PhD programs. A lot of students are high-achieving students in college, and they think that the PhD program is college. It's like, hey, I like learning things, so I'm going to go do a PhD, but it's not. A PhD is training to be a researcher, and for most people, they shouldn't do that. If someone wants to be a professional software engineer, they probably shouldn't spend their time training to be a researcher.

[[10:46](https://youtu.be/3XkmNSuHFmY?t=646)] But with a really important caveat, I think there's a really interesting and challenging developmental experience you go through in the PhD program at a top university, at least. You reach a certain point in time when you have a problem that you're facing that no one else in the world knows the answer to. You have a problem that you are the world expert on, and you can't chat about it with folks, but you can't ask your advisor because your advisor doesn't know either.

[[11:12](https://youtu.be/3XkmNSuHFmY?t=672)] Right. So you face these difficult challenges where you can't read a book, you can't ask Claude. And so you're forced to go through a quite difficult and, frankly, emotionally challenging experience of being unsure, being uncertain, and learning to think for yourself. I think that is really valuable for all engineers. I think that was really, really valuable in my career.

[[11:39](https://youtu.be/3XkmNSuHFmY?t=699)] I do see a lot of folks early in their career think that all knowledge comes from reading or absorbing it from someone else, or that there's a right way to do things. But I think being in a PhD program or being faced with really demanding, open questions does train your mind to be comfortable with that discomfort. I feel a little bit lucky that I went through grad school without large language models existing because I had to deal with this uncertainty.

[[12:15](https://youtu.be/3XkmNSuHFmY?t=735)] There was no crutch to help me out, which I think was very valuable.

**Ryan:**

[[12:18](https://youtu.be/3XkmNSuHFmY?t=738)] So, I mean, a lot of, if you want to be a researcher, go do a PhD. If you want to build stuff, go build stuff. Since leaving academia, I've done a lot of work that I guess one could call innovative. It advanced the industry in certain ways and did novel stuff. But our goal was never research. Our goal was just to solve problems.

**James:**

[[12:47](https://youtu.be/3XkmNSuHFmY?t=767)] And I think that's the difference. In academia, your goal is to advance knowledge. In industry, your goal is to solve problems. I gravitate more towards just solving problems, and I find that a more comfortable environment within which to work.

### 13:05 — Dropbox technical deep dive

**Ryan:**

[[13:05](https://youtu.be/3XkmNSuHFmY?t=785)] Going to your time in industry, at [Dropbox](https://en.wikipedia.org/wiki/Dropbox), you became the most senior engineer at the company. Looking through all the projects that you did, I had a series of just technical curiosities. I saw this idea early in your career about multi-homing, and I wasn't familiar with that concept. What is multi-homing? What's the problem it solves?

**James:**

[[13:27](https://youtu.be/3XkmNSuHFmY?t=807)] Yeah, I mean, multi-homing is the ability to have data in two locations, two homes. Multi-homing can be valuable for a variety of reasons. One is called primary-secondary or lazily replicated multi-homing, whereby all writes commit authoritatively in one region and get replicated to a secondary region. This is normally used for business continuity. One thing we did at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) was to ensure that if the entire West Coast blew up, which hopefully wouldn't happen, [Dropbox](https://en.wikipedia.org/wiki/Dropbox) would keep running because the data would be replicated in other regions, but with a window of vulnerability, with a window of time where there may be some data lost.

So that is, you know, that's kind of primary-secondary replication or multi-homing. There's something else called active-active multi-homing where there is truly an authoritative copy of the data in multiple locations. Basically, when you, for example, write to a system, you don't externalize that write as having succeeded until it has landed in all the regions. For example, in the storage system at [Dropbox](https://en.wikipedia.org/wiki/Dropbox), the block storage system, we truly had a multi-region replicated system where we could take down an entire region, say take down the region in Ashburn, Virginia, where everyone's data centers are, and there'd be zero downtime for the company and the data was still safe in multiple regions.

[[14:54](https://youtu.be/3XkmNSuHFmY?t=894)] I think multi-homing is something a lot of engineers aspire to work on because it seems like the right thing to do. But the reality is for most companies, it is not. Not because there's very high cost, but because there are very high latency costs for this. The speed of light is fixed. If you have to synchronously write data across multiple regions in the United States, you're going to have, say, 60 milliseconds in the commit path of your protocol, which for most applications is not tenable.

[[15:32](https://youtu.be/3XkmNSuHFmY?t=932)] So there is a lot of desire; a lot of engineering teams reach out for advice on how to adopt active-active multi-homing for their company. I would normally say don't do it. Frankly, if US East is down, if Amazon is down that day, that's okay. If Amazon's down that day, your company will be down. That's a shame, right? But by avoiding that complexity, you're going to be able to move much faster and build a much better product.

[[16:00](https://youtu.be/3XkmNSuHFmY?t=960)] And so in my mind, systems are all about trade-offs and making the right ones. I would generally recommend most people do not make the trade-off to have partition tolerance or multi-region availability. Even though for a company like [Dropbox](https://en.wikipedia.org/wiki/Dropbox), yes, that does make sense. When your job is storing data and you have several exabytes of it and hundreds of millions of customers, I think that's when it starts to make sense.

**Ryan:**

[[16:26](https://youtu.be/3XkmNSuHFmY?t=986)] So it's just another term for, I guess, data replication and having it available in other regions. I imagine also, I mean, the cost of storage is a concern. How many replicas would you keep for something like, let's just say I stored something in [Dropbox](https://en.wikipedia.org/wiki/Dropbox)? It's my document. Is that on the order of one or two, or are there multiple?

**James:**

[[16:47](https://youtu.be/3XkmNSuHFmY?t=1007)] No, it's on the order of many. Many. If you were to store a file in [Dropbox](https://en.wikipedia.org/wiki/Dropbox), I modeled the storage to be, as we advertise, at least 12 nines of durability internally. The models look around 24 nines of durability. That means the data is secure with 99.9999% where there's 24 nines. Right? Which means, at least according to the model, the universe will be extinct before any data is lost.

[[17:20](https://youtu.be/3XkmNSuHFmY?t=1040)] And the way that is done is by a combination of what's called erasure coding. Erasure coding is how you take several blocks of data and combine them together with an encoding scheme and spread them around in different locations. At that scale, at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) scale, you're taking things into consideration, like putting data in different racks, different rows of a data center because they're on different power feeds.

[[17:41](https://youtu.be/3XkmNSuHFmY?t=1061)] You're taking into consideration different eras of hard drives and different manufacturers of drives because they could have correlated failure patterns and then replication across regions. So you could be looking at 27 fragments, for example. That doesn't mean you're storing 27 times the data. It's kind of encoded in many regions. But the replication schemes get really quite sophisticated at that point.

[[18:06](https://youtu.be/3XkmNSuHFmY?t=1086)] And we actually had our own custom encoding matrix we had developed. It's called a [Vandermonde matrix](https://en.wikipedia.org/wiki/Vandermonde_matrix), where you take a bunch of data and combine it together to produce outputs. We would plug in some variables like how much do disks cost? How much does network bandwidth cost? Because there's a trade-off. You can either store, if you don't want to lose your data, more copies on more disks, or you can store fewer copies.

[[18:33](https://youtu.be/3XkmNSuHFmY?t=1113)] Anytime a disk fails, you re-replicate it really fast. Re-replicating really fast costs disk cross network bandwidth. These kinds of variables go into this equation. It ends up being an extremely complex field of endeavor, but it's kind of abstracted away into a part of the system that doesn't leak into anywhere else.

**Ryan:**

[[18:53](https://youtu.be/3XkmNSuHFmY?t=1133)] So with erasure encoding, my document in [Dropbox](https://en.wikipedia.org/wiki/Dropbox) is fragmented into a bunch of different chunks of data and loaded potentially from many different machines.

**James:**

[[19:03](https://youtu.be/3XkmNSuHFmY?t=1143)] Yes, absolutely.

**Ryan:**

[[19:05](https://youtu.be/3XkmNSuHFmY?t=1145)] I mean, the first thought I have is now I might be waiting there, and one of the 27 machines is slow, and I can't look at the whole document. So how do you prevent against that?

**James:**

[[19:17](https://youtu.be/3XkmNSuHFmY?t=1157)] It's actually faster than not replicated. Because if you imagine, I'll pick a simplified example. Imagine this is not the encoding scheme [Dropbox](https://en.wikipedia.org/wiki/Dropbox) uses, but to reconstruct a file, you have to read six out of nine fragments. So if you read six out of nine fragments, you can just ask all nine and reconstruct and return the data as soon as you've heard from the first six. It's actually faster.

[[19:46](https://youtu.be/3XkmNSuHFmY?t=1186)] And you can construct these encoding matrices such that it's actually faster to have a ratio-coded data than not.

**Ryan:**

[[19:53](https://youtu.be/3XkmNSuHFmY?t=1193)] I see. Okay. So you can oversubscribe, over-request, and then you complete on a portion of them being received.

**James:**

[[20:01](https://youtu.be/3XkmNSuHFmY?t=1201)] Yes. Now in practice, it was a bit more complex than that. We'd often have a copy and a single disk to provide fast access. We'd often try to make sure that you could serve your data out of a region close to your home region. So we'd make sure that your data was mostly served with low latency. But if that region had failed, you could reconstruct it from the remaining regions. So there's a lot of talk about building your own infrastructure.

[[20:28](https://youtu.be/3XkmNSuHFmY?t=1228)] And you can save money by moving off the cloud. Almost definitely you can't unless you have very small requirements, very fixed requirements, or very heavy investment. Because if you want to compete with Amazon, if you want to build a more efficient storage system than Amazon, you have to have a supply chain team that's working with Western Digital and Seagate, constantly negotiating on prices of disks and buying shipments at certain times, along with capacity teams and data center teams.

[[21:00](https://youtu.be/3XkmNSuHFmY?t=1260)] There's a lot of work that goes into optimizing this because ultimately our desire was to use the disks to 90, 95% of their disk size to maximize storage efficiency. To put it this way, that was, you know, I guess a ballpark figure of a $1 billion project. And it was, as far as I know, the largest ever data migration in history at that time.

[[21:28](https://youtu.be/3XkmNSuHFmY?t=1288)] And so, an extremely large engineering project with very high technical investment. Yes, if you have that scale and you have the engineering team to do it, and you're willing to keep innovating, if you're willing to keep optimizing and investing effort in it, then yes, you can do it. But I think the real— I mean, the cloud has been an incredible innovation. Most people are not experts at this, and most people should not be experts at this.

[[21:55](https://youtu.be/3XkmNSuHFmY?t=1315)] Most people should focus on their applications.

### 21:57 — Why Dropbox migrated from AWS

**Ryan:**

[[21:57](https://youtu.be/3XkmNSuHFmY?t=1317)] When you say that most people shouldn't, my immediate thought was, one of the big projects you worked on at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) was migrating away from Amazon Simple Storage Service. So why did [Dropbox](https://en.wikipedia.org/wiki/Dropbox) migrate away from S3?

**James:**

[[22:12](https://youtu.be/3XkmNSuHFmY?t=1332)] Yeah, that was a desire at the company for a long time, from even before I was there. I started at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) in 2010, and I spoke to Drew, the [Dropbox](https://en.wikipedia.org/wiki/Dropbox) founder, about this project. There was a desire to control the destiny of the company from a strategic perspective. At the time, this was before [Dropbox](https://en.wikipedia.org/wiki/Dropbox) reshaped itself as being more about collaboration.

[[22:36](https://youtu.be/3XkmNSuHFmY?t=1356)] At the time, it was a file sync and share category. That was the market sector, and owning the file system was really valuable to the company. Ultimately, we saved a huge amount of money. This was before the company went public. We really drove massive cost efficiencies through the project. But it was hard, in a way that I think would be very difficult to emulate without a huge investment.

[[23:03](https://youtu.be/3XkmNSuHFmY?t=1383)] And I do think there is a benefit to an organization from having hard problems to solve. If you have a company with extremely hard technical challenges, you can attract engineers who like working on those hard technical problems. When they've solved those problems, they cycle off and work on different parts of the system. After we all worked, we had such a great team.

[[23:28](https://youtu.be/3XkmNSuHFmY?t=1408)] It was a very, very small engineering team. After we shipped the storage system reliably, we all went off, and Jamie redesigned the sync protocol, the desktop client, and I worked on the file system and the distributed databases. There's value to a business in having that level of technical investment. But it's like having a baby; you have to raise the baby. You can't just build a system like this and say, "That's it, we're done."

[[23:59](https://youtu.be/3XkmNSuHFmY?t=1439)] You own it, and you have to keep investing in it.

**Ryan:**

[[24:03](https://youtu.be/3XkmNSuHFmY?t=1443)] Did S3 do any counter negotiation before you set out to leave them? Did they say, "Oh, we'll cut you a deal?"

**James:**

[[24:12](https://youtu.be/3XkmNSuHFmY?t=1452)] I guess I'm allowed to talk about this now. It was a long time ago. For the longest time, I don't think they were particularly aware that this was happening. But the data center folks talk, and certainly it was noticed that [Dropbox](https://en.wikipedia.org/wiki/Dropbox) was buying up a lot of data center space. So yeah, we had, obviously at the scales that we were at, we were negotiating very good rates with Amazon Web Services.

[[24:38](https://youtu.be/3XkmNSuHFmY?t=1478)] We weren't paying sticker price. We were paying very, very, very good discounted rates. But at a certain point, they weren't able to meet our cost efficiency because when we launched the system, it really was more efficient than Amazon Simple Storage Service. And that's for a variety of reasons. One was that we were using kind of new experimental disks called Shingled Magnetic Recording. We were the first ones, I think, to use these disks at scale.

[[25:02](https://youtu.be/3XkmNSuHFmY?t=1502)] And two, we had a very tight understanding of our workload. We were able to design the system specifically optimized for our workloads, whereas S3 has to design the system for everybody. It got to the point where Amazon would not have been able to offer us a more competitive deal because we had a more efficient system. I wouldn't recommend another company do this right now, but I think at the time it certainly made sense for us as a company.

**Ryan:**

[[25:28](https://youtu.be/3XkmNSuHFmY?t=1528)] Can you give an example of a tight understanding of your workload leading to something you could do that Amazon Simple Storage Service couldn't?

**James:**

[[25:36](https://youtu.be/3XkmNSuHFmY?t=1536)] Yeah, absolutely. So, for example, I know that, well, I'll try not to leak any confidential data, right? But when you upload a file to [Dropbox](https://en.wikipedia.org/wiki/Dropbox), there is a pattern of access. Typically, people access the file very quickly shortly afterwards because you're sharing it with someone, or maybe [Dropbox](https://en.wikipedia.org/wiki/Dropbox) is processing that file to generate an image preview, and then it decays at a certain rate. We understand in general the average block size, and we also understand the access pattern.

[[26:11](https://youtu.be/3XkmNSuHFmY?t=1571)] So we could do things like, at a certain point, we had these two clusters. One was designed for temporary storage that was kind of storage inefficient but access efficient. It was very cheap to read and write to, but it was inefficient to store. Data would get written to there first, and then in the background, it would get moved in bulk to this colder storage system. This cold storage was far more static.

[[26:40](https://youtu.be/3XkmNSuHFmY?t=1600)] And so it was able to have more efficient algorithms and be written to in bulk. If it went down for writes, that was no problem because it wasn't in the live path. We were able to trade off again; like systems are all about trade-offs. We were able to trade off the live data write path from the long-term read path. That was one of many examples where knowing the size of your data, where it's accessed from, how frequently it gets accessed, and how long it takes to delete that data, you can really tune a system to your workload.

[[27:13](https://youtu.be/3XkmNSuHFmY?t=1633)] You know, stuff like looking at even things down to knowing how much power to put in a rack. You have a rack of hardware; there's a power distribution unit, a PDU. At the top of that rack, it has a circuit breaker which can handle a certain number of amps. We would have to figure out how many amps are required for that rack based on access patterns. There were times where we got it slightly wrong.

[[27:37](https://youtu.be/3XkmNSuHFmY?t=1657)] There was a time when we got maybe a bad batch of hardware, and disks were failing too frequently. As a result, we were re-replicating the data more regularly. I was getting messages from the data center team saying, "Hey, we're running the racks really hot right now." That's the level of optimization you can make when you get to that scale. But again, that's multi-exabyte scale—million hard drive scale.

**Ryan:**

[[28:03](https://youtu.be/3XkmNSuHFmY?t=1683)] Yeah. When I was reading about this migration, I saw somewhere in the migration you initially started with Go, and then the racks or something that you're running on, the hardware itself was out of memory too much or requesting too much memory. And then you migrated to Rust.

**James:**

[[28:20](https://youtu.be/3XkmNSuHFmY?t=1700)] So initially, the prototype was in Python, if you can believe that. To be fair, Python is actually pretty efficient for I/O. I think people give Python a bad rap for I/O-bound workloads. It's pretty good at I/O, but obviously not great for concurrency, not great for memory management, and very hard to refactor. It was critical the system was correct. So we migrated everything to Go, and we built most of the storage system in Go.

[[28:47](https://youtu.be/3XkmNSuHFmY?t=1727)] This is before Go was in general availability. We built the system in Go. Go's a great language for concurrency, a great language for proxies. It's really well designed for servers that move from one place to another. At a certain point, though, we would have, let's just pick a number, let's say a million. Let's say we have a million nodes in the system, and every node has some amount of memory, some amount of disk, some amount of sheet metal in the chassis.

[[29:18](https://youtu.be/3XkmNSuHFmY?t=1758)] Right. We would itemize all these things. You'd have a pie chart of how much money is spent on all the things. It would include items like sheet metal and screws. So you're trying to optimize the storage. A big problem for us was the amount of memory these nodes were using. Not just the memory that we were using, but the unpredictability of it. With Go having a runtime, in a storage system, an out of memory error is pretty bad because if a node runs out of memory and restarts, that looks like a disk failure.

[[29:54](https://youtu.be/3XkmNSuHFmY?t=1794)] So that looks a lot like a disk has failed and has to be re-replicated. A batch of nodes running out of memory can lead to cascading failures throughout the system. I remember a time it was a band; it might have been De La Soul, I can't remember. There was a band that released an album on [Dropbox](https://en.wikipedia.org/wiki/Dropbox), which caused a big spike in load to a few files. It was very high bandwidth, and it caused the machines to run out of memory.

[[30:24](https://youtu.be/3XkmNSuHFmY?t=1824)] So those machines, those disks oomed. As a result, no problems; the system went to try to recover that data from a whole bunch of other replicas. Now all of a sudden, you've taken one amount, one fire hose worth of load coming in, and you've turned this into seven fire hoses worth of load coming. Because now you have to do a more expensive reconstruction operation, right? So now you've 7x the load.

[[30:47](https://youtu.be/3XkmNSuHFmY?t=1847)] And these are the kind of cyclical behaviors that can lead to something called congestion collapse. Congestion collapse is when workload to a system crosses a threshold where it all kind of collapses. Designing against congestion collapse is really one of the hardest parts of Magic Pocket, which is the name of the storage system. Ultimately, we switched to Rust for the storage nodes themselves.

[[31:13](https://youtu.be/3XkmNSuHFmY?t=1873)] And this, again, this is before Rust was in GA. So that was a bit of a risky move. But we rewrote the switch to Rust, which coincided with getting rid of the file system entirely on the disks and directly addressing the disk heads. There's an instruction set, I think it's called ZBC, Zone Based Block Control, something like that. There's an instruction set for accessing disks that we were using. The disk manufacturers gave us the draft specs of these new disks, and we were operating off the draft specs and directly controlling the disks.

[[31:45](https://youtu.be/3XkmNSuHFmY?t=1905)] And so all that product was tied up together into a product called Discotech, which was the disk technology project. Ultimately, if you look at that pie chart, congestion collapse stopped and reliability improved. But if you looked at the pie chart of where all the money was going, it really shifted to be almost all disks.

**Ryan:**

[[32:16](https://youtu.be/3XkmNSuHFmY?t=1936)] Metal, et cetera, the cascading failure you mentioned was there. That happened, and then there was a postmortem.

**James:**

[[32:23](https://youtu.be/3XkmNSuHFmY?t=1943)] I don't think we needed a postmortem. I think we knew as it was happening. When I was getting paged in the middle of the night on these things, it was pretty evident. This is, again, an argument in favor of the cloud. Imagine you've spent hundreds of millions of dollars on a storage system, and it's out in production on physical hardware.

[[32:47](https://youtu.be/3XkmNSuHFmY?t=1967)] You can't just go and put new memory chips in every one of them. I mean, you can, but you have to pay people to come in and swap them out. That's a tricky place. This is what I love about the industry. Some of the more challenging moments on Magic Pocket were stuff like, in one week, just a weird coincidence, two trucks crashed that were delivering servers.

[[33:13](https://youtu.be/3XkmNSuHFmY?t=1993)] So there are two trucks showing up to deliver racks, and they both crashed. I don't know, the drivers were okay. So we lost capacity for two weeks. We lost capacity for more than two weeks, probably six weeks. What do you do? What happens is the equivalent of your disk filling up on your laptop, except it's a million disks, and you can't tell the customers to go away; you can't delete their files.

[[33:43](https://youtu.be/3XkmNSuHFmY?t=2023)] A lot of tricky capacity work. Ultimately, what that led to was trying to build in all these protections against the unknowns, making sure we had the right amount of buffer planned out for anything bad that could happen, making sure we designed the system so there couldn't be congestion collapse and so there wouldn't be memory spikes. At one point, there's a process called FMEA, which is a threat modeling process where you have a big spreadsheet and you kind of write down every bad thing that could possibly happen, and then you know how bad it would be if it happened. Existential risk does someone die? If there's a fire in the data center, all these kinds of things get put into this spreadsheet, and you kind of do a bit of a pre-mortem to figure out all the potential failure modes and then design around them. I love that work. I really, I don't know, I do like the firefight. I can't say I like getting paged because I've spent my whole life on call, but I do like that rubber-hits-the-road stuff.

[[34:52](https://youtu.be/3XkmNSuHFmY?t=2092)] I like that. Wow. There's congestion collapse and there's no one that can help you. You've got to think through this problem.

**Ryan:**

[[35:01](https://youtu.be/3XkmNSuHFmY?t=2101)] When I worked on infrastructure at Instagram, we had this concept of defcon knobs, which are basically these configs that you could flip to gracefully degrade your system while still operating it. But maybe in the case of [Dropbox](https://en.wikipedia.org/wiki/Dropbox), you store fewer replicas, so you take on a temporary increase of risk in losing data because you need to. Did you have something like that, and did you flip it in that type of case?

**James:**

[[35:29](https://youtu.be/3XkmNSuHFmY?t=2129)] Never. When it came to durability, we had absolute zero, non-negotiable standards; there was no room for negotiation on user durability. We had those knobs for background processes, for CPU and memory, for example. If there was a spike in load, you could turn off background processes and then turn off the test load on the system. Eventually, we built this system called Trampoline, and what Trampoline did was save us a ton of money.

[[36:05](https://youtu.be/3XkmNSuHFmY?t=2165)] If we ever got too close to the threshold, we would just start writing data to Amazon Simple Storage Service because it's right there. You can run your capacity way closer to the edge if you're willing, under worst-case scenarios, just to dump 30 petabytes on S3 and then move it back when it's done. Now, that didn't happen very often. We would do it to test it. We would do that just to make sure the system worked. But yeah, being able to have an escape hatch for worst-case scenarios was really nice.

**Ryan:**

[[36:35](https://youtu.be/3XkmNSuHFmY?t=2195)] I see. So S3 is kind of like elastic storage.

**James:**

[[36:39](https://youtu.be/3XkmNSuHFmY?t=2199)] Exactly.

### 36:40 — How to do massive migrations

**Ryan:**

[[36:40](https://youtu.be/3XkmNSuHFmY?t=2200)] When I looked at this project, it's such a massive migration, and my first thought is how do you coordinate this whole project without breaking the system as it's running? What are your thoughts on doing such a large migration without breaking things?

**James:**

[[36:58](https://youtu.be/3XkmNSuHFmY?t=2218)] Yeah. Now, in terms of the engineers that built the initial version of the system, it was a handful—three, four, five, six engineers. It wasn't a team of a thousand; it was a very small team. So how do you build such a large system with a small number of people? And then how do you do a high-risk migration? One of the things you do is keep things simple. You try very hard to build cleanly abstracted, simple systems so that their failure modes are very understandable.

[[37:33](https://youtu.be/3XkmNSuHFmY?t=2253)] And so they're decoupled, so they don't have congestion, collapse, et cetera. Focusing on simplicity gets tricky, by the way, with people doing agentic development. They're not the best at building simple systems. Simplicity is still the domain of human beings for now, but there's a big focus on simplicity. The other was this very thick layer of validation checks during this migration.

[[37:58](https://youtu.be/3XkmNSuHFmY?t=2278)] And in fact, when we did the migration off of Amazon Simple Storage Service, we had something called the dark launch where we would be moving data off of S3, but we'd keep it in both locations. We had to demonstrate to the [Dropbox](https://en.wikipedia.org/wiki/Dropbox) founders that we would have to keep this system running with no incidents, no downtime, and no data loss for six months before we would delete any of the data from S3.

[[38:26](https://youtu.be/3XkmNSuHFmY?t=2306)] So we have double routed, and there's one point in time, halfway through this process, where a bug got through to production. Nothing bad happened with the bug, but it was like bugs slipped through our multiple layers of the release process, etc. I went to the VP and I said, "Hey, a bug made it through to production, and we're going to reset the launch clock. As a result, it's going to launch later, and it's going to cost us some amount of money, let's say double-digit millions."

[[39:05](https://youtu.be/3XkmNSuHFmY?t=2345)] And they were like, great, thank you, that's good, I trust you. That was the cool thing. I mean, [Dropbox](https://en.wikipedia.org/wiki/Dropbox) had a lot of incredible cultural values, but that was like, okay, cool. If you're prioritizing user safety, that's the right thing to do. No one was mad about that. It was almost like they were proud, you know? It was just like, yes, you're operating in accordance with the principles of this company.

**Ryan:**

[[39:31](https://youtu.be/3XkmNSuHFmY?t=2371)] Okay. So it was double writing both systems for a while and then some subset of data.

**James:**

[[39:34](https://youtu.be/3XkmNSuHFmY?t=2374)] for a while and then some subset of data.

**Ryan:**

[[39:36](https://youtu.be/3XkmNSuHFmY?t=2376)] Yeah, okay. And then you switched over reads once.

**James:**

[[39:39](https://youtu.be/3XkmNSuHFmY?t=2379)] We were sure that the system was durable and we had all the validators running in production 24/7. We were just migrating as fast as we could. I think at some point we got to 764 gigabits per second of peering bandwidth between Amazon servers and ours. Certainly, someone on the network team over there noticed that there was that much data moving out. At one point, I got a slightly nasty email from someone saying it was super weird.

[[40:08](https://youtu.be/3XkmNSuHFmY?t=2408)] I think the phrase "super weird" is like, it's super weird that you're doing so many reads and not that many writes. I didn't respond to that email. But to be fair, Amazon was a great partner for [Dropbox](https://en.wikipedia.org/wiki/Dropbox). So [Dropbox](https://en.wikipedia.org/wiki/Dropbox) still uses Amazon Web Services. There was no concern that they would do the wrong thing by us as a company. I mean, we only had an excellent experience with Amazon Web Services. But yeah, it was a moment for us.

[[40:36](https://youtu.be/3XkmNSuHFmY?t=2436)] It probably strained the relationship somewhat.

**Ryan:**

[[40:41](https://youtu.be/3XkmNSuHFmY?t=2441)] You mentioned simplicity and intuition; it makes sense. Do you have a concrete example, though?

**James:**

[[40:48](https://youtu.be/3XkmNSuHFmY?t=2448)] Yeah, I've got a concrete example for you. Maybe it shows the difference between academia and industry. The storage system is a giant distributed system with files stored in various locations. You need a mapping from the file to where it lives on these disks. All we did was have a cluster of 1,000 MySQL nodes, a big giant database. It was indexed by the block ID and indicated that this block is on these disks.

[[41:21](https://youtu.be/3XkmNSuHFmY?t=2481)] And that's pretty simple. It's not sophisticated. Every time we'd hire someone out of academia or maybe from other companies, they would say, "Oh, this is not very sophisticated because you could use a Patricia trie or you could use a distributed hash table, and that would map a block to a set of locations." I think that's optimizing for the wrong thing because the really nice thing about dumping a list of files and the locations in a giant database is that it is written in one location.

[[41:57](https://youtu.be/3XkmNSuHFmY?t=2517)] If I want to validate what happened, if I want to check all the data is where it's meant to be, I just walk over the table and check. We had services constantly walking over the table and checking. Whereas if it was a distributed hash table or some giant complex data structure, it's very hard to validate. Designing for validation is very important. Designing for understanding is very important.

[[42:19](https://youtu.be/3XkmNSuHFmY?t=2539)] It's not about getting a system to work. It's what do you do when it doesn't work. Right. And so having a very simple boundary, that's a very basic example. There are more sophisticated examples that take more time to explain. But something like that is a lot of engineers will feed, a lot of engineers will want to do interesting work, will want to advance in their career. They want to be seen as an intellectual problem solver.

[[42:49](https://youtu.be/3XkmNSuHFmY?t=2569)] And so the tendency can be to design complex systems. My argument is always that simple systems are way harder to design than complex systems. Simplicity is so hard. And I think to the untrained eye, a simple system can seem obvious. The best compliment you could ever get about anything you design is when people say, "Oh, isn't that the obvious way of doing it?" It's the same as [Convex](https://www.convex.dev/); people say, "Oh, isn't that just the obvious way of structuring?" Great, because it wasn't obvious when we did it. No one else was doing it. Everyone thought we were idiots. If after the fact people think it's obvious, then you really nailed it. But I think it requires an understanding that simplicity is the hardest thing in systems. And because simplicity is scalable. Yes, simplicity is scalable in terms of numbers of queries per second.

[[43:48](https://youtu.be/3XkmNSuHFmY?t=2628)] But what I really mean about scalability is you can take a simple system and have it run for five years, have people work in it for five years, have all sorts of features added to it, and have requirements changed because the company realized the product didn't work the way it wanted to work and it wants to change things. It still stands the test of time, whereas a complex, over-optimized system will not.

[[44:11](https://youtu.be/3XkmNSuHFmY?t=2651)] I think that's the tough thing about distributed systems design, especially LLM-augmented distributed systems design. Just because something works doesn't mean it's maintainable over a long period of time, doesn't mean it's understandable, and doesn't mean it's cleanly architected and abstracted. That stuff's really very hard.

### 44:31 — Simplicity vs complexity in promos

**Ryan:**

[[44:31](https://youtu.be/3XkmNSuHFmY?t=2671)] Absolutely. And I agree with you. I think it's the long-term beneficial thing to do. One unusual thing, though, in the industry that I've seen is the incentive system for engineers. I mean, you mentioned the desire for an engineer to want to be seen as someone who can do something difficult. There's that, but there's also the incentive system of promotions. I've had many friends whose promotions were rejected because their work wasn't complex enough.

[[45:01](https://youtu.be/3XkmNSuHFmY?t=2701)] And so that kind of forces complexity, which is kind of unusual. I wanted to know what you thought about that.

**James:**

[[45:08](https://youtu.be/3XkmNSuHFmY?t=2708)] Yeah, I mean it almost angers me. I just like it so much. Partly why I started my own company. I think the ideal for anyone is to be doing work where you're being appreciated for solving the problem. If we get philosophical, this is what it was like going back to the farming days, right? There was no incentive to make it really complicated to milk a cow because the goal is to milk the cow, and then the reward is you got milk.

[[45:42](https://youtu.be/3XkmNSuHFmY?t=2742)] Right. I think it sounds so silly, but at a startup, the goal is to build the system, have it work, have the users like it, have it grow, and everyone gets rewarded and celebrated for solving the problem. It gets hard to scale that. So at large companies, you end up with so many layers of organization that people build alternative incentive structures.

[[46:08](https://youtu.be/3XkmNSuHFmY?t=2768)] Right. It's like I'm so far away from whatever the hell we're trying to do over here that my goal now is to get all green check marks on my OKR plan. But who cares about your OKR plan unless it solves the problem? The thing that really drives me insane is when people try to chase artificial goals. I understand that if you're in a company like this, you may have no choice in the matter.

[[46:39](https://youtu.be/3XkmNSuHFmY?t=2799)] But what I want to tell people is there is a better way. That better way may not be available to you; you may not have job opportunities near where you are, for example. But if you do have the ability to work at a company where you are being appreciated for problem solving, that will make you so much better as an engineer. I see this when I interview people.

[[47:07](https://youtu.be/3XkmNSuHFmY?t=2827)] If I do a deep dive with them, they'll say they built a system, and I'll ask, "Why did you build it?" and they're like, "I don't know, the VP told me to." I'll ask, "How's the system used?" and they're like, "I don't really, I think ads use it." I'm not sure. This is a caricature, but I think it's very, very hard to do good engineering in that environment. You can do competent engineering, but the best engineering comes from a deep understanding of why. This is something we just drill into the team here at [Convex](https://www.convex.dev/); the team embodies this so strongly at [Convex](https://www.convex.dev/): everything exists for the why. Don't build a fancy load balancer unless it's needed.

[[47:57](https://youtu.be/3XkmNSuHFmY?t=2877)] Turns out we do need a fancy load balancer. We're building it right now. But you should always start with, why are we doing this? What's the point? I feel for people stuck in environments that are not like this. But you know what? Try to fight the system a little bit. I do see a lot of nihilism, a lot of defeatedness sometimes amongst junior engineers, a lot of this cynicism, like, what does it matter? Who cares? It's just a big organization and nothing matters. But I think it does matter. If I think of the happiest times in my life, it's been dedicating myself to a cause, trying really hard, and trying to do the right thing. I felt good when I went home, not trying to get promoted, just trying to do the right thing and then assuming I'm going to get promoted. If not, go somewhere else.

[[48:53](https://youtu.be/3XkmNSuHFmY?t=2933)] I know it does sound quaint when I'm saying this, but I think it's possible to do this, and especially possible if you surround yourself with people like this. If someone is in a big company and they're feeling frustrated by politics, look around and see if there's a team of folks who just seem to want to do the right thing, just seem to want to do good stuff. I don't think that's selling out. I think that's being true to yourself. That's what real engineering is. Not trying to make a complicated fancy thing to get promoted. Just build the coolest thing that solves the problem.

### 49:23 — What technical teams should be focused on

**Ryan:**

[[49:23](https://youtu.be/3XkmNSuHFmY?t=2963)] This really reminds me of something you had written. I thought it was really good writing. In the writing, there was this idea of system bias. You have this quote you're writing. It says, here are some examples: the team is spending six months to improve performance by 10% when it was completely fine to begin with, or the team is trying desperately to force their tooling on clients who don't need it.

[[49:49](https://youtu.be/3XkmNSuHFmY?t=2989)] Or the team is riding their outdated system to the grave like the captain going down on the Titanic. I've definitely seen examples of all those types of things in industry. And so, yeah, I think it was in the context of your writing about what you should orient your team around. Not systems, but actually missions. And maybe that's a way to fight system bias.

**James:**

[[50:20](https://youtu.be/3XkmNSuHFmY?t=3020)] Yeah, I mean, one of my jobs at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) wasn't the most fun job, but it might have been one of the most impactful jobs. It was shutting down projects. You know, looking around and being like, huh, that thing over there that has had 60 people working on it for two years doesn't seem to make a lot of sense to me. And then I, you know, it wasn't a hostile thing, but I'd go and chat with a team and I'd say, hey, what are you all doing?

Do you believe in what you're doing? Does this make sense? And the team in private would say, I don't really know. But inertia is so strong. You know, this whole desire to not get in trouble, to just keep doing what you were previously doing is so strong, and talented people can end up doing things that don't make a lot of sense. One of the things I said in that article is it's kind of a cheesy story, but when we started building the storage system at [Dropbox](https://en.wikipedia.org/wiki/Dropbox), the team was called the Magic Pocket Team because that was a silly code name for the system we built.

[[51:17](https://youtu.be/3XkmNSuHFmY?t=3077)] The team was oriented around building that system, but as soon as we shipped it, I renamed the team to the Storage team. That actually took a bit of work because you had to rename all the email addresses, the channels, the repos, and the things. It seems like a waste of time. But my argument to the team was that the responsibility of the storage team is not to advocate for Magic Pocket, the storage system. It's to solve the needs of storage for the organization. Because who else in the company knows more about storage than the storage team? If there was a point in time where S3 was a better idea, it would make sense to move back. Or maybe there was a different kind of storage system that meant to use. Right. It's the job of the storage team to advocate for moving back. Right. And so I've seen this before.

[[52:12](https://youtu.be/3XkmNSuHFmY?t=3132)] You have a team called the Puppet team. People don't really use Puppet that much anymore, but for the job manager, Puppet versus Chef. They'd be kind of advocating for their team's thing when really a team should be oriented around what problem they solve. They should not care about the system that survives. Because if you are on the Magic Pocket team and someone says we should move back to S3, that's pretty threatening to your identity and your career.

[[52:44](https://youtu.be/3XkmNSuHFmY?t=3164)] But if you're on the storage team and it turns out it makes sense to move back, I don't think that's the case. But then that's an exciting new product for you to own. I think it seems like such silly management philosophy, but I think it's really, really important to orient a team and an identity around solving a problem and not owning and defending a system. You just see this in big companies. Inertia is so strong.

[[53:07](https://youtu.be/3XkmNSuHFmY?t=3187)] Inertia is so strong.

**Ryan:**

[[53:10](https://youtu.be/3XkmNSuHFmY?t=3190)] Yeah.

**James:**

[[53:10](https://youtu.be/3XkmNSuHFmY?t=3190)] And you see people doing things they don't believe in because that's just what they do.

**Ryan:**

[[53:14](https://youtu.be/3XkmNSuHFmY?t=3194)] If inertia is so strong, how did you fight it and close down all those projects?

**James:**

[[53:20](https://youtu.be/3XkmNSuHFmY?t=3200)] I think I got lucky insofar as I was there pretty early on and I worked hard enough. I was putting in probably 16-hour days at the start. I'm not advocating for that, but I was dedicating my life to the company, and I think it became pretty obvious to people that I cared. This is a guy over here that really wants to do the right thing and cares about the company.

[[53:42](https://youtu.be/3XkmNSuHFmY?t=3222)] At that point, you build up enough confidence, capital, that you feel comfortable saying things. I wasn't afraid for my career; I was afraid of the wrong decisions getting made. So I felt psychologically comfortable making observations. Then at a certain point, there were a lot of engineers. I would mentor many of the staff plus engineers at the company.

[[54:16](https://youtu.be/3XkmNSuHFmY?t=3256)] And people would sometimes get grumpy because they were like, "Oh, we're not doing the right thing over here," or "This is inefficient." Every engineer listening to this has a story like this. They're annoyed about some inefficiency at the company. My response was generally, "Do you think we should solve this problem right now? Because if we should, let me know the team to take some engineers off and the product to shut down, and I can redirect resources, and we could solve this problem right now."

[[54:42](https://youtu.be/3XkmNSuHFmY?t=3282)] And they'd be like, oh, well, we shouldn't shut down any other stuff. I'm like, cool, well we just have this many engineers right now. If there's anything higher or lower priority, let's stop doing the lower priority thing and do the higher priority thing. This thing. Oftentimes the answer was, oh no, nothing else is lower priority. Then the answer is we just have to accept. Just have to accept, right?

[[55:06](https://youtu.be/3XkmNSuHFmY?t=3306)] There's no point in being angry or upset that we're not doing the right thing all the time. I think there's a dimension to "you break it, you bought it." I don't think, when I said part of my job was shutting products down, it was just going around causing problems. Ideally, it's about solving problems, like, "Oh, this product is not going in the right direction, let's redirect it and do this alternative thing."

[[55:28](https://youtu.be/3XkmNSuHFmY?t=3328)] And so I think the thing that helped me, I guess, was having a sense of ownership that instead of complaining, I just wanted to go fix problems. That was part of the culture. I mean, when I started at [Dropbox](https://en.wikipedia.org/wiki/Dropbox), the infrastructure team was, I don't know, seven, eight, nine people. We'd have someone join from Google, for example, and they'd say, "Well, someone should go build." I can't do anything without this logging framework. I couldn't possibly do anything with this logging framework. I'm like, "Well, we're going okay without it." And then someone needs to build this thing. Everyone would be like, "Well, who is someone?" Right? Because it's just us. It's just us. We build it or we don't build it. They'd pretty quickly come to understand, "Oh wait, it's just us."

[[56:17](https://youtu.be/3XkmNSuHFmY?t=3377)] There's no other idiots out there. We're the idiots, right? So that was, I don't know, I loved that time because it was just a time of accountability. Life gets easier and harder when you realize that everyone else is not an idiot. When you realize that everyone else is just dealing with their own stuff, right? I do not think someone will have good luck going around complaining about stuff and just saying this is a dumb idea and being negative.

[[56:50](https://youtu.be/3XkmNSuHFmY?t=3410)] I think people will have—everyone wants problems solved, though. So if you're someone in an organization who is willing to put their head up and say, "You know what, I think this thing over here is a bad idea, but here's a different idea, and I'm willing to own it and put the effort behind it," I think that's a recipe for success.

**Ryan:**

[[57:11](https://youtu.be/3XkmNSuHFmY?t=3431)] From that article, you had a great quote or a great question to think through this. It said you went to everyone or a bunch of people, and you would say, if we could be spending these resources working on any project at the company right now, would this still be the best use of time? I feel like it frames exactly what you just described really cleanly.

**James:**

[[57:32](https://youtu.be/3XkmNSuHFmY?t=3452)] Yeah, I mean, I guess this is like maybe a trick for being a tech lead or a manager. Nothing's a yes or no question. It's a prioritization question. It's not like, should we redesign the database? I don't know, maybe, I guess. Is it the most important thing to do right now? No. Cool, let's not do it. I think it's much easier to have those conversations than to think about it as a yes or no.

[[57:54](https://youtu.be/3XkmNSuHFmY?t=3474)] I often hear, "Oh, my VP won't let me do blah." Okay, well, it could be that your VP is uninformed, but it's probably not. It could be your VP has a different set of priorities. Maybe their VP knows that you need to ship these features, and if you don't, then the company is going to struggle. I don't know. But to really frame it around prioritization, the way I think about the career ladder for engineers is that some people—maybe it's not common—think that becoming a senior engineer means you get better at programming.

[[58:27](https://youtu.be/3XkmNSuHFmY?t=3507)] But I don't know, I think my programming abilities went down from level four onwards. I think once I got to level four, that was peak programmer for me. Then I probably went downhill from there, and I got wiser, whatever. But I think the real thing that happened is the scope that I cared about increased. At a certain point, you're just thinking about what matters most at the company for the next five years.

[[58:52](https://youtu.be/3XkmNSuHFmY?t=3532)] And I don't think a junior engineer in their first year on the job should try to do this because you probably don't yet have the wisdom, insight, or knowledge to make a good assessment. I think it would be a mistake to try to come up with redirecting company strategy. But as you grow, the real key part about growing is that the IC 6, 7, and 8 engineers are not necessarily the best programmers. They're just getting better at having a broad perspective in decisions within a company.

[[59:22](https://youtu.be/3XkmNSuHFmY?t=3562)] They're just getting better at having a broad perspective in decisions within a company.

### 1:00:15 — Doing the right thing vs promo hypothetical

**Ryan:**

[[1:00:15](https://youtu.be/3XkmNSuHFmY?t=3615)] You mentioned this idea of doing the right thing and then, you know, the byproduct, you also get promoted. I think that's the dream, you know, do the right thing, get promoted.

[[1:00:25](https://youtu.be/3XkmNSuHFmY?t=3625)] But in reality, oftentimes people would have to make the trade-off. Imagine a two-by-two matrix of doing the right thing, doing the wrong thing, getting promoted, and not getting promoted. Obviously, do the right thing, get promoted—great. Do the wrong thing, don't get promoted—obviously bad. But I'm curious about the other two quadrants. Which one would you have picked when you were earlier in your career?

[[1:00:50](https://youtu.be/3XkmNSuHFmY?t=3650)] Let's say I came to you, I said, hey, you can do the wrong thing, but you're going to get promoted, or you can do the right thing and I guarantee you're not going to get promoted. Which one?

**James:**

[[1:01:00](https://youtu.be/3XkmNSuHFmY?t=3660)] Absolutely the second one. I'm going to say a really tacky thing, right? There are a set of engineers who at a certain point just make infinity money. The amount of money they can make, you know, going to work at [Anthropic](https://en.wikipedia.org/wiki/Anthropic) is a huge amount of money. Right? And so there's a certain point where it just doesn't matter anymore. The money is whatever. But if you really want to maximize long-term income, I don't think you should try to do that.

[[1:01:31](https://youtu.be/3XkmNSuHFmY?t=3691)] But if you wanted to maximize long-term income, if you get to a certain level of experience, skill, and seniority, you've made it. That's it, you're done; the money's fine. I think there's this desire among junior engineers early in their careers to be kind of over-optimizing for promotion, income, and salary, etc., as opposed to investing in themselves.

[[1:01:59](https://youtu.be/3XkmNSuHFmY?t=3719)] They probably don't want to hear me say this because it's easier for me as an old guy to say this, right? But I think, for the longest time at [Dropbox](https://en.wikipedia.org/wiki/Dropbox), there was a time at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) where we just didn't have our level system. I was tech leading the team and I was making the least amount of money on the team because I was at some point a technical manager. I saw everyone's salary, so I was making the least money, but whatever, right?

[[1:02:20](https://youtu.be/3XkmNSuHFmY?t=3740)] It all worked out in the end, right? Now that was a happy story. But I do really think I benefited so much from working with the best people. If you have two choices—making 20% more money now or working with the best people in the world—just be around the best people because that's going to set you on the ship to success. Now, not everyone wants to do that. Not everyone wants to go on that. There's no shame in just wanting to have a regular job and just be chilling and getting paid. Fine, there's nothing wrong with that. But if you do want to maximize your career growth, then the way to maximize that is to maximize your skills. Hopefully, you're not so cynical to think that there is no correlation between talent and compensation.

[[1:02:49](https://youtu.be/3XkmNSuHFmY?t=3769)] Not everyone wants to go on that. There's no shame in just wanting to have a regular job and just be chilling and getting paid. Fine, there's nothing wrong with that. But if you do want to maximize your career growth, then the way to maximize that is to maximize your skills. Hopefully, you're not so cynical to think that there is no correlation between talent and compensation. I don't. If you think that's the case, okay, I don't know what to say, but there is a correlation between talent and compensation and growth. So my advice to people early in their career is to land at the best company with the best people doing the most important problems. Your life will be great because we are so lucky as engineers. Where else can you work solving problems for a job, solving puzzles for a job, and getting paid so well? Engineers get paid so well compared to most jobs.

[[1:03:53](https://youtu.be/3XkmNSuHFmY?t=3833)] The privilege, the real privilege that we get is to work on something cool. And that's what I advocate for.

**Ryan:**

[[1:04:02](https://youtu.be/3XkmNSuHFmY?t=3842)] I love the idea you mentioned earlier. That's kind of counter to the common opinion I often hear. The common opinion I hear is that someone working at a big company is in this machine, and it's kind of defeatist. They're going, "I ship this thing, but I hate this" or "I don't believe in this." I really liked your perspective on doing the right thing and basically giving a damn that someone outside of you is doing the right thing too and expanding your sense of ownership.

[[1:04:35](https://youtu.be/3XkmNSuHFmY?t=3875)] And I want to know what is your motivation for that? Because there are so many other people who are faced with the same inputs, and they come to a very different conclusion. So what motivates you to actually do the right thing when the machine doesn't necessarily incentivize you to do so?

**James:**

[[1:04:51](https://youtu.be/3XkmNSuHFmY?t=3891)] Yeah, well, I think the machine does incentivize you to do so, but I don't think it's visible immediately. I think people who do less job hopping really do grow the most. Because I would say very strongly, if you're not in a job for three years, you're not going to see whether your decisions were good. You can get more money as a junior engineer, but you cannot become a very talented senior engineer without being around for long enough to own the consequences of your decisions.

[[1:05:23](https://youtu.be/3XkmNSuHFmY?t=3923)] It's like playing a basketball game and leaving before the game's over. You're just not learning. I do think there's an actual structural incentive towards staying in a job now. If you're in a bad job, leave the bad job. Right? But there's a structural incentive to be able to stay long enough to have an impact. But also, I don't know, I guess it's easy for me to say. I joined the tech industry when it wasn't a very lucrative field.

[[1:05:50](https://youtu.be/3XkmNSuHFmY?t=3950)] It wasn't like it is now, but I just like it. The reason I left academia was because I wasn't confident I was making the right decision. So what would happen, how I was in academia—I'm not saying everyone was like this, but you don't know what to do. So you have to make up a problem to solve. You make up a problem, and then you make up a solution, hopefully a good one.

[[1:06:18](https://youtu.be/3XkmNSuHFmY?t=3978)] And then you write a paper where you try to convince everyone that it was a really good idea. I hated it because I didn't want to convince people. I just wanted to build it and see if it was good. I just wanted to build it and ship it and see; I didn't want to play pretend and argue about whether it was good. That's what makes me feel good. I don't know. Obviously, if you're an engineer who's living paycheck to paycheck, you should maybe ignore what I'm saying.

[[1:06:50](https://youtu.be/3XkmNSuHFmY?t=4010)] I don't want to come across as unempathetic to anyone who's really struggling financially. But if you are not struggling financially, the best thing you can do for your quality of life is to enjoy what you do every day. I don't know, you could have a fancier car or you could enjoy what you do every day. I love cars. I'm a motorhead. But I promise that enjoying what you do every day is going to have a much bigger impact on your life.

[[1:07:22](https://youtu.be/3XkmNSuHFmY?t=4042)] Personally, I don't enjoy going to work and working on products that I believe in. Jamie, my co-founder, is the same way. We really get along well in this respect. We can only put up with doing things we actually care about and believe in. I think that's the luxury—it's more luxury than taking a first-class flight.

[[1:07:49](https://youtu.be/3XkmNSuHFmY?t=4069)] That's more luxury than going to a three-million-star restaurant. The luxury is you don't get up and have to do a terrible job. You get up and go to a place where you like your coworkers, and you solve cool problems, and you go home and feel proud of yourself. If you can construct your career that way—and it's not easy, it requires very active effort—then you're going to have a good life.

### 1:08:13 — Why he dipped into management sometimes

**Ryan:**

[[1:08:13](https://youtu.be/3XkmNSuHFmY?t=4093)] I saw in your career journey it said that you're an occasional manager, and you seem like someone who really enjoys the technical aspects of things. So how did you decide to occasionally dip into management?

**James:**

[[1:08:27](https://youtu.be/3XkmNSuHFmY?t=4107)] I feel like most people should not want to be managers, and I sometimes think it's a bit of a red flag if someone wants to be a manager too much. Right. Because being a manager is a hard job. I think most people should go into management because they need to, because it's necessary. What happened every time I went into management—I'm in a management role now as well—was because you have to.

[[1:08:50](https://youtu.be/3XkmNSuHFmY?t=4130)] Right. But someone needed to manage the team, and so I do genuinely enjoy accountability. I like responsibility; I like having weight on my shoulders, I suppose. I went into management several times, but as soon as I had the opportunity to get out, as soon as someone else would come in and manage the team, I would bounce out of that role back into engineering. Now, going into management is tremendously educational.

[[1:09:22](https://youtu.be/3XkmNSuHFmY?t=4162)] Being a manager really lets you see the world in a different way. You realize companies are more complicated than you thought. You realize the engineers are more complicated than you thought. You realize everyone on the team is going through something, and you realize, oh wow, now I understand why that thing happened. So being a manager is very educational. One thing I would say, I would strongly caution people against is going into management too early.

[[1:09:44](https://youtu.be/3XkmNSuHFmY?t=4184)] In their career. I see this happen a lot with well-intentioned people who want to push others into management as a means of career advancement. I think it's doing people a disservice. You should let folks take their time in an organization, in a career journey. I don't think you should be going into management under most circumstances in the first three years of your career.

[[1:10:08](https://youtu.be/3XkmNSuHFmY?t=4208)] I think you should ideally get to staff engineer before you do that. That's not going to happen for everybody. But ideally, you take the time because if you go into management before you're an excellent technician, it will limit your ability to influence strategy later in your career.

**Ryan:**

[[1:10:24](https://youtu.be/3XkmNSuHFmY?t=4224)] How does that play out?

**James:**

[[1:10:25](https://youtu.be/3XkmNSuHFmY?t=4225)] It plays out with people who are stuck or have roles as people managers where they see their job as making a team happy or maybe coordinating a team or dealing with all the day-to-day challenges of people on a team. But they're not organizational leaders. They're not pushing the team towards excellence. They're not asking, "How can we reframe what this team is about? How can we help influence technical strategy?"

[[1:10:59](https://youtu.be/3XkmNSuHFmY?t=4259)] And again, people management is a fine job. But I think the best companies are ones where all the managers are very technical, so they're able to make sure the company's doing well at a certain point. If you're not a particularly technical manager, you're not going to be able to evaluate the work of your team. You're not going to know whether your team is even doing well. I guess maybe you might contribute to some of the stuff you were saying about cynical organizational attitudes where my manager doesn't understand me.

[[1:11:29](https://youtu.be/3XkmNSuHFmY?t=4289)] Maybe your manager doesn't understand you if they haven't spent enough time developing technical skills and struggling.

### 1:11:36 — Why you shouldn't lead by example

**Ryan:**

[[1:11:36](https://youtu.be/3XkmNSuHFmY?t=4296)] Yeah, there's another piece that you wrote I thought was really good about leading by example, and you actually say it's bad to lead by example. But there's a quote in there that says modern tech workers can be an anti-authoritarian bunch at the best of times. Let's say you're a tech lead or manager. How do you strike that balance so you don't lose credibility as a tech lead?

**James:**

[[1:12:03](https://youtu.be/3XkmNSuHFmY?t=4323)] Yeah, there are command and control companies where the manager just tells people to do things, and they just do them. Those typically are not excellent companies, and not every company needs to be excellent. But if you want to have a company where your team is really innovating, where the engineers feel very personally responsible for making high-quality decisions, you have to have them believe in what you're doing.

[[1:12:30](https://youtu.be/3XkmNSuHFmY?t=4350)] And so, at [Convex](https://www.convex.dev/), I'm the founder and CTO. I can't really go to someone's desk and say, "Do this thing." Now, they might do it just because they like me. There's a good chance they would do it, but not because I'm the boss. They'd be like, "Well, why?" And that's because that's our culture. We don't just do things because we're told. If I want someone to do something, I'll spend time with the team talking about why we're doing it, where the market's trending, where the gap in our product, what, you know.

[[1:12:57](https://youtu.be/3XkmNSuHFmY?t=4377)] And then once we've really well articulated why something matters, people are just going to do it anyway. Sometimes you have to have hard conversations, but I think about it in terms of conflict in an organization. There's this kind of hierarchy of the values you have and then why, what, and how. Engineers are very often debating the how. They're often debating what algorithm we should use for this and whether we should use this container service or that container service. These are kind of like the implementation details. Most times when I see organizational conflict, it's because well-intentioned people are debating as best they can about how to do something, but they don't agree on why we're doing it. If one team thinks the most important thing we can do right now is get more features out to expand our customer base, and the other team thinks the most important thing we can do is increase reliability because there's a risk to the business.

[[1:13:24](https://youtu.be/3XkmNSuHFmY?t=4404)] And should we use this container service or that container service? These are kind of like the implementation details. Most times when I see organizational conflict, it's because well-intentioned people are debating as best they can about how to do something, but they don't agree on why we're doing it. If one team thinks the most important thing we can do right now is get more features out to expand our customer base, and the other team thinks the most important thing we can do is increase reliability because there's a risk to the business, they're both very valid perspectives. However, it's going to lead to them doing very different things. Within an organization, I'm a strong believer that everyone needs to have 100% alignment on why. The stuff we argue about or debate or talk about ad nauseam is why. Largely, I just trust the team to do the right thing. I think that's the case for any tech lead. If you want to have credibility on a team, if you think that you can just tell someone to do something and they'll listen to you because you're the senior guy, no, they won't.

[[1:13:54](https://youtu.be/3XkmNSuHFmY?t=4434)] They're both very valid perspectives, but it's going to lead to them doing very different things. Within an organization, I'm a strong believer that everyone needs to have 100% alignment on why. The stuff we argue about or debate or talk about ad nauseam is why. Then largely, I just trust the team to do the right thing. I think that's the case for any tech lead. If you want to have credibility on a team, if you think that you can just tell someone to do something and they'll listen to you because you're the senior guy, no, they won't. They won't listen to you. If they listen to me, it's because I've come in and explained it in a way that resonates with them. Again, one of my jobs at [Dropbox](https://en.wikipedia.org/wiki/Dropbox) was to resolve situations. Someone would say, "Oh, that team's an idiot; they won't do blah." Then I'd go talk to that team. That team was not an idiot. We talked through it, and they would decide to do the project. It wasn't because they were scared of me.

[[1:14:51](https://youtu.be/3XkmNSuHFmY?t=4491)] I hope they weren't. At least it was because I took the time to figure out what their motivations are. That's something you really have to learn. If you're a tech lead, you don't really have that much authority over people, and you have to encourage them and get them to believe in what you're doing. If you are leading through authority, you're not going to have a culture where good ideas arise from within the organization.

[[1:15:17](https://youtu.be/3XkmNSuHFmY?t=4517)] People are just going to do what they're told.

**Ryan:**

[[1:15:19](https://youtu.be/3XkmNSuHFmY?t=4519)] Influence without authority is huge. Even big companies like Meta technically don't have titles; everyone's just a software engineer. Is that also how [Convex](https://www.convex.dev/) is run?

**James:**

[[1:15:32](https://youtu.be/3XkmNSuHFmY?t=4532)] I mean, we're a very flat organization. There are people in tech lead roles. I don't completely buy that everyone's a software engineer thing. It's like, you know, [Anthropic](https://en.wikipedia.org/wiki/Anthropic). Everyone's a member of technical stuff because it's kind of like a wink-wink thing. You kind of know, it's like no one's mentioned the title, but you kind of know if the most senior person in the company comes to your desk, you're probably going to notice. I think there's no point in playing pretend. People know. But I will say that you should have an organizational culture where you don't do something just because a senior person says something. Now, I do think that reputation matters. I certainly think that if a very experienced person at a company comes and tries to explain something to you, you probably should listen to them because they probably have some wisdom.

[[1:16:03](https://youtu.be/3XkmNSuHFmY?t=4563)] People know. But I will say that you should have an organizational culture where you don't do something just because a senior person says something. Now, I do think that reputation matters. Like, I certainly think that if a very experienced person at a company comes and tries to explain something to you, you probably should listen to them because they probably have some wisdom. There might be something to be learned there. You should be open to it. But ultimately, even the most senior person, I don't think should be leading through authority. They should use the benefit of their experience to be able to articulate, to win the hearts and minds. And that's how your engineering culture is so important. And if you want a culture of ownership and innovation and drive and enthusiasm, and people trying to do the right thing, not get promoted, you have to have a culture where everyone believes in what they're doing, and no one's going to believe in what they're doing.

[[1:17:00](https://youtu.be/3XkmNSuHFmY?t=4620)] If the senior principal engineer comes to the desk and says, "I'm not going to tell you why, but you have to delete this database and do this other thing," that's not an empowering statement. What the empowering statement is, "Hey, let's spend some time together to talk about where this product's trending and how this is probably not going to work out and how there might be a different way we can solve this problem."

**Ryan:**

[[1:17:20](https://youtu.be/3XkmNSuHFmY?t=4640)] On the topic of tech leadership, in that article I mentioned, the title was "Don't Lead by Example." I think that might be confusing for people. Can you explain why you think you shouldn't lead by example?

**James:**

[[1:17:33](https://youtu.be/3XkmNSuHFmY?t=4653)] Yeah, leadership by example is a very passive thing to do. Engineers are passive people at the best of times. I think that's stereotypically a little bit part of that personality. The very concrete example is when I first started becoming an engineering leader, I was trying to lead by example. I wanted to demonstrate the behaviors I wanted everyone else to have. Very specifically, with regards to on-call and people getting paged, I wanted people to have high ownership. I wanted people to jump on issues as soon as they happened. So I would do it. I'd be the first one to respond to a page. I would always be writing up the reports. I would always be jumping on all the bugs and stuff, really falling over myself to show how I wanted people to be. But from their perspective, all they see is that the lead is just doing all these jobs, and they don't know. They're like, "Oh, maybe that's James's job," or "Maybe James knows how to do it, and I don't know how to do it."

[[1:18:37](https://youtu.be/3XkmNSuHFmY?t=4717)] Turns out I didn't know. I was just kind of figuring out, or maybe he likes doing those things. At a certain point, being a leader is about understanding human psychology. I don't think you can just act a certain way in front of people and wait for them to copy you. I think you should act with integrity and values, and actually have to sit down and teach people. Have to have conversations about what you believe. Have to point out when they're doing things wrong or right.

[[1:19:08](https://youtu.be/3XkmNSuHFmY?t=4748)] So the moral of the story is I had to stop doing everything and I had to make the team do it. It felt cruel at the time, but later on I realized what's happening is I'm delegating, and I'm creating accountability and ownership. And the team needs to experience the responsibility and the learning that comes with that.

**Ryan:**

[[1:19:25](https://youtu.be/3XkmNSuHFmY?t=4765)] I mean, it's a nice leadership mantra. I'm curious with your experience in both individual contributor and management roles, how do you actually sell this to your team? Like, if you're used to just being paged once in a while and your boss handling most of the on-call stuff, and now suddenly you're on call and you're being paged more than before, that might seem unjust.

**James:**

[[1:19:51](https://youtu.be/3XkmNSuHFmY?t=4791)] Yeah, so the framing is really important. It's not like I'm removing the load; I'm redistributing the load. The framing is that having high ownership and being on call, being able to make decisions on the fly about something that impacts customers. It's actually incredibly empowering. And so if you frame it as this is a great opportunity for you to have responsibility and ownership, and by the way, I'm going to be here to support you, I'm not leaving you to drown, then people often respond really well to that.

[[1:20:24](https://youtu.be/3XkmNSuHFmY?t=4824)] Right. It's more of a supportive role as a tech lead. I'm here to help you, answer your questions, if you're confused about something, reach out to me. But ultimately, you can make these decisions. It's empowering. And in general, I think people, especially high-performing engineers, crave responsibility and ownership. It's what makes them feel engaged. It's what makes them feel like they're growing. And so if you can frame it that way, people are going to respond well to it.

**Ryan:**

[[1:20:52](https://youtu.be/3XkmNSuHFmY?t=4852)] On the topic of leadership and helping people grow, one thing that you wrote was, "Try to hire good people and then just get out of their way." That's assuming the people are self-motivated and self-directed. But what about people who need more structure or guidance? How do you think about that?

[[1:21:11](https://youtu.be/3XkmNSuHFmY?t=4871)] That's a really good question. And I would say if someone needs a lot of structure and guidance and doesn't know how to self-direct, they probably aren't going to be able to grow into a senior engineer. And that's not a judgment. It's just, I think, an observation. Like, I'm trying to get people to be highly proactive, to have high ownership, to be self-directed. If someone doesn't have those ingredients, it's going to be harder for them to advance in their career.

**James:**

[[1:21:58](https://youtu.be/3XkmNSuHFmY?t=4918)] Now, there are still things you can do to help people. I mean, you can coach them, you can mentor them, you can give them feedback, you can put them on projects that let them grow in the direction that you want. But I think at a certain point, you need to have someone who has the drive, who has the motivation, who wants to go out and do things and figure out things for themselves. And if someone doesn't have that, it's not going to work out.


[TRANSCRIPT GAP: content after ~1:21:58 unavailable — the page content available to the fetch tool was truncated around 1:18. Missing sections: 1:23:23 How to mentor Senior Staff+ engineers; 1:27:30 Career advice for the AI era; 1:37:21 Why he started his own company; 1:46:05 The most technically challenging work of his career; 1:48:10 How he got involved in Silicon Valley; 1:52:16 Career regrets; 1:55:54 Top technical book recommendation; 1:56:36 Younger self & permanent underclass advice.]
