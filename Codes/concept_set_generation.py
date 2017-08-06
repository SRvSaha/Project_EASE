#
#   @author      : SRvSaha
#   Filename     : concept_set_generation.py
#   Timestamp    : 00:22 07-August-2017 (Monday)
#   Description  : To generate Concept Set against each instruction in Recipe
#

"""
Script to generate Concept Set against each instruction in Recipe

RUN: python3 concept_set_generation.py <STANFORD_LEMMATIZED_FILE> <WORD2CONCEPT_MAPPING_FILE>

STANFORD_LEMMATIZED_FILE: File where each keyword in instruction is lemmatized
WORD2CONCEPT_MAPPING_FILE: Word2Concept HashMap or Dictionary File
"""

from sys import argv, exit
import json
from collections import OrderedDict

filename = "../Data/concept_set.txt"


if len(argv) >= 3:
    with open(argv[2]) as f:
        WORD2CONCEPT = json.load(f)
    f_out = open(filename, 'w')
    with open(argv[1]) as f:
        for line in f.readlines():
            output = ""
            CONCEPT_SET = OrderedDict()
            if line.startswith("R"):
                f_out.write(line)
            else:
                tokens = line.split('\t')
                output += 'C' + tokens[0][1:] + '\t'
                for token in tokens[1:]:
                    if WORD2CONCEPT.get(token, 0) != 0:
                        CONCEPT_SET[WORD2CONCEPT[token]] = None
                for concept in CONCEPT_SET:
                    output += concept + '\t'
                f_out.write(output.strip() + '\n')
        print("Output Successful in filename: ../Data/concept_set.txt")
else:
    print("Argument(s) Missing!\nPlease run as follows: python3 concept_set_ge\
neration.py <STANFORD_LEMMATIZED_FILE> <WORD2CONCEPT_MAPPING_FILE>")
