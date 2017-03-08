Title: CNN For Text Classification - Literature Review
Date: 2017-03-08 12:00
Tags: litreview cnn deeplearn textclassif
Category: Literature Review
Slug: cnn-text-classif-litreview

I am currently investing some of my free time into grokking Convolutional Neural Networks and their application to NLP tasks. My first stop was text classification. I thought it would be wasted time not to share them in the open, so I guess if you are short on time and want to get a good glance at the current landscape, this is a good starting point!

**Collobert, R., Weston, J., Bottou, L., Karlen, M., Kavukcuoglu, K., & Kuksa, P. (2011). Natural Language Processing (almost) from Scratch. The Journal of Machine Learning Research, 12, 2493–2537.**

> https://arxiv.org/pdf/1103.0398.pdf

Pretty much the paper that introduced for the first time a viable and simple way to apply CNNs to traditional NLP tasks. The authors set a very ambitious goal of building a universal language model that could excel at multiple NLP tasks with minimal amount of pre-processing. They postulated that the key was to build a good intermediate representation that could be reused across tasks. The targeted tasks were POS (Part-of-Speech Tagging), NER (Named Entity Recognition) and SLR (Semantic Role Labeling). 

Although they also present a "window model", it's really their Convolutional DeepNet that have our interest here. Using lookup tables, they map each input word to a vector representation that they subsequently train via backpropagation. More than one "feature" can also be used for some tasks, and so fature vectors are simply concatenated together. They follow standard practice of adding a non-linearity and max-pooling to each convolution layer.Padding techniques and max-pooling allows the model to deal with variable-length input sentences, and produce a fixed-length output to feed to the subsequent layers. After the single convolution is performed, data is fed into two fully connected layers with a HardTanh activation function.

![Accuracy of each model]({attach}/images/cnn-text-classif-litreview-3.png)

Resuls from the convolutional model are well within range of the state-of-the-arts in each respective task.

Interesting as well is the fact that before all this Deep Nets hype was even here (they even mention that they chose to go with this "10-years old" Neural Nets architecture out of curiosity) and even before the ubiquitous word2vec paper, Collobert et al. provided the first generally accessible implementation of a viable dense word embedding model, "SENNA".

**Kim, Y. (2014). Convolutional Neural Networks for Sentence Classification. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP 2014), 1746–1751.**

> https://arxiv.org/pdf/1408.5882v1.pdf

We have to wait 3 more years for a significant paper on CNN applied to Text Classification to surface. In this case, the stated goal is to prove that CNN can perform as well as state-of-the-art methods for this particular NLP task.

The architecture is quite simple: A single convolution layer sitting atop a lookup layer that transforms words into their dense vector reprentation, provided by the Word2Vec model made available by Google Brain team after their now famous paper. Words not present in the pre-trained set are initialized randomly. Apart from using the vectors as-is, the network also allows for multiple-channel training by trying to fine-tune the vector values. The channel analogy refers to image processing language, where multiple different perspectives on the input data are ofter used. Multiple channels also allows for training with multiple window sizes inside the convolution, which can potentially increase model performance.

A new addition compared to Collobert is the Dropout layer, placed after the convolution. Dropout (see Hinton et al. 2012) is simply a "boolean mask" affecting each neuron, with probability _p_ of being 1. Gradients will only be backpropagated through the unmasked units. Another novelty is the l2-norm constraint placed on that same layer, so that the maximum value cannot exceed a certain value _s_. At the very top sits a softmax layer with 2 units (binary classifier).

The configuration retained after gridsearch had window sizes 3,4 and 5, dropout probability _p_ of 0.5 and a _s_ cutoff value of 3. Adadelta minibatch gradient descent is used with a batch size of 50.

Kim also experiments with variations of the models where vectors are fined-tuned during training, and one where both static vectors and fine-tuned vectors are used simultaneously in separate channels.

![Accuracy of each model]({attach}/images/cnn-text-classif-litreview-4.png)

Results are quite impressive, with the different variations able to best Paragraph2Vec, RAE and other famous methods (which use more complicated preprocessing or tuning operations) on various benchmark datasets. The addition of Dropout seems to add an absolute accuracy gain of 2~4%. One discussed shortcoming is the tendency of the model to overfit the training data, most likely due to the lack of sufficient training data and the complexity of the model compared to the simplicity of the task at hand.


