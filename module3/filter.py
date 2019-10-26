"""Filter out stopwords for word cloud"""

import sys
import nltk
from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout","puisque","outre","avant", 
       "ils","elles", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous","quelque","part",
       "celle","ceux", "entre", "encore", "toutes","toute" "pendant", "moins", "dire", "cela", "non",
       "voudrais","considérant","leurs","plusieurs","celui","certaines","quand","quant","pense","beaucoup","pendant",
       "vient","devant","dessus","etc","agit","certaine","certain","car","alors","crois","ici","peu","pourrait",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres","quelques","cependant","notamment","toujours",
       "van", "het", "autre", "jusqu","chez","idem","avant","déjà","très","parce","que","commission","assistance","publique","question","art","article",
       "conseil","communal","mesdames","messieurs","monsieur","bourgmestre","bruxelle",
       "janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
sw = set(sw)

year = sys.argv[1]

path = f"module3/{year}.txt"
output = open(f"module3/{year}_keywords.txt", "w")

with open(path) as f:
    text = f.read()
    words = nltk.wordpunct_tokenize(text)
    kept = [w.lower() for w in words if len(w) > 2 and w.isalpha() and w.lower() not in sw]
    kept_string = " ".join(kept)
    output.write(kept_string)