"""Playing with word2vec model"""

#%%
from gensim.models import Word2Vec
from pprint import pprint

model = Word2Vec.load("data/bulletins.model")

word1 = "eaux"
pprint(model.wv[word1])

#%%
word2 = "choléra"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
word2 = "eau"
sim1 = model.wv.similarity(word1, word2)
print(f"{word1} is {100*sim1:.1f}% similar to {word2}\n")

#%%
pprint(model.wv.most_similar("eau", topn=15))

#%%
pprint(model.wv.most_similar("eaux",topn=15))

#%%
pprint(model.wv.most_similar(positive=['installation', 'eaux'], negative=['eau'],topn=20))

# %%
