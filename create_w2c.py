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

'''
Argument 1: Filename of Keywords
Argument 2: Filename of Concepts
'''
CONCEPTS = []
if len(sys.argv) >= 3:
    with open(sys.argv[2]) as f:
        for line in f.readlines():
            CONCEPTS.append(line.strip())

else:
    print("Argument(s) Missing!\nRun as: python3 create_w2c.py <RECIPE_INSTRUC\
TIONS_KEYWORD_FILE> <ONTOLOGY_CONCEPTS_FILE>")
    sys.exit()
