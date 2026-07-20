---
type: raw-transcript
slug: openai-eng-and-dev-tools-founder
title: "OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh"
guest: "Charlie Marsh"
date: 2026-06-22
url: https://www.developing.dev/p/openai-eng-and-dev-tools-founder
fetched: 2026-07-19
complete: true
---

# OpenAI Eng & Dev Tools Founder: How Software Engineering Is Changing | Charlie Marsh

**Guest:** Charlie Marsh  
**Host:** Ryan Peterman  
**Publish Date:** Jun 22, 2026

## Host's Intro

Charlie Marsh is the founder of Astral, the Python devtool startup that was acquired by OpenAI. I interviewed him about how software engineering is changing and learnings from starting his own company as an engineer.

Check out the episode wherever you get your podcasts: [YouTube](https://youtu.be/Iw65FD4MGgs), [Spotify](https://open.spotify.com/episode/2sfielYIDcNO6HpeLdnooM?si=IoRXB5JsRjuP-2_q8NarLg), [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-peterman-pod/id1777363835).

## Timestamps

- 00:40 - Origin story
- 06:04 - The front page of Hacker News
- 14:35 - Why he chose Rust
- 20:10 - Full codebase migration from Zig to Rust
- 28:40 - LLM generated code and open source
- 35:34 - Performance optimizations
- 44:54 - Optimization with AI and combating slop
- 01:02:08 - Learnings as an eng starting a company
- 01:17:55 - Top technical talk recommendation
- 01:18:56 - Advice for his younger self

## Transcript

### 00:40 — Origin story

**Ryan:**

[[00:40](https://youtu.be/Iw65FD4MGgs?t=40)] What was the space like when you were first getting into building these dev tools? Why did you think it could be better?

**Charlie:**

[[00:51](https://youtu.be/Iw65FD4MGgs?t=51)] Before I started Astral, I was at a computational biology company, and I was the second engineer. I had no bio background and no ML background, and so I was building all the software systems to do machine learning, and that was all Python. So I was learning Python. Then we had some Go and some Rust, and so I just worked across lots of different ecosystems. And I think Python, at the time when I was in that position, we were trying to do a lot as a small team.

[[01:22](https://youtu.be/Iw65FD4MGgs?t=82)] So we had a very, I mean, not compared to large code bases, but we had a comparatively large code base. And it was really a small group of us that were software engineers trying to serve the rest of the team, whether they were machine learning researchers or scientists. So I had kind of worked across a bunch of different ecosystems, seen a lot of the tooling, and now I was working on Python, and we kept trying to get lots of leverage out of the tools, whether it was the type checker or the linter or the package manager. Things were scaling up.

[[01:50](https://youtu.be/Iw65FD4MGgs?t=110)] We were a small team. We wanted to have really good static analysis, really good tooling, and we kept running into limitations around it. I mean, I think there were some. I kind of looked at the Python ecosystem, and I just didn't see the same amount of experimentation that I saw in other ecosystems, like in the web ecosystem. There were a lot of things going on that seemed pretty crazy, and there was a very intense focus on.

[[02:19](https://youtu.be/Iw65FD4MGgs?t=139)] I don't know about very intense, but there was more of a focus on performance. And that started with esbuild, which was in Go, and then you had SWC and Rust and then Bun and Deno and all these other tools that came around. And this idea that you could have native tooling for JavaScript became very accepted, especially as applications became bigger and people were doing more and more stuff on their machine.

[[02:47](https://youtu.be/Iw65FD4MGgs?t=167)] And that wasn't really happening in Python. And so that, to me, was kind of like the key question, was like, why can't we have that? Because I was seeing all this stuff that was happening in web, and I had done some Rust, I'd done some Go. I'd seen these different tool chains and how they work, what the experience is, the user experience mostly in those cases. And then I saw Python, and it was like we had a smaller set of tools.

[[03:13](https://youtu.be/Iw65FD4MGgs?t=193)] There were lots of interesting ideas from other ecosystems that I didn't see represented. They were really all written in Python. And so that to me was kind of like the interesting question. And it was sort of like the first thing I asked when I started working on this, when I released Ruff. The title of the blog post was something like, "Python tooling could be much, much faster." And for me it was really like, this is a hypothesis.

[[03:42](https://youtu.be/Iw65FD4MGgs?t=222)] Could Python tooling be much faster? And then I built a prototype, and that prototype was like, yes, I think it could be.

**Ryan:**

[[03:49](https://youtu.be/Iw65FD4MGgs?t=229)] You wrote a post kind of exploring mypy or publishing your results using mypy. And the date on that, nine days later, you published the post. That one that you mentioned, it could be so much faster.

**Charlie:**

[[04:03](https://youtu.be/Iw65FD4MGgs?t=243)] No, that's funny, I didn't even realize that. Yeah, those were so close together.

**Ryan:**

[[04:06](https://youtu.be/Iw65FD4MGgs?t=246)] Did you build that proof of concept in those nine days?

**Charlie:**

[[04:10](https://youtu.be/Iw65FD4MGgs?t=250)] Yeah, I wrote that blog post about basically type checking at scale because I was trying to think of what are things that I learned that people haven't written much about. And then I started with building a linter because I thought it would be much easier. I think it actually is a lot easier than building a type checker. We're now building a type checker and we have a type checker. And so I can say that I think building a type checker is much harder.

[[04:35](https://youtu.be/Iw65FD4MGgs?t=275)] But I started with a linter because I thought it would let me prove a lot of the same ideas, but in a smaller form factor, like building a startup or just building a tool. You want to try to get something into people's hands that they can actually use and that actually proves out value as quickly as possible. And also that lets you iterate very quickly. And a linter weirdly ended up being kind of the perfect form factor for it because it has a pretty simple core.

[[05:07](https://youtu.be/Iw65FD4MGgs?t=307)] But then you have tons and tons of rules. And so it's extensible in a lot of different ways. But people can get value very quickly from a small core plus some number of rules. And so we were able to get something out there and then iterate and ship more rules and more functionality, and people could use it alongside other tools. It was useful immediately, which I think is extremely helpful. As opposed to something like.

[[05:34](https://youtu.be/Iw65FD4MGgs?t=334)] I mean, actually, the type checker would be a good example. A type checker that's like 75% done isn't very useful. Same with the package manager. These things have to be. I mean, there are ways, I think I would challenge those as blanket statements. But the point is it's harder to ship something iteratively that's still useful to users. And I think that's one of the key properties and actually building momentum as a tool or something else.

### 06:04 — The front page of Hacker News

**Ryan:**

[[06:04](https://youtu.be/Iw65FD4MGgs?t=364)] When you posted that writing, what was the reception?

**Charlie:**

[[06:07](https://youtu.be/Iw65FD4MGgs?t=367)] I mean, the blog post itself, I published it and then it was on Hacker News and it got tweeted about a lot, and it just created some amount of excitement and interest around it. And those things, I mean, especially being on the front page of Hacker News, I have a lot of thoughts about. I mean, it's certainly not. It's like some percent luck and then some percent skill, and it is like a helpful thing but not a requisite to success.

[[06:42](https://youtu.be/Iw65FD4MGgs?t=402)] And it also doesn't guarantee success just because you got something on the front page of Hacker News. It's great if you can, but there's a lot of randomness to it. I do think, though, that maybe a couple things. So one, after that happened, some people started actually paying attention to the project. And so I really tried to capitalize on that, basically by being very engaged. And so when people would file issues, I would aggressively try to acknowledge the issue as quickly as possible, fix it, and ship a release.

[[07:19](https://youtu.be/Iw65FD4MGgs?t=439)] If you can do that within one day, it's a very, very powerful loop. You gain supporters and create more momentum around the project. And there were also a couple high-profile people in the ecosystem that started paying attention to the project, like Sebastián Ramírez, who does FastAPI and a bunch of other things. And he's been a great supporter of our projects too.

[[07:41](https://youtu.be/Iw65FD4MGgs?t=461)] But early on he was like, "Oh, this is interesting. I'd like to use it." And I was like, I basically asked myself, well, what would it take for him to use it? And then I just tried to do all those things. So I tried to capitalize on that.

I think the other is, though, I do think a lot about developer marketing, and it's sort of like a dirty word or like a dirty expression. I think a lot of engineers want technical products and tools to just win on their merits.

[[08:13](https://youtu.be/Iw65FD4MGgs?t=493)] The best technical solution should just be the one that wins and grows. But I actually, I mean, I have this sort of stupid hypothesis that there's all these, like, thousands of really amazing projects on GitHub that basically don't know how to market themselves and so never get discovered and never go anywhere. And I don't actually know if that's true, but it's sort of how I feel about a lot of technical work, where it's like, it's actually worth looking at a project like Ruff.

[[08:44](https://youtu.be/Iw65FD4MGgs?t=524)] And when I think about what to put in the blog post, or this extends to what to put in the README or what to put in the. You don't need a million emojis and a million screenshots of everything. What you need is, okay, someone's going to land on this page and I have 10 seconds to get them interested in what I'm doing and help them understand why it might matter to them and why it's useful. And so that's the key idea that I try to bring basically to everything.

[[09:17](https://youtu.be/Iw65FD4MGgs?t=557)] I mean, it's a little bit depressing because it's like, okay, I only have 10, but people really don't have. This is the attention economy, right? It's the same thing with a blog post. Ironically, I used to look at a lot of the OpenAI blog posts when I was at Spring and we were doing machine learning in bio and we were trying to publish material to explain what we do. But we had all these interesting insights.

[[09:44](https://youtu.be/Iw65FD4MGgs?t=584)] We looked at the OpenAI blog posts, especially the DALL·E ones, the older ones, and we were like, wow, that's an amazing blog post. Because if you read none of the text, you still understand what they did and you're still impressed by it. If someone just goes on the page, they leave with an impression and they have some understanding. And I was like, wow, that's a really amazing thing. And so when I write blog posts now, I.

[[10:07](https://youtu.be/Iw65FD4MGgs?t=607)] I'm like, if someone just lands on this page, I have to be prepared for the large number of people who will only read maybe the TL;DR, maybe look at the first image, maybe read the headline. Some people will read the full thing. And so I should care painstakingly about every word and everything it says, but most people will read almost none of it. And so, again, sorry, it's a little bit depressing, but I do think it's worth thinking about your audience and how do you.

[[10:33](https://youtu.be/Iw65FD4MGgs?t=633)] How do you explain to them why they should care about what you're doing in a way that's honest and genuine, not deceptive? But you do have to think hard about how do you communicate why something matters to people.

**Ryan:**

[[10:46](https://youtu.be/Iw65FD4MGgs?t=646)] Very quickly, could you give an example of what you did in your case?

**Charlie:**

[[10:51](https://youtu.be/Iw65FD4MGgs?t=651)] I think for Ruff specifically, we had a really good graph of the benchmarks that we put in the blog post, and that went viral. It was on Twitter and that was a priceless graph, basically. Sorry, not in terms of monetary value. I just mean in terms of attention. Right. It was like, oh, that's really obvious what's happening there. I think graphs of benchmarks can be a really powerful thing.

[[11:19](https://youtu.be/Iw65FD4MGgs?t=679)] All benchmarks are bad and wrong in some way. And so there's a lot more to say about that. But I do think having a visual hook that explains to people why they should care and what something is, and having a really strong tagline. I would have to look back at what we had, but we were like, okay, we're going to be compatible with your existing stuff and much faster.

[[11:44](https://youtu.be/Iw65FD4MGgs?t=704)] And that's kind of it. And it's like, okay, well, if it's compatible and it's much faster, I was like, why should you care? It can be orders of magnitude faster and it'll give you the same experience. You try to convey that as quickly as possible.

**Ryan:**

[[11:58](https://youtu.be/Iw65FD4MGgs?t=718)] Right. And even the, I mean, that blog post header, I mean, Python tooling could be much faster. Should be much faster.

**Charlie:**

[[12:07](https://youtu.be/Iw65FD4MGgs?t=727)] It's a little bit provocative, I guess. Yeah. I mean, I'm pretty against clickbait or trying to be misleading in anything that we do. You basically want to balance creating, effectively communicating the most interesting pieces to people, but you have to do it in a way that you believe is true and authentic. You could lie about a bunch of stuff and post interesting things that are clearly provocative.

[[12:38](https://youtu.be/Iw65FD4MGgs?t=758)] But I don't know, to me, that's just. Why would I ever do that? That's such a losing battle.

**Ryan:**

[[12:44](https://youtu.be/Iw65FD4MGgs?t=764)] What do you think about that graph? I don't know if the... I see this a lot, though, where the axis is not zeroed.

[[12:53](https://youtu.be/Iw65FD4MGgs?t=773)] So it's all within the range of 50 to 60 chart crimes.

**Charlie:**

[[12:58](https://youtu.be/Iw65FD4MGgs?t=778)] Yeah, I wouldn't do that. Yeah, yeah. I do think benchmarks are pretty complicated and controversial, though, and maybe most people don't even see this controversy. But I do, because it's just very hard. Performance is very nuanced, and you have to think about, okay, with caching or without caching. Those are pretty different. Or depending on the project that you're running on, the performance characteristics will be totally different.

[[13:36](https://youtu.be/Iw65FD4MGgs?t=816)] And we see this in uv. This is really hard because sometimes uv is really fast, but sometimes your package install is actually bottlenecked on a C build that's totally out of band, and it's like, okay, well, so how do you accurately capture all of the different scenarios? I mean, it's sort of impossible to accurately capture all of the different scenarios, but it's also a disservice to users not to try to communicate to them the importance or a real representation of what the difference in performance will look like and why does it matter?

[[14:14](https://youtu.be/Iw65FD4MGgs?t=854)] And so you have to balance those things, which I think is actually quite hard. And a lot of people tend to get it wrong. And maybe we've gotten it wrong a few times too. I'm happy to accept that. But I do think it's more complicated than people think. But it's also, I think, a huge disservice not to include some way to try to convey to people quickly what things feel like.

### 14:35 — Why he chose Rust

**Ryan:**

[[14:35](https://youtu.be/Iw65FD4MGgs?t=875)] I think one of the things I'm most interested in is, you mentioned that graph. I see that graph and the engineer in me is like, how did you make it so much faster? And one of the things in the tagline is Python dev tooling written in Rust. And so I guess one of the first things I'm curious about is why did you choose Rust and what are the pros and cons of that?

**Charlie:**

[[14:57](https://youtu.be/Iw65FD4MGgs?t=897)] I would say I largely chose Rust for that project because of hype. I don't think at the time I was that informed about a lot of the technical trade-offs between those different ecosystems. And I hadn't really done a lot of systems programming. So the honest answer is I was seeing it in a lot of places, and it was growing a lot, and people said it appeared to be sort of an accessible way to write.

[[15:24](https://youtu.be/Iw65FD4MGgs?t=924)] My impression was that it was an accessible way to write high-performance software. And so I started for that reason. In hindsight, I think it was an amazing decision, and I absolutely would not do it differently. And I think it was the best choice for what we're building now. I have a lot more experience writing Rust, but it is funny because I do sort of think that if I had tried to write this in C or C++, I think I probably would have given up, because even now I find those ecosystems much more intimidating.

[[16:08](https://youtu.be/Iw65FD4MGgs?t=968)] Hard to access, hard to learn. I have often felt that one of the great or underrated advantages of Rust is basically the tooling, because you drop in and you use Cargo, and that's how you do everything. And if you clone it. This isn't always true, but there are exceptions as projects get sufficiently advanced. But it's. If there's a crate out there that we use and maybe I want to submit a PR to it, I'm extremely confident that I can clone it and figure out how to run and build it without having to do any work.

[[16:44](https://youtu.be/Iw65FD4MGgs?t=1004)] Being able to just clone and run cargo, run or cargo build or cargo test, that's actually really amazing, especially for someone like me who was new to systems programming and I didn't want to have to figure out my whole C tool chain and build system, all this stuff. Rust was opinionated about all of these things. And so there were a lot of things that were hard to learn, but I was allowed to basically, I was allowed to spend my time focusing on the things that actually should be hard to learn, as opposed to all the other, basically all the bullshit that you don't want to spend time on, like how do I get this thing to actually build and run?

[[17:24](https://youtu.be/Iw65FD4MGgs?t=1044)] I think it has been an extremely good bet for us. It's scaled very well with the project. And I mean, we at OpenAI too are like, we use a lot of Rust and they're betting heavily on Rust. And then, you know, me as someone who builds software, builds developer tools, like tries to build software for people to build software, I'm very bullish on Rust. It's grown enormously and I think it will actually just keep growing enormously at the same time.

[[17:57](https://youtu.be/Iw65FD4MGgs?t=1077)] I said this at the start. I've never been someone who's super dogmatic about ecosystems. I think that all of those ecosystems have lots of redeeming qualities. I think what's happening in Zig is very interesting, and I wish I had more time to go deep on it and develop more nuanced opinions about what it does better. I'm sure it does a bunch of things better than Rust, and I'm sure there are things for Rust to learn from that ecosystem.

[[18:20](https://youtu.be/Iw65FD4MGgs?t=1100)] Similarly, people have a ton of success building stuff in Go. I think that's great too. I think all this stuff is great. But I have loved using Rust and I have complaints about it. But I view those complaints as things that we should improve, especially as the way we build software changes.

**Ryan:**

[[18:38](https://youtu.be/Iw65FD4MGgs?t=1118)] With LLMs, it sounds like you're saying C and C++ today. You would not consider them because their tooling is insufficient. But Zig, Rust, and Go are all some spectrum of trade-offs or different things.

**Charlie:**

[[18:56](https://youtu.be/Iw65FD4MGgs?t=1136)] Yeah, I mean, I think a lot of people would disagree with me, but I don't really understand why unless there are very specific technical reasons or you're working with existing software. Basically, I don't really know why I would start a net new project in C or C++. I certainly would not at a personal level. I guess if they're like the ecosystems you know really well, then it makes a lot of sense to do it.

[[19:26](https://youtu.be/Iw65FD4MGgs?t=1166)] But if I was a new programmer looking to learn systems or if I knew those languages equally well, I guess I just don't understand why I would do that, which I'm sure I'll get roasted for, but I just don't really care now. I actually care about a lot of things that Rust gives me that I didn't care about as much before, like memory safety. I don't think I even understood or cared about what memory safety was when I started working on Ruff, to be honest with you.

[[19:49](https://youtu.be/Iw65FD4MGgs?t=1189)] And now I think it's a pretty amazing thing. I want to build things that are safe, that don't crash on users, that are really fast, really performant, that don't have to make compromises, basically. And I feel like I can do that in Rust. And so for me, I don't know, it's kind of like the perfect language. I mean, it's not the perfect language, but it is my favorite language to use right now in today's world.

### 20:10 — Full codebase migration from Zig to Rust

**Ryan:**

[[20:10](https://youtu.be/Iw65FD4MGgs?t=1210)] It's not unreasonable that you could almost completely transpile or convert your existing codebase into any language of your choice. Like I saw, I think it was on Bun, I forgot. I think it was Zig to Rust. Yes, like all in one go. So if you studied some other language and you thought it was better, you could totally rewrite everything from Rust into, I don't know, Zig or Go. Would you ever consider doing that for the dev tools that you've built, for instance?

**Charlie:**

[[20:47](https://youtu.be/Iw65FD4MGgs?t=1247)] Yeah, it's such an interesting time to be building software because things are changing. This is not a novel comment, but things are just changing so fast. I didn't really program with agents at all until Christmas, like December break, basically of this year or of last year, rather. And that's really not that long ago. I mean, I was using Cursor and stuff, but I wasn't like now. I haven't edited code in an editor in a very long time.

[[21:16](https://youtu.be/Iw65FD4MGgs?t=1276)] Everything I do goes through Codex and even if it's small edits, I'm just prompting and it's completely different. And that's not that long of a time, right? And so I don't know what it's going to look like in six months. Hard to say. But the reason that I mentioned that is, I think Bun doing that rewrite, it's like I wouldn't do that right now, but I'm actually glad that they are pushing that.

[[21:50](https://youtu.be/Iw65FD4MGgs?t=1310)] They are experimenting and pushing the envelope of what's possible. And they're doing it in the face of a lot of criticism. And it will be interesting to see how it plays out for users because I think a few different things I thought about is, oh, reasons not to do that. One is, okay, maybe you don't understand the code anymore, right? If the code got completely rewritten, then as a human you may not understand any of the code anymore.

[[22:17](https://youtu.be/Iw65FD4MGgs?t=1337)] And that can be a big problem. I think there are mitigating factors around that, which are, they tried to do a very direct transpilation, quote unquote. I mean, it's not exactly a transpilation, but they tried to do very one to one. And so that hopefully helps with understanding all the abstractions. If they're building so heavily with agents, does it even matter? To what degree do they need to understand different parts of the code?

[[22:41](https://youtu.be/Iw65FD4MGgs?t=1361)] I actually don't know the answer to that, which is where everything's changing so quickly comes from. It's actually a little bit hard for me to say right now how much that actually matters anymore. If they did transpile the whole codebase, how well do they need to understand things at different levels of abstraction? They should. It's actually a very, I think, complicated question. So one reason is how well will you understand the code?

[[23:05](https://youtu.be/Iw65FD4MGgs?t=1385)] That's a confusing thing. The other is you're kind of trading, when you do a rewrite like that, you're trading known issues for new unknown issues. Imagine you merge that and it closes 50 open issues on GitHub. In a literal sense, okay, that's great, but you may have now caused 15 new issues that didn't exist before, that you don't know about, because even a great test suite is only an approximation of your program's correctness.

[[23:41](https://youtu.be/Iw65FD4MGgs?t=1421)] There's Hyrum's Law, which is like anything—I'll get the phrasing wrong, but the gist is basically any implementation detail in your software. Someone eventually comes to rely on that. And so even things that aren't encoded as behavior become part of your API, whether you like it or not, which is a scary thought. But basically that means that even if you pass your whole test suite, there's probably lots of behavior that was implicitly encoded in your program that's changed.

[[24:11](https://youtu.be/Iw65FD4MGgs?t=1451)] The unfortunate thing is you end up pushing that onto users. They are the ones that have to run into that and then report it and figure out what went wrong. That's my main area of concern. With an automated rewrite, I actually trust the models enough that I would consider allowing them to do it. But the scarier thing for me is basically what's the impact for users and how do you roll that out safely?

[[24:33](https://youtu.be/Iw65FD4MGgs?t=1473)] So I don't know. It's kind of a... We're not going to, like, we don't have anything planned to do that for any of our own projects. But it is an interesting question. I mean, I think maybe the third piece that I do think about, especially right now, where everything's changing so quickly and there's basically the spectrum of how you write software has gotten way wider. This is a terrible analogy, but there's so many different ways to build software now.

[[25:05](https://youtu.be/Iw65FD4MGgs?t=1505)] There's the true Andrej Karpathy definition of vibe coding, where you're like, don't look at the code at all. All the way to don't use LLMs and blah, blah, blah. There's a lot of different stuff in between. And I actually think that right now I have pretty different approaches to different projects in terms of what I do. I built a tool last week that was. It's basically personal software. It's like a custom Rust linter to help us enforce certain things in our projects that I've always wanted to enforce but didn't fit into existing tools.

[[25:45](https://youtu.be/Iw65FD4MGgs?t=1545)] And I didn't read any of the code. GPT-5 did the whole thing, and it's like, okay, I can have a really different standard for that than uv because that project, we are the only users. It's easy to tell if it's correct or not. Not to go too deep into the weeds on what the project does, but we know if the output is incorrect and there's no other users. uv is relied on by millions of engineers and every single company.

[[26:21](https://youtu.be/Iw65FD4MGgs?t=1581)] And so it's like we want to be really careful about what we ship there and how. But there's a lot of room right now, I think, for exploring how we build software. You do have to be careful. What project are you working on, and what responsibility do you have to users? And that's not meant to be a subtweet on what Bun did. It's just how I think about how do we want to push the envelope in different places.

**Ryan:**

[[26:45](https://youtu.be/Iw65FD4MGgs?t=1605)] Right. I mean, to me that just reminds me of the pre-LLM tradeoff navigating, I guess, the risk of the code change and how much you verify it. Because if it's not risky, it's an internal dev tool that only you and I are using. Maybe I just ship it with, I just say stamp it, don't worry about it. It's not going to break anything. But if it's the critical thing that's blocking customers from checking out or something, maybe we have two people reviewing it, and there's a lot of checks in that part of the codebase. So it feels like the similar spectrum is just now there's a new level of trying less, which is not just a human doesn't even interact with it. You just ship it and maybe you just stamp it, and no one ever even looked at it.

[[27:40](https://youtu.be/Iw65FD4MGgs?t=1660)] Whereas before, at least to have written it, a human would have had to.

**Charlie:**

[[27:45](https://youtu.be/Iw65FD4MGgs?t=1665)] Yes, do it. Yeah, yeah, yeah, yeah. I mean, I think. Well, okay, a lot of reactions to that. So, one, I guess, the other thing I would just say quickly about Bun is, sometimes I go over to their repo and it's just so different than our repo. And it's very interesting to look at because if you look at basically the number one contributor, it's the RoboBun bot, and sometimes you'll click on PRs by humans and there's, like, human accounts talking back and forth.

[[28:14](https://youtu.be/Iw65FD4MGgs?t=1694)] But it's clear that all the comments were written by agents. And you're like, wow, this is very interesting. And so I look at that, but my perspective on that is basically like, okay, I'm glad that people are like that. They are experimenting with different ways to build software. I don't know that I'm ready to do that. But I do think that basically a lot of things are going to change.

[[28:34](https://youtu.be/Iw65FD4MGgs?t=1714)] And I think it's very interesting to be experimenting. So I'm glad that they are experimenting with things. Sorry, is my conclusion there.

### 28:40 — LLM generated code and open source

**Ryan:**

[[28:40](https://youtu.be/Iw65FD4MGgs?t=1720)] Do you block if people are just submitting full agent stuff on your repos?

**Charlie:**

[[28:47](https://youtu.be/Iw65FD4MGgs?t=1727)] We do, yeah. So we have an AI policy now, which isn't intended to be anti-AI, but it's really intended to. Because, I mean, we develop very heavily with LLMs. That is true, but it's more intended to be like, how do we retain useful contributions while filtering out net negative interactions from the repo? Because a contributor coming in and posting a comment that their agent wrote, and then we ask them a question and then they just paste the agent response back.

[[29:31](https://youtu.be/Iw65FD4MGgs?t=1771)] There's very little value in that. We could just ask the question to the agent. And so we want to retain the things that are useful from human contributors, which is insight, ways to reproduce the information we would need to plug it into our agent. Because there's no point in just having a conversation with an LLM on a GitHub issue. It doesn't really do anything for us. Our policy is roughly, you need to understand what you're pasting in or what you are submitting, which sounds like a low bar, but it's not.

**Ryan:**

[[30:13](https://youtu.be/Iw65FD4MGgs?t=1813)] How do you police that?

**Charlie:**

[[30:15](https://youtu.be/Iw65FD4MGgs?t=1815)] If we can't tell and it is agent-written, then I guess that's fine, right? But at least right now there are just lots of tells: being way more thorough than a human would ever be, including way too much detail, way more formatting, using terminology that a human wouldn't use, inventing random jargon, tons of links. I guess the broad sign would be putting in way more effort in ways that aren't necessary, in a way that a human wouldn't. It's almost always agent-authored.

[[30:51](https://youtu.be/Iw65FD4MGgs?t=1851)] But it's been, yeah, it's been challenging. I mean, I think the hard thing, Zig has a much more strict LLM policy, which is like no LLM-written code or no LLM-assisted code at all in the project, which is very different than us. I mean, all of my PRs now are LLM-written, right? LLM-written. And they had a blog post about this idea of, like, they called it something along the lines of contributor poker, where it's like you're kind of trying to place bets on contributors.

[[31:19](https://youtu.be/Iw65FD4MGgs?t=1879)] Historically, in open source, when a contributor came around, they might be new to the project, but they could show signs of promise or they're really engaged or really interested, and you give them feedback, they take the feedback and they fix up their PR, and then the next time they put up a PR, they've learned from that feedback. It's the same way as mentoring a new engineer who joins your team. It's like they learn from feedback, it compounds, they get better, and then they can actually mentor someone else in the future.

[[31:46](https://youtu.be/Iw65FD4MGgs?t=1906)] You're making investments in people. In a way, it's the same for open source. It's like you want to—I thought about this law historically. It's like you want to invest in good contributors who are going to grow to help others and be maintainers in their own right. That's kind of gone for PRs, especially those that are written by agents, because people don't really learn anything. Someone can put up a PR that's written by an agent, and you leave comments, and then they take your comments and put them into the agent, and then update the PR, and then merge it, and it's like there's no compounding feedback.

[[32:19](https://youtu.be/Iw65FD4MGgs?t=1939)] And so I actually do understand that perspective. A lot of the contract between maintainers and contributors is pretty different now. And relatedly, again, not a novel insight, but the cost of putting up a plausible PR has gone to zero, while the cost to review and vet a plausible PR has remained the same and is very high. Especially for the projects that we work on, where I'm not trying to overstate it, they're just hard projects.

[[32:55](https://youtu.be/Iw65FD4MGgs?t=1975)] Ty is our type checker, probably hardest project I've worked on technically to get a change merged because of the complexity in the architecture, but also the problem space. It's just very, very hard. If someone puts up a plausible PR to Ty, it might take them two minutes, and then it could take us an hour to understand it. And so it's created very poor dynamics in open source. And I don't know how we've solved that.

[[33:25](https://youtu.be/Iw65FD4MGgs?t=2005)] I think it will continue to get worse until hopefully it gets better in some way. We find ways to solve this, but it's certainly something we've experienced in our projects.

**Ryan:**

[[33:36](https://youtu.be/Iw65FD4MGgs?t=2016)] Right. It sounds like review is becoming more and more of a bottleneck for that Bun rewrite. Do you know if it was human? Like, humans read that code, or that was just kind of...

**Charlie:**

[[33:46](https://youtu.be/Iw65FD4MGgs?t=2026)] No, I don't think it was human reviewed.

**Ryan:**

[[33:48](https://youtu.be/Iw65FD4MGgs?t=2028)] So it's just yolo rewrite the whole thing.

**Charlie:**

[[33:51](https://youtu.be/Iw65FD4MGgs?t=2031)] Yeah, I mean, in a way I think they did have. And I'm excited for, at least at time of recording, quote unquote. Jared hasn't published the blog post yet, which is like. I mean, he keeps making jokes about how the blog post is taking way longer than the rewrite. But I'm actually really interested in the blog post because I think they did have a pretty sophisticated approach to how the rewrite worked, which will be interesting to read about.

[[34:17](https://youtu.be/Iw65FD4MGgs?t=2057)] It wasn't just they had one prompt that was, "Rewrite this in Rust." They tried to have, at least my impression from looking at the PR, was there were actually different phases of the rewrite, and each file had to go through a couple different phases that had ways to validate whether it was correct or not. The answer is no, though. I don't think a human was reading significant amounts of that code.

[[34:42](https://youtu.be/Iw65FD4MGgs?t=2082)] It's just not possible.

**Ryan:**

[[34:43](https://youtu.be/Iw65FD4MGgs?t=2083)] Basically, what if we both agreed today that Zig was objectively better than Rust, and then someone on your team said, I can do this rewrite into Zig. Would you block it?

**Charlie:**

[[34:58](https://youtu.be/Iw65FD4MGgs?t=2098)] I think I would block it. I don't know whether I'd be right to do so, but I think we as a team aren't there yet. And maybe we will get there, and that's how we will feel eventually. But right now, I think we just feel like there's still a lot of value in deeply understanding our code and our tool chain and the ecosystem. And so I would say we don't want to do that, but it might depend on the project.

[[35:03](https://youtu.be/Iw65FD4MGgs?t=2103)] I don't know.

### 35:34 — Performance optimizations

**Ryan:**

[[35:34](https://youtu.be/Iw65FD4MGgs?t=2134)] All the things that you built, they're like an order of magnitude faster than what was available at the time. How much of a difference did Rust make on that graph?

**Charlie:**

[[35:45](https://youtu.be/Iw65FD4MGgs?t=2145)] I think it depends a bit on the project. I think in a rough lot of it was just Rust. And then over time, I think we've improved on that a lot because you can even look at the history of the project. Hopefully no one, hopefully this is still true, but basically over time the project gets faster and sometimes that regresses. But maybe I'll put it differently. You could write Ruff in a couple different ways, all in Rust, and they could have really different performance characteristics.

[[36:30](https://youtu.be/Iw65FD4MGgs?t=2190)] So that's just to say that I generally think of Rust as the floor, or the baseline performance that you get is going to be significantly better. But you still get a lot more out of thinking deeply about performance and design. If you take the same program in Rust and in Python, the exact same implementation, to the closest approximation you can get, the Rust one will be faster, but you can then take that program and you can probably optimize it.

[[36:58](https://youtu.be/Iw65FD4MGgs?t=2218)] Another 10x. I don't know about 10x, but my point is, even within being written in Rust, there's a ton of room for how to make things more performant, how to write really performant software. And again, when I started working on Ruff, part of my goal was to learn Rust. And so I did write a lot of bad code, which is fine. I shipped something out that was really helpful to people, but it's gotten a lot better, I think, over time, and we've made it more and more performant.

[[37:26](https://youtu.be/Iw65FD4MGgs?t=2246)] I think in uv, there was more sort of architectural innovation beyond just being in Rust, especially because uv. So as a package manager, you're doing a ton of I/O and downloading files over the network, unzipping things, writing them to disk, moving them around. The linter doesn't have to do as much of that. I mean, it has to read all your files, but there's not a huge amount of I/O. The package manager is mostly I/O, and then you're trying to do things very efficiently.

[[38:01](https://youtu.be/Iw65FD4MGgs?t=2281)] So there, it was more. I mean, Rust was important. But I do think that in uv, there are more architectural things that we did, or ways that we thought a lot about performance. The design of the cache is very, very intentional and makes it so that repeated installs of the same package on your machine are near instant because of the way that we lay out the cache and the way that we install from the cache into your projects.

[[38:34](https://youtu.be/Iw65FD4MGgs?t=2314)] It basically means that if you've installed a package before, installing it again is extremely cheap, both in terms of disk space and time. And so that's a very different design than any of the other Python package managers had. So, again, it kind of depends on the project. I do tend to think that whether you're writing code in Rust or in Python, there's always room to be thinking about performance.

[[38:59](https://youtu.be/Iw65FD4MGgs?t=2339)] You can always make things faster or slower. Even if you're writing in Python, you can still make things much, much faster by thinking harder about performance and design. So it's some mix, but it depends on the project.

**Ryan:**

[[40:01](https://youtu.be/Iw65FD4MGgs?t=2401)] Over the course of the project, do you have a top few things that were implementing the project that were technically challenging or most interesting to you?

**Charlie:**

[[40:11](https://youtu.be/Iw65FD4MGgs?t=2411)] I really like this optimization that Andrew on our team, who goes by BurntSushi, he's the author of ripgrep and a bunch of other things. He's a really amazing engineer. He did this really cool optimization around how we represent versions. It's pretty cool. I mean, basically, if you think about resolving and installing a very complex Python project, it turns out that we have to parse and create lots of versions, as in 1.

[[40:11](https://youtu.be/Iw65FD4MGgs?t=2411)] 0.11.0.2 version objects within the program. We end up parsing and creating a lot of those. And it turns out that actually allocating that memory was expensive given the scale, the number of times we were doing it. He came up with a representation where we can represent 90-something percent of versions with a single u64 integer. So it's just way more efficient. And the benchmarks around that and the implementation were very cool.

[[41:12](https://youtu.be/Iw65FD4MGgs?t=2472)] It's like one of the coolest PRs I've read. I think in Ty, which is our type checker, there's a lot of very interesting performance work that's happening, especially to make it incremental. So Ty is designed to be a type checker and a language server. The whole system is highly incremental. The idea there is if you're in a text editor and you open up one file, you don't necessarily want to have to type check your entire project, all your dependencies, every file in the project, just to get analysis for that file, because you don't need to.

[[41:55](https://youtu.be/Iw65FD4MGgs?t=2515)] So how do you make that work? That's sort of like, that would be lazy. You want to be lazy. But the other piece to that is if you have a file open and you edit it, or you have two files open, you edit one of them, you only want to recompute exactly what you need to recompute. You don't want to have to go and retype check the entire code base again, especially because maybe you're working on a big project like PyTorch, and it's like you have two files open, you edit one of them, you don't want it to like, and then you save.

[[42:22](https://youtu.be/Iw65FD4MGgs?t=2542)] You don't want it to take two seconds to retype check the project and give you new analysis. So the whole system is built around queries, which is pretty interesting. This is more of a macro design thing, but we built it on top of a framework called Salsa, which is also what rust-analyzer uses, which is the popular Rust language server. And now we've intentionally or inadvertently become very large contributors.

[[42:53](https://youtu.be/Iw65FD4MGgs?t=2573)] But the whole system is built around that, which has been very interesting, architecturally interesting.

**Ryan:**

[[42:58](https://youtu.be/Iw65FD4MGgs?t=2578)] So it's lazy. So it doesn't type check the whole codebase. And it's incremental.

**Charlie:**

[[43:02](https://youtu.be/Iw65FD4MGgs?t=2582)] Yeah, the incremental part is the thing that's hard because you kind of need a way to basically model a dependency graph of everything that's happening in the code. And so then when you change something, we want to just flow the data back through all the different pieces, only the pieces. Yeah, so that took a lot of work, but it has come together, and I've been doing a lot of optimization lately with Codex because it tends to be very good, especially at micro-optimizations.

[[43:41](https://youtu.be/Iw65FD4MGgs?t=2621)] And in Ty in particular, we also need to think a lot about memory, not just speed, because if you work on a very large project, you don't want it to take many, many, many gigabytes just to run your language server. Ideally you want it to be relatively efficient. So I spend a lot of time now kind of continuously optimizing memory usage and performance, and I can just set a goal that's like, try to reduce Salsa memory by like 1% on this project.

[[44:11](https://youtu.be/Iw65FD4MGgs?t=2651)] And you can't do these things that you might try to do. And it's very good at just coming up with very reasonable things. And so I don't know, I find that very cool because it's kind of like you can almost have continuously. I won't say self-optimizing, that's a bit grandiose. But you can kind of be continuously just optimizing your software.

[[44:35](https://youtu.be/Iw65FD4MGgs?t=2675)] So I've been enjoying that a lot. But most of those are trying to find ways to represent things that take up less memory, or trying to come up with, sometimes it's trying to come up with broader redesigns to fix pathological performance.

### 44:54 — Optimization with AI and combating slop

**Ryan:**

[[44:54](https://youtu.be/Iw65FD4MGgs?t=2694)] That one optimization with the version numbering and seeing that you can limit it just to a u64. If you think back to some of these more creative optimizations that were done, that was in the human era. Do you think if you just ran Codex and you're like, hey, just don't break things but lower, do you have faith that it would come up with that? Or is that kind of a step above what?

**Charlie:**

[[45:20](https://youtu.be/Iw65FD4MGgs?t=2720)] That's a very interesting question. If you just, at least in my experience, if you use these things to reduce memory or improve performance by some moderate percentage, it will typically come up with things around the edges as opposed to larger redesigns or reconsiderations. But you can get to those larger redesigns if you prompt and collaborate with the agent. If you ask, well, should we be thinking a bit bigger about why we have to represent the data?

[[45:51](https://youtu.be/Iw65FD4MGgs?t=2751)] This way, you can get to bigger ideas. That might be an idea that you could have gotten to with prompting if you were like, okay, let's start by profiling and figuring out where we're spending a lot of time. And then maybe it would eventually come back to you and say, we're spending a lot of time in version parsing and version drop and version allocation, blah, blah. And we'd be like, okay, well, how could we represent these more compactly?

[[46:17](https://youtu.be/Iw65FD4MGgs?t=2777)] And we'd probably start by finding micro-optimizations in the representation of, well, this field. You combine these two fields, save a few bytes, blah, blah, blah. But I think if you kept pushing it, it's possible it would get there. But that's not the thing it's going to come up with by default. Mitchell Hashimoto, who was one of the HashiCorp founders, works on Ghostty. He had a post that was insightful.

[[46:42](https://youtu.be/Iw65FD4MGgs?t=2802)] I thought last week or this weekend about a renderer he wrote where it was a really terrible renderer. I'll probably butcher the tweet, but it was a really terrible renderer. And then he hadn't intentionally. And then he had an LLM optimize it and it made it 10 times faster. And he's like, great. Actually, no, my handwritten version was 100 times faster. And it's like, if you're not using your brain to think about from first principles, how fast should it be and how should the system work?

[[47:10](https://youtu.be/Iw65FD4MGgs?t=2830)] Then you just ship all these accumulated. I won't necessarily call it slop, but it's like you just ship these things, and you're like, yeah, oh my God, I made it 10 times faster. But really it should be 100 times faster. And so I think it shouldn't be controversial. There's still a lot of room for using your brain. But I do think it's like, I struggle with this stuff a lot. I mean, I'm changing how I write software a lot.

[[47:36](https://youtu.be/Iw65FD4MGgs?t=2856)] And I've had people on my team because I'm using agents a lot and also was, to some degree, trying to push our team to use agents more. I mean, some of that for me came from a place of we build tools for software engineers, and a lot of our users are now using agents. And so if everything good that we do— that's an exaggeration, but if everything good that we do comes from understanding our users very well and how they work, then we should probably be using agents so that we understand what it's like to build software with them, so that we can build better tools for our users.

[[48:14](https://youtu.be/Iw65FD4MGgs?t=2894)] That was part of my motivation, and part of it was just kind of seeing how it can change how you work. And I don't know. I think I'm shipping a lot more. But it has been a difficult process. I've had people on the team tell me, which I think is great that they tell me this, but they're like, "Oh, it used to be the case that whenever you put up a PR, I could review it pretty minimally because I had a lot of confidence in it, in your work."

[[48:43](https://youtu.be/Iw65FD4MGgs?t=2923)] And now it's like, when you put up a PR, I actually have to review it really closely because you're not writing anymore. It's like the agent. And I was like, wow, that's very interesting. They're completely right, which is. And the same thing happens to me. It's like, if I go to sleep and then wake up in the morning and look at one of the PRs I put up, I'm like, wait, this is terrible.

[[49:02](https://youtu.be/Iw65FD4MGgs?t=2942)] You know what I mean? It's just. It is easy to trick yourself into basically believing work that isn't at the same standard as what you would do before. And I don't think. I think we have. We don't really know what to do with that. And I'm kind of learning, getting better. And I mean, this was. I think I'm doing a lot better job now than I was in probably, February or something, where I was like.

[[49:28](https://youtu.be/Iw65FD4MGgs?t=2968)] I was just fully agent killed. And I'm like, now I'm a little bit more like. But so my point is, that was a powerful moment for me when someone on the team said that, and I was like, wow. You're right. And I see that in other people's work too. It's not just limited to me, but it really does throw a lot of things on their head.

**Ryan:**

[[49:50](https://youtu.be/Iw65FD4MGgs?t=2990)] If you generate pure slop, that's easy, but I think there's this gray area where you generate partially AI slop, or it's acceptable, but it's not at the bar that you used to have. What are the tactics that you've used on the team that have worked for combating this kind of gray area? AI slop.

**Charlie:**

[[50:12](https://youtu.be/Iw65FD4MGgs?t=3012)] I'd like to get to a world where we're not here, and I don't know if we'll ever get there. I'd like to get to a world where if you put up a PR and it's all green, then the odds of it getting merged are extremely high. Right. Because that would mean that you have automated verification for most of what matters. And we have a lot of that in our projects, and we've tried to add more over time, and I think it's helpful in Ty especially.

[[50:42](https://youtu.be/Iw65FD4MGgs?t=3042)] We have tons of benchmarks that run under Valgrind through CodSpeed on every PR, and that includes memory. So we benchmark memory usage and simulation time and wall time on every PR. And then we also have a really big suite of ecosystem tests. So basically every time you put up a PR, we run before and after on a bunch of projects in the ecosystem, and then we create this report of the diff of all the diagnostics, like the errors that got removed and added and everything.

[[51:19](https://youtu.be/Iw65FD4MGgs?t=3079)] So we have, over time, we've tried to do more and more. These are important. Honestly, even before we had agents, we basically couldn't build without these things. But the point is, I want to have more automated verification and try to get better at that. And that includes things too. Like, we basically assume now that anyone on the team that puts up a PR has already run that through Codex Review, probably several times.

[[51:49](https://youtu.be/Iw65FD4MGgs?t=3109)] And that's basically an assumption. I mean, we could automate that process, but Codex Review is just an agent reviewing the code and double-checking.

[[51:56](https://youtu.be/Iw65FD4MGgs?t=3116)] Yeah, it's just running Codex and then just doing slash review.

[[51:58](https://youtu.be/Iw65FD4MGgs?t=3118)] That's it. Yeah. It's not that fancy. I mean, it's not. Sorry, it's not that sophisticated. But it's just like because now it's like, if a contributor puts up a PR, that's the first thing that we do because it tends to find good things. Basically, I think one bucket is: how do you create more automated systems that just help get things, make sure things are right.

[[52:28](https://youtu.be/Iw65FD4MGgs?t=3148)] And that also includes things like trying to improve your AGENTS.md file over time. If there are things, if there's feedback you're giving in a review that the agent's not respecting, try to find a way to help the agent learn that, even learn skills. We have some shared skills on the team, stuff like that. None of this stuff is very sophisticated, by the way. It's pretty simple. The other piece is how do I make sure that I put in the work to ensure that I'm creating a good PR.

[[52:56](https://youtu.be/Iw65FD4MGgs?t=3176)] And so for me, that's like, I really should understand, again, it sounds like a really not. It really sounds like a low bar, but I should understand each line in the PR. I know it's crazy, but also I do try to review each PR myself in the GitHub UI. This is something I've always found really helpful. If you actually just open up your PR and click files and read through it as if you were a reviewer, you tend to find things that you would miss if you were just looking at your local diff.

[[53:34](https://youtu.be/Iw65FD4MGgs?t=3214)] I find that very useful. And then the other is trying to encode skill. I guess this is a little bit more in the first category, but trying to encode in skills things I'm consistently getting wrong that the agent is getting wrong. A recent example would be I found that I was often getting feedback on PRs that was of the form, this condition here, this if statement, what case is this intended to catch?

[[54:07](https://youtu.be/Iw65FD4MGgs?t=3247)] Because if I commented out all the tests pass, and so I was like, okay, I should probably have a pass before I put up any PR where I have the agent go through and check: are these conditions still relevant, or are they left over from a prior refactor or something else? So I don't know, I'm still learning, but those are some of the things I've been doing. Yeah, again, I think it's a pretty hard time to be building software, but I felt for a long time where I had a fear that AI was going to make us more productive, but that programming would be, like, a lot less fun.

[[54:44](https://youtu.be/Iw65FD4MGgs?t=3284)] Because I just love programming. And I was like, oh, now I'm gonna have to spend all my time reviewing code and prompting this idiot agent that keeps getting things wrong but ultimately is probably more productive. I actually feel way better about that right now than I did a few months ago. And I don't exactly know why. I think it's because, well, I think the agents getting better and the tooling getting better and me getting more comfortable with it is one factor.

[[55:21](https://youtu.be/Iw65FD4MGgs?t=3321)] I think the other is I've grown to appreciate more of the kinds of things that working with agents has unlocked. The cost of running an experiment is incredibly low. There's so many things I've wanted to try or questions I've wanted to answer that I can now answer almost instantly. Sort of a dumb example. In uv, everything is snapshot tested. So basically all of our testing is effectively running uv and verifying the output.

[[55:56](https://youtu.be/Iw65FD4MGgs?t=3356)] That's how we test basically the entire program. And so that means, and we have a lot of tests. That means we have a lot of test output. And the test output is... it actually ends up in the test files. So we have Rust files. We have a file called lock.rs that tests all our uv lock tests. It's all our uv lock tests. And it's very, very long in part because it has all the lock output snapshotted in the test.

[[56:21](https://youtu.be/Iw65FD4MGgs?t=3381)] And I was like, what if we stored the snapshots in separate files? Would that somehow make our compiles faster? Because then you don't have—technically, that's like Rust code. And so it's like, would that all disappear and would that make our builds faster or blah, blah, blah. And I'd always want to do that, but it sounded like to do that experiment as a human would be extremely painful because you have to convert all of those tests.

[[56:48](https://youtu.be/Iw65FD4MGgs?t=3408)] And I just had an agent do it in the background while I did a bunch of other things. I got a bunch of data on it, and the answer is no. But it's a little bit more nuanced. It actually does have a good impact. If you're just iterating on the snapshot outputs, you no longer have to recompile your program at all because the outputs are stored somewhere else anyway.

[[57:08](https://youtu.be/Iw65FD4MGgs?t=3428)] That's the thing that makes a difference on you. But my point is, I'm just running experiments like that all day, trying things that used to be hard, used to cost a lot to. To answer the work of then going from that to production. There's still real work there, but. So I think one piece is the tools and the agents getting better. The other is things that I just wouldn't have been able to do before that I can now do incredibly easily.

[[57:37](https://youtu.be/Iw65FD4MGgs?t=3457)] And then the third is, I think I'm more and more realizing that a lot of the value I get from building software is not retained because some of it is thinking hard about it. It doesn't have to be typing out the code, but it's thinking hard about the layout of a data structure. A lot of it is merging a PR that causes a user issue. I get a lot of satisfaction from actually fixing and improving something.

[[58:01](https://youtu.be/Iw65FD4MGgs?t=3481)] It's not necessarily just from typing out the code. I do feel for people a lot who feel like they're losing something by working with agents, because I do feel that myself. But I feel better now than I did a few months ago about, like, what it's like to work as a software engineer with agents.

**Ryan:**

[[58:23](https://youtu.be/Iw65FD4MGgs?t=3503)] You mentioned in one of the performance optimization examples, you said if you just unleash Codex, it kind of does these local optimizations, and it's very good at that. But it's not great at some of the, I mean, today it's more human ingenuity of system-level optimizations. And it kind of reminded me of this tweet that you had. You said, "I'm slightly concerned by how much garbage I would be churning out if I was trying to use these tools without significant software engineering experience."

**Charlie:**

[[58:56](https://youtu.be/Iw65FD4MGgs?t=3536)] Yeah, I remain concerned about that. Yeah.

**Ryan:**

[[59:00](https://youtu.be/Iw65FD4MGgs?t=3540)] It reminds me, and similar to what Mitchell Hashimoto said in that tweet, there's a very big difference between Codex, go and do this, versus you are wielding it like this tool and you're kind of prodding in the right direction.

[[59:18](https://youtu.be/Iw65FD4MGgs?t=3558)] Yeah. I was curious your thoughts on that because it seemed like it went pretty viral. And I think a lot of people are thinking about that.

**Charlie:**

[[59:24](https://youtu.be/Iw65FD4MGgs?t=3564)] Being a great software engineer is more useful than ever. I don't think it's still the case that the people on our team who have the strongest engineering skills are the most effective, even at using agents. And it's funny because there's a lot of talk about token maxing. I don't know if you're familiar with this.

[[59:54](https://youtu.be/Iw65FD4MGgs?t=3594)] Right. Yeah. The idea of, should you have a leaderboard? For example, this is getting tweeted about a lot: companies that have token leaderboards. It's like, how do you create some terrible incentives to just use as many tokens as possible? And it's funny because that does get tracked. Or sorry, there's not a leaderboard. But token usage is something you can look up, for example, internally. I mean, and it's interesting to look at because I don't care who on the team is using the most tokens.

[[01:00:23](https://youtu.be/Iw65FD4MGgs?t=3623)] And there are people on the team who are like, "I'm actively trying not to care about that, like being where I am on the token leaderboard," which I think is great. I don't care. They should just do a great job, and that's fine. I don't care if they use a lot of tokens or not. But it is interesting to look at the token leaderboard because some of the people on the team who are most productive are using a lot of tokens.

[[01:00:47](https://youtu.be/Iw65FD4MGgs?t=3647)] There is a correlation. I'm not saying it's causal, but I do think that a lot of great engineers are able to use agents very effectively and hopefully to multiply their skills. So I do think it would be really hard to be an early career software engineer right now. And I'm not spending that much time with early career engineers right now. Just based on it, at Astral, we're just a very small team, and we tended to hire very senior.

[[01:01:21](https://youtu.be/Iw65FD4MGgs?t=3681)] But it's sort of hard for me to think about, what would we, like how would I learn, basically? What would the iteration loop be? I would be learning from Codex, I guess, as opposed to the other way around, basically. I mean, a lot of the time I'm actually instructing Codex and trying to correct it and providing a safeguard on it or Opus or whatever you're using. And so, yeah, I think I just don't know where you would get.

[[01:02:02](https://youtu.be/Iw65FD4MGgs?t=3722)] It would just be way too easy to fall prey to a lot of the bad things that happen when you use agents.

### 01:02:08 — Learnings as an eng starting a company

**Ryan:**

[[01:02:08](https://youtu.be/Iw65FD4MGgs?t=3728)] You built this proof of concept in Rust, and it was really well received. But why did you start a company around it, and how did the raising go and all of that? What was the motivation there?

**Charlie:**

[[01:02:20](https://youtu.be/Iw65FD4MGgs?t=3740)] Yeah, yeah. So I left Spring. I was actually convinced to leave by a friend who, a very close friend who left Meta around the same time. And he was like, we should start a company together. And I was like, okay, fine. I mean it wasn't quite that simple, but. But I did. I laughed. And then we kind of went into the idea maze of what do we want to build? We went into it not knowing what we wanted to build, and we spent a bunch of time exploring the Venn diagram of ideas.

[[01:02:55](https://youtu.be/Iw65FD4MGgs?t=3775)] There were things he was interested in that I thought were not interesting and vice versa. And there was some stuff in the middle, and we spent time exploring the stuff in the middle. But then in all my spare time I was working on developer tools. Because that's what I thought was really interesting, and it wasn't quite like a fit for him, basically. But around then I was working on Ruff. I was working on a couple other projects that you can see in my GitHub that are like, I don't know, probably not as interesting, but they were like.

[[01:03:23](https://youtu.be/Iw65FD4MGgs?t=3803)] I was experimenting with lots of different things at the time. I was pretty interested in WebAssembly. I wrote a sort of CI/CD toolkit in TypeScript. It's sort of like you wrote pipelines in TypeScript and it transpiled them to Docker. And I was like, oh, this could be cool. I don't know. I was building a lot of stuff. And at that point in time I decided I wanted to start developing relationships with investors, but that I wasn't ready to raise money because I didn't know what I was actually going to build.

[[01:03:54](https://youtu.be/Iw65FD4MGgs?t=3834)] And so my thinking was I'm going to try to get connected to some people who like to invest in this kind of stuff, with an eye toward reaching back out to them in three to six months and being like, hey, we had a great conversation, now I'm working on X. So that was my thinking. So I got connected to a couple investors who invest in software infrastructure and developer tools, and I had some good conversations.

[[01:04:19](https://youtu.be/Iw65FD4MGgs?t=3859)] And then the problem is things just can move really quickly. And so I didn't actually expect to start raising so soon, but I effectively got convinced. And at the same time, Ruff was growing a lot. And so I effectively got convinced that there was enough there to start a company, which is a very interesting process. I was like, I don't quite know how this becomes a company, but I was effectively convinced that there was enough there to build a company.

[[01:04:43](https://youtu.be/Iw65FD4MGgs?t=3883)] Which is interesting by the investors. Yeah. Which I'm grateful for. The other thing I was convinced of was, which is funny, is if I hated it, I could stop in like six months. It's like if you decide it's not for you, you could give the money back. The investor said that. Yes. Which I actually think was brilliant because, like, I was probably never going to do that, but it did make me feel like there was less pressure.

[[01:05:14](https://youtu.be/Iw65FD4MGgs?t=3914)] So, sorry, very weird roundabout details, but basically I was working on Ruff more full time eventually. And then it was kind of, I would say, collaborative with the potential early investors, where it was like we would just have long conversations about my ideas, and then it basically became clear that it was like, there's enough here. And I wrote out kind of a product roadmap, which honestly a lot of it stayed true to what we ended up building, what we've ended up building so far at least.

[[01:05:47](https://youtu.be/Iw65FD4MGgs?t=3947)] And from there, it basically became like, yeah, we want to fund you. Here are the terms that we would do. And I was like, oh, wow, okay, so I guess it's happening. So it was just interesting. And I had never done anything like this before. I mean, I was just an IC software engineer my whole career, and then suddenly I was like starting a company. And it's funny because I actually think the decision to go all in and start the company wasn't that stressful.

[[01:06:22](https://youtu.be/Iw65FD4MGgs?t=3982)] I actually think a lot of the stress came later as the company started to succeed because at the beginning I kind of had nothing to lose. But then as the company started to succeed, I was like, oh wow, the company's kind of working. What's going to happen from here? And I had a team of 20 people who were depending on me. And so I don't know, just for me as a founder it was like, I'm pretty risk averse, but I actually found that starting the company was an easier, it was an easier decision than maybe some of the stressful things that came later to navigate.

[[01:06:59](https://youtu.be/Iw65FD4MGgs?t=4019)] But it happened very quickly and sort of unintentionally and in a symbiotic way with investors, which I hadn't really anticipated.

**Ryan:**

[[01:07:09](https://youtu.be/Iw65FD4MGgs?t=4029)] I didn't expect the investors, because I thought the founders were hungry for the fundraising and go, please fund me. But the investors were like, I think it can happen a million different ways.

**Charlie:**

[[01:07:19](https://youtu.be/Iw65FD4MGgs?t=4039)] And actually, I mean, we did three fundraises. We did a C to Series A and a Series B. We actually never even announced the Series A or the Series B. They were, I mean, they were announced in the acquisition blog post. But we sort of complicated. It's like we basically just never got around to it, and why don't you guys publish it?

**Ryan:**

[[01:07:44](https://youtu.be/Iw65FD4MGgs?t=4064)] Because isn't that good marketing for talent?

**Charlie:**

[[01:07:46](https://youtu.be/Iw65FD4MGgs?t=4066)] It's good marketing, but basically there kept being reasons that we wanted to wait a little bit. And to me, it always felt like a lot of work, and then I was like, it just never honestly felt like the most important thing because we were building a lot of stuff and the company was going well, and I was like, we don't need the marketing. We did finally plan to announce it, but then we got bought, so it didn't happen.

[[01:08:12](https://youtu.be/Iw65FD4MGgs?t=4092)] Each of those fundraisers was preemptive, basically initiated by investors, which is fortunate because the company was going well and people wanted to invest. But it was also just a funny position for me to be in, I guess. I think I was just always a little bit conservative, and I wasn't super aggressive about trying to go out and raise money.

[[01:08:47](https://youtu.be/Iw65FD4MGgs?t=4127)] But we were lucky enough to be building things that people really had a lot of confidence in or had a lot of belief in.

**Ryan:**

[[01:08:52](https://youtu.be/Iw65FD4MGgs?t=4132)] That probably gave you a lot of negotiating leverage because one of the best positions you'd be in is that you're willing to walk away, you don't need it. And by definition you didn't even come there to begin with. They came to you and they said, please take the money.

**Charlie:**

[[01:09:07](https://youtu.be/Iw65FD4MGgs?t=4147)] That's true. Yeah, yeah. I wouldn't say I'm a great negotiator, but yeah, I guess at least I had a strong hand. But we were very lucky with investors. We had amazing investors, super supportive and really, really aligned with how I wanted to build the company. Never any conflict, never any pressure to do anything specific, just support. And maybe the only thing, maybe the only piece of consistent feedback is that I could have been more aggressive and.

[[01:09:42](https://youtu.be/Iw65FD4MGgs?t=4182)] But I don't know, in terms of scaling, growing, and doing. But I liked the way that we operated, and yeah, we just had such good experiences with our investors too. So I felt lucky about that because it can easily go the other way.

**Ryan:**

[[01:09:55](https://youtu.be/Iw65FD4MGgs?t=4195)] I imagine if someone invests, there's a promise of future revenue. But how does this company make money? Because you guys give away your software for free, right?

**Charlie:**

[[01:10:05](https://youtu.be/Iw65FD4MGgs?t=4205)] Yeah, we launched a commercial product in, like, August of last year, and it was sort of—it was called Pyx. It was kind of like a hosted counterpart to uv. So a lot of our, a lot of uv users, will purchase a private registry software instead of using the public registries, either for security or maybe they need to publish their own private artifacts, things like that. And we basically built our own private registry that had some first-class support for uv.

[[01:10:37](https://youtu.be/Iw65FD4MGgs?t=4237)] And it let us solve a bunch of problems that we saw in our issue tracker around users using other solutions. Also let us build something really fast because we vertically integrated the client and the server. There were special things they could do to be really fast and really easy to use and all that. And we spent a while selling that, and our revenue actually grew pretty well. I mean, it wasn't like, I think in this era of AI, you're constantly hearing about fastest company to go to 100 million in revenue and things like that.

[[01:11:10](https://youtu.be/Iw65FD4MGgs?t=4270)] It didn't look like that, but we were definitely able to sell this to some big enterprises. And the cool thing was we had a very good, because we built the open source and everyone was using our open source, we had a really good funnel. We had a small number of extremely high quality customers, is the way I would put it. So the general idea for how we wanted to make money was to keep building open source and the tooling. The tooling remains free, open source, entirely noncommercial.

[[01:11:43](https://youtu.be/Iw65FD4MGgs?t=4303)] And then we build software that's kind of like the natural next thing you need when you're using our tooling. So if you're using uv, there are likely problems we can solve for you with a private registry. And then the funnel is people using uv, they have these problems, and then we sell them the registry. And the registry was meant to be one piece of a platform of a bunch of different things.

[[01:12:03](https://youtu.be/Iw65FD4MGgs?t=4323)] We sell like a Python cloud. So that's what we were building towards. I mean, part of the cool thing about the acquisition is we'll be able to take parts of that platform and make it basically freely available. Like we did just as an example. A big part of that was we did a lot of, like, in Python, there's a big part of the community that uses Python with GPUs like PyTorch. And then there's like a whole ecosystem around PyTorch of software that kind of builds against PyTorch.

[[01:12:44](https://youtu.be/Iw65FD4MGgs?t=4364)] And that's for a variety of reasons. The ergonomics around that are not great. It can be kind of hard to work with, hard to install. The right version depends on the GPU that you have and what version of CUDA you have installed and all this stuff. And so we kind of tried to solve that in a certain way where we built our own distribution. You could think of it kind of like in the sense of a Linux distribution.

[[01:13:11](https://youtu.be/Iw65FD4MGgs?t=4391)] We pre-built a lot of things like that that all worked together and made that available to customers. And so now we can actually take that and just make that freely available to everyone. Because we're no longer, we no longer are trying to build an independent business. We're just trying to build great tools that grow a broader ecosystem. So, I mean, more to come on that. But that's been kind of like one cool thing that I'm excited about.

**Ryan:**

[[01:13:34](https://youtu.be/Iw65FD4MGgs?t=4414)] As a first-time founder, especially with the engineering background, was there anything that was a surprising learning or something you would share with someone if they were an engineer and they were going down that founder path?

**Charlie:**

[[01:13:48](https://youtu.be/Iw65FD4MGgs?t=4428)] There are so many different ways to do it. I'm actually not a huge fan of people giving startup advice in general because so much of this industry is survivorship bias. You could give the exact same advice. You can go to two talks and people give you two incredibly successful founders give you completely contradictory advice, and you're like, I don't really know what to do. And I tend to view that as you've got to figure out what's true to you.

[[01:14:16](https://youtu.be/Iw65FD4MGgs?t=4456)] And so there's all these decisions you have to make: in person versus remote, right? Have a principle and stick to it. Either one can be great. We built the whole company remotely. It went super well. It was great. Do I think there are benefits to being a person? Of course. Would I have been able to hire the team that we put together if we were in person? Absolutely not. And so there are trade-offs to all these things.

[[01:14:40](https://youtu.be/Iw65FD4MGgs?t=3480)] You just have to be principled and figure out what resonates with you. And there's a million of those decisions that you have to think through. I feel fortunate in a lot of the ways I got to run the company. I tried to spend very minimal time fundraising and with investors, and I tried to optimize for investors I really trusted, as opposed to trying to talk to a billion different investors and pit them all against each other to get the best terms.

[[01:15:07](https://youtu.be/Iw65FD4MGgs?t=4507)] My goal was always to find a partner that I really trust and get good terms, and then move quickly. Spend as little time on fundraising as possible. And so think about what you care about and focus on that. There's no right answer to a lot of this stuff. I got a lot of advice to get a cofounder when I first started the company, and I basically ignored that. I mean, well, sorry, I did ignore it because I didn't get a cofounder, I guess.

[[01:15:32](https://youtu.be/Iw65FD4MGgs?t=4532)] For me, I kind of knew they were right probably, but I didn't really have someone in mind. I didn't want to force it, and so I just didn't. And over time, I felt like it would have been helpful to have someone that's kind of in the trenches with you in the same way. But you find other ways to compensate for it. I don't know.

[[01:16:01](https://youtu.be/Iw65FD4MGgs?t=4561)] I lean on my wife a lot, probably more than I should. Probably more open with my employees than I otherwise would be, which I think can be good or bad. But it's like, I share a lot with the early team, especially when I need advice on things. Try to build a network of other founders, especially here in New York. I have a pretty good group of.

[[01:16:22](https://youtu.be/Iw65FD4MGgs?t=4582)] There's like six or seven of us who. We try to get dinner twice a year. Doesn't sound like a lot, but everyone's busy. Yeah, yeah, yeah. And that's been a really helpful support system. So you just find other ways to compensate. But yeah, it's. I don't know. There's no. I really don't. I really think there's not one right way to do it. Yeah, and it extends everywhere.

[[01:16:49](https://youtu.be/Iw65FD4MGgs?t=4609)] I mean, also, everyone on X is talking about, should everyone in your company be working seven days a week? This kind of thing. And it's like, I don't know, we just built a very different company and we were able to do it. That was not. I mean, I work basically all the time, and that's a choice I made and that I'm very happy with.

[[01:17:13](https://youtu.be/Iw65FD4MGgs?t=4633)] But I don't expect people on the team to work all the time. And I want it to be a company where you can be highly, highly successful working normal hours, but also where you're rewarded for your output and your performance. And I try to keep all those things in sync, but again, there's no one right way to do it. Other companies, that is their culture and that's what they want to do.

[[01:17:38](https://youtu.be/Iw65FD4MGgs?t=4658)] And sure, whatever. If that's what you sign up for, just make sure that you're honest about what you're doing. So I don't know, I just think figure out what you care about and, in my opinion, don't focus too much on how you think you should be doing things. Think about how you want to be doing things and what actually fits with how you want to work.

### 01:17:55 — Top technical talk recommendation

**Ryan:**

[[01:17:55](https://youtu.be/Iw65FD4MGgs?t=4675)] What's your top book recommendation, whether technical or maybe something that helped you as a founder?

**Charlie:**

[[01:18:01](https://youtu.be/Iw65FD4MGgs?t=4681)] I don't read a lot of technical material. I have definitely watched a few talks that were very influential to me, which is a little bit different.

**Ryan:**

[[01:18:10](https://youtu.be/Iw65FD4MGgs?t=4690)] What are those talks?

**Charlie:**

[[01:18:12](https://youtu.be/Iw65FD4MGgs?t=4692)] The Zig creator, Andrew Kelley had a really good talk about data-oriented design that I learned a lot from. I mean, even apart from learning things, it sort of inspired me to look at software quite differently. And so I think about that talk a lot. Yeah, things like that. It's really good. Yeah, it's about. Well, I haven't watched it in a while, so I'll probably mess it up, but it's like a lot of it's about basically design decisions they made in the Zig compiler and just thinking about memory and allocation and all this stuff.

[[01:18:44](https://youtu.be/Iw65FD4MGgs?t=4724)] And I was like, I watched that when I was pretty early in my career of systems programming, and I was like, wow, these people really care about what they're doing. And I was like, that's cool.

### 01:18:56 — Advice for his younger self

**Ryan:**

[[01:18:56](https://youtu.be/Iw65FD4MGgs?t=4736)] Yeah. And then last question is, if you could go back to the beginning of your career, right when you graduated college, what advice would you give yourself, knowing what you know now?

**Charlie:**

[[01:19:07](https://youtu.be/Iw65FD4MGgs?t=4747)] I don't know, it's so hard to give myself advice without feeling like I have all this hindsight bias. I mean, I think, I guess there are some things where I'd basically tell myself that it is the right decision and I shouldn't worry so much. But it's hard to know how that would have played out if I did it a thousand times over. But for example, I think when I left school and I went to work at Khan Academy, part of me was definitely like, wow, should I be taking more of a big tech job, and am I gonna really regret not having that experience?

[[01:19:38](https://youtu.be/Iw65FD4MGgs?t=4778)] The Khan Academy pay was good, but the big tech pay was certainly better. And I was seeing my friends get huge bonuses and all this stuff, and I felt sort of insecure about whether I should be doing that. And I think it actually, in the long term, really paid off. I mean, maybe it would have been great, but the experience I had was really what I wanted, and I thought I made that decision for the right reason.

[[01:20:06](https://youtu.be/Iw65FD4MGgs?t=4806)] So I think some of these things are, I don't know, everything happens for a reason, you know, and it's like, have some faith in what you're doing for the right, you know, for the. If you're making decisions based on principles, I think it can work out.

**Ryan:**

[[01:20:24](https://youtu.be/Iw65FD4MGgs?t=4824)] When we started this conversation, you said the reason you got into what you got into is because you tried all these different ecosystems and you had a broader perspective. Imagine if you went to Google and you just kind of used Google's closed thing, and then you might not have had the same insight.

**Charlie:**

[[01:20:43](https://youtu.be/Iw65FD4MGgs?t=4843)] Yeah. And I think about this with Spring, too, because Spring, I was there for four and a half years, and then I left, right, as they decided to do a pivot, and then they ended up joining Genentech. But we had set out to build this kind of crazy drug discovery company. We were focused on aging, and it was all with computer vision. It was very, very ambitious what we were trying to do. Yeah, yeah.

[[01:21:10](https://youtu.be/Iw65FD4MGgs?t=4870)] And then afterwards, I was like, oh, the company didn't have the huge exit or the huge. We didn't achieve all of our dreams. Did I waste all my time? And ultimately I was like, no, because I learned by being an early employee, seeing all these stages. I learned so much about how to run my own company and also all the technical learnings that I rolled into my own company. So, again, I feel weird giving this advice because everything has worked out really well, but I feel like there are moments in time where I sort of doubted some of my career decisions.

[[01:21:44](https://youtu.be/Iw65FD4MGgs?t=4904)] And then in hindsight, you can only connect the dots. Looking backwards, everything kind of added up to finding the thing I really love, which is building tools and feeding into that.

**Ryan:**

[[01:21:55](https://youtu.be/Iw65FD4MGgs?t=4915)] Awesome. Well, thank you so much for your time, Charlie. I really appreciate it.

**Charlie:**

[[01:21:58](https://youtu.be/Iw65FD4MGgs?t=4918)] Yeah, thank you. No, it was super fun.

---

