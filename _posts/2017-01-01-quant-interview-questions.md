---
layout:            post
title:             "Quantitative Analyst Interview Questions"
menutitle:         "Quantitative Analyst Interview Questions"
date:              2017-12-01 06:31:00 +0100
tags:              Quantitative Analyst Interview Questions London
category:          Jobs
author:            am
published:         false
redirect_from:     "/quant-interview-questions/"
language:          EN
comments:          true
---

I have interviewed for Quantitative Analyst positions (with varying success!) at a number of places at some point in time in London. 

Without ado, the first section dives straight into questions. The second is some discussion on how to prepare.

# Questions
Multiple questions given in one block correspond to the same interview session. Most interviews are equally detailed and extremely challenging. Ones that appear short or easy are because I forgot the rest. I particularly tend to forget most of the statistics questions are they are so similar and there were a **lot** more than represented here.

> What are the assumptions of the Black Scholes model? 
> 
> <cite>Bank of America</cite> 

> An online test on the platform *Codility*.
> 
> <cite>Barclays, Quant</cite> 

> Can you explain the Local Volatility Model? What are the parameters of the Black Scholes model? What is convexity? What would happen to the price of a Call if volatility increased?
> 
> <cite>Citi, Quant</cite> 

> Write down the Taylor series. Expand $e^x$, $\cos(x)$ and $\sin(x)$ as separate power series. Find a relation for the last two with respect to the first. Cross out the $i$ in both expressions. Sketch the resultant functions, $y(x)$. Can you explain how to price a barrier option? Give an example of other exotic derivatives.
> 
> <cite>Commerzbank, Quant Intern</cite> 

> Find the derivative of $\sin(x)$, $\cos(x)$, $e^x$ and $\tan(x)$. Describe with an example of code how you would sort an array of length $n$: What is the complexity of this algorithm? You have three identical options valued at $7,8,9$ by the market and three strikes of $30, 40, 50$ for the same set of three options. Find which price corresponds to which strike. Is there arbitrage? Constructing a portfolio to demonstrate your answer. You have three operations for three memory locations, $\\{A,B,R\\}$ such that $A \to R$; $B\to R$; $R-A \to A$. Create a sequence of operations to represent $B\to A$.
> 
> <cite>Commerzbank, Quant</cite> 

> What would happen to the price of a Call if volatility increased?
> 
> <cite>Goldman Sachs, Strats</cite> 

> A coffee grinder gives an i.i.d. uniformly distributed volume of ground coffee beans, $V\sim\mathcal{U}(0,1)$ when a button is pressed. If you have a cup of unit volume, how many times do you expect to press the button before filling the cup *(hint: overflow is also considered filling the cup)*.
> 
> <cite>Goldman Sachs, Strats</cite> 

> You have three arrays each of equal length $n$ containing positive and negative integers. A *zero-sum triplet* will be defined as three numbers in each respective array that sum to zero. Write an algorithm to efficiently find all such *zero-sum triplets*. Note that there will only be one integer in each corresponding array: $a\in A; b\in B; c\in C$ where $\\{A,B,C\\}$ are the arrays and $\\{a,b,c\\}$ the integers.
> 
> <cite>Goldman Sachs, Strats</cite> 

> What is the expected number of times you must flip a coin to get 66 heads, not necessarily consecutively? Find the mean and standard deviation of the resultant distribution.
> 
> <cite>Goldman Sachs, Strats</cite> 

> Solve the following SDE:
> $$dS_{t}=\mu S_{t} dt + \sigma S_{t}\,dW_{t}$$
> Explain the difference between interpolation and extrapolation.
> 
> <cite>Goldman Sachs, Strats</cite> 

> You have an array of integers. Sort this array in the most efficient manner.
> You have 10 i.i.d random uniform numbers $X_i \sim \mathcal{U}(0,1): i\in \\{1,\dots,10\\}$. If you select
> what is the PDF, mean and variance of $\max\\{X_i\\}$?
> 
> <cite>Goldman Sachs, Strats</cite> 

> You may have three throws of a 6-sided dice and you can stop rolling at the first, second or final roll. I will pay you face of the dice when you decide to stop. What is the fair price of this game? What would you pay if I let you have unlimited throws? Explain what delta is. Sketch delta and gamma. 5 people come into this room in a given period of time on average. How would you model this? Sketch the PDF of this model. Find the mean of this model. You have a file that contains an unknown number of lines, $n$. The aim is to output $m$ lines from the file that are sampled with a uniform distributed from the total number of lines available. The following constraints apply: You must read each line sequentially, but you can only read each line once and you may only store 3 lines at any time.
> 
> <cite>Nomura, Quant</cite> 

> Simple multiple choice questions on `C#` programming (this can be passed by just being good at OO coding and having common sense). A *Codility* test that can be performed in `C#` or `python`.
> 
> <cite>Tibra Capital, Algo


# Preparation
The biggest take home is that preparation is key. Interviewing for positions without preparing is tantamount to putting a gun to your head and I learned this the hard way during my Masters degree. If you simply don't have the time to prepare for the interviews, cancel and wait until you can.

To prepare, I use the following resources:

  - [Heard on the Street: Quantitative Questions from Wall Street Job Interviews](https://www.amazon.co.uk/dp/0994103867)
  - [Part 1A: Probability](https://www.dpmms.cam.ac.uk/study/IA/Probability/)
  - [Part III: Advanced Financial Models](https://github.com/ajtulloch/CambridgeMathematicsPartIII)
 
Most interview questions will be covered by one of the above. The book has some interesting logical puzzles which require nothing but thought and are excellent think about whilst doing something else.

For general further nerding the following are also decent:
 
  - [Part II: Advanced Probability](https://www.dpmms.cam.ac.uk/study/II/AppliedProbability/)
  - [Part III: Advanced Probability](https://www.maths.cam.ac.uk/sites/www.maths.cam.ac.uk/files/advancedprobability.pdf)
 
### Why the focus on Part III notes? 
 
 The people interviewing for the top roles to be exclusively from Cambridge / Edinburgh / Oxford / UCL / Warwick from Theoretical Physics / Maths. Ordering is relative to the number of interviews I have had from these alumni (see below for a note on the bias!). Out of these programmes only Cambridge has decent notes available online and I had already solved the Edinburgh ones ! 
 
Most of my interviews seem to be from teams with Cambridge or Edinburgh alumni, possibly due to the similarity between Part III and the Higgs Centre MSc. programme as the courses / exams are more or less identical to the title. It is certainly worth targeting places that have hired people from your course particularly if you took the more challenging route !

### Don't give up

Even after doing extremely well in an interview you may not get asked back. The team may have filled the vacancy with a previous hire or intern or friend. The headcount may no longer be present. It is impossible to know as most times feedback will not be available or is highly limited.

It is key therefore to apply for a large number of positions particularly if your industry experience is lacking.

Finally, to make you feel better about your own application process here are some of my best application / interview blunders ...

 - The *Classic*: Sending a cover letter with the address of another firm
 - Forgetting which gained the negative sign when taking the derivative of $sin(x)$ and $cos(x)$ and later adding a mystery $x$ by incorrectly writing $\frac{\partial}{\partial x} e^x = x e^x$
 - $9+4 = 36$

In fact, despite these being my worst incidents all resulted in positive outcomes and progression through to the following stage. If an interview seems like a lost cause it is probably not as bad as you think.