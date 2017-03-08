
# coding: utf-8

# In[32]:

import os
import sys
import re


# In[85]:

abstract_dir = "data/hep-th-abs"
citation_doc = "data/hep-th-citations"

abstract_dict = {}
def organize_abstract(text):
    lines = text.split('\n')
    for l in lines:
        if l.startswith("Paper: "):
            id=l.split("/")[1]
            abstract_dict[id] = {}
        if l.startswith("Date: "):
            dateline = re.split("[:()]", l)
            abstract_dict[id]['date'] = dateline[1][:-3]
        if l.startswith('Title: '):
            titleline = l.split("Title: ")[1]
            abstract_dict[id]['title'] = titleline
        if l.startswith('Authors: '):
            authorline = l.split("Authors: ")[1]
            authors = authorline.replace(',',' and').split(' and ')
            abstract_dict[id]['authors'] = authors
        if l.startswith('Comments: '):
            commentline = l.split("Comments: ")[1]
            abstract_dict[id]['comments'] = commentline
        if l.startswith("Journal-ref: "):
            abstract_dict[id]['journal'] = l.split(' ')[1]
            
    text.split('\\')[-1]
    abstract_dict[id]['abstract'] = text.split('\\')[-3].replace('\n','')

def import_abstracts():
    for (dirpath, dirnames, filenames) in os.walk(abstract_dir):
        for d in dirnames:
            d = abstract_dir + "/" + d
            for (dirpath, dirnames, filenames) in os.walk(d):  
                for f in filenames:
                    f = d + '/' + f
                    with open(f, 'r') as myfile:
                        text=myfile.read()
                        organize_abstract(text)
def import_citations():
    citations = [tuple(line.rstrip('\n').split(' ')) for line in open(citation_doc)]

import_abstracts()
import_citations()


# In[ ]:





# In[ ]:




# In[ ]:




# In[ ]:



