---
type: raw-transcript
slug: the-creator-of-kubernetes-on-building
title: "The Creator of Kubernetes On Building Kubernetes"
guest: "Brendan Burns"
date: 2026-03-23
url: https://www.developing.dev/p/the-creator-of-kubernetes-on-building
fetched: 2026-07-19
complete: true   # Full episode covered through sign-off. Note: text is detailed extraction with quotes, not fully verbatim (fetch model declined full verbatim reproduction).
---

# The Creator of Kubernetes On Building Kubernetes

**Episode Title:** The Creator of Kubernetes On Building Kubernetes

**Guest:** Brendan Burns (co-creator of Kubernetes, technical fellow/CVP at Microsoft)

**Publish Date:** March 23, 2026

---

## Host Introduction

This conversation features Brendan Burns, who co-created Kubernetes and currently serves as a technical fellow at Microsoft working on Azure infrastructure. The discussion covers his experience building Kubernetes at Google, securing organizational buy-in, and lessons learned throughout the project's evolution.

---

## Timestamps

- 00:00:37 — How he convinced Google leaders
- 00:09:26 — Building the MVP
- 00:11:43 — How he made time for Kubernetes
- 00:25:28 — Technical details on building Kubernetes
- 00:38:46 — Rallying the open source community
- 00:50:01 — Scaling Kubernetes up for AI training workloads
- 00:55:31 — Reflections on getting a PhD
- 01:00:22 — The inevitable trajectory of software is death
- 01:04:16 — Top book recommendations
- 01:05:22 — Advice for his younger self

---

## Transcript

### 00:00:37 — How he convinced Google leaders

**Ryan:**
Let's start with Kubernetes. I don't fully understand the business motivation. If I were your director and you came to me saying let's do this for everyone, what strategy would you present?

**Brendan:**
The hardest part was articulating the value. We framed it several ways. One connected to the MapReduce white paper—Google published it, but Hadoop became the open-source implementation. We argued that "if it doesn't run, if it's not something that people can run, we're not going to be in the driver's seat."

We also emphasized that "the demands of writing reliable software necessitate having systems that are sort of like autopilots for your application."

On open source, others questioned: wouldn't it be better if only available on our platform? Burns responded: "you can't win if you make it only on your platform" because "the majority of people are going to be not on your platform."

**Ryan:**
What about the competitive landscape at that time?

**Brendan:**
AWS dominated, GCP was emerging. The strategy involved "creating a brand new playing field where you are the thought leader, suddenly people are listening to you."

---

### 00:09:26 — Building the MVP

**Ryan:**
How long did the initial MVP take?

**Brendan:**
"I wrote it in, I don't know, a little under a week maybe, something like that...Four days. Five days."

The demo showed container deployment across machines, load balancing (showing different replicas with each request), basic health checking, and V1 to V2 upgrades.

---

### 00:11:43 — How he made time for Kubernetes

**Ryan:**
Many engineers think they can't pursue side projects. Do you have advice?

**Brendan:**
"I believe you can hide order 10% of your effort from your management." He elaborates: "you should always have something that is that nobody told you to do, but that you think is important."

He acknowledges trade-offs: "you're going to bet five times and the payout from one of them hitting is going to be way better than the grinding to get that exceeds every single time."

However, he's honest about sacrifice: "maybe not going to watch YouTube for a while, maybe not going to watch...sporting events for a while."

Burns found the project addictive: "I'm going to go till I'm falling asleep on my laptop" because "I enjoy that."

---

### 00:25:28 — Technical details on building Kubernetes

**Ryan:**
Which part was hardest to build?

**Brendan:**
"The hard part was the decision that we made early on that it was going to be a really loosely coupled system." This created excellent resiliency but made debugging difficult because "you've got 15 different processes that are all having to work together."

When issues arose, "you can see that the outcome wasn't achieved. But then you're like, okay, but what happened? And now I have to sift through a bunch of different logs."

**Ryan:**
I'd expect leader election to be challenging.

**Brendan:**
"We relied pretty exclusively on Etcd to do that for us." Etcd is "a RAFT based consensus system key value store," implementing a provably correct consensus algorithm that's "way easier to implement" than Paxos.

Burns pushed hard for "everyone gets to access the store through an API server." The benefit: "everybody gets to restart all the time and they just come up and they work."

This design choice proved consequential: "the whole system was just a lot easier to make stable." The tradeoff involved loose coupling making debugging harder.

**Ryan:**
This reminds me of Kubernetes being declarative rather than imperative.

**Brendan:**
"You have clarity about the way you want the world to work." With declarative approaches, "you actually write it down, you say, I'm trying to create a reliable website...you have that record."

---

### 00:38:46 — Rallying the open source community

