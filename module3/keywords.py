"""Testing keyword extraction with YAKE"""

import os
import yake
import sys

ignored = set(["conseil communal", "conseil général",
"commission d'assistance","commission d'assistance publique","commission assistance","assistance publique"
"monsieur le bourgmestre","bourgmestre","monsieur le président",
"ville de bruxelles","ville","bruxelle","mesdames et messieurs","mesdames","messieurs","van","het","een"])

year = sys.argv[1]

kw_extractor = yake.KeywordExtractor(lan="fr", top=20)
data_path = "data/txt/"
files = os.listdir(data_path)
for f in sorted(files):
    if f.startswith(f"Bxl_{year}"):
        text = open(data_path + f).read()
        keywords = kw_extractor.extract_keywords(text)
        kept = []
        for score, kw in keywords:
            words = kw.split()
            if len(words) > 1 and kw not in ignored:
                kept.append(kw)
        print(f"{f} mentions these keywords: {', '.join(kept)}...")

