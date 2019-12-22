"""Named-entity recognition with SpaCy"""

from collections import defaultdict
import sys
import csv
import os

import spacy
from spacy.lang.fr.examples import sentences 

nlp = spacy.load('fr_core_news_sm')

def test():
    """Basic test on sample sentences"""
    for sent in sentences:
        doc = nlp(sent)
        entities = []
        for ent in doc.ents:
            entities.append(f"{ent.text} ({ent.label_})")
        if entities:
            print(f"'{doc.text}' contains the following entities: {', '.join(entities)}")
        else:
            print(f"'{doc.text}' contains no entities")

year=sys.argv[3]
ents=sys.argv[2]
def search():
    os.system('say "Prêt pour "'+year) 
    text = open(f"module3/{year}.txt").read()[:1000000]
    doc = nlp(text)
    people = defaultdict(int)
    for ent in doc.ents:
        if ent.label_ == sys.argv[2] and len(ent.text) > 3:
            people[ent.text] += 1
    sorted_people = sorted(people.items(), key=lambda kv: kv[1], reverse=True)

  #  for person, freq in sorted_people[:20]:
   #     print(f"{person} appears {freq} times in the corpus")
    
    with open(f'/Users/myriam/tac/venv/csv/{year}{ents}.csv','w') as f:
        w = csv.writer(f)
        w.writerows(sorted_people)
        f.close

if __name__ == "__main__":
    try:
        if sys.argv[1] == "test":
            test()
        elif sys.argv[1] == "search" and sys.argv[2]!=[] and sys.argv[3]!=[]:
            search()
        else:
            print("Unknown option, please use either 'test' or 'search' with an entity abbreviation as PER, LOC, ORG ...")
    except IndexError:
        print("No option, please specify either 'test' or 'search' with an entity abbreviation as PER, LOC, ORG ...")