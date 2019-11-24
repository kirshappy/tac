"""Playing with word2vec model"""

#%%
from gensim.models import Word2Vec
from pprint import pprint

model = Word2Vec.load("data/bulletins.model")

word1 = "théâtre"
pprint(model.wv[word1])

#%%
word2 = "église"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
word2 = "cimetière"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
pprint(model.wv.most_similar("école", topn=15))

#%%
pprint(model.wv.most_similar("hôpital",topn=10))

#%%
pprint(model.wv.most_similar(positive=['mathématiques', 'université'], negative=['athénée'],topn=20))

# %%
