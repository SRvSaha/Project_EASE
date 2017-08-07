#
#   @author      : SRvSaha
#   Filename     : database_creation.py.py
#   Timestamp    : 02:17 07-August-2017 (Monday)
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
#Occurance: Number of times the concept occured in the recipe
#DiscourseDistance: Distance from the last occuring concept set, eg. If Concept X occured in C2.2 and the in C2.4, distance = 4
#Co_occurance_Set: Set of all the other concepts that co-occured with the present concept in this recipe

To Run: python3 database_creation.py <CONCEPT_SET_FILE>
CONCEPT_SET_FILE: File Consisting of Recipes and Concepts
"""
from sys import argv, exit
import json

# For removing duplicates & maintaining order of insertion
from collections import OrderedDict

filename = '../Data/database.json'

DATABASE = OrderedDict()
CONCEPT_SET = OrderedDict()

if len(argv) >= 2:
    with open(argv[1]) as f:
        for line in f.readlines():


else:
    print("Argument(s) Missing!\nPlease run as: python3 database_creation.py <CONCEPT_SET_FILE>")
    exit()
