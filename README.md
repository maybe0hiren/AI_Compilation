# AI_Compilation
A compilation of AI services


## About Sentiment Analysis Tool with 85% Accuracy
Overview:  
- This model is designed to classify sentiment in social media comments as Negative, Neutral, or Positive. It is built from scratch using classic machine learning and natural language processing, prioritizing modularity, easy maintenance, and transparent feature engineering. No pre-trained transformers or deep learning models are used.
  
Logistic Regression:
- Selected for its balance of simplicity, interpretability, and performance. It’s easy to understand and debug, making it a great starting point for text classification tasks. The model performs efficiently with bag-of-words and TF-IDF features, which makes it well-suited for linearly separable data. Handles large, sparse datasets — such as social media text

Python Packages:
- pandas: Data handling and manipulation (install via pip)
- scikit-learn: Modeling, TF-IDF, splitting, metrics (install via pip)
- joblib: Save model and vectorizer (install via pip)
- re: Text cleaning (preinstalled)

TF-IDF Vectorizer Tweaks:
Expanded the feature space with important context words and phrases, removed noise, and improved the descriptiveness of inputs for the model.
- max_features = 15000 – Captures a wide vocabulary and subtle sentiment cues
- ngram_range = (1, 3) – Includes unigrams, bigrams, and trigrams for better context
- stop_words = 'english' – Removes common, non-informative words
- min_df = 2 – Filters out rare words to reduce noise
- max_df = 0.95 – Ignores overly frequent words that add little value
- sublinear_tf = True – Reduces the weight of very frequent terms for balanced importance

Logistic Regression Tweaks:
This setup allowed the model to learn nuanced patterns, avoid underfitting, and correctly identify all classes—including minority ones—resulting in better overall accuracy.
- max_iter = 15000: Ensures complete convergence with high-dimensional data
- class_weight = 'balanced': Handles class imbalance in sentiment data
- C = 2.5: Lowers regularization strength to capture subtle patterns

