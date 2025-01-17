"""Query Wikidata for Belgian politicians"""

import argparse
from datetime import datetime as dt
import sys

from SPARQLWrapper import SPARQLWrapper, JSON 

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?item ?itemLabel ?place ?placeLabel WHERE {
        ?place wdt:P17 wd:Q31;
          wdt:P31 wd:Q39614;
          wdt:P131 ?item.
        ?item wdt:P131 wd:Q90870.

        SERVICE wikibase:label { bd:serviceParam wikibase:language "en","fr". }
    }
order by ?itemLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Brussels cimeterys found\n")
    return rows

def show(rows, filter=None, n=10):
    """Display n cemeterys (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    if filter:
        rows = [row for row in rows if filter in row['placeLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            commune= row['itemLabel']['value']
        except ValueError:
            commune = "????"
        print(f"{row['placeLabel']['value']} ({commune})")

if __name__ == "__main__":
    args = parser.parse_args()
    rows = get_rows()
    filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(rows, filter, number)
