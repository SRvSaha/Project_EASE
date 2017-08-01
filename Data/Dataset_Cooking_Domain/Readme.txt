The Corpus is built by scrapping(unofficially) the website 'http://kitchenstories.io' 
on 01/08/2017 by a python script developed by Saurav Saha (Github: SRvSaha) with
the help of Python Requests, Beautiful Soup with lxml parser.

The Corpus is built for cooking domain which consist of 698 recipes and instructions
for the recipes. The corpus is of the format:

R1<tab>Length1<\n>
I1.1<tab>INSTRUCTION 1 / STEP 1<\n>
I1.2<tab>INSTRUCTION 2 / STEP 2<\n>
I1.3<tab>INSTRUCTION 3 / STEP 3<\n>
.
.
.
I1.(Length1)<tab>INSTRUCTION Length1 / STEP Length1<\n>
R2<tab>Length2
I2.1<tab>INSTRUCTION 1 / STEP 1<\n>
I2.2<tab>INSTRUCTION 2 / STEP 2<\n>
.
.
.
I2.(Length2)INSTRUCTION Lenght2 / STEP Length2<\n>
.
.
.
.

The Corpus can be reproduced using the Python Script - full_dataset_building.py
Requirements:
1. Python3
2. Requests
3. BeautifulSoup4
4. lxml

In Case of UNIX/LINUX based systems, go to the TERMINAL and just run:

python3 full_dataset_building.py

For Windows, go to cmd, and run:

python3 full_dataset_building.py


NOTE: It'll take around 20-25 minutes depending on the number of recipes available
in the website. In the Terminal/Command Promt, a number will be prompted stating
the number of recipes crawled. Once, done it'll show "Operation Successful in file: Data/full_dataset.txt"


Copyright: Saurav Saha (SRvSaha), Digital Media Lab, University of Bremen
Email: contact[dot]srvsaha[at]gmail[dot]com

