# Preface

---

layout: post
title:  "notes of TDD with Python - Preface"
date: 2018-07-27 16:00:09 +0800
categories: notes
description: This is a note reading Test-Driven Development with Python, 2nd edition, by Harry J.W. Percival (O’Reilly). Copyright 2017 Harry Percival, 978-1-491-95870-4. 

---

## What is the main theme of this book?

### What's the difference between hacking and software engineering?

> This book is my attempt to share with the world the journey I’ve taken from "hacking" to "software engineering". 

This is a hot topic, so there are many posts discussing on it. I have read the first one. 

[Daniel Miessler](https://danielmiessler.com/study/programmer_hacker_developer/) gave a simple definition:

![](https://danielmiessler.com/images/DeveloperHackerProgrammer-e1464829544285.png)

> 1. A Programmer is someone who can solve problems by by manipulating computer code. 
> 2. A Hacker is someone who makes things. 
> 3. A Developer is a formally trained programmer. 

Dan:
[Hackers and Software Engineer](https://dandreamsofcoding.com/2013/09/16/hackers-and-software-engineers/)

PETER CHRISTENSEN:
[Hacker vs Engineer – Know The Difference!](http://pchristensen.com/blog/articles/hacker-vs-engineer-know-the-difference/)

Melanie Pinola:
[Hackers vs. programmers, engineers, and computer scientists: What these terms mean](https://www.itworld.com/article/2975749/development/hackers-vs-programmers-engineers-and-computer-scientists-what-these-terms-mean.html)


## Was the author happy in writing this book?

> I hope you’ll enjoy reading this book as much as I enjoyed writing it.

Yes! He also made a ten sets of videos for part one, putting it on Orealy. I have seen the first three minutes of video one. He is a man of energy.


## What stages is he on?

> They say that in any discipline, you go from apprentice, to journeyman, and eventually, sometimes, on to master. I’d say that I’m—​at best—​a journeyman programmer.

It is a [Medieval guild system of Master, Journeyman, Apprentice](http://www.e-budo.com/forum/showthread.php?22967-Master-Journeyman-Apprentice).

I am a journeyman, on the road.

> A journeyman is a skilled worker who has successfully completed an official apprenticeship qualification in a building trade or craft. Journeymen are considered competent and authorized to work in that field as a fully qualified employee. They earn their license by education, supervised experience and examination. - [Journeyman - Wikipedia](https://en.wikipedia.org/wiki/Journeyman)

Here are different words of this three-level model.
[The Apprenticeship Model: A Journey toward Mastery](https://www.classicalu.com/the-apprenticeship-model-three-levels-to-mastery/)


## Where did Harry start in learning Python?

> Mark Pilgrim's excellent [Dive into Python](http://www.diveintopython.net/toc/index.html)

It is updated until 2004, and still being recomended by MITx600 series on the top one, before *Think Python*.

Scrolling this book's table of contents, I found it is not a introduction to python, but a deep discuss on interesting topics around this language: what are the pig-falls, and what's the tricks, and what we can do with TDD and HTML.

Note: the author had updated to Python 3 version: [Dive Into Python 3](http://www.diveintopython3.net/)


## Why did he Wrote a Book About Test-Driven Development?

Because he have suffered these mind modes.

1. It sounds like a really sensible approach, a really good habit to get into—​like regularly flossing your teeth.
2. Under client and deadline, any good intentions about TDD went straight out of the window.
3. Soon I had a hideous, ugly mess of code. New development became painful.
4. I was lucky enough to get a job with a company, where Extreme Programming (XP) was the norm. They introduced me to rigorous TDD.
5. I still dragged my feet at every stage. “I mean, testing in general might be a good idea, but really? All these tests? Some of them seem like a total waste of time…​ What? Functional tests as well as unit tests? Come on, that’s overdoing it! And this TDD test/minimal-code-change/test cycle? This is just silly! We don’t need all these baby steps! Come on, we can see what the right answer is, why don’t we just skip to the end?”
6. Believe me, I second-guessed every rule, I suggested every shortcut, I demanded justifications for every seemingly pointless aspect of TDD, and I came out seeing the wisdom of it all.
7. Psychologically, it’s made development a much less stressful process. It produces code that’s a pleasure to work with.

### What is Extreme programming?

Extreme programming (XP) is a software development methodology which is intended to improve software quality and responsiveness to changing customer requirements. As a type of agile software development,[1][2][3] it advocates frequent "releases" in short development cycles, which is intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Extreme_Programming.svg/734px-Extreme_Programming.svg.png)

from [Extreme programming?-wikipedia](https://en.wikipedia.org/wiki/Extreme_programming)

## What the aim is, and what they are not?

> My main aim is to impart a methodology—​a way of doing web development, which I think makes for better web apps and happier developers. 

impart | imˈpärt |
verb [with object]
- make (information) known; communicate: teachers had a duty to impart strong morals to their students.
- bestow (a quality): its main use has been to impart a high surface gloss to finished articles.

> There’s not much point in a book that just covers material you could find by Googling, so this book isn’t a guide to Python syntax, or a tutorial on web development per se. 

per se | ˌpər ˈsā |
adverb
- by or in itself or themselves; intrinsically: it is not these facts per se that are important.

> Instead, I hope to teach you how to use TDD to get more reliably to our shared, holy goal: clean code that works.

holy | ˈhōlē |
adjective (holier, holiest)
1. dedicated or consecrated to God or a religious purpose; sacred: the Holy Bible | the holy month of Ramadan.
- (of a person) devoted to the service of God: saints and holy men.
- morally and spiritually excellent: I do not lead a holy life.
2. dated or humorous used in exclamations of surprise or dismay: holy smoke!


## What are the tools to take off when coming out of the other end of this book?

Django

Selenium

### jQuery

jQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers. With a combination of versatility and extensibility, jQuery has changed the way that millions of people write JavaScript.

from jquery.com

There is a introduction on [w3schools.com](https://www.w3schools.com/jquery/default.asp)

### Mocks

It seems object type for simulation in testing.
- see [Mock object - wikipedia](https://en.wikipedia.org/wiki/Mock_object)

It is like a stub, but used in different circumstances. 
- see [Mocks - Sinon.JS](http://sinonjs.org/releases/v6.1.0/mocks/)


## What role dose pair-program take in wrting this book?

> In Extreme Programming we always pair-program, so I’ve imagined writing this book as if I was pairing with my previous self, having to explain how the tools work and answer questions about why we code in this particular way.

in patronising tone: try to be patient with that not all that smart myself.
 
sounds defensive: systematically disagree with whatever anyone else says.


## What are the general parts of this book?

[part1](https://www.obeythetestinggoat.com/book/part1.harry.html) The basics: Dives straight into building a simple web app using TDD.
 
[part2](https://www.obeythetestinggoat.com/book/part2.harry.html) Web development essentials: Covers some of the trickier but unavoidable aspects of web development, and shows how testing can help us with them.

[part3](https://www.obeythetestinggoat.com/book/part3.harry.html) More advanced testing topics: Mocking, integrating a third-party system, test fixtures, Outside-In TDD, and Continuous Integration (CI).


## Where are the example codes?

Code examples are available at [this site](https://github.com/hjwp/book-example/); 

you’ll find branches for each chapter there (e.g., [here](https://github.com/hjwp/book-example/tree/chapter_unit_test_first_view). 

You’ll find a full list, and some suggestions on ways of working with this repository, in [appendix_github_links](https://www.obeythetestinggoat.com/book/appendix_github_links.html).