**Wang, P., Xu, J., Xu, B., Liu, C., Zhang, H., Wang, F., & Hao, H. (2015). Semantic Clustering and Convolutional Neural Network for Short Text Categorization. Proceedings ACL 2015, 352–357.**

> http://www.aclweb.org/anthology/P15-2058

An interesting paper that introduces the concept of semantic clustering of word vector embeddings, to arguably counteract the poor performance of modeling on short text. The postulate is that this is due to their very low keyword/keyphrase content. For example, simply averaging all words is likely to cause divergeance that will impact decision negatively. Teh authors want to leverage the fact that in well-trained dense embedding spaces, conceptually-related terms normally appear close to one another.

They first perform clustering (fast clustering based on density peaks, see Rodriguez & Laio 2014) on pre-trained word embedding to from what they call _semantic cliques_. The cluster centers constitues a reference point which will be used at a later stage to evaluate the value of _semantic units_.

Those _semantic units_ (SU) are constructed by element-wise additive composition of the word vectors over the input short text. Multiple window sizes are used to capture multiple candidate units. To determine which SUs are meaningful, Euclidean distance is computed from each candidate to the nearest semantic clique from the initial step. If the result is under a set threshold, the candidate is selected as input to the convolutional layer.

A single layer of convolution (n=6) with max-pooling is used (K=3), after which a tan transformation is applied. The results are concatenated to be fed into a fully connected softmax layer. Cross-entropy between predicted and actual distributions is minimized. SGD minibatch of size 100 is used.

![Accuracy of each model]({attach}/images/cnn-text-classif-litreview-5.png)

Results are collected for all 3 popular word embeddings (word2vec [d=300], GloVe [d=50] and SENNA [d=50]). Their method obtains state-of-the-art performance on two different benchmark datasets. The number of window matrices selected at the first stage of the architecture has a substantial influence over performance, and cross-validation can be used to find the optimum. All three vector representations require different parameters for distance threshold and window size to produce their best results.


**Zhang, X., Zhao, J., & LeCun, Y. (2015). Character-level Convolutional Networks for Text Classification. Proceedings of the Annual Conference of the International Speech Communication Association, INTERSPEECH, 3057–3061.**

> https://arxiv.org/pdf/1509.01626v3.pdf

This paper goes one step further into the generalisation of text representation for NLP tasks, as it applies a deep CNN to raw character inputs in an attempt to prove knowledge of words, syntax or even semantics is not necessary to understand a language.

The input characters need to be encoded in a prescribed alphabet (to limit noise and exclude non-meaningful characters), in a one-hot encoding fashion. A limit is also set for the number of characters in one sentence.

The authors chose to augment preprocessing with the WordNet Synsets thesaurus to randomly replace words by one of their synonyms (following a geometric distribution). The replacement word probability also follows a geometric distribution according to its relative frequency. This ensures the most frequently occuring words are the most frequently chosen. This strategy, although it does not seem to produce any subtantial effect here, goes against the publication goal of showing that a network can model language without any knowledge of words, and is surely criticizable.

Two models were trained - One were lettercase is not taken into consideration, and another one where uppercase letters are encoded separately. One of the benchmark datasets consists of Chinese language news - To be able to feed it into the network, the authors convert it to Pinyin (latin representation of CChinese characters) and then encode it.

6 layers of 1d convolutions (stride=1) are used with a max activation and max-pooling, which feed through 3 fully-connected layers interlaced with dropout masks (p=0.5). SGD minibatch (size 128) is used, with momentum 0.9 and initial step size of 0.01 (halved every 3 epochs for 10 times). Alphabet size is 70 characters, and max sentence length is 1014 characters.

![Testing error of all models]({attach}/images/cnn-text-classif-litreview-6.png)

Compared to most well-known paradigms (word2vec, bow + tfidf, LSTM, etc.), the models presented in this paper are performing comparably on various evaluation datasets (corpuses ranging from 100k to 3M+ documents). Seems like the case-insensitive model performs better.
