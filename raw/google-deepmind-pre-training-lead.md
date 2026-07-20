---
type: raw-transcript
slug: google-deepmind-pre-training-lead
title: "Google DeepMind Pre-Training Lead: How To Get a Job at a Frontier Lab | Vlad Feinberg"
guest: "Vlad Feinberg"
date: 2026-06-15
url: https://www.developing.dev/p/google-deepmind-pre-training-lead
fetched: 2026-07-19
complete: true
---

# Google DeepMind Pre-Training Lead: How To Get a Job at a Frontier Lab | Vlad Feinberg

**Guest:** Vlad Feinberg  
**Host:** Ryan Peterman  
**Publish Date:** Jun 15, 2026

## Host's Intro

Vlad Feinberg is Google DeepMind's pre-training area lead and I asked him all about how to land a job at a frontier lab like Google DeepMind, Anthropic or OpenAI.

Check out the episode wherever you get your podcasts: YouTube, Spotify, Apple Podcasts.

## Timestamps

- 00:33 - Skills frontier labs need
- 08:45 - The difference between AI research and engineering
- 21:41 - Domains that matter for the frontier
- 30:50 - Marketing yourself to frontier labs
- 35:13 - Concrete steps engineers can take
- 38:29 - Overview of pre-training areas
- 47:23 - Jeff Dean spot bonus story
- 50:14 - Favorite Gemini war story
- 58:59 - Advice for his younger self

## Transcript

### 00:33 — Skills frontier labs need

**Ryan:**

