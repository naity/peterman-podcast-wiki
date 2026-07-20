---
type: raw-transcript
slug: stripe-cto-on-what-grew-his-career
title: "Stripe CTO on What Grew His Career, Hiring Without Leetcode, Coding as a Leader (Career Story)"
guest: "David Singleton"
date: 2025-08-29
url: https://www.developing.dev/p/stripe-cto-on-what-grew-his-career
fetched: 2026-07-19
complete: false   # transcript cuts off ~01:26:00 (mid "How to set culture"); remaining sections through 02:04:55 unavailable — fetch pipeline truncated the page
---

# Stripe CTO on What Grew His Career, Hiring Without Leetcode, Coding as a Leader (Career Story)

**Guest:** David Singleton
**Host:** Ryan Peterman
**Publish Date:** Aug 29, 2025

## Host's Introduction

David Singleton was the CTO at Stripe for 7 years before he left to start /dev/agents. Prior to Stripe, he grew from a junior engineer to a VP at Google. Ryan Peterman recently asked him about everything he knows about career growth and being an excellent engineering leader. They discussed how Stripe hired at scale without Leetcode, why he thinks all engineering leaders should write code, the book that impacted his career most and many more topics.

Check out the episode wherever you get your podcasts: YouTube, Spotify, Apple Podcasts.

---

## Timestamps

- (00:56) Before Google
- (06:49) Joining Google
- (13:27) Deciding to try management
- (25:28) How to decide on EM vs IC
- (30:36) Biggest gap in managing managers
- (36:14) The difference between VP and Senior EM
- (39:36) How to communicate well
- (48:42) How managers can scale themselves
- (54:08) How to build a new engineering site
- (01:04:47) What kept him at Google
- (01:07:34) The story behind joining Stripe
- (01:16:53) Comparing and constrasting cultures
- (01:25:55) How to set culture
- (01:34:59) Is Stripe too reliable?
- (01:39:36) Hiring at scale without Leetcode
- (01:44:15) Lessons learned working with Stripe's leadership
- (01:46:45) Why leave Stripe
- (01:51:26) How his AI startup plans to compete
- (01:55:31) Career reflections: regrets, what went well
- (02:01:05) Top book & habit that impacted his career
- (02:04:55) Advice for younger self

---

## Transcript

### **00:00:56 — Before Google**

**Ryan:**

