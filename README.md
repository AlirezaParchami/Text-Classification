# Text-Classification-using-KNN-and-Decision-Tree
Information Retrieval Final Project

This project classifies data into several categories. "SmsSpamCollection" is used for the Dataset.

There are 4 major steps for classification:
  1-Preprocessing
  2-Feature Generation
  3-Feature Weighting
  4-Interpretation/Evaluation
  
  
#Preprocessing
In this stage, useless words (which is called StopWords) should be eliminated and the stem of each word should be found.

#Feature Generation
I have used N-gram for this stem.

In most cases, Unigram, Bigram or Trigram is used for Feature Generation.

#Feature Weighting
Each word should be weighted for better classification. TF-IDF is one of the most common methods for this step.
It considers the frequency of each word in a document and a dataset. This can specify the importance of the word.

#Evaluation
Precision, Recall and F1-Score are the evaluators in this project.