**Ryan:**
How'd you secure buy-in from companies like Red Hat?

**Brendan:**
Early partners saw "undifferentiated heavy lifting" they'd build anyway. OpenShift needed orchestration, so contributing made sense: "we're going to get more value out of the collective than out of trying to do it ourselves."

He emphasized partnership: "you can come take a dependency on us, but also we'll give you a seat at the design table."

**Ryan:**
How did you prevent Google from dominating the roadmap?

**Brendan:**
"Giving it independence" was critical. First, "we created the Cloud Native Compute foundation...we donated all of Kubernetes" to it. Second, "we sat down in 2016 to write the governance rules."

The team agreed: "we didn't want any one company to be able to take control of the community." They built governance to be "Democratic...distributed ownership."

**Ryan:**
Did you literally write a constitution?

**Brendan:**
"That's literally what we wrote." This involved "a couple, three fairly intense meetings amongst six or seven of us." They examined other communities and "codified stuff that already existed" plus created "this steering committee that had never existed before."

---

### 00:50:01 — Scaling Kubernetes up for AI training workloads

**Ryan:**
OpenAI scaled Kubernetes to 7,500 nodes. How's the system adjusted for AI workloads?

**Brendan:**
"We couldn't really handle more than about 100 nodes" initially. Optimization focused on "APIs were pretty noisy and we needed to reduce the noise level."

"Etcd in particular actually could be the main bottleneck." However, an unexpected pattern emerged: "a lot of our users actually have much, much smaller clusters, but lots of them...hundreds or thousands of clusters."

This contrasted with the "physical data center" mindset where "you only want one because you don't want to have to set it up a bunch of times."

**Ryan:**
Is there an upper bound where Kubernetes breaks down?

**Brendan:**
"Everything else is basically horizontally scalable...It's the storage layer that is the bottleneck." Beyond that, "every time you increase by an order of magnitude what you thought was the main problem is going to become easy and then the problem moves somewhere else."

---

### 00:55:31 — Reflections on getting a PhD

**Ryan:**
Many say they don't recommend PhDs. What's your take?

**Brendan:**
Burns tells two stories. First: he met an undergrad classmate who'd done startups and reached identical career levels despite his PhD. "It probably doesn't matter one way or the other."

Second: "I had a lot of fun right? So I had a lot of fun doing a PhD in robotics, so that's worth it to me."

Additionally, his PhD developed skills: "I learned a lot about how to write and put my ideas forth in both written and presentation form...that benefited my ability to argue."

Teaching experience proved valuable: "having to explain stuff to students who didn't really know anything about computers...really helped me organize the initial parts of the Kubernetes project so that somebody could learn about Kubernetes."

**Ryan:**
What's your top question people ask?

**Brendan:**
"How do I know what I should learn?" His response: "I actually kind of don't care what you learn, I care that you're learning...find something that you're excited about and energized about."

---

### 01:00:22 — The inevitable trajectory of software is death

**Ryan:**
You wrote "the inevitable trajectory of software is death." How does that apply to Kubernetes?

**Brendan:**
"Don't stick with it past when it's dying. You should always be willing to throw away stuff."

He acknowledges reality: "the source code that I wrote has been rewritten a number of times over the 10 plus years history of the project."

What replaces systems? "Something coming along that achieves similar things, but easier with less complexity and more utility."

He imagines natural language interfaces: "if you could actually really get it to be an interface that worked 100% of the time, it's way easier to come in and say I would like a reliable web service than it is to say YAML, YAML, YAML."

Alternatively, systems become invisible: "It could be that people focus so much on the AI that they forget about the Kubernetes part. And I think that's happening already."

---

### 01:04:16 — Top book recommendations

**Brendan:**
Early career: "Design Patterns: Elements of Reusable Object-Oriented Software" by Gang of Four

As a leader: "Leadership on the Line" and "The Five Dysfunctions of a Team"

---

### 01:05:22 — Advice for his younger self

**Ryan:** Last question for you is if you could go back to yourself when you just graduated college and give yourself some advice, what would you say?

**Brendan:** "Keep better notes. I feel like there's a great MBA thesis or a great book in the whole Kubernetes Journey and Beyond."

The gap: "all of the partner discussions, all of the interpersonal stuff...I remember a lot of it, but I don't remember all of it." Better documentation of partner discussions and interpersonal dynamics would have been valuable.

**Ryan:** Right, well, you got all the code there. Maybe an LLM can parse it or something.

**Brendan:** Notes about partner interactions and relationship-building matter more than code documentation for capturing the full story.

**Ryan:** Well, thank you so much for your time, Brendan. I really appreciate it.

**Brendan:** Yeah, for sure.

---

TRANSCRIPT COMPLETE (LAST POINT REACHED: 01:06:21)