[[00:00:56](https://youtu.be/hl6Ryc_NUm8?t=56)] The first thing I wanted to ask you is how did you get into programming to begin with?

**David:**

[[00:01:00](https://youtu.be/hl6Ryc_NUm8?t=60)] Like many people, I got into computers as a kid. A computer came into our household for my parents' business, and I ended up teaching myself to code. A lot of kids back then, this is like the late eighties, early nineties, were learning to code to write computer games. I coded bespoke business software for my parents' business. I built them an invoicing system. It was actually really cool, mostly because I learned that I could do this creative thing with this piece of technology, and I was always really inquisitive about how things worked.

Then the thing that I built ended up being pretty impactful to our family. Before that, my parents did all of their invoice tabulation for their tax returns manually. My sister and I would notice that once a quarter they got super grumpy because they were up all night tabulating their accounts. Once we built the invoicing software, you could press a button and it came out of the printer. It showed me that this thing could have a big impact for people, and it's been the impact of building software for people that really gave me the bug to then go on and study computer science and get into the industry. But yeah, that's how it all started.

**Ryan:**

[[00:02:06](https://youtu.be/hl6Ryc_NUm8?t=126)] After you graduated from college, I understand that the first role you had was at Symbian. Can you tell me the story about working at Symbian?

**David:**

[[00:02:13](https://youtu.be/hl6Ryc_NUm8?t=133)] Yeah. Well, first of all, it's a funny story how I ended up there. I'm originally from Northern Ireland. I planned to go back there to join a software company in Belfast, which is my hometown, but it was an internet boom company and unfortunately went under as the internet bust happened. So there I was in Cambridge, England, and I had to find a job at pretty short notice. Some folks from Symbian visited, and I thought these are really lovely people.

I decided to apply for the job there. I was incredibly lucky because, for those that don't know, Symbian built smartphone mobile phone operating system software before smartphones were a thing. We're talking here like 2001. I ended up going there because I liked the people. As soon as I arrived, I realized we were working on technology that we all believed was going to have a profound impact on how people used computers at scale. It was obvious that we were all going to have these little smart computers in our pockets, but we were inventing stuff that today we might take for granted.

I remember whiteboards where we were drawing what turn-by-turn directions in maps would look like when there were GPS chips in the handsets, which we knew was coming. We were trying to figure out the right way to plug that into the operating system. I was super fortunate to end up there and find that I was passionate about what we were doing. I started off as a software engineer, building some core parts of the Bluetooth stack on the Symbian OS and also some of the PC Connect software.

In the final couple of years at Symbian, I went from being an IC software engineer working in the core to doing a role called technical consultant. I was still an individual contributor software engineer, but I was assigned to teams from handset manufacturers who were turning the Symbian OS into actual handsets and products. Symbian arrived as a kind of bag of bits, and you had to put your own UI on top and build a whole bunch of things.

It was quite a complex project. I ended up being the technical lead on the Symbian side for essentially the same project executed again and again by teams at different companies. I worked with companies like Panasonic in the US, Samsung in both Korea and China, Nokia in Finland, etc. The right way for me to help on each of those projects ended up being quite different. For one of the teams, I was helping them set up source control for the first time. For another team, I was helping them debug some graphics issue they were having.

Because I saw how the culture of a software engineering team in different companies impacted how things got built, it gave me an intellectual pursuit of how you organize teams and how you set them up to have impact. Just to give you a flavor of that, I'm sure these companies work completely differently today. But Samsung back then ran very small teams, and they would give multiple teams essentially the same mission. The team that finished first was the one that got to ship. Imagine the kind of incentive structure that sets up.

At Nokia, everything was planned in much more intricate detail. Things were definitely much more predictable, but everything took significantly longer. I became a bit of a geek for thinking not only about what software we were writing but how teams were organized to get it done.

**Ryan:**

[[00:05:59](https://youtu.be/hl6Ryc_NUm8?t=359)] Would you say that that role was similar to the popular role of forward deployed engineer in the industry today?

**David:**

[[00:06:06](https://youtu.be/hl6Ryc_NUm8?t=366)] Yeah, actually that's a great question. I haven't thought about it that way, but I think that is a really good observation. It was the case that I and people in the same role were tasked with not only helping the customers integrate the thing into their own product but also to bring back insights and questions from the customers to inform our future roadmap at Symbian.

So, yeah, I guess it was. We didn't call it that back then, and I hadn't even made the connection until now. But yeah, it's a pretty interesting model. For what it's worth, I was pretty young at that time. I really enjoyed it. I got to travel all over the world, and it was a very rewarding period of my career, even though I probably wouldn't want to do that right now.

### **00:06:49 — Joining Google**

**Ryan:**

[[00:06:49](https://youtu.be/hl6Ryc_NUm8?t=409)] So you talked about the future companies. I know we're talking about Google and Stripe. I'd love to hear the story about how you got into working at Google.

**David:**

[[00:07:00](https://youtu.be/hl6Ryc_NUm8?t=420)] Yeah. So I was living in London at the time working for Symbian. This was immediately post Google's IPO. Google recognized that Symbian realized smartphones were going to be very important for how people accessed services online.

Believe it or not, London at the time was recognized globally as a center of excellence in the mobile industry because there were so many people working at companies like Symbian there. Google decided to open an engineering office with a specific focus on mobile in the early days. I attended a recruiting event and interviewed. It was a pretty tough process interviewing at Google back then. I did some interviews in London and flew to California. It was the first time I'd ever been to California as part of that interview process.

What I realized through the quality of people I was meeting and the energy at the company was that this is where I needed to be next in my career. For what it's worth, I never imagined I would stay at Google for nearly 12 years. I thought I would go to Google, learn a lot about building distributed systems at scale, and learn about the best engineering being done in the industry so I could take it somewhere else. But I ended up staying at Google so long because every 18 months or two years, I'd pick up my head, think about what I had been doing, and realize I learned a tremendous amount. So I just kept staying because I was learning so much.

**Ryan:**

[[00:08:33](https://youtu.be/hl6Ryc_NUm8?t=513)] I've noticed that in a lot of people who have had a lot of career success and stay at one place for a while, they don't stay there out of complacency. They're constantly trying to leave, but that place is treating them so well that they end up staying rather than job hopping.

**David:**

[[00:08:51](https://youtu.be/hl6Ryc_NUm8?t=531)] Yeah, at Google I probably did six different jobs. You'd look at them and say that is a very different job with very gradual transitions between them.

[[00:08:58](https://youtu.be/hl6Ryc_NUm8?t=538)] The dynamic range of skills that I learned there was incredibly useful and diverse. In the very early days, it was just an amazing place to be. Incredible talent density, everyone was really driven to have an impact, and everyone was given a lot of autonomy. So back then, the 20% culture at Google was really true.

[[00:09:19](https://youtu.be/hl6Ryc_NUm8?t=559)] I definitely had things that my own manager and team were expecting me to get done, but I was really welcomed to pick up a lot of other things as long as I could get the core done. I looked at it as my opportunity to learn, and I was going to find all the opportunities to learn as much as I could.

[[00:09:37](https://youtu.be/hl6Ryc_NUm8?t=577)] I think that's actually why I ended up being given more and more things to do at Google. One example of that is I was working on a feature for Google Maps for mobile at the time. This is before Android, to be clear. Mobile search was growing pretty rapidly.

[[00:09:56](https://youtu.be/hl6Ryc_NUm8?t=596)] I noticed that every time anyone on a mobile phone would go to google.com, we would immediately redirect them to google.com/m. Back then, mobile network round trip times were super long, like multiple seconds, maybe two and a half seconds to follow one redirect. We were subjecting every mobile user to that.

[[00:10:17](https://youtu.be/hl6Ryc_NUm8?t=617)] I remember talking to my coworkers and being like, this is bonkers. We were wasting 2.5 seconds of users' time every time they accessed this page. Everyone said it was too hard to fix that. It was really complicated, and it was in this kind of front-end infrastructure that no one really on this team knew how to work with.

[[00:10:33](https://youtu.be/hl6Ryc_NUm8?t=633)] I was determined that this didn't make sense, and it's just software, so I must be able to figure it out. I wanted to learn about how that infrastructure worked, and I went and chased that. Eventually, I merged a change in the main Google web server and did a whole bunch of stuff on that front-end infrastructure to remove that redirect.

[[00:10:51](https://youtu.be/hl6Ryc_NUm8?t=651)] That ultimately ended up saving something like 70 years of user time every year and was pretty impactful. I think it had a noticeable impact on usage as well. You get a real bug for those things, like being able to just follow your nose to learn and take agency to do stuff that matters.

[[00:11:11](https://youtu.be/hl6Ryc_NUm8?t=671)] I find that really fun and a great environment to be in and to continue to learn.

**Ryan:**

[[00:11:17](https://youtu.be/hl6Ryc_NUm8?t=677)] The thing that motivated you in that agency that worked out for your career, was that the perceived impact that you would have or was that the technical curiosity?

**David:**

[[00:11:27](https://youtu.be/hl6Ryc_NUm8?t=687)] That's a good question. I'm sure that initially early in my career, it was technical curiosity.

[[00:11:33](https://youtu.be/hl6Ryc_NUm8?t=693)] I honestly had no real sense of just how many people we were impacting in the work I was doing at Google. It was a lot, but I was very technically curious. Then I worked with a product manager, a good friend of mine still, called Gummi, and he started putting all the product metrics in terms that everyone could understand.

[[00:11:56](https://youtu.be/hl6Ryc_NUm8?t=716)] He's Icelandic, and I remember one day the product we were working on, he said, we now have as many active users as the population of the country that I come from. Now, Iceland's not a very big country, but he kept doing that every week. This week we surpassed the population of Ireland, and this week it was Scotland, and then next week, eventually it was like Germany.

[[00:12:13](https://youtu.be/hl6Ryc_NUm8?t=733)] That was really amazing because I found myself picturing the whole population of Iceland using our product in a day. I started out with technical curiosity as the motivator, and then it was really Google that taught me to start thinking about how many people you could impact.

[[00:12:29](https://youtu.be/hl6Ryc_NUm8?t=749)] That has been the real driver for me behind everything that I've done since.

**Ryan:**

[[00:12:33](https://youtu.be/hl6Ryc_NUm8?t=753)] Yeah, that framing is really powerful. I imagine in motivating a team to move forward towards things that are impactful. I remember YouTube also had a very similar thing, which was that for the longest time they were driving towards maybe a billion minutes watched per some unit of time.

[[00:12:55](https://youtu.be/hl6Ryc_NUm8?t=775)] That unifying goal, just everyone's saying, okay, a billion's a big number, I'm going to chase that. I could totally see why that was very motivating for you as an engineer.

**David:**

[[00:13:06](https://youtu.be/hl6Ryc_NUm8?t=786)] Yeah, I think anytime that you're able to lay out a clearly defined executable, possible but audacious goal and have everyone rally behind it, teams often do incredible things to make that happen.

[[00:13:21](https://youtu.be/hl6Ryc_NUm8?t=801)] I've been lucky to experience that as an engineer and then later try to use that kind of tool as a manager and leader.

### **00:13:27 — Deciding to try management**

**Ryan:**

[[00:13:27](https://youtu.be/hl6Ryc_NUm8?t=807)] So you talked about management, and I understand that you grew from an IC to a manager quite quickly. When people think about the management versus senior engineer fork in the road, it's not a clear-cut decision for everyone.

[[00:13:43](https://youtu.be/hl6Ryc_NUm8?t=823)] I'm curious, what was the story behind you making that decision for yourself?

**David:**

[[00:13:48](https://youtu.be/hl6Ryc_NUm8?t=828)] Yeah, it's a funny story actually. I was an IC engineer and was having a blast and learning a lot. I think it was because I was around a lot of product managers that were really helping the team see how much impact they had.

[[00:14:00](https://youtu.be/hl6Ryc_NUm8?t=840)] I remember I walked into my manager's office one day and I said, Hey Dave, he still is a good friend. I want to be a product manager. He looked at me and said, well, if you really want that, we can figure out how to make it happen, but you should be an engineering manager.

[[00:14:17](https://youtu.be/hl6Ryc_NUm8?t=857)] He pitched me on the idea that as an engineering manager, I'd be able to feel the same kind of fulfillment in terms of impact that I might in a PM role, and I'd be able to continue to do technical work. Google at that time had this role, which was variously called TLM or Uber Tech Lead.

[[00:14:36](https://youtu.be/hl6Ryc_NUm8?t=876)] He really pitched me on doing that. He said, you love engineering, you love writing code, so do this. For me, that was quite an easy choice. To be clear, the team needed more managers at the time, so I'm sure I was solving a problem for him. I do get a lot of fulfillment and energy out of helping people accomplish more together than they might on their own.

[[00:14:57](https://youtu.be/hl6Ryc_NUm8?t=897)] I was able to continue being super in the details, writing code, producing designs, and so forth. As I developed in my career at Google, I ended up taking on more and more teams at the same time. I was still managing ICs, but multiple teams at a time. The management job definitely took over the vast majority of what you would think of as normal work time.

[[00:15:23](https://youtu.be/hl6Ryc_NUm8?t=923)] Something that was true then at Google was that everyone was encouraged to use their 20% time. This was a period of my life where my wife was working a very busy job, and I was super energized by the work I was doing. I spent a good couple of years managing teams during the day, and then I would have my own personal engineering projects as soon as folks started to go home.

[[00:15:49](https://youtu.be/hl6Ryc_NUm8?t=949)] One of those, for instance, was I built the first version of Google Translate on the iPhone. That was cool. It gave me a chance to interact with a whole new group at Google. It was some hands-on engineering work with impact that helped me continue to scratch both itches.

[[00:16:08](https://youtu.be/hl6Ryc_NUm8?t=968)] I feel very fortunate to have had that experience. If you're someone out there who's thinking about, I love writing code, but I think I could have a lot of impact as a manager, I do think if you can find a place where you can continue to do both, it can be incredibly fulfilling. I decided to work pretty hard during that period, but I was loving it.

[[00:16:26](https://youtu.be/hl6Ryc_NUm8?t=986)] If you derive a lot of energy from something, just go at it.

**Ryan:**

[[00:16:31](https://youtu.be/hl6Ryc_NUm8?t=991)] Most of the people that I talk to who tried the TLM role and I ask them, do you recommend it? They tell me no. They say you're doing two jobs at the same time, and it's difficult to excel in either one. So what do you say to that, 'cause it sounds like you're supportive.

**David:**

[[00:16:48](https://youtu.be/hl6Ryc_NUm8?t=1008)] Yeah, I understand that perspective. The projects I was managing were different from the ones that I was being an IC on. I think if you're trying to be an IC on projects that you're also managing, which by the way I'm doing right now in the startup and having a blast, it can be more challenging because you have to continually figure out how to make sure that you're putting on both hats.

[[00:17:11](https://youtu.be/hl6Ryc_NUm8?t=1031)] If you're working as an IC on a project that you're also the manager for, it's very easy to get sucked into your own personal work and lose track of what every individual on the team also needs to be unblocked. It just requires a constant prompt to go into this different mode.

[[00:17:28](https://youtu.be/hl6Ryc_NUm8?t=1048)] Many years later, at Stripe I worked with a management coach, a guy called Jeff Lawrence, and he had this analogy he used, which was, when you're a leader, you have to continually step onto the balcony. You're on the dance floor doing stuff in the org, but you have to prompt yourself to step onto the balcony and look down at how everything is working.

[[00:17:49](https://youtu.be/hl6Ryc_NUm8?t=1069)] He was teaching me that in a completely different context, but I think that's true for TLMs as well. I think it's a particularly challenging role to make work well, but I think you can make it work well, and I've certainly had a blast doing it, as long as I think through and try to create the moments in the week and the day to do that.

[[00:18:07](https://youtu.be/hl6Ryc_NUm8?t=1087)] Step onto the balcony thing.

**Ryan:**

[[00:18:09](https://youtu.be/hl6Ryc_NUm8?t=1089)] I mean, eventually though you grew to a VP at Google, so I can't imagine you were still taking on feature work when you're at that level of org leader. Right?

**David:**

[[00:18:20](https://youtu.be/hl6Ryc_NUm8?t=1100)] Funny story, certainly by the time I was a VP at Google, I was not a critical contributor in any of the projects, but something I really believe deeply, and I took this into my work at Stripe as well, is that no matter how senior you are, the most effective leaders find some way to experience the work of the team at what I describe as the one foot level, the actual work of the team.

[[00:18:46](https://youtu.be/hl6Ryc_NUm8?t=1126)] I found an actual tool for this, which I call engineer-acation, when I was at Stripe, but I did this at Google as well as a VP of engineering. I was running this program called Android Wear. It is the foundation of the wearables platform that is in all of the Google smartwatches today. I was running that almost as a GM, product engineering, business partnerships, user experience, marketing, everything.

[[00:19:10](https://youtu.be/hl6Ryc_NUm8?t=1150)] It was great. I still find it incredibly valuable to actually experience the tool chain that the engineers in my org were working in. It just made it much easier for me to ask smart questions and to see what was necessary to unblock them. So periodically, during that period, probably once every two or three months, I would find a way to go and do a little project in the code base.

[[00:19:36](https://youtu.be/hl6Ryc_NUm8?t=1176)] The context that that gave me back then made me a much more effective VP of engineering. I still do that today and did that for my whole career at Stripe.

**Ryan:**

[[00:19:50](https://youtu.be/hl6Ryc_NUm8?t=1190)] I remember when Elon Musk bought Twitter and there was this strong influence from his side on managers should code and this push, basically what you're saying, and I guess some of the downstream benefits of it came in.

[[00:20:06](https://youtu.be/hl6Ryc_NUm8?t=1206)] There was a big debate in the industry on that thing. When I think about going deep versus scaling yourself, the very brainless quick thing I can think of is that IC project that you might have done, like the iPhone one for instance. You could also have positioned someone to do that work and then you go focus on more high leverage things.

[[00:20:30](https://youtu.be/hl6Ryc_NUm8?t=1230)] So what's the case against that?

**David:**

[[00:20:32](https://youtu.be/hl6Ryc_NUm8?t=1232)] Yeah, so these were two very different moments in my career. When I did the iOS Translate app, I was still relatively junior. I think it was my first year as a TLM at Google. Doing a real engineering project end to end was quite appropriate to keep my skills fully sharp.

[[00:20:54](https://youtu.be/hl6Ryc_NUm8?t=1254)] By the time I was in these org leader roles, it certainly would be pretty damaging if I was trying to code the whole time. There's so much work to be done in those jobs to help the team have the right context to unblock things, to have the right partnerships in place, especially in a large company like Google, to work across the company so that folks know what you're up to.

[[00:21:17](https://youtu.be/hl6Ryc_NUm8?t=1277)] That is the work; that is 95% of where you need to spend your time. I do have this deep belief and experience that carving out a little bit of time and being quite deliberate about it to go and actually work in the same mode as the teams that the managers of managers are running gives you tremendous context.

[[00:21:44](https://youtu.be/hl6Ryc_NUm8?t=1304)] This practice is not new. If you study manufacturing, there is a practice of managers and senior leaders going and working one day a year on the factory floor so they really understand what they're talking about. I think this is applying that already known practice to the software industry.

[[00:22:05](https://youtu.be/hl6Ryc_NUm8?t=1325)] At Stripe, I would take time at least once a quarter, except maybe the final quarter of the year, which is always pretty busy, to go and join a team for a few days and complete a small real project. I called it engineer-acation. It's a portmanteau of engineer and vacation because it was really just a few days.

[[00:22:23](https://youtu.be/hl6Ryc_NUm8?t=1343)] There were a lot of other things that people expected of me in my role, but I could take a few days of vacation and it was fine. Everything continued. For these three days, think of me as being on vacation. If it's a crisis, I'll answer the phone, but if it's not urgent and can wait a few days, just don't bother me because I'm doing this thing. Every single time, I would make a very detailed friction log. Here are all the things that we ran into that were frustrating.

[[00:22:58](https://youtu.be/hl6Ryc_NUm8?t=1378)] That served as great input for me as CTO. I was thinking a lot about how much and where we should invest in developer productivity. I had this visceral sense of how things were going, and it also served as a great resource for me to ask all of the right questions when it came to operational reviews and so forth.

[[00:23:18](https://youtu.be/hl6Ryc_NUm8?t=1398)] That practice was something that I used and encouraged other managers in the organization to use as well. Not everyone did it, but those who did found it incredibly valuable. I think it's a good practice, especially if you're working at a large organization and you're thinking, "I'm getting a little bit out of touch with what's really going on." Do an engineer occasion.

**Ryan:**

[[00:23:40](https://youtu.be/hl6Ryc_NUm8?t=1420)] So if I'm understanding correctly, that first case on the iOS team, you were hands-on, through and through. You were an individual contributor as a manager, right? But the latter thing that you're recommending as an org leader is more of an educational thing for yourself.

**David:**

[[00:23:57](https://youtu.be/hl6Ryc_NUm8?t=1437)] It's important to embrace it as an opportunity to show what you've seen to everyone else. It can give context. I find that the reports I wrote from my engineer occasion were useful, not only for me conveying some context, but also for a bunch of other managers like, "Oh, that's how that thing works."

[[00:24:17](https://youtu.be/hl6Ryc_NUm8?t=1457)] I kind of had this mental model, but I see that it's slightly different, especially as all of the infrastructure we were working on was changing over time. That kind of educational exercise is the heart of the value.

**Ryan:**

[[00:24:28](https://youtu.be/hl6Ryc_NUm8?t=1468)] Eventually, you mentioned transitioning to org leader. You still got involved here and there, but ultimately you weren't hands-on.

[[00:24:36](https://youtu.be/hl6Ryc_NUm8?t=1476)] It's just the nature of the role. To me, you seem like an engineer through and through. Were you ever afraid of losing your technical edge?

**David:**

[[00:24:45](https://youtu.be/hl6Ryc_NUm8?t=1485)] The really short answer here is not really, no, because between opportunities to write bits and pieces of code at work and the ability to invest my free time in programming, I love programming.

[[00:25:00](https://youtu.be/hl6Ryc_NUm8?t=1500)] I get into flow state when I'm programming. If I'm not getting a chance to do a lot of it at work, by the way, right now, I get a lot at work, so I don't need to do very much in my spare time. In fact, I don't have spare time. I just work on the stuff that we're doing, which is fun.

[[00:25:13](https://youtu.be/hl6Ryc_NUm8?t=1513)] If I have spare time and I haven't programmed for a while, then yeah, I'm going to jump in. For instance, the last several years I've been doing Advent of Code in December. It's awesome. I get a chance to make sure that I'm keeping some of those skills sharp.

### **00:25:28 — How to decide on EM vs IC**

**Ryan:**

[[00:25:28](https://youtu.be/hl6Ryc_NUm8?t=1528)] Before we leave the IC versus EM decision, a lot of people in the audience are probably making this decision for themselves or kind of near it. How do you think about what's the optimal way to make that decision?

**David:**

[[00:25:40](https://youtu.be/hl6Ryc_NUm8?t=1540)] The advice you mentioned, which is being a manager and being an IC are different jobs, resonates with me. I've given that advice to many people. If you are considering becoming a manager, the best way to do it is not to try to join it on the side of something you're doing. Try to find an environment where you can do that full time, really focus on it.

[[00:26:21](https://youtu.be/hl6Ryc_NUm8?t=1581)] Put your own IC work to one side so that you can think very carefully and pay a lot of attention to what it takes to make this team the most productive, the happiest, the best version of itself that it can be.

[[00:26:39](https://youtu.be/hl6Ryc_NUm8?t=1599)] When I see people do it that way, they tend to thrive. When they try to do both at the same time, unless it's very carefully structured, it can be harder. If you find yourself at a company that is willing to let you do that on a trial basis and then make the decision, you're very fortunate because many companies don't have that luxury.

[[00:26:52](https://youtu.be/hl6Ryc_NUm8?t=1612)] There are larger companies that will make that possible. If that option is on the table for you, I definitely suggest doing that. Many people I've worked with have let me know that they want to go into management, and often the first thing I do is try to talk them out of it.

[[00:27:12](https://youtu.be/hl6Ryc_NUm8?t=1632)] Sometimes I think this has changed a lot in the industry over the last five years, but certainly if you wind the clock back 10 years ago, there was this weird incentive structure where everyone felt like becoming a manager and managing bigger teams was the prize and therefore I should do that because that's what success looks like.

[[00:27:30](https://youtu.be/hl6Ryc_NUm8?t=1650)] Luckily, a lot of companies, like Google and Meta, have cultivated the idea that the IC career ladder can go all the way up. You don't just have to have these big teams in order to win. Back then, I would see a lot of folks wanting to switch into management because it felt like the right thing to do or the way to progress your career.

[[00:27:49](https://youtu.be/hl6Ryc_NUm8?t=1669)] Being a good manager and feeling fulfillment from the job requires you to take a lot of energy and get a lot of energy from getting more out of other people. That's not for everybody. Really reflect on whether that's something that gets you excited, and if it is, give it a try. If you're in an environment where you can try and go back, amazing. If you aren't, give it a try, and I'm sure there are other ways that things can go in the future.

**Ryan:**

[[00:28:03](https://youtu.be/hl6Ryc_NUm8?t=1683)] You mentioned at Google and Meta there are these parallel tracks and they can go equivalently as deep, but there are differences between the roles and probably differences between the progressions.

[[00:28:16](https://youtu.be/hl6Ryc_NUm8?t=1696)] Let's say you're someone in the audience who's hell-bent on, "I just want to go up." What path would you recommend, or do you have any thoughts on that?

**David:**

[[00:28:23](https://youtu.be/hl6Ryc_NUm8?t=1703)] I'm gonna choose to answer this question differently. When I was an early and mid-career engineer at Google, they had this very clear incentive structure. You start off as a level two, then you become a level three, and then a level four, and it's great.

[[00:28:42](https://youtu.be/hl6Ryc_NUm8?t=1722)] It's like, awesome. I've been put into a game, and now I know that the next thing I need to do is figure out how to get to the next level. I'll be honest, that's what I did for a little while. Luckily, that aligned very nicely with things that I was getting a lot of energy from. But the more I have worked with many people and talked to them about their own experiences, and even later in my own career, what I've realized is the way to have the most fulfillment out of your work is to try and figure out what you want out of it.

[[00:29:15](https://youtu.be/hl6Ryc_NUm8?t=1755)] Is it the flow state from coding? Is it working on something that's incredibly impactful to many people? Is it working with a team that you have a really strong bond with? While many of these companies set up these obvious games to play, take a step aside and try and think, what am I trying to get out of this?

[[00:29:37](https://youtu.be/hl6Ryc_NUm8?t=1777)] It might be to take the next step on the career ladder that's been put in front of you, or it might be to do something quite different. By the time I came to think about leaving Google, I really figured that out and I've reflected on my own work that way ever since.

[[00:29:52](https://youtu.be/hl6Ryc_NUm8?t=1792)] I feel very confident saying I feel significantly more fulfilled for it.

**Ryan:**

[[00:29:57](https://youtu.be/hl6Ryc_NUm8?t=1797)] I think there are so many things to optimize for in career fulfillment, of course, and obviously there are a lot of benefits to it. I still think there are people who will chase the carrot, even if you gave them that advice.

**David:**

[[00:30:14](https://youtu.be/hl6Ryc_NUm8?t=1814)] That's okay because the carrot for them is the thing that they want to chase. I think it's just make sure you're chasing the right carrot.

### **00:30:36 — Biggest gap in managing managers**

**Ryan:**

[[00:30:22](https://youtu.be/hl6Ryc_NUm8?t=1822)] At Google, I understand that you went from an entry-level IC all the way to VP of engineering, and you must have a very unique perspective because almost no one gets promoted to levels of that height.

[[00:30:36](https://youtu.be/hl6Ryc_NUm8?t=1836)] I want to ask you, because you went through levels of management. I wanted to hear your perspective on the differences. The first step is frontline manager versus manager of managers. When you made that jump, what was your biggest skill gap?

**David:**

[[00:30:56](https://youtu.be/hl6Ryc_NUm8?t=1856)] I actually think that my early career as a manager at Google taught me a lot of the wrong lessons.

[[00:31:02](https://youtu.be/hl6Ryc_NUm8?t=1862)] Something you can do as a manager of one team is to do everything you can to make that team happy. That is not the same thing as getting the best impact out of that team. It may not be the case that they look back on that time as the best time of their career.

[[00:31:19](https://youtu.be/hl6Ryc_NUm8?t=1879)] I think that's what I did as an early manager at Google. I won this thing called the Great Manager Award when I had a single team reporting to me, which was a pretty prestigious award inside of Google. I'm grateful to the folks that put that together because it's a nice program of investing in those folks.

[[00:31:38](https://youtu.be/hl6Ryc_NUm8?t=1898)] I don't think I deserved it. The reason is that award was voted for by the teams. Whichever team gave the most votes to their manager, that manager got the Great Manager Award. What I learned later, especially as I started managing managers, was that those teams that are perfectly happy are rarely performing at their very best potential.

[[00:32:04](https://youtu.be/hl6Ryc_NUm8?t=1924)] In order to have the biggest impact, it's really important to make sure that low performers are being managed. You can't make a whole team happy without ensuring that they feel surrounded by folks that are all pulling their weight. As a manager of managers, you start to realize, here's a manager in my orbit who has a really good sense of what we're trying to do, is good at moving distractions out of the way, and will push the team a little bit to fulfill the most impact they can.

[[00:32:37](https://youtu.be/hl6Ryc_NUm8?t=1957)] Here's someone else that is doing what I used to do. The answer for me was to help them get more out of the team. As I became a manager of managers, I stepped onto that balcony I talked about earlier, much more and reflected on how this entire group of people is configuring themselves to get the most out of everybody.

[[00:33:01](https://youtu.be/hl6Ryc_NUm8?t=1981)] The tools you have available as a manager of managers change. As a line manager, I need to have the right one-on-ones, the right one-on-one docs, and the right goal set for the team to make progress. You also want to get into the craft a little bit with folks to help them. Once you're a manager of managers, you can start to think about the systems we're running in this organization that will help us achieve our goals best.

[[00:33:21](https://youtu.be/hl6Ryc_NUm8?t=2001)] How do we do things like product reviews? How is our hiring process working? Only in some companies can managers change that. I've been lucky enough to be at each stage in a state where I could do that. You really start reflecting on not just how you show up day to day, but what tools and systems you're putting in place for the organization.

[[00:33:55](https://youtu.be/hl6Ryc_NUm8?t=2035)] As a software geek and a distributed systems geek, I find it quite exciting to think about the organization I was running as if it were a little bit of an operating system. How do all the things we do every day, week, month, quarter, and year fit together to help us get the most out of everybody? That's just a whole new toolkit that you don't think about when you're a line manager.

**Ryan:**

[[00:34:17](https://youtu.be/hl6Ryc_NUm8?t=2057)] Am I understanding correctly that if a team is too happy, that's actually a red flag for you?

**David:**

[[00:34:23](https://youtu.be/hl6Ryc_NUm8?t=2063)] I'm not saying I want anyone to be unhappy. A key trait of the organizations I aspire to build is that I'd be very happy to do any of the jobs in the organization.

[[00:34:35](https://youtu.be/hl6Ryc_NUm8?t=2075)] I really mean that. I find over time that when I compare the teams reporting the greatest happiness to the teams reporting pretty happy but with feedback on things that could go better, it is usually the case that if I grab the same people a year later and ask them how it was, the folks that were not perfectly happy and had a desire to change things tended to have had the best time in retrospect.

[[00:35:13](https://youtu.be/hl6Ryc_NUm8?t=2113)] At Stripe, I learned about this thing called type two fun. It's the fun that you think of as some of the best times in your life when you look back on it, but it's kind of hard in the moment. As a manager, I want to create a lot of type two fun for the teams I work with.

[[00:35:33](https://youtu.be/hl6Ryc_NUm8?t=2133)] It doesn't mean it's not going to be a good sustainable experience, but let's look back on it and think we got a lot done in that time. Does that make sense?

**Ryan:**

[[00:35:40](https://youtu.be/hl6Ryc_NUm8?t=2140)] That makes sense. I think that's a really interesting spectrum that you call out in the happiness of teams. It reminds me of a similar concept where teams that are not breaking anything are probably moving too slow.

**David:**

[[00:36:01](https://youtu.be/hl6Ryc_NUm8?t=2161)] It's a great analogy. There should be some balance.

### **00:36:14 — The difference between VP and Senior EM**

**Ryan:**

[[00:36:02](https://youtu.be/hl6Ryc_NUm8?t=2162)] You know, we talked about frontline manager versus manager of managers. Now I'm curious about the step that very few people ever experience, which is you went through senior management all the way to VP.

[[00:36:14](https://youtu.be/hl6Ryc_NUm8?t=2174)] What's the difference between your role as a senior manager versus when you are a VP?

**David:**

[[00:36:20](https://youtu.be/hl6Ryc_NUm8?t=2180)] I think this probably takes different forms for different individuals. For me, the thing that defined the difference between being a VP at Google and being a very senior manager was that I took on responsibility for leading functions beyond engineering.

[[00:36:37](https://youtu.be/hl6Ryc_NUm8?t=2197)] By the way, my title was VP engineering, but by that stage at Google, we didn't pay a lot of attention to the exact job family you were in. It's all about getting a thing done. What's the full set of skill sets that have to come together to make this happen?

[[00:36:53](https://youtu.be/hl6Ryc_NUm8?t=2213)] That does change your perspective. For me, it changed my perspective quite a lot. Much earlier in my career, I had tended to think Google was a classically engineering-first company. I had tended to think of all the other functions as existing to feed the engineers to help us all have impact.

[[00:37:14](https://youtu.be/hl6Ryc_NUm8?t=2234)] Not true. If you are working in an environment where you don't have the other functions to help ensure that you're solving the right problem, getting the right user input, and having the right business deals in place for a lot of impact, you're going to have much less fun and much less impact on the world.

[[00:37:32](https://youtu.be/hl6Ryc_NUm8?t=2252)] I hadn't really understood that until I was put in the position of leading multiple functions. It is quite a mental transition. There are much better engineers than me that work on my team today and have worked in most of my teams all along. When you're managing a function you have been part of before, you have a visceral understanding of how to do the work, which is valuable.

[[00:37:58](https://youtu.be/hl6Ryc_NUm8?t=2278)] I have designers who report to me. I can tell you I am a pretty poor designer. If you put me in Figma, I will not do a very good job. Yet I have to figure out how to be a good manager and leader of those folks. It turns out I care a lot about design and can have really good high-bandwidth conversations about a lot of the work, but it took a real adjustment for me to feel some confidence in that when I knew I would not be able to jump into any seat in the organization and perform the job.

[[00:38:31](https://youtu.be/hl6Ryc_NUm8?t=2311)] That was a little bit of a personal confidence thing, as well as a whole new set of problems to solve. That was the biggest transition in that jump in my career.

**Ryan:**

[[00:38:42](https://youtu.be/hl6Ryc_NUm8?t=2322)] Did you ever consider that engineer-acation, but for the other roles?

**David:**

[[00:38:48](https://youtu.be/hl6Ryc_NUm8?t=2328)] Yeah, so I've actually done it at Stripe.

[[00:38:51](https://youtu.be/hl6Ryc_NUm8?t=2331)] I had a team which was part of the technology org that built tools for sales, super important for a company like that. I wanted to understand better how these tools were being used. So I actually did at one point do the equivalent. I called it a sales-acation. I shadowed a couple of salespeople within the org.

[[00:39:11](https://youtu.be/hl6Ryc_NUm8?t=2351)] Super useful. I was doing that mostly to gain context for how we should prioritize work on the engineering side. But yeah, it's a pretty valuable tool. I wouldn't do it in quite the same way, obviously. For instance, if you asked me to do a design occasion, I think I would have to do it more as a kind of shadow someone than jump in and do all the work myself.

[[00:39:34](https://youtu.be/hl6Ryc_NUm8?t=2374)] But it's a useful tool.

### **00:39:36 — How to communicate well**

**Ryan:**

[[00:39:36](https://youtu.be/hl6Ryc_NUm8?t=2376)] In a previous interview, you had mentioned that communication is incredibly important for senior engineering leaders. What are your thoughts on how to get better at communication?

**David:**

[[00:39:49](https://youtu.be/hl6Ryc_NUm8?t=2389)] So there's two forms of communication at least, writing and speaking. So let's start with speaking.

[[00:39:57](https://youtu.be/hl6Ryc_NUm8?t=2397)] The number one way to get better at speaking to large audiences is practice. I remember very early in my career being really quite nervous when I had to present to, I think at that time was like the whole Android org or something like that. It's pretty hard when you're nervous to think clearly about what you're saying and communicate it naturally.

[[00:40:23](https://youtu.be/hl6Ryc_NUm8?t=2423)] I was very fortunate to have a super supportive manager at the time who said, yeah, okay, if you want to get better at this, we'll just give you more at bats. Essentially it was in London, so they didn't say that. More chances to practice this. I got sent along to speak to whole auditoria of Google customers.

[[00:40:45](https://youtu.be/hl6Ryc_NUm8?t=2445)] I was working on ads stuff at the time. I remember doing one of those in an office near King's Cross in London and looking out into the crowd. It was one of the first I'd done with maybe a thousand people in the crowd, and I was to give a live demo and an inspirational talk about local ads.

[[00:41:02](https://youtu.be/hl6Ryc_NUm8?t=2462)] It was really scary. But I did it. There's actually a video of it on YouTube. I look back on that and think about how today I probably do a much better job, but getting the reps in is what makes that go well. Then there's communicating in writing. This is something I'm definitely still learning to do better today.

[[00:41:23](https://youtu.be/hl6Ryc_NUm8?t=2483)] I use Claude a lot to help with that. But I think if you can condense the most important things you need to convey into a short, clear document, that can be incredibly valuable. I can talk to one person and it takes a certain amount of time. I can talk to a whole audience of people and maybe 30% are really paying attention.

[[00:41:49](https://youtu.be/hl6Ryc_NUm8?t=2509)] If you get a really good document out there, people will pass it to each other. They'll read it once, they might come back to it again later. It's an incredibly leveraged way to communicate at scale. But I also think you have to do both of these things. I think people like to listen to folks that they feel like they have some kind of personal relationship with.

[[00:42:12](https://youtu.be/hl6Ryc_NUm8?t=2532)] The personal relationship really only comes from live conversations. Once a strong personal relationship has been established, it becomes really easy and scalable to read things and take it from there.

**Ryan:**

[[00:42:27](https://youtu.be/hl6Ryc_NUm8?t=2547)] There are a lot of people that speak a lot, but I don't think they speak like you do.

[[00:42:34](https://youtu.be/hl6Ryc_NUm8?t=2554)] I watched you give a keynote in 2019 for Stripe Sessions, and you came onto stage and immediately within a second I'm like, this guy's confident. He knows what he's saying. There's something different about the practice that you did, 'cause there are managers who speak all the time, but I've been to many all hands where people are zoning out.

**David:**

[[00:43:00](https://youtu.be/hl6Ryc_NUm8?t=2580)] Well, I appreciate you saying that.

[[00:43:02](https://youtu.be/hl6Ryc_NUm8?t=2582)] I mean, look, I am enthusiastic about what I do, and I think hopefully a little bit of that comes through in how I speak. It really is the case though, that if you had tried to put me on that Stripe session stage in 2012, you would've had a completely different conclusion. You would've thought that guy seems a bit out of his depth.

[[00:43:22](https://youtu.be/hl6Ryc_NUm8?t=2602)] It was the practice that helped with those things. I credit the manager who said, you need to practice this a lot, and I can see that there's something there, so let's go get it done. One other thing I want to say in speaking is it's not just about giving these big keynote presentations.

[[00:43:37](https://youtu.be/hl6Ryc_NUm8?t=2617)] One thing that happens as a relatively senior leader is you're essentially always on stage as you walk around the building in the office. Folks pay a lot of attention to how you're doing. They'll take a lot of their own confidence in the plans of the company from the body language of the CTO.

[[00:43:54](https://youtu.be/hl6Ryc_NUm8?t=2634)] I find myself keeping that in mind a lot. I wasn't ever putting on a weird face or whatever, but that means hallway conversations or this random meeting you're in, it's another opportunity to remind people of what we're doing and why we're doing it.

[[00:44:13](https://youtu.be/hl6Ryc_NUm8?t=2653)] Using all of those opportunities to convey an overarching message was something I learned over time was important and valuable. It's also important to have some dynamic range in how you talk about things. If everything's awesome all the time, everyone knows that everything's not awesome all the time, so no one's gonna believe you when it is awesome and no one's gonna believe you when it's not.

[[00:44:42](https://youtu.be/hl6Ryc_NUm8?t=2682)] I find it valuable to take a moment before I open my mouth in any meeting, whether it was one person or a hundred people, and think, what am I actually trying to communicate here and make sure that I'm using the dynamic range?

**Ryan:**

[[00:44:55](https://youtu.be/hl6Ryc_NUm8?t=2695)] A lot of engineers who get into leadership roles are tasked with giving their top of mind in all hands, et cetera.

[[00:45:02](https://youtu.be/hl6Ryc_NUm8?t=2702)] I think 95% of those, if not more, everyone's got their laptops out and most of the message is falling flat. Do you have any tips on how that manager can do storytelling in a way that the org is actually gonna pay attention?

**David:**

[[00:45:21](https://youtu.be/hl6Ryc_NUm8?t=2721)] Yeah. Number one, prepare. I have made this mistake many times where I'd be told, oh, just show up and give us a bit of your top of mind.

[[00:45:29](https://youtu.be/hl6Ryc_NUm8?t=2729)] I'm like, okay, great. I'll show up and give you what's on top of my mind. It's like, oh, what's on top of my mind right now is that I'm kind of hungry, and I'm not gonna say that. It's incredibly important to prepare. Think about what is the most useful context for that audience to hear about and put some thought into it.

[[00:45:47](https://youtu.be/hl6Ryc_NUm8?t=2747)] They're all spending 15, 20 minutes of their time listening to you. The least you can do is spend 30 minutes of your time preparing. One thing two is there was a leader at Google called Alan Ti. I think he was VP of all engineering at Google when I was an entry-level engineer who always did this amazing thing.

[[00:46:05](https://youtu.be/hl6Ryc_NUm8?t=2765)] When he would come up to answer questions or explain things, he'd be asked a question and rather than just answer the question, he always took the time to take one step back and explain the context behind the question and why it might matter, so that folks who weren't immediately familiar with the problem at hand could actually both understand what was going on and learn something broader from that.

[[00:46:32](https://youtu.be/hl6Ryc_NUm8?t=2792)] I aspire to be like Alan. I'm certainly not that good, but that really stuck with me. That's part of the take a beat. Is it possible to take a step back and explain the context behind what you're about to jump into? It always makes it easier for folks to pay attention.

[[00:46:53](https://youtu.be/hl6Ryc_NUm8?t=2813)] Certainly if you're talking about something that people have no idea what it is, they're never gonna pay attention. It also helps with a bit of a storytelling arc, which is like, first of all, let me tell you why this matters. Then let me tell you the thing, maybe there's another detail. And then let me remind you what I just told you.

**Ryan:**

[[00:47:10](https://youtu.be/hl6Ryc_NUm8?t=2830)] For writing, the thing you called out was condensing the writing. Yeah. You recently wrote this post about agents crossing a chasm, and I scroll to the bottom of it, and it says, you know, Ari Grant, a bunch of these people had reviewed it.

[[00:47:27](https://youtu.be/hl6Ryc_NUm8?t=2847)] How important are the people reviewing your writing in that process of condensing?

**David:**

[[00:47:33](https://youtu.be/hl6Ryc_NUm8?t=2853)] Yeah. This is something I learned at Stripe. I used to write blog posts and just throw them out onto the internet, and I'd get pretty good feedback about them. Sometimes there's one about a neural network controlled car that I wrote that got a lot of coverage, but I would see people at Stripe writing really good documents and crediting the people who'd reviewed them.

[[00:47:53](https://youtu.be/hl6Ryc_NUm8?t=2873)] I was like, oh, that's interesting. I started sending drafts of things that I thought were important to other people, and it improved the quality of my writing immensely. As an author of a piece, you always have a mental model of what am I trying to convince someone of or convey? What might they already know?

[[00:48:13](https://youtu.be/hl6Ryc_NUm8?t=2893)] It's quite common that I would share something I've written with a friend or former coworker and be completely blown away by the feedback they give me in terms of like, it would surprise me. It's like, oh, I wouldn't have thought you would've asked that question. Then you can go back and adjust your draft.

[[00:48:29](https://youtu.be/hl6Ryc_NUm8?t=2909)] To be clear, you don't need to do this for every email. That would be a waste of time. But for something that you think is an important piece of information, it's incredibly useful to run it by some people.

### **00:48:42 — How managers can scale themselves**

**Ryan:**

[[00:48:42](https://youtu.be/hl6Ryc_NUm8?t=2922)] Before we leave, just general management practices, we talked a little bit about scaling yourself and you said it was especially important as a senior manager and hire. What are those high leverage ways to scale yourself, aside from coaching your direct reports?

**David:**

[[00:48:59](https://youtu.be/hl6Ryc_NUm8?t=2939)] Yeah, so I alluded to this. One of the tools in your toolkit as you become quite senior is to start thinking about how the organization works, the rituals, the processes. By the way, when I was an early career engineer, I used to think that the word process was kind of a dirty word. In fact, it's symbian.

[[00:49:17](https://youtu.be/hl6Ryc_NUm8?t=2957)] Since the company doesn't exist anymore, I feel a little comfortable sharing some of the stuff that wasn't so good. They had this thing called a process library. If you were doing anything at the company, you were supposed to go to the process library and look up the process and then follow it. I think this was part of ISO 9,001 certification or something, which is like this British, maybe it's international quality certification.

[[00:49:36](https://youtu.be/hl6Ryc_NUm8?t=2976)] Anyway, everyone was supposed to do that. Of course, nobody did that because you're just like, well, I know what I need to get done. I'm under a lot of pressure. Gotta move, right? But sometimes afterwards someone would come along and ask you, "Hey, show me the documentation of how you followed that process."

[[00:49:49](https://youtu.be/hl6Ryc_NUm8?t=2989)] So, you know, you grab it and fill it out. I never really heard the word process before and I thought a process was kind of a joke honestly. Then I find myself being an organizational leader and someone told me, "David, just really think about the processes in your organization." I was like, oh my God, no. Then I realized, hang on a second, think from first principles here. What are they actually talking about? They meant the rituals and how we work and how we get stuff done. Leaning into getting those set up right is incredibly impactful.

[[00:50:20](https://youtu.be/hl6Ryc_NUm8?t=3020)] For instance, one of the things that I did with the help of some folks who reported to me at Stripe was set up a set of meetings, which we called ops review, which nested in the org. There was a weekly one that I ran and looked at the most important stuff, but there was a nested set of them that ran across all of the engineering teams and the whole company.

[[00:50:43](https://youtu.be/hl6Ryc_NUm8?t=3043)] That was a really valuable tool to help the whole company pay attention to and improve on a whole bunch of things like reliability and efficiency that would have been very hard to impact through just talking to your directs and having it trickle down.

[[00:51:04](https://youtu.be/hl6Ryc_NUm8?t=3064)] So that's the main tool.

**Ryan:**

[[00:51:05](https://youtu.be/hl6Ryc_NUm8?t=3065)] You mentioned hating processes, and I think that's pretty common among engineers. How do you decide when the process is net positive versus net negative?

**David:**

[[00:51:16](https://youtu.be/hl6Ryc_NUm8?t=3076)] I think as someone who is in control of our process or is responsible for running it, your job is to make sure that it only exists as long as it is clearly a net positive for everyone responsible for operating within it.

[[00:51:32](https://youtu.be/hl6Ryc_NUm8?t=3092)] There's a really interesting organizational design aspect here because in some companies, I'm not talking about Stripe here. I think we did a really nice job of it. In some companies, there will be a person who's responsible for executing and overseeing the process that is not actually the person that cared about it existing in the first place or even brought it in to solve a particular problem.

[[00:51:54](https://youtu.be/hl6Ryc_NUm8?t=3114)] Because it's their thing and it's kind of their job, it's very hard for them to say, is it actually fit for purpose? Running large organizations, our jobs are to make sure that we just don't do that. There's always tons of work for everyone to do, so no one should feel like they're boxed into continuing a thing for no particular reason.

**Ryan:**

[[00:52:15](https://youtu.be/hl6Ryc_NUm8?t=3135)] But how do you prevent that if you're the VP or the manager and you say, okay, we need a sev review process? You go to some tech lead and you say, "Hey, this is your thing."

**David:**

[[00:52:29](https://youtu.be/hl6Ryc_NUm8?t=3149)] Now I can tell you worked at Meta. You call them Sevs.

[[00:52:32](https://youtu.be/hl6Ryc_NUm8?t=3152)] Sevs incidents. It's all the same thing.

**Ryan:**

[[00:52:33](https://youtu.be/hl6Ryc_NUm8?t=3153)] Yeah, yeah. Well, that person that was just handed this thing top down is unlikely to be passionate about it and really think critically about whether this is net positive. But how did you get them to care about the process?

**David:**

[[00:52:46](https://youtu.be/hl6Ryc_NUm8?t=3166)] I think it's possible to build teams of program managers that are really passionate about the why behind what they're doing.

[[00:52:52](https://youtu.be/hl6Ryc_NUm8?t=3172)] The program management group was something that I helped set up at Stripe, and I feel pretty confident saying that the vast majority of folks there were really just making sure that we were doing the right thing and very focused on impact for Stripe's users. A lot of that, by the way, comes from company culture.

[[00:53:14](https://youtu.be/hl6Ryc_NUm8?t=3194)] Stripe has a set of operating principles and the first one of those is users first. Everyone is always looking through the work they're doing to say, why does this matter? That's something I think is very precious there, and I think makes sense for, I certainly bring that mentality to what I'm doing at this company as well.

**Ryan:**

[[00:53:33](https://youtu.be/hl6Ryc_NUm8?t=3213)] Makes sense. I could see the culture of the people you are delegating to is important, but also probably how you delegate is important. If you gave the context behind why it's impactful.

**David:**

[[00:53:46](https://youtu.be/hl6Ryc_NUm8?t=3226)] That's a good observation. If you tell someone, "Do this well," what else can they do?

[[00:53:51](https://youtu.be/hl6Ryc_NUm8?t=3231)] But do that. If you tell them, "Here's the problem we're trying to solve and I think that we should probably do this, you go do it and please take agency in making sure that we're really solving the real problem," you have completely different outcomes.

### **00:54:08 — How to build a new engineering site**

**Ryan:**

[[00:54:03](https://youtu.be/hl6Ryc_NUm8?t=3243)] One topic that I want to touch on, and this is something that Philip mentioned.

[[00:54:08](https://youtu.be/hl6Ryc_NUm8?t=3248)] Philip is, there was another podcast that I did. He was the site lead for Facebook in London. He said, "Who did he talk to that gave the best advice on how to start that site?" It was David Singleton. It was you. Wow. He said you had a track record of doing it and you had learned about doing that at Google. At the same time, I imagine there's a lot of AI companies today that probably started in San Francisco. They're probably thinking about scaling up. How do you get a remote location to carry the right culture so that it's successful?

**David:**

[[00:54:49](https://youtu.be/hl6Ryc_NUm8?t=3289)] Yeah. Well, Philip Su was the Facebook London engineering site leader, and I was the Google London engineering site leader at the same time. We found ourselves in this fierce battle for talent, the number of times that we both had offers with candidates.

[[00:55:06](https://youtu.be/hl6Ryc_NUm8?t=3306)] We would realize we had both been talking to the same person a lot. Eventually, Philip reached out to me and said, "Hey, seems like we should probably talk," which was amazing, and I really respect that. One thing I love about Silicon Valley, which exists right here in literal Silicon Valley, but also is kind of a state of mind of these ambitious tech companies, is the idea that even some of the fiercest competitors will help each other in the craft. That's what Philip and I were doing back then. I think we were genuinely able to help raise the bar for engineering in general in London.

To get back to your actual question about the right way to set up effective remote sites, there are a couple of different things. I have a lot of experience running a site that was quite far from headquarters. Google's headquarters were in Mountain View, and I was running this site in London. That distance means it's a lot of time zones away, so the overlap during the day is very small. You have to think about that quite carefully.

[[00:56:10](https://youtu.be/hl6Ryc_NUm8?t=3370)] When I was at Stripe, we had a very vibrant engineering site in Seattle. It was a completely different setup because it's in the same time zone, and therefore you can do different things. In the setup where you're quite far away, it's important to think about how to enable the team on the ground in London to unblock themselves as much as possible and run as autonomously as possible so they can use that little overlap in the day with the folks in California for as few things as possible.

[[00:56:48](https://youtu.be/hl6Ryc_NUm8?t=3408)] Then they're just going to be able to make more progress. What I pushed very hard on was that every team in London engineering had to have a clear and complete mission. They needed to know what they were doing at a very high level, like this is the goal. They were given a lot of autonomy and all the equipment to execute that pretty autonomously. For eight hours of the day when Mountain View's not around, everyone's just cranking along. A few things come up that you need to reach out to another team for, and you can solve them in that little time overlap.

[[00:57:23](https://youtu.be/hl6Ryc_NUm8?t=3443)] The worst way to set up a team like that would be to have half the team in Mountain View and half the team in London because then you come up with a hundred things every day where two people need to have a conversation to unblock it. There are so many of them that you can't make progress in that little time window, and progress grinds to a halt.

For those teams, that's the right setup. The other thing I realized was that the engineering site lead for Google London before me didn't spend very long in London. I remember asking him, "Hey Shannon, why are you never here?" He said, "You have to understand the best thing I can do for London is be in Mountain View, creating good personal relationships with all the people whose work we are part of, making sure they know what we're all up to, and then bringing a lot of context back here to enable us all to operate very autonomously." He was right. I appreciated what he did for us all, and I tried to do the same thing later when I was in the other position. I would travel a lot to California so everyone else didn't have to. They could if they wanted to. This was a different era where that was always possible at Google.

[[00:58:45](https://youtu.be/hl6Ryc_NUm8?t=3525)] A big part of that job was just making sure the team is visible and that the capabilities of the team are very clear so that folks understand if they need to implement something like a mobile browser feature, there's actually a team of experts at the Google London org who used to work on the WebKit project or whatever. Just making sure that context is shared. That's the best way to set up sites like that.

I think the other thing is that every effective remote site I've worked with or helped set up always had a little bit of its own culture. It's useful to have a sense of identity because it creates an opportunity for folks to say, "We have a sense of identity, so we can rally around this cause," which means that we will actually spend energy to think about how to help make this better. When you identify with being part of a clan, you think about how to make sure that this set of people has a great experience. If you don't have that, the little pieces of friction that people run into may not feel like they ladder up to something worth addressing.

[[00:59:48](https://youtu.be/hl6Ryc_NUm8?t=3588)] When there is a sense of identity, it's worth leaning into, and that makes the whole team much more productive. However, it is not a good idea to have a radically different culture from the company you are part of because the whole point is that everyone is part of that company. If you start feeling like everyone on the other side of the ocean is a bozo, you're never going to have a good time at work. The trick is to have enough of an identity that folks think about collectively helping each other and make sure that identity is rooted in the culture of the whole company because that's what everyone is there for. Those are some of the things I talked with Philip about back then.

**Ryan:**

[[01:00:28](https://youtu.be/hl6Ryc_NUm8?t=3628)] And when you say culture, you don't just mean Google. You mean Google London. Google London. Yeah. Like you're a clan, like a specific group.

**David:**

[[01:00:37](https://youtu.be/hl6Ryc_NUm8?t=3637)] We made t-shirts, we had logos that we put on our laptops, and we would get together and talk about what kind of work this site was really good at and what we would like to see more of.

[[01:00:49](https://youtu.be/hl6Ryc_NUm8?t=3649)] I could make sure that when I was spending time in California, I was talking to folks about that to see if we could create those opportunities.

**Ryan:**

[[01:00:55](https://youtu.be/hl6Ryc_NUm8?t=3655)] If I'm understanding correctly, the earlier part was, the further away the time zones are, the more independently you'd want each site to be to execute.

**David:**

[[01:01:06](https://youtu.be/hl6Ryc_NUm8?t=3666)] That's right.

**Ryan:**

[[01:01:06](https://youtu.be/hl6Ryc_NUm8?t=3666)] When COVID happened, there was this big move towards remote being more acceptable as a collaboration model. Now that you're starting your own company, when you think about teams in this post-COVID environment, which one do you think is optimal? Do you think a team purely in person is better? Do you think full remote is best? Is hybrid best? What are your thoughts on that?

**David:**

[[01:01:30](https://youtu.be/hl6Ryc_NUm8?t=3690)] At Stripe, we had a remote hub well before COVID. We recognized that there is amazing technical talent everywhere. Certainly, all across the US, there are amazing engineers that are not in San Francisco, New York, or Seattle.

[[01:01:50](https://youtu.be/hl6Ryc_NUm8?t=3710)] We were missing out if we didn't find a way to have great opportunities for those folks to contribute to our mission. We put a lot of thought into what it takes to make a remote team really effective. One of those things is a document-based communication and decision-making culture, which is incredibly valuable.

[[01:02:14](https://youtu.be/hl6Ryc_NUm8?t=3734)] We worked hard to make sure that conversations that happened between individuals on the same team, whether on a video call or in person, got written up for the rest of the team so they weren't left out of the conversation and could follow along. Any critical decisions came with a document, which meant that yes, it's slightly slower to make any given decision. Not always, actually, because the deliberation that you put in writing is often a big part of what makes more effective decisions in the first place. Because every decision was happening in a document, everyone had a chance to understand the context, contribute their ideas, follow along, and be more bought into the decisions once they happened.

[[01:02:57](https://youtu.be/hl6Ryc_NUm8?t=3777)] Those are the most important things to make remote teams work well. If you do them, remote teams can work very well. The other thing I think is important is there is no substitute for spending time together in person to build up personal rapport, but you don't have to spend every single day in person together to make that happen.

[[01:03:16](https://youtu.be/hl6Ryc_NUm8?t=3796)] If you and I went out for a drink and had a chat about all kinds of things, like what we like to do on the weekends, we would come away feeling significantly more bonded and able to do good work together than if we'd never spoken to each other before. If you do that on a cadence, it could be every six months. Teams can then be incredibly effective even when they're not together.

All of these things are worth doing to make remote teams effective, and for certain companies, teams, and circumstances, I think remote can be almost as effective as if you're all just jamming in one spot together. I do personally believe, though, that the very best is if you're actually all jamming in one spot together. I've started a new company; we're very small right now. Maybe we'll talk more about it in a little bit, but we are all here together in San Francisco. For this stage of the company, I'm excited that that's the right model.

[[01:04:12](https://youtu.be/hl6Ryc_NUm8?t=3852)] As the company grows, I'm sure we will revisit that because there are amazing people who won't be able to come and join us to work together in San Francisco. I think it's a balance. It is very hard to build a huge company today without deciding to lean into how to make sure that distributed, which is different offices around the world, and remote, which is folks that are not necessarily able to get in the same room together, work well. It's something that in our industry we all have to get used to and lean into.

### **01:04:47 — What kept him at Google**

**Ryan:**

[[01:04:47](https://youtu.be/hl6Ryc_NUm8?t=3887)] Coming to the end of your time at Google, I saw that after you were promoted to a VP, you remained in that role for two years and five months. My question to you is what was keeping you in that role for that long?

**David:**

[[01:05:07](https://youtu.be/hl6Ryc_NUm8?t=3907)] The short answer is unfinished business. Google made me a VP not long after we shipped the first version of Android Wear, and we had a bunch of really exciting plans and projects that I had already kicked off with a bunch of handset watch manufacturers. I was really excited to see those over the line.

[[01:05:36](https://youtu.be/hl6Ryc_NUm8?t=3936)] That's what kind of kept me there. At that stage, I definitely felt like I was continuing to learn a lot. Part of my whole philosophy for why to stay at somewhere like that for so long is always be learning. I was still learning a lot. I think I was managing some of the new functions that we talked about earlier, so it was awesome.

[[01:05:58](https://youtu.be/hl6Ryc_NUm8?t=3958)] You could easily ask the question, why did you decide to leave Google? There came a year, I guess it was about two years after the moment I mentioned where I realized I was very happy. I have so much respect and appreciation for everything that that company did for me.

[[01:06:16](https://youtu.be/hl6Ryc_NUm8?t=3976)] I was very happy, but I realized if I think about the last year at this company, what I had done was exactly the same as the year before. You could change the code names of all the projects, but it was essentially like turning the crank on the same thing again. I realized I hadn't learned very much, and I'm here to learn, so what's going on?

[[01:06:36](https://youtu.be/hl6Ryc_NUm8?t=3996)] That was the wake-up call. I happened to have some conversations with a good friend, Philip Su, about the possibility of maybe starting a company together. I realized that would be an amazing learning experience. That kind of shook me into the mode of thinking about making the next move in my career.

**Ryan:**

[[01:06:56](https://youtu.be/hl6Ryc_NUm8?t=4016)] That's so interesting because now that I have more of the context, you and Philip were not enemies, but kind of though.

**David:**

[[01:07:05](https://youtu.be/hl6Ryc_NUm8?t=4025)] Definitely in a tussle for the best talent.

**Ryan:**

[[01:07:08](https://youtu.be/hl6Ryc_NUm8?t=4028)] It's just so interesting that actually that's the number one person you were thinking about banding together with for starting a new venture.

**David:**

[[01:07:17](https://youtu.be/hl6Ryc_NUm8?t=4037)] Well, we found that we had a lot of mutual respect for each other. Those were some of the best relationships to form in business. I feel very privileged to have been able to bond with someone that I was sometimes on the other side of the table from.

### **01:07:34 — The story behind joining Stripe**

**Ryan:**

[[01:07:34](https://youtu.be/hl6Ryc_NUm8?t=4054)] You mentioned wanting to start a venture after Google, and I saw in the post that you wrote about leaving Stripe that a company was the thing you were considering doing before you got into Stripe. That's right. I'm curious, what was the company idea? What's the story there?

**David:**

[[01:07:53](https://youtu.be/hl6Ryc_NUm8?t=4073)] I already mentioned that Philip and I bonded and we were talking about the idea of starting a company.

[[01:08:01](https://youtu.be/hl6Ryc_NUm8?t=4081)] We had what I think is a pretty cool idea. I think it's still a cool idea if someone out there wants to build this company, give me a call.

**Ryan:**

[[01:08:07](https://youtu.be/hl6Ryc_NUm8?t=4087)] Would you fund it if someone is trying to start it?

**David:**

[[01:08:10](https://youtu.be/hl6Ryc_NUm8?t=4090)] Sure. At the time, we saw the rise of the gig economy, the Ubers and Lyfts of the world.

[[01:08:17](https://youtu.be/hl6Ryc_NUm8?t=4097)] I had a little side project where I was making journals and wanted to sell them. I found that in order to do that side project, I needed legal help and a graphic designer. It was quite challenging to find those folks. There were some new platforms like Fiverr, where you could get some help.

[[01:08:37](https://youtu.be/hl6Ryc_NUm8?t=4117)] I actually used that for some graphic design. I realized, with this trend towards gig work, it would be really awesome if folks in more professional job families could take advantage of this trend but also benefit from some of the stability, benefits packages, and so forth of actually working for a company.

[[01:09:00](https://youtu.be/hl6Ryc_NUm8?t=4140)] The idea was to make it possible to have fractional folks in those legal and graphic design job families that you could recruit as a company on a platform. They'd be employed by our firm, and we would invest in their professional development. A lot of the stuff we've talked about before, and then they would be able to benefit from diverse work and the career development that you would get if you were working for an in-house firm.

[[01:09:28](https://youtu.be/hl6Ryc_NUm8?t=4168)] We were planning to build that platform. As it happened, we ended up not starting a company at that stage because of complicated personal things. We decided it wasn't immediately the right moment. I ended up spending time talking to the folks at Stripe.

[[01:09:49](https://youtu.be/hl6Ryc_NUm8?t=4189)] What I realized as soon as I spent time with folks at Stripe was that company had, and still has, this incredible mission. Their mission is to increase the GDP of the internet. It really is about helping entrepreneurs start and scale companies to create jobs and enable people to move money in ways they haven't been able to before.

[[01:10:15](https://youtu.be/hl6Ryc_NUm8?t=4215)] That deeply resonated with me. I got into software in the first place by building a very small company invoicing system. I realized that what Stripe does is really important in the world. To my surprise, a lot of what they needed back then to scale the company was things that I'd done before.

[[01:10:36](https://youtu.be/hl6Ryc_NUm8?t=4236)] For instance, I'd run the London Engineering Office at Google, and we were looking to open engineering offices around the world at that time. I had a lot of experience in building new products at Google, and we wanted to do some of that as well. I quickly fell in love with the mission at Stripe and felt drawn to something where I thought I could do something profound for a good number of years.

[[01:11:07](https://youtu.be/hl6Ryc_NUm8?t=4267)] So I joined, and it was awesome.

**Ryan:**

[[01:11:09](https://youtu.be/hl6Ryc_NUm8?t=4269)] In the post, it almost sounds like you went to them for advice on starting the company. That is correct. How did you realize the conversation was turning towards them recruiting you?

**David:**

[[01:11:23](https://youtu.be/hl6Ryc_NUm8?t=4283)] I did first reach out for advice. Someone once told me, anytime you want money, ask for advice, and anytime you want advice, ask for money.

[[01:11:31](https://youtu.be/hl6Ryc_NUm8?t=4291)] At the time, I thought that was such a cynical view. Since then, it's come back to me like, oh, that was actually pretty good advice. I reached out for advice on how to build something. Stripe has this product called Connect, which powers these two-sided marketplaces.

[[01:11:46](https://youtu.be/hl6Ryc_NUm8?t=4306)] It was clearly something we would have wanted to use to build this company. I didn't know that much about the space, so I thought if I reach out to folks at Stripe, I would learn a ton. They'd give me some tips, and maybe they might even invest.

[[01:12:02](https://youtu.be/hl6Ryc_NUm8?t=4322)] That's why I reached out. The first conversation was lots of advice and super valuable, which I appreciated. Patrick, the co-founder and CEO there, said, "Hey, I'm going to be in town soon, so let's get together." I thought we were talking about advice, but from the very beginning of that conversation, I presume he was approaching it as a hiring conversation.

[[01:12:23](https://youtu.be/hl6Ryc_NUm8?t=4343)] I was learning so much about Stripe and felt drawn to the mission that it became immediately obvious to me that this was the next place I wanted for the next chapter of my career. Since then, I have hired a bunch of senior execs. It really is very custom to find and attract the very best senior people.

[[01:12:49](https://youtu.be/hl6Ryc_NUm8?t=4369)] It's important to have a systematic approach, but for almost every person you'll end up hiring that will be a good fit, they're going to be doing something already that they are super committed to and having fun at. You need to find the right way to identify them, get on their radar, start with an advice conversation, and then help them see the opportunity.

[[01:13:10](https://youtu.be/hl6Ryc_NUm8?t=4390)] It's incredibly important to vet along the way to make sure that this person is really going to supercharge the team. There's a real art to transitioning from the getting-to-know-you conversation to figuring out if this could actually be a fit conversation. It's a lot of fun.

**Ryan:**

[[01:13:38](https://youtu.be/hl6Ryc_NUm8?t=4418)] I understand you took the role as head of engineering at Stripe at the time, and then later you grew to CTO. That kind of promotion is probably very bespoke.

[[01:13:51](https://youtu.be/hl6Ryc_NUm8?t=4431)] What is the story behind getting promoted from head of engineering to CTO?

**David:**

[[01:13:57](https://youtu.be/hl6Ryc_NUm8?t=4437)] In actual fact, one thing that I did not care about very much when joining Stripe was my title. I was joining the leadership team, the core leadership team of the company. And that was important to me.

[[01:14:07](https://youtu.be/hl6Ryc_NUm8?t=4447)] That was where I felt like if we were going to get done the things that the company needed done, that was the right spot to be. So that was the most important thing for me: am I landing in a spot where I can actually help and have enough agency to make things happen? I don't think we were ever particularly formal about what the job really was.

[[01:14:27](https://youtu.be/hl6Ryc_NUm8?t=4467)] Later we decided that it made sense to give the job a title of CTO. I think that was mostly in view of it being helpful to the company to signal that I was in that spot, someone worth listening to. That's right around the time that I started running a lot of these company-wide processes I talked about earlier.

[[01:14:51](https://youtu.be/hl6Ryc_NUm8?t=4491)] It was also super valuable for helping me engage with customers and folks outside of the company. It's a pretty natural onboarding: pay attention to internal stuff first once you've got your arms around that and what's the business. In any senior role, no matter whether it's engineering, design, or product, it's really valuable to be able to talk to folks outside of the organization, customers, partners, and so forth.

[[01:15:20](https://youtu.be/hl6Ryc_NUm8?t=4520)] And that's where these titles kind of actually start to matter. I really like that kind of culture where we're not necessarily listened to because we have a title. And that's certainly the culture at Stripe. It's the culture I would seek to build and it's the culture I seek to build here as well.

[[01:15:37](https://youtu.be/hl6Ryc_NUm8?t=4537)] But it's also the case that when you think about interfacing with the rest of the world, this can matter.

**Ryan:**

[[01:15:43](https://youtu.be/hl6Ryc_NUm8?t=4543)] Definitely, I've heard a similar opinion that at a large company, the organizations within the company are almost strangers as well. It's helpful when the director is reaching out as opposed to this person in engineering reaching out; they'll get alignment and stuff like that.

**David:**

[[01:16:02](https://youtu.be/hl6Ryc_NUm8?t=4562)] It makes sense. At one point, I'm rewinding back to Google. When I was made a director at Google, they sent all the new directors off on a training course. They said, "The secret is, it's really directors that run this company," because it was the spot in the organization where all of the detailed plans were being transferred between each other.

[[01:16:30](https://youtu.be/hl6Ryc_NUm8?t=4590)] Knowing that cohort was incredibly valuable. I think there's something to that. You have to think about your org design and who does what. Having some set of people on different scales of organization is going to have different forms. Having a network of people that are making sure there's high fidelity of context being transferred is incredibly valuable.

[[01:16:51](https://youtu.be/hl6Ryc_NUm8?t=4611)] At Google at that time, it was directors.

### **01:16:53 — Comparing and constrasting cultures**

**Ryan:**

[[01:16:53](https://youtu.be/hl6Ryc_NUm8?t=4613)] You mentioned org design, and as a CTO, I imagine that was something you thought about a lot. I see all these famous engineering cultures; Facebook has its own thing with "move fast and break things" and all of these principles. Similarly, Google has its own principles.

[[01:17:11](https://youtu.be/hl6Ryc_NUm8?t=4631)] Amazon has its own principles. I thought it'd be interesting to hear your take on which big tech companies' engineering culture you thought is most well designed and maybe less well designed.

**David:**

[[01:17:24](https://youtu.be/hl6Ryc_NUm8?t=4644)] I'm at a bit of a disadvantage here because I've only worked at Google among the big engineering companies, and I kind of know some of the others by reputation.

[[01:17:33](https://youtu.be/hl6Ryc_NUm8?t=4653)] The culture of Google, which I joined, was phenomenal. It was a place where everyone was there to do big things. There was the ability and the encouragement to try to have a lot of impact. Everyone was given a lot of agency. The one thing I would say is it was not very deliberately designed.

[[01:17:52](https://youtu.be/hl6Ryc_NUm8?t=4672)] To be clear, it wasn't total chaos. There was an org structure, but I think it grew up mostly organically or at least in large part organically. By contrast, there are companies that have been much more deliberate about the structure they put in place.

[[01:18:12](https://youtu.be/hl6Ryc_NUm8?t=4692)] Amazon comes immediately to mind. As we were designing a lot of the org structure and ways of working as we scaled Stripe, I tended to look at companies like Amazon who'd been very deliberate in their design for inspiration. I was very fortunate to have been able to talk to a lot of senior leaders there and get their tips.

[[01:18:32](https://youtu.be/hl6Ryc_NUm8?t=4712)] In fact, the ops review that I mentioned earlier that we ran at Stripe and continues to run at Stripe was very much modeled off of the Amazon one. Charlie Bell was very kind to spend a nice lunch with me and run me through exactly how it worked there. We tried to take the good bits of that that were applicable to the size and culture of Stripe and apply them.

[[01:18:56](https://youtu.be/hl6Ryc_NUm8?t=4736)] Amazon is definitely the company with the very systematic org and operational design that over time I've taken a lot of inspiration from, even though I've never worked there. I joked with a friend recently that I would love to work at each of these companies for one project just to experience what it's like.

[[01:19:19](https://youtu.be/hl6Ryc_NUm8?t=4759)] I love the products that Apple builds, but they famously have this not very transparent within the company culture. It obviously works for them. I think they're also very deliberate about what their org structure is. There's this thing called Apple University; everyone who joins learns how to work in the Apple way. That's really cool. I'd love to experience it to see what I could take from that. That reminds me of that time all the way back at the start of my career where I was working with all these different mobile handset manufacturers and realized there are so many different ways to accomplish the same ends.

[[01:19:48](https://youtu.be/hl6Ryc_NUm8?t=4788)] I'd love to be able to choose from the smorgasbord, but unfortunately I've only worked at one big company and I've only really gone deep with leaders at one other.

**Ryan:**

[[01:19:57](https://youtu.be/hl6Ryc_NUm8?t=4797)] When I look at Stripe's operating principles, I do see the Amazon influence specifically in its users first, and at Amazon, it's customer obsession.

[[01:20:08](https://youtu.be/hl6Ryc_NUm8?t=4808)] I think those are kind of similar.

**David:**

[[01:20:11](https://youtu.be/hl6Ryc_NUm8?t=4811)] I think that's right. Users first is the idea that everything that folks do at Stripe is really focused on understanding why it matters to the user. That's a real maxim that I live by as well. Think through why are we doing what we're doing? What's the ultimate end?

[[01:20:28](https://youtu.be/hl6Ryc_NUm8?t=4828)] Another one of Stripe's operating principles, and by the way, just for folks who may not be familiar with this, operating principles are a little bit different from values. This is something I really respect about the early Stripe team. Once they had found product market fit in their core, which is the payment infrastructure for early stage businesses, they do much more now.

[[01:20:50](https://youtu.be/hl6Ryc_NUm8?t=4850)] But once they found that early stage product market fit, they took a little step aside and thought about what is it about how we're working that makes us most effective. Stripe's operating principles are not abstract; they're very concrete, and they are distilled from the behaviors of the most effective Stripes.

[[01:21:08](https://youtu.be/hl6Ryc_NUm8?t=4868)] That means they've also been mutable over time. They revisit them periodically, not very often because they're pretty stable, but periodically they'll revisit and make sure they're still fit for purpose. One of Stripe's operating principles that really motivated me and sticks with me is being meticulous in your craft.

[[01:21:26](https://youtu.be/hl6Ryc_NUm8?t=4886)] That means taking pride in how well things are done for the sake of how well they're done. Making sure that engineering systems are designed well, making sure that we can offer reliable services to users, taking the time to polish the edges a little bit, and taking the time to get some external people to review a blog post before you publish it. That's all being meticulous.

[[01:21:49](https://youtu.be/hl6Ryc_NUm8?t=4909)] The thing that's interesting about that is a lot of people will look at that and say, does it make any sense? Surely just focus on the cold, hard numbers. It's been my experience that there is something that is hard to quantify that actually has a very dramatic impact on how well products and services that you offer are perceived because you take that time to be meticulous in your craft.

[[01:22:14](https://youtu.be/hl6Ryc_NUm8?t=4934)] I couldn't tell you the number of times that I would meet a Stripe customer, a very large company that had started in Stripe when they were much smaller. The person I would be talking to was often the CTO, and they'd say, "I just gotta tell you, I was the one that did the Stripe integration back in the day. I was so inspired by the error messages on Stripe that I kind of brought some of that energy into our own culture."

[[01:22:29](https://youtu.be/hl6Ryc_NUm8?t=4949)] At Stripe, if you use the API, instead of just getting a 404 not found, which is what every engineer would implement as a first cut, it actually takes the time to run some extra code and say, "Not found, but an object with that ID exists in the other mode." That's the kind of thing that's meticulous in your craft, and people remember it.

[[01:23:02](https://youtu.be/hl6Ryc_NUm8?t=4982)] It ends up being incredibly valuable. All of this is just to say that being deliberate about operating principles, the ways of working that have brought you where you are when you have any form of success is incredibly useful.

**Ryan:**

[[01:23:38](https://youtu.be/hl6Ryc_NUm8?t=5018)] I'm curious, depending on the stage of the company, I could see people thinking that it might be too early to be thinking about those things and maybe go more with that less intentional Google approach that you were talking about.

[[01:23:52](https://youtu.be/hl6Ryc_NUm8?t=5032)] How do you see that with the stage of the company? When do you start thinking about we need to scale this culture?

**David:**

[[01:23:59](https://youtu.be/hl6Ryc_NUm8?t=5039)] Yeah, that's a good question. I'm building a very early stage company right now. I think it matters to care about culture from day one. So my co-founders and I, literally the day that we incorporated the company, went out for a drink and spent some time writing down what we think our values are as we build this company. That's been useful. We've certainly been paying attention to that as we think about the people we're hiring and the ways that we're running things. It's also the case that running an early stage company is an exercise in being smacked in the face quite often. The world will surprise you. It's important to have values that help you know where you might want to compromise and where not. Now at the same time, I think it would be way too early for us right now to kind of spin up a, you know, every week we're going to think about what we can do that contributes to the company culture. It needs to be more organic at this stage. But I do think it's something that, obviously I've worked in much later stage companies as well. I think it's something that you have to be very intentional about all the way through because fundamentally companies are just large groups of people. Nonetheless, you do something to bring large groups of people together and give them a shared sense of purpose and alignment. Naturally, entropy will just take over. If you don't invest in culture, you almost by definition will not have a culture. Of course, there are all these quotes like culture eats execution for breakfast, something like that. I think it's true if you find yourself in an organization that is very intentional about how it works. You just mentioned Stripe, Amazon, they tend to be very effective. Some of the companies I worked at very early in my career were not intentional about this and have not lasted. So I think it matters.

### **01:25:55 — How to set culture**

**Ryan:**

[[01:25:55](https://youtu.be/hl6Ryc_NUm8?t=5155)] How do you concretely, as an engineering leader, enforce culture?

**David:**

[[01:26:00](https://youtu.be/hl6Ryc_NUm8?t=5160)] So, I think there are basically two ways. One is it's important to just be an amazing exemplar of the culture in the first place. It can't just be made up; it has to be authentic. So it is, first of all, important to work at a place where the culture is actually a culture that you really identify with. Then you should ooze it out of every pore. That really helps. I genuinely was at Stripe because I really cared about the mission, users, and helping these businesses start and scale in ways that they otherwise would not. I also cared about being meticulous in our craft and all the other operating principles. It was very hard for me not to just show up, oozing the culture. If I found myself in an environment where the values were not aligned with my personal values, I probably wouldn't be very effective at establishing that culture.

*[Transcript ends here. Remaining sections — Is Stripe too reliable? (01:34:59), Hiring at scale without Leetcode (01:39:36), Lessons learned working with Stripe's leadership (01:44:15), Why leave Stripe (01:46:45), How his AI startup plans to compete (01:51:26), Career reflections (01:55:31), Top book & habit (02:01:05), Advice for younger self (02:04:55) — could not be fetched; the page content was truncated at ~01:26:00 by the fetch pipeline.]*