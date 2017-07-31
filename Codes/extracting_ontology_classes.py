#
#   @author      : SRvSaha
#   Filename     : extracting_ontology_classes.py
#   Timestamp    : 11:41 31-July-2017 (Monday)
#   Description  : Extracting the Ontology Concepts from OWL/XML file by REGEX
#

"""
Extracting the Ontology Concepts from OWL/XML file by REGEX

To Run: python3 extracting_ontology_classes.py <INPUTFILE> <OUTPUTFILE>
<INPUTFILE>  : Any file, as in our case : foo.owl or bar.xml both works
<OUTPUTFILE> : Name of the output file to save one ontology concept per line
"""

import sys
import re


# TODO: Add Argument Parser

def file_read():
    '''
    Reads the input file passed as argument from command line.
    '''
    if len(sys.argv) < 2:
        print("Argument(s) Missing")
        sys.exit()
    elif len(sys.argv) >= 2:
        return open(sys.argv[1])


def file_write(output_list):
    '''
    Writes the Ontology Concepts Extracted by RegularExpression in a format
    of one concept per line
    '''
    if len(sys.argv) < 2:
        print("Argument(s) Missing")
        sys.exit()
    elif len(sys.argv) == 2:
        f = open('../Data/ontology_concepts.txt', 'w')
        f.write('\n'.join(output_list))
        print("Output Successful :)")

    elif len(sys.argv) >= 3:
        f = open(sys.argv[2], 'w')
        f.write('\n'.join(output_list))
        print("Output Successful :)")
    f.close()


def extract_concepts(file_object):
    # Using Regex & Groups in Regex to Extract only the concepts in the Owl
    # Class
    pattern = re.compile("<owl:Class .*\#(.*)\">")
    output_list = pattern.findall(file_object.read())
    file_write(output_list)

if __name__ == '__main__':
    extract_concepts(file_read())
