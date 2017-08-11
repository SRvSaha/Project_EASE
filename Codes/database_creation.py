#
#   @author      : SRvSaha
#   Filename     : database_creation.py.py
#   Timestamp    : 12:44 11-August-2017 (Friday)
#   Description  : Database for Querying Discourse Relationships
#

"""
Artificial Episodic Memory Prototype
Database for Querying Discourse Relationships where each Recipes has n episodes
and each episode consist of Concept Set

Format of Database:
{
    'R1' :  {
                'C1.1'  :   {'Preheating':[#Occurance, #DiscourseDistance, #Co-occurance_Set], 'Action':[#Occurance, #DiscourseDistance, #Co-occurance_Set], .....},
                'C1.2'  :   {'sugar': [], 'Add':[],.....    }

            },
    'R2' :  {
                'C2.1'  :   { }
            }
}

Tail/Episodic Details:
# Occurance: Number of times the concept occured in the recipe
# DiscourseDistance: Distance from the last occuring concept set, eg. If Concept X occured in C2.2 and the in C2.4, distance = 4
# Co_occurance_Set: Set of all the other concepts that co-occured with the present concept in this recipe

To Run: python3 database_creation.py <CONCEPT_SET_FILE>
CONCEPT_SET_FILE: File Consisting of Recipes and Concepts
"""
from sys import argv, exit
import json

# For removing duplicates & maintaining order of insertion
from collections import OrderedDict

filename = '../Data/database.json'


output = '{'
if len(argv) >= 2:
    with open(argv[1]) as f:
        for line_num, line in enumerate(f):
            if line.startswith("R"):
                CONCEPT_SET = {}
                INDEX = {}

                splitted_recipe = line.split("\t")
                len_instruction = int(splitted_recipe[1].strip())
                if line_num == 0:
                    output += '"' + splitted_recipe[0] + '" : {'
                else:
                    output += '},"' + splitted_recipe[0] + '" : {'

            elif line.startswith("C"):
                splitted_line = line.split("\t")
                concept_num = splitted_line[0]
                concepts = splitted_line[1:]
                concepts[-1] = concepts[-1].strip()
                output += '"' + concept_num + '" : {'
                for i, concept in enumerate(concepts):

                    if CONCEPT_SET.get(concept, 0) == 0:
                        INDEX[concept] = int(
                            concept_num[concept_num.rfind(".") + 1:])
                        CONCEPT_SET[concept] = [0, INDEX[concept], concepts]
                    else:
                        CONCEPT_SET[concept][0] += 1
                        CONCEPT_SET[concept][1] = abs(
                            int(concept_num[concept_num.rfind(".") + 1:]) - INDEX[concept])
                        INDEX[concept] = int(
                            concept_num[concept_num.rfind(".") + 1:])
                        # print(CONCEPT_SET[concept][1], int(
                        #     concept_num[concept_num.rfind(".") + 1:]), abs(
                        #     CONCEPT_SET[concept][1] - int(concept_num[concept_num.rfind(".") + 1:])))
                        CONCEPT_SET[concept][2] = list(
                            set().union(CONCEPT_SET[concept][2], concepts))
                    if i != len(concepts) - 1:
                        if CONCEPT_SET[concept][0] != 0:
                            output += '"' + concept + '" : "' + \
                                str(CONCEPT_SET[concept]) + '",'
                        else:
                            output += '"' + concept + \
                                '" : "' + str(None) + '",'
                    else:
                        if len_instruction != int(concept_num[concept_num.rfind(".") + 1:]):
                            if CONCEPT_SET[concept][0] != 0:
                                output += '"' + concept + '" : "' + \
                                    str(CONCEPT_SET[concept]) + '" },'
                            else:
                                output += '"' + concept + \
                                    '" : "' + str(None) + '" },'
                        else:
                            if CONCEPT_SET[concept][0] != 0:
                                output += '"' + concept + '" : "' + \
                                    str(CONCEPT_SET[concept]) + '" }'
                            else:
                                output += '"' + concept + '" : "' + \
                                    str(None) + '" }'
    output += '}}'
    with open(filename, 'w') as f:
        json.dump(json.loads(output, object_pairs_hook=OrderedDict),
                  f, indent=4)
        print("Output successful in", filename)
else:
    print("Argument(s) Missing!\nPlease run as: python3 database_creation.py <CONCEPT_SET_FILE>")
    exit()
