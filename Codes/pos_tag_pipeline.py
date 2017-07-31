# author    : SRvSaha
# Timestamp :  10:17 28-July-2017 (Friday)

####################################################################
## Pipeline for NLP to extract only tokens which are Noun & Verbs ##
####################################################################

import sys
from nltk import pos_tag, word_tokenize

# TODO: Remove Hardcoded Tags and pass tags as parameters


def word_pos_tag(input_sentence):
    output = []
    pos_tags = pos_tag(word_tokenize(input_sentence))
    for token, tag in pos_tags:
        if tag.startswith('N') or tag.startswith('V'):
            output.append(token.lower())
    return "\t".join(output)


if len(sys.argv) < 2:
    print("Argument(s) Missing.\nPlease run the program as follows: \
          python3 phrase_1_script.py < INPUT_FILE >")
    sys.exit()
else:
    with open(sys.argv[1]) as f:
        output = []
        for line in f.readlines():
            line = line.split("\t")
            if len(line) == 3:
                output.append('R' + line[0] + '\n')
            elif len(line) == 2:
                # TODO Pass the tags needed as parameters
                output.append(
                    'I' + line[0] + '\t' + word_pos_tag(line[1]) + '\n')
    with open("../Data/extracted_keywords.txt", 'w') as f:
        f.writelines(output)
        print("Output Successful :)")
