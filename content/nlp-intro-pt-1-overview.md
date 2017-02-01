Title: Introduction to NLP - Part 1: Overview
Date: 2017-01-31 12:00
Tags: nlp, natural language processing, theory
Category: NLP
Slug: nlp-intro-pt-1-overview

I realized lately that getting started with Natural Language Processing can be scary, intimidating and/or confusing for a lot of people. I am not quite sure if this is due to the complexity of the task (especially to get meaningful results), the amount of theoretical knowledge needed to come up with a working solution, the sparsity of good resources available out there, or a mixture of all of the above. This prompted me to start writing a series of articles in the hope of helping some of you to take that first step.

My ambitions are humble: I am not an NLP expert, but I feel like I have accumulated enough real-world experience to at least have something meaningful to say about it. With that said, let's get started today with a simple, global overview...

## Objective

The end goals of Natural Language Processing projects can be quite diverse: spam classification on emails/sms, sentiment analysis on movie reviews or tweets, or document similarity for plagiarism detection on written essays. Whatever it is you are trying to accomplish, the underlying motive stays the same: Extract meaningful and valuable information from text data on a somewhat large scale.

For this reason, a modern NLP pipeline will always adopt a similar architecture. Understanding this, and seeing where each piece of the puzzle fits in the overall picture will go a long way in helping you come up with solutions.

## Modern NLP Pipeline

![NLP Pipeline]({attach}/images/nlp-intro-pt-1-overview-1.png)

A NLP pipeline always starts with an homogenous collection of documents (tweets, paper abstracts, news articles, etc.), called _corpus_, and ends up with a well-defined task, like mentionned above. Many steps are involved, and one can picture the whole thing as a factory/assembly line, where step by step we transform our raw data, eliminating the noise, extracting its most characteristic features, until we end up with a representation of our documents that makes it possible to perform well at the chosen task.

### Language detection

Language detection is often the first stop along the way. Traditional pipelines require you to fine-tune almost every step of the process to cater to the specificities of a particular language, and neglecting this part is almost guaranteed to cause you headaches. As we will see later, deep learning changed the game a bit in this regard, but it is nonetheless important to separate your documents according to their language.

### Preprocessing

Arguably the most time-consuming part of the process (with data annotation also a contender), this is where you can really set yourself up for good or bad results right of the bat by putting your data in the proper format. Preprocessing can involve as little or as many steps as needed/required/wanted. This often requires good linguistic knowledge and domain knowledge to truly optimize this process. Spending time understanding your data and the context is always a good idea.

Preprocessing for example can include:

- Sentence/word segmentation (a.k.a. "tokenization")
- Stopwords removal
- Part-Of-Speech (a.k.a. "POS") tagging
- Named Entity Recognition
- Dependency Parsing
- And many more...

Don't worry, I plan to go much more in details about preprocessing techniques in the second article of the series.

### Modeling

This is where you take your properly curated and formatted documents and start applying regression/clustering/etc. For this, you first need to convert your text data, on which you cannot directly do maths, into a proper vector/matrix representation that will allow you to manipulate them. 

![Vectorization]({attach}/images/nlp-intro-pt-1-overview-3.png)

As for the modeling task itself, there is a couple of very well-known, ubiquitous algorithms, and also some lesser known ones - This of course depends on the nature of the task you are trying to perform. I'll try to cover as many of them in a subsequent article.

## The Deep Learning Revolution

![Deep Learning NLP Pipeline]({attach}/images/nlp-intro-pt-1-overview-2.png)

Deep learning is all the rage nowadays, and it is in pass of radically transforming the NLP paradigms used for almost every task. Aside from providing state-of-the-art results, it also present desirable characteristic that we would be foolish to ignore, like being more flexible in regards to multilinguism. I suspect this will be the subject of many articles to come, as DeepNets for NLP are a complex beast to tame, and getting good results often requires a lot of training data (understatement)... and patience!

_*The diagrams I used are inspired by similar ones I saw on [Aylien's blog](http://blog.aylien.com/leveraging-deep-learning-for-multilingual/). They often post very interesting articles over there, I suggest you go take a peek!_