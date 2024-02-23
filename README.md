# Predicting-emotions-in-music-using-artificial-intelligence
Code for the project 'Predicting emotion in music: Harnessing multimodal artificial intelligence to predict emotional dominance, valence and arousal'.

### Acoustic models: feature selection and grid search
- Acoustic Data Feature Selection.ipnyb
- Acoustic Data Grid Search Part 2.ipnyb (grid search for traditional model types )
- Acoustic Data Grid Search Part 3.ipnyb (grid search for neural networks types)

### Language models: feature selection and grid search
- HuggingFace Sentiment Extraction.ipnyb (extracting pre-computed features from HuggingFace)
- Language Feature Extraction and Selection.ipnyb (extracting language features from the lyrics + performing feature selection on said features)
- Language Data Grid Search - Traditional and NN (3).ipynb (grid search for both traditional and neural network model types, this notebook also contains grid search for the traditional model based on BERT embeddings)
- RoBERTa Fine Tuning (3).ipynb (finetuning the RoBERTa language model to predict sentiment labels from our data)
  
### Ensemble/multimodal models
- One Multimodal Model.ipynb (grid search for traditional model types based on acoustic AND language features)
- Ensemble Models.ipynb (this notebook was > 25 MB, so could not upload to GitHub)

### Important!
The code in the notebooks mentioned above was repeated for the dominance, valence and arousal labels. Instead of uploading the same files three times, I have only uploaded the notebooks regarding predictions of the dominance label.