[[00:33](https://youtu.be/cDyi91onoJ8?t=33)] You wrote this post that was titled "How to Land a Job at a Frontier Lab". What are the skills that are kind of in demand in Frontier Labs? Maybe we can talk about the shape of the work.

**Vlad:**

[[00:49](https://youtu.be/cDyi91onoJ8?t=49)] There's quite a range of different things that Frontier Labs require at this point. LLMs are artifacts that are connected to research and product in ways that machine learning really hasn't been as connected to before. And so it really touches on so many different things. The goal of my post was to propose just a couple tangible directions in which labs could require a certain set of skills, not to be fully exhaustive.

[[01:24](https://youtu.be/cDyi91onoJ8?t=84)] And really the ones that I dive into have to do with kernel development and low-level engineering to improve the runtime for these LLMs in practice. And so that was a particular skill that I see voracious demand for across all the different Frontier Labs and among different projects within the labs. So that seemed like a very sharp one to call out as an overall need. And so specifically, whenever we're doing a research project that involves changing the architecture for the neural net in a particular way, or rethinking how we might do serving to do better KV caching or something like that, again, across the stack, you just need to be able to implement these new techniques in efficient ways.

[[02:21](https://youtu.be/cDyi91onoJ8?t=141)] And the inner loop of all these different changes is creating software artifacts that can function at large scales with high throughput, low latency. And this is just fundamental work that's tied to classical backend engineering thinking. So yeah, it seemed like a very open thing for people to specialize in.

**Ryan:**

[[02:46](https://youtu.be/cDyi91onoJ8?t=166)] My friends that work at OpenAI and Anthropic have told me, there's a distinction between an applied org and the research org, and I was wondering if Google DeepMind has a similar distinction and if you could speak about what that difference is.

**Vlad:**

[[03:03](https://youtu.be/cDyi91onoJ8?t=183)] So we have different focus areas and, for instance, within Google DeepMind, there's a team that focuses on how we can use our Gemini LLMs to better inform Search results. And so that might be in some way an applied version of the LLMs. But I am hesitant to make a very sharp distinction here because there's so much actual hard research that has to go into this kind of level of product integration. Specifically, for the one I mentioned, quite a lot of work goes into making sure that these LLMs are factual and can cite sources to have very precise, grounded answers.

[[03:53](https://youtu.be/cDyi91onoJ8?t=233)] Assessing the quality of these sources to make sure that you're not referring to anything that's sarcastic or a joke. This is, I guess, a good example of how even in product-specific applied AI verticals, you're still doing research. That being said, there's definitely what I would say is very classical LLM research teams, pre-training, post-training. These are things that are still standalone teams inside of Google DeepMind that are focused on what I would say is creating SOTA models.

[[04:30](https://youtu.be/cDyi91onoJ8?t=270)] Pure research. Again, the caveat is the pure research that we do. The extent that it matters is the extent to which we can realize it. And so we're just as responsible with delivering these models and making sure they train stably and actually being like the SREs of sorts for the training run to make sure that the model training is going smoothly as we are for coming up with the recipes to make these LLMs.

[[04:59](https://youtu.be/cDyi91onoJ8?t=299)] And you can't separate those two roles. It's really crucial to wear both of those hats. So yeah, I think you can draw up a spectrum between research and applied. But no matter what, in today's world, I think everyone needs to be fluid across that spectrum.

**Ryan:**

[[05:19](https://youtu.be/cDyi91onoJ8?t=319)] I noticed there's also another spectrum of software engineer to pure AI researcher. And how do you think of that spectrum? Software engineering versus AI researcher roles.

**Vlad:**

[[05:31](https://youtu.be/cDyi91onoJ8?t=331)] So I guess in my case specifically, I think a lot of what we do and a lot of the new techniques that we develop, the groundwork is laid in infrastructure investment. So I can walk through what my team does a little bit more detail later. But one of the verticals is distillation. And in order to do distillation, it's some way of transferring the knowledge or some form of statistics about the underlying dataset through a teacher model into the student model to make the student model better than if it hadn't ever seen these auxiliary statistics from the teacher.

[[06:21](https://youtu.be/cDyi91onoJ8?t=381)] When you're talking about statistics derived from a massive LLM applied to trillions and trillions of tokens, you're talking about a level of FLOPs investment that is millions and millions of dollars. And that in turn means that you have to be able to think through how do you optimize the system to be as efficient as possible? Because every operation that we're performing is multiplied by such a large factor that every second counts, every byte of storage counts.

[[07:00](https://youtu.be/cDyi91onoJ8?t=420)] And quite a bit of that work is good old-fashioned software engineering. In particular, the infrastructure for distillation has evolved through maybe three to four generations. At this point in each one, we've taken a step back, looked at what kind of research methods we've been applying for distillation, holistically thought about how do we broaden what the infrastructure is capable of. And there's definitely a couple discrete points where rethinking the system design of how we perform distillation enables us to do research on distillation methods much more quickly.

[[07:49](https://youtu.be/cDyi91onoJ8?t=469)] And so it's this kind of investment that, okay, this four-month or whatever rewrite of our distillation infrastructure then results in a dramatically new understanding of distillation scaling laws that translates to really strong models. So it really requires just work across the stack. And I can't imagine that we would have gotten results like Flash 3.0 without having made those distillation infrastructure investments that are at the end of the day things that started with a good old-fashioned design doc and thinking about what the right abstractions are for generating these teacher statistics, coming up with the right storage system for them, thinking through what could support the reading and writing across multiple different data centers at this scale.

[[08:42](https://youtu.be/cDyi91onoJ8?t=522)] Really classical distributed systems problems?

### 08:45 — The difference between AI research and engineering

**Ryan:**

[[08:45](https://youtu.be/cDyi91onoJ8?t=525)] Yeah, I mean it sounds like there's a lot of software engineering backend infra-type problems given just the scale of the compute at this point. It still feels like though at some point in that spectrum there's some crossover where there's these new skills. Like somewhere where if you had, you took an arbitrary backend engineer and you placed them to, I don't know, adjust the model architecture or something like that, is like a bit of a jump more than the infra work.

[[09:16](https://youtu.be/cDyi91onoJ8?t=556)] How do you see that distinction?

**Vlad:**

[[09:18](https://youtu.be/cDyi91onoJ8?t=558)] Yeah, so I think there is a crossover point in terms of doing research where research is an endeavor where the payoffs become a lot higher risk, higher reward. And we have this notion of kind of research taste, which is some high-level intuition about what path you should be proceeding through the DAG of the multiple different milestones that you need to accomplish in a particular project.

[[09:51](https://youtu.be/cDyi91onoJ8?t=591)] In some sense, we can view software engineering projects through a similar DAG, where you have all of these intermediate artifacts that you want to hit in a software program to get to the final result. But in the software engineering case, the DAG is more or less deterministic, where you build one service, then a different service, then a third service, and you figure out your storage infrastructure layer first, that kind of thing, and you can just make monotone progress.

[[10:19](https://youtu.be/cDyi91onoJ8?t=619)] But in the research case, you have to kind of explore this DAG, which is now stochastic, because some of the nodes, which might be some research ideas or some aspect of getting to a final goal, may or may not work out. And I think that requires a bit of a mindset shift. And that kind of mindset shift takes a while to learn, and it takes specialized skills to learn. This would be the kind of skills you pick up in a PhD, for instance.

[[10:49](https://youtu.be/cDyi91onoJ8?t=649)] One succinct way I could put it, there's a really excellent post by this professor Jacob Steinhardt, and I love to frame a lot of the research work that I do in this way. And it's research as an MDP. So MDP here. Markov decision process. Again, we have this high-level idea of a stochastic dependency graph between different milestones in a research project where you might need to have a certain kind of result or prove a certain kind of theorem before you get to a certain kind of conclusion.

[[11:24](https://youtu.be/cDyi91onoJ8?t=684)] Similarly, for a machine learning research project, you might need to have this and that featurization working before you can get this and that ImageNet accuracy or something like that, expanding those nodes in this graph. It's this stochastic endeavor where these approaches may or may not work out. And whether or not one works out opens up a set of new possibilities for you. The approach that you might have in the software engineering case, where you could fully write out, here are all the paths to the goal across walking this graph.

[[12:01](https://youtu.be/cDyi91onoJ8?t=721)] What's the shortest path to your goal? That approach is not optimal in the research case because if all of a sudden the transitions between the edges in this graph become unreliable, and some of the nodes you might not even be aware of, it might be a hidden MDP, then the way that you might approach this problem would really differ. And in particular, you have to factor in the success rate and the time investment that you're going to be putting into these different research ideas, as well as a priori estimating what those different rates are.

[[12:41](https://youtu.be/cDyi91onoJ8?t=761)] And that's a very different exercise than writing up what the design for your software engineering project might be. And it's this skill set of building an intuition of how likely an approach is to work out without having yet done that approach that I think people often correlate with this research taste notion, but that's exactly the one that you need to build up in order to properly traverse this MDP for the research projects and just generally the nature of the research work.

**Ryan:**

[[13:12](https://youtu.be/cDyi91onoJ8?t=792)] It sounds like you're saying that there's a lot more uncertainty. I'm still trying to get a sense of the nature of the work. If you threw this backend engineer into a team that's doing research, what are those concrete examples where they fall short?

**Vlad:**

[[13:34](https://youtu.be/cDyi91onoJ8?t=814)] I think the very first thing that comes to mind is having the right context for the research landscape in which you're operating. So quite a bit of research work involves almost this kind of. You have to take on this very humble viewpoint of there's been quite a lot of investment in related work in the past and until I know the sum total of humanity's bleeding edge in this topic, I'm definitely not going to be able to further that bleeding edge.

[[14:15](https://youtu.be/cDyi91onoJ8?t=855)] So building up a solid understanding of past work in a particular area and doing that related literature review is maybe the first thing that I would imagine people might stumble on: having read and having the skills to effectively traverse the historical citation tree for a particular topic. Because you don't have the time to read all of these different papers, you need to build up a sense of what are the high-value papers and what are the ways in which I can assess if a paper is worth reading without fully reading it.

[[14:52](https://youtu.be/cDyi91onoJ8?t=892)] That's the first thing that comes to mind as the skill that people need to build up. Even to be able to read these research-level papers. You have to have a background in machine learning and some computer science, and depending on the paper and depending on the domain, there might be all sorts of prerequisites in terms of the underlying math and coursework that you would want to have to properly understand.

[[15:21](https://youtu.be/cDyi91onoJ8?t=921)] So that's quite important to be able to have a deep understanding of what methodology is available, because you really won't have a lot of hope of improving upon the methodology if you don't understand what's there already. So I think I mentioned earlier, one of the things that my team works on is distillation. In order to advance our understanding in distillation for large language models, you have to have a good understanding of what we're trying to do with LLMs.

[[15:59](https://youtu.be/cDyi91onoJ8?t=959)] Just to give a cursory overview here, the name of the game for LLM research is, especially in pre-training, scaling laws. And so what are scaling laws? People focus a lot about this power law structure and the fact that you have this and that exponent, but what matters is less so the functional form. What matters is, for a given recipe of scaling up your LLM, as you invest more and more FLOPs into the pre-training run of an LLM, you have to be able to predict what the final test loss of this LLM is going to be.

[[16:39](https://youtu.be/cDyi91onoJ8?t=999)] And why do we care about this question? Why do we care about predicting what our generalization error is? In the classical machine learning world, say we're trying to win ImageNet, we have our test loss, which is our classification error for 1,000 different classes, and you run your VGG or your ResNet proposal to get that classification error. That's an estimate of how well that model does at classifying among those thousand classes, various different images.

[[17:15](https://youtu.be/cDyi91onoJ8?t=1035)] We can estimate how good our method is going to be by taking a validation set. And then whenever we have an architecture idea for a neural net, we just train it, and then we do a bunch of validation set runs, and we get a cross-validation error that is itself an estimator of our final test error. In this way, you can just iterate on different ideas through this process. But what's different in LLM world is every single time you go up for a pre-training run, you're about to put in more FLOPs into this run than you've ever done before.

[[17:45](https://youtu.be/cDyi91onoJ8?t=1065)] So it's in some sense like a one-shot version of this ImageNet problem. You never get to see the full ImageNet training dataset. You have to practice on MNIST and then CIFAR and then maybe based on those, you try to come up with a method that just works right off the bat on ImageNet. If you were to just do that by itself, as I'm sure many people have tried, certainly when I was learning how to do all of those different things, you get something, it works really great on MNIST, it maybe even works on CIFAR, and then all of a sudden it breaks on ImageNet.

[[18:16](https://youtu.be/cDyi91onoJ8?t=1096)] You'll find out that things don't just generalize easily across scale like this. And so much of what we do for LLMs is coming up with recipes, where a recipe is this function that goes from number of FLOPs you'd like to train on to a training routine for this LLM. And if you can couple this recipe with a prediction rule that can predict accurately what your LLM accuracy is going to be, then you're able to make decisions about how to improve your recipe because you can use that prediction.

[[18:49](https://youtu.be/cDyi91onoJ8?t=1129)] That is a ton of context on what LLM research looks like in general. But that's an understanding that we got to, that we even thought was feasible thanks to so much initial LLM scaling work that we've seen across the Kaplan paper, across Chinchilla. Since those two papers, there's been a lot more work in terms of what other factors are there beyond number of params and number of tokens that you train on that influence your prediction accuracy, like number of unique tokens, for instance.

[[19:28](https://youtu.be/cDyi91onoJ8?t=1168)] But I would say those two foundational papers for LLMs, those are informed by an even longer line of different scaling works going back to, say, the original GPTs. And then Google has had a ton of scaling work across its PaLM papers. This is just a set of works that have informed that viewpoint that I described earlier, that you kind of just need to build up by having gone through that literature review yourself.

**Ryan:**

[[20:01](https://youtu.be/cDyi91onoJ8?t=1201)] If you were, for instance, if you were trying to pick someone that was going on your team, and the way that you would judge their fitness to help you push the frontier is their understanding of the frontier, including the existing literature, which requires all these prerequisites. I think you called it mathematical maturity in your post.

**Vlad:**

[[20:23](https://youtu.be/cDyi91onoJ8?t=1223)] Yeah, so I think it's easy to read and understand those papers once you have mathematical maturity. So I guess the ones I mentioned in particular, nowadays they're table stakes, so I would expect candidates to be familiar with them. I think the general skill set is being able to dive into a paper of that level and then understand it, being able to take a research idea from a paper and implement it yourself. That's just a very important skill set to be able to have.

[[21:06](https://youtu.be/cDyi91onoJ8?t=1266)] We get all sorts of different ideas presented. They might not all directly apply to our domain, but if you can deeply understand them, then you can iterate on them and you can improve them inside our domain. And so when we assess people who can work with the mathematical concepts in these machine learning papers, that's, I guess, the key skill there. That would be evidence that you can go pick up this arbitrary paper and see to what extent these ideas carry over in the Google setting.

### 21:41 — Domains that matter for the frontier

**Ryan:**

[[21:41](https://youtu.be/cDyi91onoJ8?t=1301)] This probably won't be exhaustive, but I'd be curious to hear other domains that maybe people could dig into to see what kind of matters in frontier AI research. So you'd mentioned distillation. You also mentioned kernels. It sounds like kernels are helpful everywhere, but are there other areas that come to mind if you were just rattle off areas that are not necessarily exhaustive?

**Vlad:**

[[22:05](https://youtu.be/cDyi91onoJ8?t=1325)] One thing that I think is quite powerful is actually programming language research. So by looking into how we can create abstractions at the programming language level, we can facilitate kernel development. I think ThunderKittens is a really good example of this. Coming up with an abstraction that allows you to write kernels through four functions instead of arbitrary globs of C code allows you to move really quickly in developing algorithms that fully utilize hardware.

[[22:42](https://youtu.be/cDyi91onoJ8?t=1362)] At that point, it's not about the PL research itself, it's about having a passion for these kinds of programming language abstractions and working with low-level hardware people who are interested in and will try to work with CuTe DSL. This kind of thing, where there's a lot of hardware-specific domain-specific languages. One other thing that comes to mind besides PL and scaling law literature would be reinforcement learning literature.

[[23:17](https://youtu.be/cDyi91onoJ8?t=1397)] So in particular, ever since RLHF, I think we've seen that deep RL algorithms like PPO do have a place in production systems, and there was a time where that was in question. But now it's pretty unanimous that we see these kinds of algorithms applied to real production systems. And the theory behind that, you kind of have to start with the basics for reinforcement learning and work your way up to the myriad value-based methods and policy gradient methods that we have today.

[[24:00](https://youtu.be/cDyi91onoJ8?t=1440)] That's another domain that I think is just a very rich literature tree to crawl. And then for more of the backend engineer folks, beyond just the kernels themselves, there's I think a pretty fun overlap between distributed systems and optimization work, where figuring out how to design neural net training algorithms that allow for training across many GPUs. There's all sorts of fun challenges between asynchronicity, how up to date your gradients are, how pipelining affects the staleness.

[[24:43](https://youtu.be/cDyi91onoJ8?t=1483)] All of these system choices that you could make in your training algorithm design will impact convergence and the final quality of your neural net. And those are things that can be analyzed independently of the LLM setting and have been for a while, especially if you're more infra inclined, then having a good understanding of how those different algorithms work is a really good place to start.

**Ryan:**

[[25:09](https://youtu.be/cDyi91onoJ8?t=1509)] Do you see any difference between the demands of the different Frontier Lab? So, for instance, if someone wants to work at Google DeepMind, is there a particular area that you see Google DeepMind cares about more than Anthropic? For instance, I think in terms of the skill set, it's probably pretty similar.

**Vlad:**

[[25:24](https://youtu.be/cDyi91onoJ8?t=1524)] Yeah, I think there's maybe differences in business strategy and the set of offerings that's a function of the specialties of the labs and the kind of different customers that the labs could have. But I would say that there's quite a lot of overlap between the labs in terms of what people look for. And when I posted my post, you would see people from both OpenAI and Anthropic saying, yeah, we agree with this advice.

[[26:04](https://youtu.be/cDyi91onoJ8?t=1564)] And so I think that's just a little bit of evidence towards that.

**Ryan:**

[[26:09](https://youtu.be/cDyi91onoJ8?t=1569)] I think one reason for the huge demand for wanting to go closer to AI research is because people are thinking, oh, software engineering is not going to be as important in the future. Is there a similar thought when it comes to research where LLMs are also going to handle a lot of that work as well? So there's no reason to favor AI research versus software engineering.

**Vlad:**

[[26:34](https://youtu.be/cDyi91onoJ8?t=1594)] So I think the research skill set is going to become increasingly important. So I would say being able to handle stochastic components in the planning of your work is just going to be a larger and larger part of how we approach our jobs. Figuring out how to leverage AI in whatever thing you work on, which doesn't even have to be software related, is just an important muscle to start building right away because these components aren't deterministic.

[[27:09](https://youtu.be/cDyi91onoJ8?t=1629)] And thinking about how do I construct systems around these LLMs to do my job more effectively, that's going to be the thing that sets you apart in the future. And I think that's true no matter what you're going to be doing. Look, I think there's FUD everywhere, especially with some of the approach to marketing that some people have in terms of AI. It's FUD that is being intentionally leveraged. And so I feel like people should really just focus on themselves and trying to be more productive themselves.

[[27:42](https://youtu.be/cDyi91onoJ8?t=1662)] I don't think that AI is going to replace all of our roles. And so the reason for that is that one of the important aspects of what we do as humans in an organization, which is really this web of trust from this organization that is this pool of resources and this pool of people that manages these resources. One of the important things that we do is we allocate those resources towards certain goals.

[[28:15](https://youtu.be/cDyi91onoJ8?t=1695)] And even when we can accelerate our execution, there's an element of making decisions around how we allocate these resources that will always be something that needs to be attributable to a human making that decision. That's simply because you can't hand off blame to AI. So we at this point have LLMs that really deeply understand law, and they could review your contract for you or something like that, but they can't represent you in court because they can't be disbarred.

[[28:53](https://youtu.be/cDyi91onoJ8?t=1733)] And so that's, I think, a really sharp way that I might describe, okay, this is why the legal profession will go on, even though LLMs are really good at recalling precedent, is you want to have someone who is responsible, who can validate the output of AI to perform legal work more effectively for you rather than hand off your legal defense to an LLM.

**Ryan:**

[[29:25](https://youtu.be/cDyi91onoJ8?t=1765)] Yeah, I think the FUD was actually the original motivation for your post.

**Vlad:**

[[29:30](https://youtu.be/cDyi91onoJ8?t=1770)] Yeah, I really think that the mindset that people should have is a constructive one. And so there was a tweet that I saw, I think by Deedy, that was like some long-form fear mongering about AI permanent underclass or something like that. And it's easy to get stuck in that loop. But I think the important thing to think about is that we all have agency over our future and we can start investing in skills that matter for tomorrow, today.

[[30:09](https://youtu.be/cDyi91onoJ8?t=1809)] And that's really the only thing you should be doing, right? Worrying about it is not going to help you. And so part of why I wanted to write this post is in response to that, because it was something that I could see echoed. I gave a lecture at Princeton a while back, and a big question that came up is, how do I work at Google DeepMind? And it's something that just when people find out what I do, that's the top question people ask.

[[30:41](https://youtu.be/cDyi91onoJ8?t=1841)] I figured it would be helpful to add a little bit more constructive direction to the discourse here.

### 30:50 — Marketing yourself to frontier labs

**Ryan:**

[[30:50](https://youtu.be/cDyi91onoJ8?t=1850)] One last thing on the post because if you think about getting a role, there's obviously the skills, and we talked a lot about the skills and your fitness for the role, but there's also kind of the signaling for that role and what is kind of valued. If you were to be marketing yourself to one of these Frontier Labs, what signals matter most?

**Vlad:**

[[31:13](https://youtu.be/cDyi91onoJ8?t=1873)] Actual evidence that you've created something of use to other people along the line of kernels. Right. You can take any of the many open-source LLMs that we have and optimize them. You don't have to make them better. In every case, you could show that, oh, I have an improvement for this and that setting. It doesn't even have to be something that speeds up the model. On GPU, there's all sorts of open-source stacks like vLLM.

[[31:43](https://youtu.be/cDyi91onoJ8?t=1903)] There's a lot of other things that you can do besides accelerating the LLM inference on device. The serving stack that surrounds LLMs is a very sophisticated distributed system that has to maintain this KV cache memory and deal with all sorts of load balancing and request queuing and very common problems for backend servers. These projects are always looking for help. So contributions to vLLM or SGLang or demonstrations with TensorRT, they have, I think, a distributed system called Dynamo that allows for disaggregated serving where you could show that you made a project using these components, you improved these components.

[[32:34](https://youtu.be/cDyi91onoJ8?t=1954)] That would be an extremely positive signal for any candidate that I'm looking at and a very welcome contribution to open source, I think.

**Ryan:**

[[32:44](https://youtu.be/cDyi91onoJ8?t=1964)] Also, a lot of what we said is kind of assuming the path of external hire into Frontier Lab, but a lot of these Frontier Labs have large organizations that aren't necessarily doing the cutting-edge Frontier work. So let's say, yeah, for instance, I mean, Google DeepMind versus let's say there's some infrastructure eng that's working on Search and they have the backend skill set, maybe not as much domain context, and they try to internal transfer to Google DeepMind.

[[33:16](https://youtu.be/cDyi91onoJ8?t=1996)] Does any of your advice differ in that kind of case for an internal transfer versus someone who's coming from external?

**Vlad:**

[[33:23](https://youtu.be/cDyi91onoJ8?t=2003)] There's someone who I worked with closely on the search side who actually did transfer to my team, Nate Lintz, and he's amazing, and now he owns so much of what we do on my team in terms of inference, co-design for Flash and Flash-Lite. And I would say he's a really great example of this, where his approach was, how do I help my product area adopt this technology as effectively as possible?

[[34:00](https://youtu.be/cDyi91onoJ8?t=2040)] So I think there's definitely, if you're in an organization that isn't directly generating these models but in some way trying to leverage them, there's a very big gap in terms of applying these LLMs effectively, serving them effectively within your organization, and becoming someone who does that really effectively not only creates a ton of value in terms of the specific business need for your org, which will definitely elevate you in your org, but it'll also be the case that you're going to just naturally become the partner that we work with on the research side to make sure that our models are effective within your org.

[[34:51](https://youtu.be/cDyi91onoJ8?t=2091)] So at that point, you may or may not want to transfer. Definitely, if you transfer, we'd be happy to work with you. But at that point, I think you're already doing something that is cutting edge, which is integrating this new technology into a real product that people use. And so, yeah, that'd be my advice there.

### 35:13 — Concrete steps engineers can take

**Ryan:**

[[35:13](https://youtu.be/cDyi91onoJ8?t=2113)] Towards the end of this post, as we leave this topic, you had the concrete invitation because I know you were hiring. Do you want to say what that was?

**Vlad:**

[[35:23](https://youtu.be/cDyi91onoJ8?t=2123)] Yeah, so I was just trying to think of, how do I put my money where my mouth is? How do I demonstrate, look, this is a good way to show that you have at least some evidence of the skills that I called out as important: intent, mathematical maturity, grit. And so I listed out a couple of exercises that demonstrate some initial knowledge of scaling laws, some willingness to get into the weeds engineering-wise in terms of implementing a real transformer, and sort of willingness to pick up the kind of bread-and-butter math that we use every day to size these LLMs.

[[36:07](https://youtu.be/cDyi91onoJ8?t=2167)] And I won't recall the full list of the exercises that I expected here, but if you do the detailed handwritten version of The Scaling Book exercises and send me a video of yourself doing them, along with the transformer exercise on my post, then that's something. If you can work in the New York office, I would love to interview you. Quite a few people reached out to me about that. I actually already have had a couple submissions, and we're proceeding with the loop with those people.

[[36:41](https://youtu.be/cDyi91onoJ8?t=2201)] So yeah, it's quite a bit of work. But impressively, I got a response within, like, I think, a week of posting. So it's definitely doable. Yeah, I mean, I don't have unlimited headcount, so the offer's on the table, but I can only hire so many people. The good thing is, though, that is such a strong sign of self-development that not only is this something that you should be doing for its own sake regardless of whether or not you will get a job at Google DeepMind specifically, but I think it'll be something that lets you basically prepare for interviews in other places.

[[37:27](https://youtu.be/cDyi91onoJ8?t=2247)] Certainly, if you reach out to me with these exercises completed, even if I do all my hiring, there's tons of people who I know who are hiring as well, and I'd be happy to refer people as well.

### 38:29 — Overview of pre-training areas

**Ryan:**

[[38:29](https://youtu.be/cDyi91onoJ8?t=2309)] On the next topic, I saw you're the area lead for pre-training on Gemini, and I just thought it might be interesting to hear you give kind of a high-level overview of what pre-training is in your words and maybe what are the high-level challenges in the area.

[[38:45](https://youtu.be/cDyi91onoJ8?t=2325)] We can talk about that.

**Vlad:**

[[38:46](https://youtu.be/cDyi91onoJ8?t=2326)] Yeah, so there's quite a lot of work that we do in pre-training as an area lead for it. The specific things that my team is responsible for delivering include the Flash model, the Flash-Lite model. These are models that get used for AI Overviews and AI Mode in the search bar, as well as some other 1P models that are used by different orgs like ads and YouTube. Besides this, we're also key technical PoCs for the Google-Apple partnership, and so we do technical work there.

[[39:25](https://youtu.be/cDyi91onoJ8?t=2365)] Those are the actual product-level deliverables from my team. Beyond that, we do research to make sure that these deliverables are SOTA. And also we do general pre-training research that contributes to the pro series model as well. And the nature of the research I would say generally breaks down into three different verticals. There's distillation, which I mentioned earlier. There's what I like to call inference co-design.

[[39:58](https://youtu.be/cDyi91onoJ8?t=2398)] So creating neural architectures that are efficient to run inference on. So coming up with the network topology, the shapes of the matrices that the matmuls use inside of gating and linear layers for this transformer, as well as the attention shapes, num heads, that kind of thing. So that is effectively utilizing the hardware that you're serving on. And then the final pillar here is new quantization methods.

[[40:32](https://youtu.be/cDyi91onoJ8?t=2432)] And so quantization is just something that's been near and dear to my heart that I've been working on the research side for ever since I joined Google. And it really changes what's feasible for the first two. So that's why furthering the state of the art in terms of how you can compress models is also a very important pillar in the research that my team does. Generally, quantization refers to reducing in some sense the size that the neural nets take up in order to represent their weights.

[[41:11](https://youtu.be/cDyi91onoJ8?t=2471)] So typically, a neural net, when you're training, it is represented as a series of numbers that make up the matrices inside of the neural net that are stored in FP32, 32-bit floating-point weights. It turns out that when you do these computations, you don't need all of that extra precision to still maintain the quality of your neural net. And you can, with pretty simple methods, reduce the precision at which you store these weights down to four bits.

[[41:44](https://youtu.be/cDyi91onoJ8?t=2504)] So all of a sudden, this huge range of numbers that would take this FP32 to represent something that gets you down to seven digits of precision can, with somewhat high fidelity, still be represented well by 4-bit ints, which just cover this tiny range of minus 8 to 7. And it's kind of a miracle that you can do this. But what's even more of a miracle is that you can apply these kinds of quantization transforms to the runtime activations that the neural net processes.

[[42:27](https://youtu.be/cDyi91onoJ8?t=2547)] And as soon as you do that, the actual math that you're performing, because you're taking much smaller operands to your matmul than what you were doing before, the amount of electricity that it takes to compute the neural net drops significantly. And what's interesting is that 99% of the total cost of operation for AI hardware comes from the power that it takes to run these chips. If you can do these operations, you could just make neural nets run more cheaply, run more efficiently.

[[43:02](https://youtu.be/cDyi91onoJ8?t=2582)] That helps in terms of serving more requests and helps in terms of latency. So the name of the game for quant research is how do we push the frontier beyond this 4-bit range?

**Ryan:**

[[43:16](https://youtu.be/cDyi91onoJ8?t=2596)] There's this take that I see on Twitter all the time, which is just talking about MFU, and someone who's not in the space, or model FLOPs utilization, someone who's not in the space. They see a number in the low tens and they think, wow, they're wasting all of those GPU resources. I was curious if you could just clarify that for people why a low MFU, or I guess naively low, is actually not low at all.

[[43:42](https://youtu.be/cDyi91onoJ8?t=2622)] And maybe also explain what MFU is.

**Vlad:**

[[43:44](https://youtu.be/cDyi91onoJ8?t=2624)] Yeah, so when we compute MFU, you want to divide the actual number of FLOPs that the neural net is performing here by the total number of FLOPs that the accelerator could have done in the time of your request. And so in some sense, this is giving us the percent of time that we're usefully utilizing the FLOPs rate of the accelerator. And to get to 100% MFU, you would just need to be fully utilizing the matmul unit of whatever accelerator you're doing here.

[[44:20](https://youtu.be/cDyi91onoJ8?t=2660)] So it would just have to be doing a bunch of matmuls in a loop without reading any memory or doing any other operations. That's not a very useful computation in practice. Neural nets have to apply activation functions or do attention or write intermediate outputs back to HBM. And all of those different operations will require utilizing the memory bus or utilizing vector processing units. Or simply they might be mathematical operations that the underlying hardware performs more slowly than it might perform a matmul.

[[45:06](https://youtu.be/cDyi91onoJ8?t=2706)] And so all of those things contribute to not running at the full speed that the processor is rated at. That's why you might not see 100% MFU all the time, is because part of the time your neural net was reading and writing to memory, or part of the time it was doing an operation that fundamentally runs slower than certain other units on your device. I think quite a bit of this inference co-design work that I talked about earlier is across all of the different capabilities of the chip.

[[45:44](https://youtu.be/cDyi91onoJ8?t=2744)] So communication to other chips, memory bandwidth, the speed at which we can read parameters from memory, FLOPs, of course this can be matmul FLOPs, this could be FLOPs for processing vectors. So things like doing activations, all of these have different rates in the hardware, and a given computation isn't going to match the natural hardware's rate of each of those operations. So when you design a neural net, you want to be able to choose shapes for this neural net that fully saturate all of those hardware units to get you as high of an MFU as possible when you are doing inference here.

[[46:32](https://youtu.be/cDyi91onoJ8?t=2792)] What makes this more than just an algebra problem is that those choices translate to different quality outcomes when you actually train this neural net. The process of this kind of inference co-design is how do we come up with neural architectures that scale predictably, have a good prediction, so are high quality and still make the MFU as large as possible during inference. This kind of joint optimization is what makes inference co-design really fun.

[[47:06](https://youtu.be/cDyi91onoJ8?t=2826)] And also this kind of evergreen problem because as the hardware changes, all of those relative constants of FLOPs to memory bandwidth to communication bandwidth change. And those will have different implications for what the optimal neural net shape should be.

### 47:23 — Jeff Dean spot bonus story

**Ryan:**

[[47:23](https://youtu.be/cDyi91onoJ8?t=2843)] On another topic, Google has this idea of a spot bonus where someone can give you a one-off lump sum of money as a thank you for good performance. And I saw on your resume that Jeff Dean, the legend himself, gave you a spot bonus. And if you can tell that story, I'd love to hear. Why did he give you a spot bonus?

**Vlad:**

[[47:46](https://youtu.be/cDyi91onoJ8?t=2866)] Yeah, so that one actually was at the very beginning of the Gemini program. He gave out his spot bonus to people who hopped on and launched the first version of Bard. And I had a very small contribution to a very, very large project at the time. I helped with SFT for one of the first versions of supervised fine-tuning for one of the first versions of Bard that got released, like, right? The biggest lesson out of that experience was, at that time I was just doing pure research in Google Brain, and I was super focused on just how do I maximize the number of first-author papers at NeurIPS, ICML, ICLR.

[[48:38](https://youtu.be/cDyi91onoJ8?t=2918)] And I remember distinctly thinking, I had this instinct of like, oh, should I just keep my head down and try to write more papers? Luckily, at the time, my manager, Rohan Anil, really encouraged all of us to get involved in this space, and that was just the right motivation that I needed to roll up sleeves, do a bunch of hyperparameter tuning and engineering work to get this model running on some really old TPUs, to get some extra cycles in for SFT attempts.

[[49:25](https://youtu.be/cDyi91onoJ8?t=2965)] That very small initial engagement that was recognized by Jeff Dean, I think, blossomed into more and more investments on the LLM side by me and ultimately led me to where I am today. So, yeah, I would say it's less so about how much that SFT helped the initial release. And it's much more about recognizing that there's quite a bit of work, some of it not glamorous, some of it just hyperparameter tuning and golfing the XLA compiler to make your program fit in a certain memory amount that contributes to a wider business goal that is really quite important for getting involved in very high-value projects.

### 50:14 — Favorite Gemini war story

**Ryan:**

[[50:14](https://youtu.be/cDyi91onoJ8?t=3014)] You've been working on Gemini for a while now, and because it's a top priority, there have to be some incidents or war stories that you've been involved in. So I'm curious, what's your favorite war story when working on Gemini?

**Vlad:**

[[50:30](https://youtu.be/cDyi91onoJ8?t=3030)] So I think my all-time favorite would have to be Flash 2.0. So this one was quite a challenge and a very long journey to get there. But one of the main things that we were optimizing for, which Flash 1.5 established, is this category of very fast, low-latency model that's still quite good. And in particular it has to be fast because it's used by Search to serve responses in AI Mode very quickly.

[[51:25](https://youtu.be/cDyi91onoJ8?t=3085)] Because of that, for Flash 1, eventhough at the time we knew about MoE models and how they increase capacity. And so I think one thing that came up was, okay, we sure would like to use this new architecture, but it's difficult to just simply switch to an MoE. Because what happens with an MoE is it uses a lot more parameters in general. And because it uses more parameters, it takes up more HBM. These chips that we serve on have a finite amount of HBM.

[[51:55](https://youtu.be/cDyi91onoJ8?t=3115)] So you have to shard the MoE across multiple different chips. So if you have whatever N experts, then you might shard it across N chips or some factor of N. What this causes is a lot of communication in the middle of the model. When you have a token that needs to be routed to an expert, and that token might live on the first TPU, but it needs to go to the last TPU, that's a lot of communication that you're inducing in the forward pass.

[[52:26](https://youtu.be/cDyi91onoJ8?t=3146)] So the latency of this operation increases dramatically with N. And the challenge with MoEs is they increase N. So that kind of really bottlenecked this approach. And one interesting thing that happened was we definitely knew about pipeline serving for a while. It's just in the dense case, it never really ended up mattering. I distinctly remember a very early conversation I had with Sholto about it, and Sholto's like, oh yeah, you're so FLOP bound and so pipelining is just not gonna change your prefill profile.

[[53:07](https://youtu.be/cDyi91onoJ8?t=3187)] And then he was right. I tested it out and then abandoned the idea. But what's interesting is I had a very small team at the time. And one of my reports, Geng Yan, had a very nice idea. He was working with Rahul Arya and a couple folks from the Israel team at Google, and that was to apply pipeline prefill to MoE. Pipelining is a technique where instead of parallelizing those end-machine experts across those end machines, you parallelize layers across those end machines.

[[53:45](https://youtu.be/cDyi91onoJ8?t=3225)] So instead of on a particular layer, you have to route tokens from machine to machine. Now one layer does the computation for one subset of your pre-fill request and then hands off the processed tokens to the next machine to process the second layer, and then the third layer and the fourth layer. And all of the experts can then stay resident to a single machine or a smaller set of machines. So what this does effectively is it changes the communication pattern from something that required a lot of token exchange on every single layer to something that actually can be hidden behind other computation.

[[54:28](https://youtu.be/cDyi91onoJ8?t=3268)] Because you can do this pipeline pre-fill across different parts of your request. So while layer two is working on the first thousand tokens of your request, layer one on the first chip is processing the second thousand tokens of your request. So it was a way of breaking this HBM constraint by moving layers across the machines rather than moving experts across these machines. And because of that, the communication overhead has gone down, and all of a sudden MoE latency looks really attractive.

[[51:25](https://youtu.be/cDyi91onoJ8?t=3085)] Now, the Gemini 2.0 report says it's an MoE series of models, and the thing that made that possible is, or one of the things that made that possible, is this serving-time innovation. Dwarkesh and Reiner have an amazing post about exactly this optimization that you can write up in the algebra of The Scaling Book. And it's just a wonderful example of how this kind of change can have really dramatic implications on LLM quality.

[[55:41](https://youtu.be/cDyi91onoJ8?t=3341)] What really made Flash 2.0 rewarding is this giant MoE decision. It sounds like a small technical decision at the time, but people were really worried about whether or not the latency of this MoE would actually be reasonable. Luckily, I was able to run a very transparent technical process to get to the bottom of this. And by the end of it, we made the right call, but then we had to train it. This was a bigger model than we've ever trained before at the Flash scale, and we knew this would be the right call.

[[56:18](https://youtu.be/cDyi91onoJ8?t=3378)] But it was just going to be 40 days of grueling work for a really, really small team. We probably had five people on the rotation for training this model. I remember all of us just kind of rotated day by day, handing off all of this SRE-style work of keeping the training job alive, which at the time was a very interactive thing because you had to make sure that everything was moving stably, that you had tuned data iterators that aren't slowing down your job, that if there's a gap in the data somewhere or an indexing issue, you had to really quickly put up a fix because it's wasting all of this GPU time.

**Ryan:**

[[57:05](https://youtu.be/cDyi91onoJ8?t=3425)] What about at nighttime and on the weekends?

**Vlad:**

[[57:08](https://youtu.be/cDyi91onoJ8?t=3428)] So, yeah, I think for those 40 days, we did not do a lot of sleeping. We had to do these dual shifts across the Paris office and Mountain View. And the thing that made it so rewarding was when this model came out around the same time DeepSeek-V3 came out, and the Wall Street Journal put out this article that was this giant red scare article about how China's going to take over AI with open source models.

[[57:39](https://youtu.be/cDyi91onoJ8?t=3459)] And I remember my friend sent me a screenshot of this table of the LMSYS Chatbot Arena leaderboard, and all the way at the top right you've got ChatGPT and DeepSeek right behind it. And like, oh, DeepSeek was trained for whatever few million dollars, and they're right there. And then my friend was like, oh, Gemini is so behind because they had a version of, I think, Flash 1.5 Pro or something in that table at the very bottom.

[[58:15](https://youtu.be/cDyi91onoJ8?t=3495)] Then I looked at it. It's like, oh, that's really interesting. I was just looking at this leaderboard because we just released a model, and it definitely doesn't look like that when you go to the website. So it turns out there were some elided rows on the Wall Street Journal article. And so now if you go to that article today, you can see what at the time was the state-of-the-art model, Flash 2.0 Thinking up in the top right corner, way far ahead of DeepSeek-V3, might be messing with the open source narrative that they were trying to publish there. But it was a really important accomplishment for the team.

### 58:59 — Advice for his younger self

**Ryan:**

[[58:59](https://youtu.be/cDyi91onoJ8?t=3539)] Last question for you is if you could go back to yourself when you just graduated college, I guess, undergrad, and give yourself some advice, knowing what you know now, what would you say?

**Vlad:**

[[59:11](https://youtu.be/cDyi91onoJ8?t=3551)] You gotta chase the problems that people are facing in the world today. Go after the challenges that people see in everyday life, and don't be afraid to tackle a smaller part of this problem or maybe a more menial sounding part of this problem. Even if it's not fancy research, math, or something like that. Trust that by working on what's important, even if it's a smaller part of a larger project for what's important, you're going to get to see what really matters in terms of moving the frontier forward.

[[59:54](https://youtu.be/cDyi91onoJ8?t=3594)] And it's this kind of humility, maybe, in your problem approach that you should really be chasing. That's one piece of advice. I think the other bit that I would give, maybe as professional advice, perhaps, would be be the kind of coworker that people would want to see succeed. And so what I mean by that is there's this conception of workplace psychopath or Machiavellian leaders or whatever, people who will do anything at all costs to get the results they want, and they might be able to squeeze people to get some short-term gain.

[[01:00:45](https://youtu.be/cDyi91onoJ8?t=3645)] But having interacted with a variety of people professionally for so long, what is interesting to me is there have been a select few. One in particular is probably a very dear friend and mentor of mine, Todd Lipkin, who first got me into computer science, that are just so kind and people that you can learn from, someone that I can follow and be successful by following, that just genuinely inspire me to want to help them succeed.

[[01:01:33](https://youtu.be/cDyi91onoJ8?t=3693)] And so in particular, if you are the kind of person who helps people succeed in their projects, comes up with projects that can leverage other people's complementary skills in ways that help them shine, people will notice that people will want to contribute to projects that you come up with in the future and, in general, will want to support you going forward. And so people can get really cynical thinking about the game theory of how to interact at work.

[[01:02:10](https://youtu.be/cDyi91onoJ8?t=3730)] But I found that this kind of more amicable approach generally creates this deep sense of collaboration and willingness to help that is so important to get very large projects that require multiple people and multiple skill sets over the line. And so, yeah, I think if I could give any kind of interpersonal feedback or professional feedback or whatever to earlier version of myself, it's to be that guy, is to be the kind of person that other people want to see succeed.

**Ryan:**

[[01:02:51](https://youtu.be/cDyi91onoJ8?t=3771)] I love that this advice combats the cynical advice. And I also love that your original post combats the doomer, permanent underclass stuff. So, yeah, thank you so much for your time. It was a lot of fun. Really appreciate it.

**Vlad:**

[[01:03:05](https://youtu.be/cDyi91onoJ8?t=3785)] Thanks for having me, Ryan.
