---
type: raw-transcript
slug: turing-award-winner-nsa-public-key
title: "Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman"
guest: "Martin Hellman"
date: 2026-07-06
url: https://www.developing.dev/p/turing-award-winner-nsa-public-key
fetched: 2026-07-19
complete: true
---

**Episode Title:** Turing Award Winner: NSA, Public Key Cryptography, Crypto Wars | Martin Hellman

**Guest Name:** Martin Hellman

**Publish Date:** Jul 06, 2026

## Host's Intro

Interviewed Martin Hellman recently who was one of the inventors of the Diffie-Hellman key exchange algorithm. I had heard of his name ever since I learned the concept when I studied computer science in college.

Pretty surreal to get to talk to him. He explained some of the key concepts but also it was interesting to hear the stories behind what we learn in the textbooks.

Also, I have a ton of content recorded that I'm working on editing. Several Turing Award winners and programming language creators. I learned a lot during the latter since I basically talked to them as if I was a student curious to learn about programming languages. Excited to share these episode with you all!

## Timestamps

[00:34 - Why his work broke the law](https://www.developing.dev/i/204966592/0034-why-his-work-broke-the-law)

[08:39 - How people did encryption before](https://www.developing.dev/i/204966592/0839-how-people-did-encryption-before)

[18:51 - The crypto wars](https://www.developing.dev/i/204966592/1851-the-crypto-wars)

[26:22 - The story behind Diffie Hellman key exchange](https://www.developing.dev/i/204966592/2622-the-story-behind-diffie-hellman-key-exchange)

[36:48 - Signatures vs key exchange](https://www.developing.dev/i/204966592/3648-signatures-vs-key-exchange)

[43:05 - RSA patent wars](https://www.developing.dev/i/204966592/4305-rsa-patent-wars)

[48:08 - Why inventions happen at similar times](https://www.developing.dev/i/204966592/4808-why-inventions-happen-at-similar-times)

[50:29 - What he worked on after cryptography](https://www.developing.dev/i/204966592/5029-what-he-worked-on-after-cryptography)

[57:31 - His thoughts on death](https://www.developing.dev/i/204966592/5731-his-thoughts-on-death)

[59:40 - Advice for his younger self](https://www.developing.dev/i/204966592/5940-advice-for-his-younger-self)

## Transcript

### 00:34 — Why his work broke the law

**Ryan:**

[[00:34](https://youtu.be/AZLOETBCQM4?t=34)] I saw your initial work in cryptography was potentially breaking laws, or it was kind of in this gray area where the U.S. National Security Agency was kind of not super happy with your work, and there was some conflict with the government. Could you explain what the field of cryptography was like at the time and its relationship to the government and how you got into the field?

**Martin:**

[[00:57](https://youtu.be/AZLOETBCQM4?t=57)] Cryptography is the study of codes and ciphers for keeping information secret. When I started to get interested in this area in 1968, I was at IBM Research just after finishing my PhD. They'd hired Horst Feistel, who you may have heard of, who was the father of IBM's work in this area and really started the unclassified research in cryptography. So I started there. And then I realized when I was teaching at MIT from '69 to '71 that I might actually be able to do something.

[[01:32](https://youtu.be/AZLOETBCQM4?t=92)] I won't go into the details of that right now. And I did it in my own time because I didn't think I was breaking any laws by doing it. I didn't think anybody could make that case. But I realized that there was a part of the government, the U.S. National Security Agency, that would be very concerned about this. And then it was as our work really became visible that they started saying we were breaking the laws.

[[01:59](https://youtu.be/AZLOETBCQM4?t=119)] And that's when I looked into it more carefully. We got a letter in July 1977 from a guy who worked at. We determined he worked at the U.S. National Security Agency. He wrote from his home address in Maryland, which is a good indicator that he works at the U.S. National Security Agency. To the Institute of Electrical and Electronics Engineers, which is the main electrical engineering professional society, saying that as an IEEE member, he was concerned that they were breaking the law by publishing certain papers.

[[02:31](https://youtu.be/AZLOETBCQM4?t=151)] He never mentioned me by name, but I had an article in almost every issue that he mentioned of the IEEE Transactions. The IEEE wrote back to him, copying me. They didn't copy me as Martin Hellman, troublemaker. They copied me as a member of the Board of Governors of the Information Theory Group, which was then publishing most of these papers. And so it's a funny thing that when people start to talk about cryptography, they talk in code all the time.

[[03:01](https://youtu.be/AZLOETBCQM4?t=181)] The NSA was maintaining I was breaking the law by publishing my papers in international journals. The ITAR, the International Traffic in Arms Regulations, which I'd been unaware of up to that point, defines anything cryptographic as an implement of war. And I wasn't exporting an implement of war, which would mean you need a license from the State Department. I was exporting technical data from their perspective on implements of war.

[[03:27](https://youtu.be/AZLOETBCQM4?t=207)] And so that's why I was breaking the law. So I took the letter to Stanford's general counsel at the time, John Schwartz. He said if the laws interpreted that broadly, he thought it was unconstitutional. But that's only his legal opinion. It had to be settled in a court of law.

**Ryan:**

[[03:43](https://youtu.be/AZLOETBCQM4?t=223)] I mean, when you got these warnings, did it deter you at all, or what was your immediate reaction?

**Martin:**

[[03:49](https://youtu.be/AZLOETBCQM4?t=229)] I kind of fell into this at first with Whit Diffie, and I thought that the 56-bit key size of DES, the Data Encryption Standard, was a mistake. We realized that you could break it with exhaustive search. Today, AES, the Advanced Encryption Standard, has a minimum 128-bit key size, which is much, much bigger than a 56-bit key size. Two to the 128th is much bigger than two to the 56th. So we wrote letters.

[[04:20](https://youtu.be/AZLOETBCQM4?t=260)] We thought that they'd change it. It was cheap and easy to change it. And after six months we realized that we had a political problem, not a technical problem. And then we had to decide whether to back down or not. And we went forward because at that point I was invested in this. And also I'm from the Bronx, as I mentioned to you earlier, and I'm a street fighter. Not with my fists, I got beat up a lot, but I'm a street fighter with my mouth and my mind.

[[04:45](https://youtu.be/AZLOETBCQM4?t=285)] And they picked the wrong person, basically. I wasn't going to back down.

**Ryan:**

[[04:51](https://youtu.be/AZLOETBCQM4?t=291)] What could have gone wrong? I mean, would they pursue you with lawyers, or would...

**Martin:**

[[04:55](https://youtu.be/AZLOETBCQM4?t=295)] Oh, I could have gotten killed.

**Ryan:**

[[04:57](https://youtu.be/AZLOETBCQM4?t=297)] You could have gotten killed?

**Martin:**

[[04:58](https://youtu.be/AZLOETBCQM4?t=298)] Oh, yeah, not necessarily by them, but maybe by the GRU, the Russian equivalent. I mean, I wasn't just pissing off the NSA, I was pissing off the Russians, Soviets.

**Ryan:**

[[05:07](https://youtu.be/AZLOETBCQM4?t=307)] Why would they be pissed off?

**Martin:**

[[05:09](https://youtu.be/AZLOETBCQM4?t=309)] Oh, we and the Soviets sold our World War II surplus cryptographic equipment to third-world countries. We'd rather that they were able to break it, and they'd rather that we were able to break it than no one was able to break it. So my mother called me up. My mother was still alive. She died in 1984. And she called me up and said, "What are you doing? You're going to get yourself killed." She was really upset.

[[05:35](https://youtu.be/AZLOETBCQM4?t=335)] Okay, so you get issued the warning, and then you go to the general counsel at Stanford. Then what happens?

**Martin:**

[[05:42](https://youtu.be/AZLOETBCQM4?t=342)] This was July 1977, in I think October. Early October, yes, it was October. There was an IEEE symposium on information theory at Cornell University. And I had two papers there. One with Ralph Merkle, who deserves, I believe, a lot of credit for inventing public-key cryptography, as you probably know, and one with Stephen Pohlig, which really. Stephen and I have a paper which is really the RSA system, except it's mod P instead of mod N.

[[06:12](https://youtu.be/AZLOETBCQM4?t=372)] It's modular prime number instead of modular composite number. We realized that you could do it mod N, but we didn't have public-key cryptography then. Anyway, Stephen and Ralph and I had papers. And John Schwartz said that he strongly recommended that I give the papers instead of the students. I was going to have the students give the papers. And so I went to the students and I told them, look, if you want to give the papers, that's okay, but Stanford's not sure they can defend you, whereas it's clear they could defend me.

[[06:42](https://youtu.be/AZLOETBCQM4?t=402)] And I feel very comfortable going forward with Stanford's financial resources. And the students initially bravely said that they would give the papers. After a week they came back to me. Their mothers were beating on them like my mother beat on me. And they said, "Okay, you give the paper." So when it came time for each of those papers to be given at Cornell, I went up to the podium and I said, "I had the student come up with me."

[[07:09](https://youtu.be/AZLOETBCQM4?t=429)] And I said, normally the student would be giving this paper, but on the advice of counsel, and everyone knew what I was talking about, I will be giving the paper. And I want you to consider, in every way but legally, the words coming from my mouth as if they're coming from his. And so the students got more credit that way than they ever would have if they gave the papers by themselves.

**Ryan:**

[[07:29](https://youtu.be/AZLOETBCQM4?t=449)] It sounds like you had a lot of opposition at the time. Why did you still pursue it?

**Martin:**

[[07:34](https://youtu.be/AZLOETBCQM4?t=454)] Well, my colleagues all told me that I was crazy to work in cryptography. And they had two reasons, one of which was the U.S. National Security Agency has a multibillion-dollar-a-year budget, and they've got a decade's head start. How can you hope to discover something they don't already know? And my attitude was, I don't care what they know. It's not available for commercial use. Even if I only develop things that they know, it doesn't matter.

[[07:57](https://youtu.be/AZLOETBCQM4?t=477)] And yet we developed things that they didn't know about, which is a whole other thing. GCHQ, the British equivalent of the NSA, has claimed that they invented public-key cryptography a little bit before us. Not a lot, by the way. Just around the same time. Except they never had anything on digital signatures. They never had anything that allowed my phone to accept a software update and to use a secret key to sign it, which Apple has, and a public key in the phone.

[[08:26](https://youtu.be/AZLOETBCQM4?t=506)] So even if someone takes the phone apart and gets the public key, that doesn't tell them how to sign future software updates. And GCHQ had nothing on digital signatures, only on the privacy aspect.

### 08:39 — How people did encryption before

**Ryan:**

[[08:39](https://youtu.be/AZLOETBCQM4?t=519)] Prior to the solutions you came up with, how did people encrypt it? How did people encrypt it?

**Martin:**

[[08:46](https://youtu.be/AZLOETBCQM4?t=526)] Encrypt?

**Ryan:**

[[08:47](https://youtu.be/AZLOETBCQM4?t=527)] Yeah. Encryption messages.

**Martin:**

[[08:49](https://youtu.be/AZLOETBCQM4?t=529)] They didn't. No, actually. NSA, GCHQ, GRU, all these foreign United States and foreign intelligence services were sucking up huge amounts of unencrypted data. It was only mining companies and banks that used encryption, and they used very bad encryption.

**Ryan:**

[[09:07](https://youtu.be/AZLOETBCQM4?t=547)] What about during wars and stuff? Sending messages that they didn't want other adversaries to be able to read.

**Martin:**

[[09:16](https://youtu.be/AZLOETBCQM4?t=556)] You're talking about military use.

**Ryan:**

[[09:17](https://youtu.be/AZLOETBCQM4?t=557)] Yeah, exactly.

**Martin:**

[[09:18](https://youtu.be/AZLOETBCQM4?t=558)] Well, that was where the major use had been, in the military. And one of the things I have a talk on the evolution of public-key cryptography. And I start off by saying, I love that. People call it revolutionary. Don't stop saying that. But by the end of this talk, you wonder why it took us so long rather than how we ever found it. And they were almost like big arrows pointing: Go here, go here, go here.

[[09:43](https://youtu.be/AZLOETBCQM4?t=583)] And one of them was Whit and I had come up with the idea of a trapdoor cipher. That was a cipher that was impossible to break unless you knew trapdoor information that went into its design. We've never been able to develop such a cipher, but we realized that was a possibility. And that would be a general's dream, because he could use it. If he knew the trapdoor information, he could use it securely against his adversary in the war.

[[10:10](https://youtu.be/AZLOETBCQM4?t=610)] But his adversary, if they captured it, couldn't use it securely because he knew the trapdoor information and could break it. And from there to public-key cryptography as a minor step.

**Ryan:**

[[10:19](https://youtu.be/AZLOETBCQM4?t=619)] I know there's this famous machine. I think it's called the Enigma machine. And Turing was involved in that. That's some sort of encryption mechanism.

**Martin:**

[[10:29](https://youtu.be/AZLOETBCQM4?t=629)] Basically, it's a World War II. It's the main German field cipher of World War II, the Enigma machine. It was gear-based. And encryption is a special-purpose form of computation. And computation has gotten a hell of a lot better. We do, I don't know, I'm 80 years old. So it's 16 periods of five years. We can do about maybe 10 to the 14th, it's not quite 10 to the 16th times as much computation for a dollar today as we could when I was born at the end of World War II. I was born in '45.

[[11:01](https://youtu.be/AZLOETBCQM4?t=661)] So Enigma, what was the primary computing device of World War II? Gear-based adding machines. What was the primary encryption device? Gear-based encryption machines. Today we can do not only computation much better, we can do encryption much better. In that case, it substituted electricity. You pressed the letter on a keyboard, it generated an electrical signal that went through a sequence of rotors, as they're called, which transformed it into another letter that lit up.

[[11:31](https://youtu.be/AZLOETBCQM4?t=691)] And so you'd set up the key, which was which rotors to use and what order to put them in, and some other things. And then you'd type out the message on the keyboard, and you'd read off the enciphered message on the lights. And Alan Turing, who you pointed out in The Imitation Game, which was the major movie of like five years ago, Alan Turing figured out how to build a primitive form of computer to break the Enigma machine.

[[11:59](https://youtu.be/AZLOETBCQM4?t=719)] Now, the Germans knew Enigma was breakable. They never thought that the Allies would build a computer to break it. And so the Allies were reading German encrypted messages almost as fast, maybe faster than the Germans were. And that's what was different. And as they knew Enigma was breakable, they never realized that. They never thought that we would build a machine like that. And it's interesting, Alan Turing was hounded to death in the 1950s in spite of his wartime activities.

[[12:27](https://youtu.be/AZLOETBCQM4?t=747)] And this is covered in The Imitation Game. In that movie, he was hounded to death because of his homosexual tendencies, or more than tendencies. I mean, he was homosexual. Today we wonder how our parents, grandparents could have been so uncivilized as to do things like that.

**Ryan:**

[[12:47](https://youtu.be/AZLOETBCQM4?t=767)] You mentioned in that talk on the history of public cryptography, there's this. Everything is pointing toward these directions. What did you mean by that?

**Martin:**

[[12:57](https://youtu.be/AZLOETBCQM4?t=777)] Well, I mean, the trapdoor cipher was pointing us toward public-key cryptography. And yet a trapdoor cipher makes perfect sense because almost everything in cryptography involves trapdoors. People usually think of public-key cryptography as a trapdoor cryptographic system. But even a cryptographic system is a trapdoor. And this is fundamentally related to a question called P vs NP or not in computer science.

[[13:26](https://youtu.be/AZLOETBCQM4?t=806)] Are there any problems that are easily checked that are hard to solve? That's basically what that means. If there are any secure cryptographic systems, then there are problems that are easily checked that are hard to solve. For example, one-way function is the simplest form of trapdoor. This is a function that's easy to compute but hard to invert. And this figures importantly in cryptography and blockchains, among other things.

[[13:57](https://youtu.be/AZLOETBCQM4?t=837)] We've all taken trapdoor quizzes where the professor gives you an hour to solve the problem. At the end of the hour, he says, "Pencils down, papers in," and he says, "Oh, we have a few minutes remaining. Let me give you the solution and convince you it's right." That's a trapdoor quiz problem. It's a primitive form. And there the professor has in mind a particular method for solving it, whereas you have many methods.

[[14:23](https://youtu.be/AZLOETBCQM4?t=863)] And a real trapdoor quiz problem would work like this. The professor would say, here's a one-way function. I've generated an X, here's the Y that comes out. You find the X that comes in after a million years goes by. He says, papers down, pencils in. He says, oh, by the way, in the few seconds remaining, let me convince you. Let me give you the solution and convince you it's right. What does he do?

[[14:46](https://youtu.be/AZLOETBCQM4?t=886)] He takes X, he puts it through the one-way function, he gets Y. And you know that he had the right value of X, and yet you could never find it.

**Ryan:**

[[14:55](https://youtu.be/AZLOETBCQM4?t=895)] When I imagine you kind of competing or butting heads with the NSA, I can imagine one solution for them might be to try to recruit you to their side. Did they ever try to recruit you?

**Martin:**

[[15:07](https://youtu.be/AZLOETBCQM4?t=907)] Yes. Early on, before we had public, before we had any good results, I'd go to conferences and I'd give talks on cryptography, which in hindsight were very primitive. And NSA people with name badges that said Department of Defense, which was the simple substitution cipher for NSA, would always ask me. They explained they were at NSA and they'd love to hire me as a consultant because they needed new blood.

[[15:32](https://youtu.be/AZLOETBCQM4?t=932)] And I said, I'd love to know what you know, but only if I can publish my papers independently. And he said, of course not, which I knew was the answer. And so I never took any classified consulting contracts, et cetera, until 1995. There was a National Research Council committee called CRISIS. It's called the CRISIS Report. Cryptography's Role in Securing the Information Society, which comes out as CRISIS.

[[16:02](https://youtu.be/AZLOETBCQM4?t=962)] And that was about 1995. And the question was, were U.S. government regulations helping national security or hurting national security? We concluded that in many ways they were hurting national security. And we had a former deputy director of the NSA on the committee. We had a former Attorney General on the committee, Benjamin Civiletti, who had been Attorney General under Jimmy Carter. We had people like me who were privacy advocates, but who had come around and started to understand how the NSA viewed things.

[[16:34](https://youtu.be/AZLOETBCQM4?t=994)] We had Ray Ozzie on that committee, who was the chief software architect at Microsoft. When Bill Gates retired, he did Lotus Notes. And we reached unanimous conclusions. And one of the most important conclusions we reached was that the classified briefings. I did take a classified. I didn't get paid for that, but I did have a security clearance for that and intelligence coins, which I'd never taken before.

[[17:04](https://youtu.be/AZLOETBCQM4?t=1024)] But I was retiring at that point, and I figured it didn't matter. And it was important for me to be able to, say, get past the people who said, "If you knew what I knew, you'd think differently." And there were people in the unclassified briefings who said, "If you knew what we knew, you'd think differently." But we concluded, and it's in our report, which you can get free of charge on the National Academy, National Academy's website, that the classified briefings helped fill in details, but they did not change our fundamental conclusions.

[[17:39](https://youtu.be/AZLOETBCQM4?t=1059)] And that was one of the most important conclusions we reached. And yet people said, if you knew what we knew, you'd think differently. And yet that was not true.

**Ryan:**

[[17:47](https://youtu.be/AZLOETBCQM4?t=1067)] When they were trying to recruit you, I imagine it would have been very advantageous for them to classify your work.

Oh, yeah, they did. I mean, when you turned down their offer, I imagine they would have had to compensate you handsomely to kind of go to the.

**Martin:**

[[18:04](https://youtu.be/AZLOETBCQM4?t=1084)] I don't. We never got that far. And by the time we had a fight on our hands, it was too late. Basically, I'd committed to see this thing through. And when I realized that my life might be in danger, I might go to jail, although I didn't think about those possibilities very much, and I didn't think they were real, although they may have been. I felt like I was committed and I couldn't back down.

[[18:35](https://youtu.be/AZLOETBCQM4?t=1115)] I mean, what would you do? I kind of fell into it. It's like a friend of mine who was a helicopter pilot in Iraq. He went through ROTC in the late 90s, he said, to pay for his education. There were no wars. He said, why is everybody calling me a hero?

### 18:51 — The crypto wars

**Ryan:**

[[18:51](https://youtu.be/AZLOETBCQM4?t=1131)] When I was doing the research, I kept seeing this mention of the first crypto wars. What are the crypto wars, and how did they play out?

**Martin:**

[[19:00](https://youtu.be/AZLOETBCQM4?t=1140)] The first crypto war was the one we've been talking about, which occurred in the late '70s, early '80s, where NSA threatened to throw me in jail. My life may have been in danger, things like that. And that was over two things. It was over the freedom to publish papers in international journals, which has now been established. And it was over the key size of DES, which is something that people today know almost nothing about.

[[19:24](https://youtu.be/AZLOETBCQM4?t=1164)] As I mentioned before, it was a 56-bit key size. And Whit and I did a quick calculation that you could probably break that for $10,000 even with 1976 technology, 1975 technology. And if we were wrong, Moore's law would, if we were off by a factor of 10, an order of magnitude that would be erased in five years' time because Moore's law was advancing the state of computing by an order of magnitude every five years in those days.

[[19:54](https://youtu.be/AZLOETBCQM4?t=1194)] So that was the first crypto war. It was over the freedom to publish and the key size of DES. The second crypto war, which people don't really remember, was in the '90s and Clipper Chip was a big piece of that. This was the idea that there should be an escrow service, that the government would allow strong encryption, but it would maintain master keys somewhere. And if they got a court order that said that they were able to get into something, they'd be able to do it.

[[20:26](https://youtu.be/AZLOETBCQM4?t=1226)] Well, this sounds great, and it was great from certain points of view, but there were problems with it, like in the National Research Council Committee, the CRISIS Committee that I talked about. We wasted a lot of time talking about key escrow. And then we realized, I may have actually said this, although I think we came to it as a whole. Look, there are major problems with key escrow. How is it going to work internationally?

[[20:49](https://youtu.be/AZLOETBCQM4?t=1249)] Who's going to hold the keys when someone's in France and someone's in the United States, or someone's in Russia and someone's in the United States? So what we said in the report is, we said it very nicely, that we don't see how to solve many of the problems with public key with key escrow. And the U.S. Government should experiment with it, and if they came up with a solution, come back to us, and they never did.

[[21:14](https://youtu.be/AZLOETBCQM4?t=1274)] That was the second crypto war. And Clipper Chip was a chip that had a key escrow built into it. Basically, the third crypto war, which some people may remember, occurred about 10, 15 years ago. It was over things like the San Bernardino Apple iPhone. There were terrorists who committed acts, and they had an Apple iPhone, and the FBI wanted to break into it. FBI, not NSA, wanted to break into it. And they asked Apple to give them the key.

[[21:48](https://youtu.be/AZLOETBCQM4?t=1308)] Apple does not have a key. Ron Rivest is one of the authors of a report called Keys Under Doormats. If you build what they call a backdoor into a cryptographic system to allow access. And that was the third crypto war. It was really a repeat of the second crypto war, the key escrow with a different name. And it's really putting keys under doormats because if Apple can recover one key, they can recover any key.

[[22:16](https://youtu.be/AZLOETBCQM4?t=1336)] And they're going to be asked repeatedly. And there's a danger that if that information gets out there, that all of Apple's devices become insecure. So how do you do it? We don't see how to do it. It's unfortunate, but there is no way to give access. I'd love to give access to the U.S. Government when it had legitimate reason for doing it. I would love to withhold that access from the U.S. Government when it has an illegitimate reason for doing it, which it sometimes does, and from the Russian government, which also would use it illegitimately.

**Ryan:**

[[22:46](https://youtu.be/AZLOETBCQM4?t=1366)] You mentioned DES, 56 bits, was not secure enough. Why would the government want fewer bits?

**Martin:**

[[22:53](https://youtu.be/AZLOETBCQM4?t=1373)] Oh, easy. The government wanted fewer bits because they didn't want a publicly available standard that they couldn't break. They figured that there was a crude form of trapdoor that Whit and I made an estimate in '75, and I refined it when NSA, actually NBS, the National Bureau of Standards, but it was two guys from NSA that we were always communicating with, who had moved over to NBS. We estimated that 2 to the 56 is roughly 10 to the 17th power.

[[23:28](https://youtu.be/AZLOETBCQM4?t=1408)] That's 100,000 million million keys. We estimated that you could build a search chip, even with 1975 technology, that would search a million keys per second, a microsecond per key. And we then said, you wouldn't just build one of these, you'd build a million of them. And now you're searching a million million keys per second. And how long does it take to search 100,000 million million keys? 100,000 seconds, which is about a day.

[[23:54](https://youtu.be/AZLOETBCQM4?t=1434)] It's roughly 80,000 seconds. We estimated that the cost of searching a 56-bit key size was roughly $10,000 per solution in 1975. We were probably optimistic, but as I said, even a factor of 10 optimism would be erased within five years. The crude form of trapdoor was, if I build a machine like that, I can't keep it fully loaded. I don't have roughly 60 problems a month to keep it fully loaded. The U.S. National Security Agency has 60 problems a month to keep it fully loaded.

[[24:29](https://youtu.be/AZLOETBCQM4?t=1469)] And they have the $20 million to build the machine. I don't.

**Ryan:**

[[24:36](https://youtu.be/AZLOETBCQM4?t=1476)] So they would retain access to privileged information through superior computing resources was their hope, and snoopiness.

**Martin:**

[[24:47](https://youtu.be/AZLOETBCQM4?t=1487)] The problem is you and I might want to snoop on one problem a year. How do we do that? Do we wait a year to get a solution? No, we want it quickly, but then it's sitting idle most of the time and our cost goes way, way up.

**Ryan:**

[[25:00](https://youtu.be/AZLOETBCQM4?t=1500)] With modern public key cryptography, anyone can securely message anyone else, and no one can snoop. But that also includes the bad guys as well. What are your thoughts on, I guess, the devil's advocate that says, why do you need to hide something if you have nothing bad to hide?

**Martin:**

[[25:23](https://youtu.be/AZLOETBCQM4?t=1523)] Well, if you want to put all your banking information out there in the public, if you want Apple to sign software updates in ways that bad guys can do, yeah, there's no problem. But we do have reasons for being secure. We don't live in a world where we trust everybody yet. And so there's a fundamental trade-off. You cannot make strong encryption and give it only to the good guys and not to the bad guys.

[[25:48](https://youtu.be/AZLOETBCQM4?t=1548)] It's like cars. If cars had been invented in the classified literature, the government might say, "This is great. We can catch bad guys, we can fight wars, and we can always win them because we have tanks, we have cars, we have things like that." And they've got horses. And now imagine Whit and I invent a car 50 years ago in the unclassified literature. They'd be up in arms. We wouldn't see ambulances, we wouldn't see commuting, we wouldn't see vacations that people could take.

[[26:16](https://youtu.be/AZLOETBCQM4?t=1576)] There's a fundamental trade-off. It's there with cars, and it's there with cryptography as well.

### 26:22 — The story behind Diffie Hellman key exchange

**Ryan:**

[[26:22](https://youtu.be/AZLOETBCQM4?t=1582)] So I wanted to talk about the obviously the big invention that you had, public-key cryptography, the Diffie-Hellman key exchange algorithm. What's the story behind you inventing this Diffie-Hellman, and maybe Diffie-Hellman-Merkle key exchange algorithm? Whit showed up on my doorstep, almost literally speaking, in the fall of 1974.

**Martin:**

[[26:49](https://youtu.be/AZLOETBCQM4?t=1609)] He had been traveling around the country. He'd worked at the AI Lab, the artificial intelligence lab here at Stanford. And he'd done some work on cryptography. He wanted to do more. They could not support it. So he took a small inheritance that he got from his mother, and he traveled around the country. And if you work in AI, if you're known, there are people that will put you up in their garages, in their homes.

[[27:12](https://youtu.be/AZLOETBCQM4?t=1632)] They'll feed you. Maybe John McCarthy lives up the hill. And Whit was a good friend of his. And there was a high school student living in his attic, I think, who was from Cambridge. And I asked him why he didn't just go to the MIT Artificial Intelligence Lab. And he said he didn't like their politics. I don't know what that means. So Whit traveled around the country. And when he was at IBM Research, a secrecy order had descended on them just about this time.

[[27:40](https://youtu.be/AZLOETBCQM4?t=1660)] I'd been there a few months before. They told me they couldn't tell me very much. They told Whit, when he came through, the same thing. But they told him one thing additional: "Oh, when you're back out at Stanford, look up Hellman." So he called me in the fall of '74. And we set up maybe a half hour, hour meeting, max. And it went through the night. They came back here, he and Mary Fischer, his then girlfriend, now wife, then wife.

[[28:08](https://youtu.be/AZLOETBCQM4?t=1688)] She's passed away since then. And we had a real meeting of the minds. It was amazing. And so Whit and I started working together in the fall of '74. The Data Encryption Standard came out. In March '75, it was announced. We came up with the idea of public-key cryptography around then. And we did not know about Ralph Merkle at the time. Ralph was an undergraduate and later a master's student at UC Berkeley.

[[28:37](https://youtu.be/AZLOETBCQM4?t=1717)] And he came up with half of public-key cryptography. He came up with public-key distribution. And I have his paper in which he. In the fall of '74, we didn't know about him then. He was taking CS244, computer security. And he had to do a term project. And he proposes two term projects. One is the privacy half of public-key cryptography. And the other is something much more mundane. And I have the professor's handwriting in blue scanned.

[[29:06](https://youtu.be/AZLOETBCQM4?t=1746)] I've scanned this across the top. That idea number two, the mundane idea, looks much better than idea number one. Maybe because his description of idea number one is so muddled. But Ralph had major problems. So he drops the course. The professor says, "See me today about this." Ralph, instead of seeing the professor, drops the course and goes and does it on his own. He then submits a paper to CACM, the primary Communications of the ACM, the primary journal of the ACM, and it's rejected.

[[29:40](https://youtu.be/AZLOETBCQM4?t=1780)] I have the rejection letter. Susan Graham, who was the editor who rejected it based on a referee's report, writes, "It bothers her that there are no references in the paper. Has no one thought of doing anything like this before?" The answer is no. Now, he still sort of had references. Ralph didn't know how to write a paper at that point. I helped him rewrite the paper, and it was later accepted, but it was actually submitted a little before ours.

[[30:09](https://youtu.be/AZLOETBCQM4?t=1809)] Whit and I came up with public-key cryptography. Ralph came up with public-key distribution. We eventually learned about one another. Afterward, I bring him here in the summer of 76, and I talk to Ralph and I say, have you ever thought of coming to Stanford to do your PhD? And Ralph says, I can't afford it. I said, yes, you can. How about you making it Berkeley as a TA? And I said, I pay you roughly the same as an RA here at Stanford, and your tuition would be covered.

[[30:37](https://youtu.be/AZLOETBCQM4?t=1837)] So he came to Stanford. He did his PhD under my supervision, supposedly, although we really worked together.

**Ryan:**

[[31:31](https://youtu.be/AZLOETBCQM4?t=1891)] It seems like this cryptography space was not so well resourced. I mean, Diffie is kind of going couch to couch to.

[[31:39](https://youtu.be/AZLOETBCQM4?t=1899)] To kind of support himself on this. Ralph's also kind of doing this on his own, fully his own initiative, and people aren't really supporting him throughout. Is that, was that common in cryptography at that time?

**Martin:**

[[31:52](https://youtu.be/AZLOETBCQM4?t=1912)] Yeah, I told you. All my colleagues, and it's not an exaggeration, told me I was crazy to work in cryptography. And one of their reasons was NSA has a huge budget and a multidecade head start. One of them, Jim Omura, who passed away about a year, two years ago, he was a professor at UCLA. I mentioned him to you earlier. Jim told me I was crazy. And the best ideas often seem crazy ahead of time. So I was at Tom Kailath 10 years ago.

[[32:20](https://youtu.be/AZLOETBCQM4?t=1940)] I was at Tom Kailath's 80th birthday celebration. He won the National Medal of Technology and Science, I think given to him by President Obama for his work keeping Moore's law going for 10 years. According to the former dean of engineering at Stanford at the time, Jim Omura is standing six feet away. I motioned him over. I said, "Jim, tell this woman what you told me when I first started working in cryptography and I just won the Turing Award, the top prize in computer science for that work."

[[32:47](https://youtu.be/AZLOETBCQM4?t=1967)] Jim said, "Oh, I told Marty he was crazy." I knew he would do that because he'd given me permission to quote him on this. The best work often appears crazy a priori—GPS, which we use daily. Brad Parkinson, who won the top prize from the IEEE for that work, says that the Air Force thought GPS was crazy initially. High-speed Internet access. I won't go into details there. And I've spoken to a number of Nobel laureates, and almost all of them had the same reaction from people that I did.

[[33:22](https://youtu.be/AZLOETBCQM4?t=2002)] One of them, I'll tell you one story. Louis Ignarro, who won the Nobel Prize in physiology or medicine, I think, in 1998, told me that the dean of his medical school came to him and said, Louis, why are you doing this crazy stuff? We hired you because you do good work. Crazy stuff that won him a Nobel Prize.

**Ryan:**

[[33:43](https://youtu.be/AZLOETBCQM4?t=2023)] It makes sense. But I guess the unique aspect is I think a lot of people would receive that pushback and everyone thinks they're foolish, and they wouldn't go for it. What is it that gave you the confidence to continue when everyone was saying this is foolish?

**Martin:**

[[34:04](https://youtu.be/AZLOETBCQM4?t=2044)] Two reasons. One is I got beaten up as a Christ killer as a kid. And that's a little bit of a joke, but not totally. As a kid, we moved to an Irish Catholic neighborhood. I'm Jewish. We moved there when I was four and a half years old. I went to my parents and I said, "I want the pretty tree that the other kids have, the Christmas tree. I want the presents under the tree. I want to go to the same school as the other kids in the neighborhood."

[[34:27](https://youtu.be/AZLOETBCQM4?t=2067)] St. Nicholas of Tolentine Parochial School. I was telling my parents I didn't want to be Jewish. And so, in self-defense, I adopted the attitude of who would want to be like anybody else? That had a very simple answer. Me. I would have given my eye teeth to have been like everybody else. But in time, I came to believe my own bullshit. And so when my colleagues said I was crazy to work in cryptography, instead of scaring me off, it actually attracted me.

[[34:58](https://youtu.be/AZLOETBCQM4?t=2098)] So that's one reason. And the other reason, I think it runs in my family. I have an uncle who in 1940, with his wife, a Jew, took trains across the country with bicycles, bicycling through national parks. I mean, who but a crazy person would do that? I come from a crazy family. We've done crazy things. And this was a crazy thing to do.

**Ryan:**

[[35:23](https://youtu.be/AZLOETBCQM4?t=2123)] When you put out that paper in 1976, what was the problem you were trying to solve, or what was guiding your research direction at that time?

**Martin:**

[[35:33](https://youtu.be/AZLOETBCQM4?t=2133)] Well, it started as trying to develop a theory of cryptography. And Jim Massey, who was the editor at the time of the IEEE Transactions on Information Theory, of which I was on the board of governors, as I mentioned, Jim invited me to write a paper on that. I mean, this was beginning to get some traction. And I asked if Whit could be included. And he said absolutely. And so Whit and I were working on this paper.

[[36:03](https://youtu.be/AZLOETBCQM4?t=2163)] We had several drafts. Then in May 76, I came up with what is now Diffie-Hellman key exchange. And I included that. I threw that into a paper I'm giving in June 76, a month later at the IEEE Symposium on Information Theory in Ronneby, Sweden. Jim Massey's there, of course, and he says, you get that into the paper, I'll have it out in the November issue, which he did. Now, the November issue, Whit is fond of pointing out, did not come out until February 1977.

[[36:31](https://youtu.be/AZLOETBCQM4?t=2191)] Was usually late, but that's how it worked. And Ralph, unfortunately, as I said, had his idea rejected, his paper rejected. So his paper did not appear until 1978, even though it was submitted slightly before ours. I see.

### 36:48 — Signatures vs key exchange

**Ryan:**

[[36:48](https://youtu.be/AZLOETBCQM4?t=2208)] I think in this conversation you mentioned key exchange, also signatures. It seems like there are these components of a full cryptographic system. Could you explain each of these?

**Martin:**

[[37:02](https://youtu.be/AZLOETBCQM4?t=2222)] Key exchange is how do you and your bank exchange a key to protect your banking transactions, to use a modern example, with somebody listening on the Internet, and so use public key cryptography to do that Ralph Merkle had a puzzle method. Ralph Merkle had a puzzle method where he generated a sequence of puzzles and you solved. Your bank would solve one of them and it would then use that key. And you could quickly tell which key it was using.

[[37:33](https://youtu.be/AZLOETBCQM4?t=2253)] But somebody else had to solve half the puzzles, on average, before it could do it. And so it took a lot more effort on the part of an opponent. I'll explain Diffie-Hellman key exchange very briefly. And that is only key exchange. It's not yet signatures. You and I want to exchange physical messages. I want to write them out to you and pass them to you. But my wife, who is not supposed to see them, is sitting between us and has to hand them to you.

[[38:06](https://youtu.be/AZLOETBCQM4?t=2286)] So what do I do? I put my message in a strong box. I put a lock on that strong box. I'd like to tell you the combination to that lock. But if I tell you how to open it, I'm also telling my wife how to open it. So I don't tell anybody how to open it. I pass it to my wife. She can't open it. She passes it to you. You can't open it. You put a second lock on the strong box. You then pass the double. You don't tell me the combination.

[[38:31](https://youtu.be/AZLOETBCQM4?t=2311)] You don't tell Dorothy the combination. Only you know the combination. You pass it to Dorothy. She can't take either lock off. She passes it to me. What can I do? Take off my lock, leaving only your lock. I pass it back to Dorothy. She can't take off your lock. But when you get it, you can. You get the message inside. That's basically how Diffie-Hellman-Merkle key exchange works.

[[38:55](https://youtu.be/AZLOETBCQM4?t=2335)] Now, what's critical about this is that I made the strongbox big enough for you to put a second lock on it. If I hadn't done that, if I'd only made it big enough for one lock, you could have taken the strongbox that you got and put it in a bigger strongbox. But now there's a problem. When I get it, I can't get inside to take my lock off. It has to be what's called commutative. And everybody knows what commutative means, although they may have forgotten it.

[[39:20](https://youtu.be/AZLOETBCQM4?t=2360)] Addition is commutative. Three plus five is the same as five plus three. It doesn't matter which order you do the operations in. You get 8. 5 minus 3 is 2, 3 minus 5 is minus 2. You get a different answer. It's not commutative. Subtraction is not commutative. What I had to do was find a commutative one-way function, although I didn't know that at the time. The function I used is a commutative one-way function.

[[39:47](https://youtu.be/AZLOETBCQM4?t=2387)] It's exponentiation and modular arithmetic. It doesn't matter whether you first raise alpha to the x1 power and then to the x2 power or raise it to the x2 power and then to the x1 power. You get the same result. You get alpha to the x1 x2; multiplication in the exponent is commutative. And we did this over a finite field where exponentiation is not a smooth function, which would be easy to invert. It jumps all over the place.

[[40:15](https://youtu.be/AZLOETBCQM4?t=2415)] But it turns out it still works that way. So that is public key exchange, public key distribution. Digital signatures are more complicated. That's something that Whit Diffie came up with. It's called a public key cryptosystem. And then RSA, Rivest, Shamir, and Adleman came up with the first instance of that. There you have a public key and a secret key, and it doesn't matter which order you operate on them. Whether you first use the public key and then the secret key or the secret key and then the public key.

[[40:42](https://youtu.be/AZLOETBCQM4?t=2442)] You get the initial result, they undo one another there. If I use my secret key, I can sign a message because there's no privacy. But I send the encrypted message to you using my secret key. You use my public key, which you get from a public file, to verify it. That's how my phone works. It's got a public key built into it. Apple knows the secret key. Apple can sign software updates. People can take my phone apart and get the public key.

[[41:13](https://youtu.be/AZLOETBCQM4?t=2473)] But that doesn't give them the secret key that allows them to sign software updates.

**Ryan:**

[[41:18](https://youtu.be/AZLOETBCQM4?t=2478)] I see. So in that case, Apple is signing their updates to your phone.

**Martin:**

[[41:24](https://youtu.be/AZLOETBCQM4?t=2484)] Right.

**Ryan:**

[[41:25](https://youtu.be/AZLOETBCQM4?t=2485)] So I also was reading about symmetric versus asymmetric, and what you're describing sounds like asymmetric.

**Martin:**

[[41:31](https://youtu.be/AZLOETBCQM4?t=2491)] Yes. Asymmetric cryptography uses a public key and a secret key. It's asymmetric. Conventional cryptography uses the same secret key to encrypt and decrypt. And that requires a courier, which is what was required before public key cryptography. If you were a general in another division, I could send you a key. I would send a messenger with a key locked to his wrist. And when you got it, you could open it up and get the key and then you and I could use a radio channel to communicate very cheaply and very fast.

[[42:05](https://youtu.be/AZLOETBCQM4?t=2525)] But you can't use couriers to communicate keys between a bank and a client.

**Ryan:**

[[42:11](https://youtu.be/AZLOETBCQM4?t=2531)] Yeah. So I saw modern systems. It's almost like multiple different mechanisms where there's this asymmetric key exchange at the beginning to establish the connection. And then that gets you that key symmetric thing.

**Martin:**

[[42:26](https://youtu.be/AZLOETBCQM4?t=2546)] Exactly. It's just like I described. First, Apple signing the software update. They don't sign the whole thing. They only sign a hash. In the same way, we could use a public key cryptosystem like RSA to exchange messages, but it's too slow. So what I do is I send you one message, use the following key in AES, the Advanced Encryption Standard, and then we use AES very quickly to exchange messages. And that's the difference between asymmetric encryption, which we use at first, where I use the public key to encipher the message and use the secret key to get the key, and then we use a symmetric system to very quickly communicate afterward.

### 43:05 — RSA patent wars

**Ryan:**

[[43:05](https://youtu.be/AZLOETBCQM4?t=2585)] I was reading about RSA versus the Diffie-Hellman key exchange, and it seems like there were a lot of patents or something like that. Patent wars. What's the context behind that?

**Martin:**

[[43:18](https://youtu.be/AZLOETBCQM4?t=2598)] I didn't know how patents worked when we wrote the first patent on public key cryptography. If I'd known we could have covered RSA, we would have made a lot of money. Basically, RSA sold their company for $250 million. We made nothing, virtually nothing, from our patents in cryptography. There was a patent fight between RSA and us, MIT and Stanford, or between their licensees. And basically MIT won that fight.

[[43:55](https://youtu.be/AZLOETBCQM4?t=2635)] And I was pissed at RSA for a long time, and I was pissed with Jim Bidzos, the president of RSA Data Security. And around 1990, around 2000, sometime around there, I realized it was inconsistent with my approach to life to be pissed at RSA. They'd won. The fight was over. And so I approached Jim Bidzos and I said, look, Jim, I told him that, and I said, let's be friends. Let's bury the hatchet. And we essentially have.

[[44:24](https://youtu.be/AZLOETBCQM4?t=2664)] And friends are better than enemies. I'm not sure, but I think Ron Rivest might have actually nominated Whit Diffie for the Turing Award. Now, he wouldn't have done that if he didn't think we deserved it, but he wouldn't do it if he was pissed at us. And friends are better than enemies. That's not why I did it. That's not why I became friends with them. But again, it worked out very well.

**Ryan:**

[[44:48](https://youtu.be/AZLOETBCQM4?t=2688)] How did they win the patent war if your ideas came first?

**Martin:**

[[44:54](https://youtu.be/AZLOETBCQM4?t=2694)] I remember I told you I didn't know how patents worked. It's only the claims that matter. And so if I'd known that, we could have written a claim that would have covered RSA easily, but we didn't. And so the patent was written very badly. Stanford didn't want to invest a lot of money in this patent, so it had a law school intern write the patent instead of a patent attorney. We made a lot of mistakes.

**Ryan:**

[[45:23](https://youtu.be/AZLOETBCQM4?t=2723)] You mentioned friends are better than enemies. Yeah, a lot of people would agree with you, but I also think most people wouldn't be able to get over losing a $250 million outcome. How did you kind of get over that and establish friendship?

**Martin:**

[[45:43](https://youtu.be/AZLOETBCQM4?t=2743)] Well, some of it is in my genes, but a lot of it comes from my wife, basically. My wife and I have been married 59 years last March, and we were madly in love when we met. We followed society's rules, and we developed a toxic relationship. Ten years later, my wife was ready to leave me, but I didn't know it because I had blinders on, the way many husbands do. And fortunately, when she met me, she decided I was the one.

[[46:12](https://youtu.be/AZLOETBCQM4?t=2772)] And 10, 15 years after we're married, roughly 50 years ago, she says he's still the one, although life with him is impossible, and life with her was no picnic. So she went around looking for catalysts, ways to improve our relationship, and she eventually found a group. I won't go into all the details there. I tend to do that. That worked on the international and the interpersonal at the same time.

[[46:39](https://youtu.be/AZLOETBCQM4?t=2799)] It was founded by Professor Harry Rathbun, who was a professor here at Stanford, born in the 1890s. So he's no longer alive. I knew him late in his life, and that's how I. It was based on the teachings of Jesus, which was a problem for me as a Jew because it was okay not to go to synagogue, which I didn't do, but it was not okay to study the teachings of Jesus. That was traitorous. But eventually, Dorothy dragged me to enough meetings that over a year's time, I came to see that these people, Creative Initiative, as the group was called at the time, knew something I had to learn if my marriage was going to survive.

[[47:17](https://youtu.be/AZLOETBCQM4?t=2837)] And I surprised myself by being willing to do things that seemed crazy to me. The most important things were accepting ideas that Dorothy had that seemed crazy to me, that weren't crazy. Because what happened when she had an idea that seemed crazy to me? I treated her like she was crazy. What did that do? It drove her crazy. What did that do? It convinced me I was right, that she was crazy. Kept the whole cycle going.

[[47:43](https://youtu.be/AZLOETBCQM4?t=2863)] By the way, the same happens internationally. We treat countries in ways that they don't like. They react in ways that seem crazy to us. We treat them like they're crazy, and it keeps the whole cycle going. So that's how I came. And so it's based on the Gospels. And while I'm not a Christian, I see Jesus as a Jewish reformer rather than as a Christian messiah. I view myself as a follower of Jesus.

### 48:08 — Why inventions happen at similar times

**Ryan:**

[[48:08](https://youtu.be/AZLOETBCQM4?t=2888)] When I was researching the discovery that you had, it seems like all of a sudden many of the similar discoveries were happening all at the same time. So, for instance, you mentioned Ralph Merkle and us. Yes.

**Martin:**

[[48:22](https://youtu.be/AZLOETBCQM4?t=2902)] Oh, and GCHQ claims that they invented it just a couple of years before us, but they only have half of it, which is, if they're right, which is the privacy part. They didn't have anything on digital signatures, but they claim everything.

**Ryan:**

[[48:36](https://youtu.be/AZLOETBCQM4?t=2916)] Right. And then there's also the MIT folks.

**Martin:**

[[48:38](https://youtu.be/AZLOETBCQM4?t=2918)] The MIT folks. Yeah. So I have a theory about that. I'm going to tell it as a joke, but there's more to this joke than I think is just a joke. There's a muse that whispers in our ears. There's a muse of poetry. There's a muse of calculus who whispered in Newton's ear and Leibniz's ear about the same time. There's a muse that whispered in Ralph's ear about the same time that she whispered in our ears.

[[49:05](https://youtu.be/AZLOETBCQM4?t=2945)] Most people don't pay attention to this muse because she sounds crazy. A few people do. And so that's why I think there's something in the air. I mean, it's not necessarily a muse, but there's something in the air that comes to people.

**Ryan:**

[[49:20](https://youtu.be/AZLOETBCQM4?t=2960)] But why didn't it come 50 years earlier? Or how come it seemed like they all came very similar? I noticed. I interviewed Barbara Liskov as well, who did a lot in data abstraction and modularity. And there also, it was like on the West Coast and the East Coast, without even communicating, they had the same discovery. Very similar.

**Martin:**

[[49:46](https://youtu.be/AZLOETBCQM4?t=2986)] I think my joke might actually have something to say about that. But also there's something that goes on technologically. We didn't have the computing power to do public-key cryptography. If someone had come up with it 50 years before, it would have been a nice idea that couldn't be implemented.

**Ryan:**

[[50:00](https://youtu.be/AZLOETBCQM4?t=3000)] So there's a logistical part to this, which is just the tools weren't there, and once they were there, it kind of inspired the right thinking.

**Martin:**

[[50:10](https://youtu.be/AZLOETBCQM4?t=3010)] Yeah, but calculus, I mean, why? That occurred to Leibniz and Newton about the same time. Oh, and Darwin and someone else thought of evolution about the same time. So, I don't know. It is mystical, and maybe we should treat it as that. Even though I'm a scientist, I believe in the mystical side of life.

### 50:29 — What he worked on after cryptography

**Ryan:**

[[50:29](https://youtu.be/AZLOETBCQM4?t=3029)] There's a cryptography work that you're doing. And then later in your career, I saw this rethinking national security, and I was curious how you got into this, I guess, area, this body of work. And what's the problem you're trying to solve?

**Martin:**

[[50:46](https://youtu.be/AZLOETBCQM4?t=3046)] Well, the problem we're trying to solve is simple. We're going to kill ourselves. I mean, right now, I estimate that a child born today has probably worse than even odds of living out his or her natural life as a result of nuclear weapons all by themselves, without climate change, without AI, without any of this other stuff.

**Ryan:**

[[51:05](https://youtu.be/AZLOETBCQM4?t=3065)] What are you talking about with this AI threat?

**Martin:**

[[51:07](https://youtu.be/AZLOETBCQM4?t=3067)] Well, there's debate on that. Geoffrey Hinton, Yoshua Bengio, who won the Turing Award for their work in artificial intelligence, think that AI may actually kill human beings off, something like that, because it'll say, "Why do I need these stupid people?" Whereas Ed Feigenbaum and Raj Reddy, who won the Turing Award 30 years ago for their work in artificial intelligence, have both told me and given me permission to quote them.

[[51:38](https://youtu.be/AZLOETBCQM4?t=3098)] So I'm not giving any secrets away that calling AI an existential threat is ridiculous. It's science fiction. I don't know who's right, but I do know we need to build a more cooperative world for a number of other reasons, even if not that one. So why not solve that one? At the same time, we're likely to build AI into our nuclear command and control system. Oh, my God, what a mess. Right now, I'm working on a bill.

[[52:04](https://youtu.be/AZLOETBCQM4?t=3124)] It's H.R. 3564, and we have 25 on paper, 24 co-sponsors. The bill is so bad it's passable, but so good that it's a game changer. Why is it so bad that it's passable? It has an exception for launch on warning. If our warning system shows a bunch of ICBMs coming our way, the President doesn't need a second opinion to launch our nuclear weapons. He can do so all on his own. There have been mistakes in our warning system, so I don't like that.

[[52:37](https://youtu.be/AZLOETBCQM4?t=3157)] But that's why it's so bad. It's passable. This makes it easy for people to get on board. Most people don't realize that the president can launch a nuclear war all on his own. Right now, a president could be awakened at 3 a.m. in the morning during a crisis, too drunk to legally drive a car, asked what to do, he might say drunkenly, nuke him. And right now, theoretically, the military's supposed to do that.

**Ryan:**

[[53:02](https://youtu.be/AZLOETBCQM4?t=3182)] I didn't consider that AI could be coupled with the nuclear bombs too. I guess AI could.

**Martin:**

[[53:07](https://youtu.be/AZLOETBCQM4?t=3187)] Oh, it's likely to be. I mean, we have this problem that we have just minutes of decision time. Do you not think we're going to use computers to help us there?

**Ryan:**

[[53:18](https://youtu.be/AZLOETBCQM4?t=3198)] Looking back on your career, being at Stanford during the growth of computing, I imagine you had a lot of opportunities to work with other famous folks in the industry. For instance, Don Knuth.

**Martin:**

[[53:33](https://youtu.be/AZLOETBCQM4?t=3213)] Don Knuth is a good friend.

**Ryan:**

[[53:34](https://youtu.be/AZLOETBCQM4?t=3214)] Yeah.

**Martin:**

[[53:35](https://youtu.be/AZLOETBCQM4?t=3215)] Don Knuth doesn't use email. I think he does, but whenever I want to reach him, I have to call his home and talk to his wife, Jill. That's the other story. Stories that I have John McCarthy at AI Lab up the hill, where Whit stayed there, by the way, when we were working on public-key cryptography because John was away and Whit and Mary were taking care of his daughter, driving her to her writing lessons.

[[54:03](https://youtu.be/AZLOETBCQM4?t=3243)] And so Whit just walked down the hill to talk to me. But John McCarthy, there's a meeting at the faculty club maybe 45 years ago. Bob Floyd, who many of your people will know, who's a famous— he died, but a famous computer scientist here at Stanford. John McCarthy comes in. Bob Floyd's in the meeting. He goes over to Bob Floyd. I say, hi, John. He doesn't pay any attention to me because everybody knows that I.

[[54:30](https://youtu.be/AZLOETBCQM4?t=3270)] I/O is a waste of time. And so he's not going to waste time on I/O. So he has a very rapid exchange with Bob Floyd and he leaves. Well, I'll tell you another thing. I'm finishing my... It's 1968. Several months early in '68, I thought, who am I to think I can make an original contribution to knowledge, which is the definition of a PhD thesis? I'm thinking of dropping out of the program over spring break.

[[55:01](https://youtu.be/AZLOETBCQM4?t=3301)] I basically solved my thesis. It's that quick. I go to Tom Cover, who's since died, my advisor and very famous information theorist. And I go to Tom and I say, I just have barely enough units, but I have enough units to meet the course requirements for the PhD. But I don't have enough units to meet the PhD requirements. I'm going to have to take units of research if I work at IBM Research. Would you give me credit for my units of research?

[[55:34](https://youtu.be/AZLOETBCQM4?t=3334)] Because my wife was pregnant with our first child then. We'd been married roughly a year, year and a half. I was concerned about money. He says, sure. And so I go to IBM Research, Yorktown Heights. Tom wants to have me come teach at Stanford, which I've done. But he says, "You really should leave for a couple of years because Stanford." I sometimes joke that I had to leave for several years to lose the taint of the Stanford PhD.

[[56:04](https://youtu.be/AZLOETBCQM4?t=3364)] Why is that? Stanford was worried about inbreeding. If they hired me, I was just going to be doing research like Tom Cover. And they don't need two of them. They need somebody different. And so I went away to IBM for a year because my thesis broke very suddenly. And I then taught at MIT for two years before coming back on the faculty in '71. And this seemed like just a stupid hoop I had to jump through.

[[56:26](https://youtu.be/AZLOETBCQM4?t=3386)] But it actually turned out to be very important because when I was at IBM, Horst Feistel, whose name many people may recognize, he was really the father of IBM's research in cryptography. He was hired in '68. He was in the same department as me. I didn't work in cryptography, but I had lunch with Horst, and he told me some of the amazing things that got me started. And then when I'm at MIT, Peter Elias, whose name many people today will not recognize, but he was one of the original contributors to information theory.

[[57:00](https://youtu.be/AZLOETBCQM4?t=3420)] Peter gives me a paper by Claude Shannon, whose name your audience probably will recognize, written in 1949. I'm sorry, published in 1949 in the Bell System Technical Journal, connecting information theory to cryptography. Which is when I realized that, oh, I've already done a PhD in information theory. Maybe I can do something worthwhile in cryptography. So that stupid hoop I had to jump through was actually very important because when I got back to Stanford, I started working in cryptography, among other things.

### 57:31 — His thoughts on death

**Ryan:**

[[57:31](https://youtu.be/AZLOETBCQM4?t=3451)] I think at the beginning of the conversation, you said something quickly that you had thoughts on death. And I was curious, what are your thoughts on death and how does it impact you?

**Martin:**

[[57:44](https://youtu.be/AZLOETBCQM4?t=3464)] And I got an email from somebody at The New York Times about a month ago saying that he's working with my obituary, and it made me macabre, but he was wondering if I could read it over and if I have any comments. And so, the two things are that I'm 80 years old, so my older brother died just after he turned 80. My mother died at 70. My father lived to 98. I hope I'll have more years, but if I don't, that's okay.

[[58:10](https://youtu.be/AZLOETBCQM4?t=3490)] I've had a great ride. But the two things that concern me about dying are the people I'll leave behind, who I think are dependent on me but probably aren't, and the work I do because very few people are working on the nuclear issue, the growth of humanity as a whole to save itself, that we're headed for disaster. Very few people realize that. And very few people put it in terms of a process of change.

[[58:38](https://youtu.be/AZLOETBCQM4?t=3518)] We can't stay where we are. We're going to kill ourselves, we're going to die. We can't jump to where we need to go. The world is too dangerous. But we can get there via a process of change. I'll tell you one other thing. Humanity is going to die. I've come to this realization. I mean, it's clear. I mean, we might last a million years, but at some point. We might last a billion years, but at some point the sun's going to burn out.

[[59:02](https://youtu.be/AZLOETBCQM4?t=3542)] Maybe we'll move to other galaxies and we'll find ways to cheat death for a while. But eventually humanity is likely to die. But if humanity were to die now, it would be an infant. It would be infant mortality. It would be really sad. If we've lived a full life, that's something else. If I had died when I was a child, people would say, oh, what have we missed? If I die at 80, people will say, some people will be saddened by it, but.

[[59:31](https://youtu.be/AZLOETBCQM4?t=3571)] But they'll feel like I've lived a full life. We need to save humanity from an infant death. We've only been around about 100,000 years.

### 59:40 — Advice for his younger self

**Ryan:**

[[59:40](https://youtu.be/AZLOETBCQM4?t=3580)] With all the experience that you have now, if you could go back to when you had just graduated college and give yourself some advice, what would you say?

**Martin:**

[[59:49](https://youtu.be/AZLOETBCQM4?t=3589)] If when I was just graduating college and I was interested in saving the world, which I was not, I might have gone up to the top of a mountain to a guru and asked him what to do. Imagine what you'd say. You'd expect him to tell you, work for the UN or something like that. Imagine what you'd say if he told me, forget about saving the world, which was not a problem because I didn't think about saving the world.

[[01:00:13](https://youtu.be/AZLOETBCQM4?t=3613)] Go out and become as famous as you can, make as much money as you can, come back in 10 years, and I'll tell you what to do. That would have seemed like a detour, but it was actually the shortest distance between two points. Because 10 years later, when I was 30, 35 years old and I was interested in saving the world, I had a reputation, I had money, and I had to screw up to get where I am. I had to not be concerned with the world to become concerned with the world to be able to do something, to do what I can do about it.

**Ryan:**

[[01:00:40](https://youtu.be/AZLOETBCQM4?t=3640)] Awesome. Well, thank you so much for your time today. I really appreciate it.

**Martin:**

[[01:00:43](https://youtu.be/AZLOETBCQM4?t=3643)] You're welcome. And thank you.

