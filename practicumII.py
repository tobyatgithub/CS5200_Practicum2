import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

xml_path = '/Users/toby/Documents/ACADEMIC_Northeastern/2021_fall/CS 5200 database/Practicum_II/pubmed_sample.xml'
# tree = et.parse(
#   xml_path
# )

# root = tree.getroot()
# pages = list(root)

# for member in root.findall('PubmedArticle'):
#     name = member.find('Article').text
#     break

# # `import pdb

# # pdb.set_trace()`

# # for article in root.iter("PubmedArticle"):
# #     print(article.text)
# #     # break

# for page in pages[:3]:
#     article = page.findall("Article")

#     # PMID = page.find("PMID").text
#     print(citation, PMID)
#     # break

# # print(root)

from bs4 import BeautifulSoup

with open(xml_path) as file:
    soup = BeautifulSoup(file, "html.parser")
    # print(soup)

articles = soup.find_all("pubmedarticle")
title = []
MedlineCitation = []
for article in articles[:1]:
    # import pdb
    # pdb.set_trace()
    medcitations = article.find_all("MedlineCitation".lower())
    for medcite in medcitations:
        pmid = medcite.find("pmid").get_text()
        print("PMID = ", pmid)
        MedlineCitation.append(medcite.get_text())
    title.append(article.get_text())
    # break
# print(title)
print(len(MedlineCitation), MedlineCitation)