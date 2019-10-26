"""Named-entity recognition with SpaCy"""

from collections import defaultdict
import sys

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

def search():
    text = open("module3/1959.txt").read()[:1000000]
    doc = nlp(text)
    people = defaultdict(int)
    for ent in doc.ents:
        if ent.label_ == sys.argv[2] and len(ent.text) > 3:
            people[ent.text] += 1
    sorted_people = sorted(people.items(), key=lambda kv: kv[1], reverse=True)

    for person, freq in sorted_people[:10]:
        print(f"{person} appears {freq} times in the corpus")


if __name__ == "__main__":
    try:
        if sys.argv[1] == "test":
            test()
        elif sys.argv[1] == "search" and sys.argv[2]!=[]:
            search()
        else:
            print("Unknown option, please use either 'test' or 'search' with an entity abbreviation as PER, LOC, ORG ...")
    except IndexError:
        print("No option, please specify either 'test' or 'search' with an entity abbreviation as PER, LOC, ORG ...")