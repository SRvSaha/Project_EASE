#
#   @author      : SRvSaha
#   Filename     : create_w2c.py
#   Timestamp    : 11:57 03-August-2017 (Thursday)
#   Description  : Script to generate Word2Concept file in (KEY,VALUE) format
#

"""
Script to generate Word2Concept file in (KEY,VALUE) format.
This script takes in the keywords from recipes and assign concepts to keywords
from the Ontology Concepts. If found, concept is assigned, else None!
"""

import json
import sys
from collections import defaultdict

'''
Argument 1: Filename of Keywords
Argument 2: Filename of Concepts
'''
CONCEPTS = []
WORD2CONCEPT = {}
filename = '../Data/word2concept.txt'

try:
    with open(filename) as fp:
        WORD2CONCEPT = json.load(fp)
except FileNotFoundError:
    WORD2CONCEPT = defaultdict(int)  # Returns 0 if key is not found


def word2concept(word):
    if WORD2CONCEPT.get(word, 0) == 0:  # If the key doesn't exists
                                                        # check if you want to
                                                        # add concept or not.
        print("\nConcept List: \n")
        for i, c in enumerate(CONCEPTS):
            print(str(i) + '. ' + c)
        print("\nCurrent word is:", word,
              "|| Is Concept Available in the list?\n")
        choice = input(
            "Enter your choice:\n1. Yes  (Choose Appropriate Concept)\n2. No   (Skip this Word)\n3. Save and Exit\n\n")
        if choice == '1':
            concept = input("Enter Concept Number: ")
            WORD2CONCEPT[word] = CONCEPTS[int(concept)]
        elif choice == '2':
            pass
        else:
            print("Are you sure you want to exit?\n")
            option = input("1. Yes\n2. No\n\n")
            if option == '1':
                with open(filename, 'w') as f:
                    json.dump(WORD2CONCEPT, f,
                              indent=4, sort_keys=True, ensure_ascii=False)
                sys.exit()
            else:
                word2concept(word)


def main():
    if len(sys.argv) >= 3:
        with open(sys.argv[2]) as f:
            for line in f.readlines():
                CONCEPTS.append(line.strip())
        with open(sys.argv[1]) as f:
            for line in f.readlines():
                if line.strip().startswith("I"):
                    words = line.split('\t')[1:]
                    for word in words:
                        word = word.strip()
                        word2concept(word)  # Recursive Function
            with open(filename, 'w') as f:
                json.dump(WORD2CONCEPT, f,
                          indent=4, sort_keys=True, ensure_ascii=False)
    else:
        print("Argument(s) Missing!\nRun as: python3 create_w2c.py <RECIPE_INSTRUC\
    TIONS_KEYWORD_FILE> <ONTOLOGY_CONCEPTS_FILE>")
        sys.exit()


if __name__ == "__main__":
    main()
