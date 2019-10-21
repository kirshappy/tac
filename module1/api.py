"""Testing web APIs with HTTP GET method"""

import json
import requests
import sys #

def print_info(person_name):
    """Retrieve gender by name  from GENDER BY NAME API"""
    base_url = "https://udayogra-find-gender-by-name-v2/"
    name_url = base_url + "name/"
    code_url = base_url + "analysis/"
    resp = requests.get(name_url + person_name)
    try:
        pname = json.loads(resp.text)[0]
        female = pname['female']
        print(f"Female: {', '.join([lang['name'] for lang in female])}")
        male = pname['male']
        border_names = []
        print(f"Female: {', '.join([lang['name'] for lang in male])}")
    except KeyError:
        print("Unknown name please use first name")

if __name__ == "__main__":
    try:
        service = sys.argv[1]
        if service == "gender":
            try:
                person_name = sys.argv[2]
                print_info(person_name)
            except IndexError:
                print("Please enter a person name")
        else:
            print("Unknown action, please use 'gender'")
    except IndexError:
        print("Missing action, please use either 'gender'")
