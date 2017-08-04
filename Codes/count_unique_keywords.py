#
#   @author      : SRvSaha
#   Filename     : count_unique_keywords.py
#   Timestamp    : 04-August-2017 (Friday)21:49
#   Description  : Script to count unique keywords for Word2Concept file
#

"""
Script to count unique keywords for Word2Concept file and to generate the set
of unique words in test data <10 Recipes>
"""

import sys
KEYWORDS = set()

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if line.startswith('I'):
            words = line.split("\t")[1:]
            for word in words:
                KEYWORDS.add(word.strip())
print(len(KEYWORDS))
print(KEYWORDS)
