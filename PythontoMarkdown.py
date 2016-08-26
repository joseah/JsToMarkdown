#!/usr/bin/python

#' ---
#' title:        python2markdown
#' author:       Jose Alquicira Hernandez
#' ---


#' | Parameters |                  Description                  |
#' |:----------:|:---------------------------------------------:|
#' | -s         | script file (with comments in markdown style) |
#' | -o         |              output format (html)             |
#' | -c         |                    css file                   |


#' # Usage example
#'
#' ```shell
#' python PythontoMarkdown.py -s example.pl -o html -c kult.css 
#' ```
#'


import re


md = []

#' Open file via a connection
file = open("/Users/joseah/Documents/lab_collado/github/SrcToMarkdown/test.py", 'r')
script = map(str.strip,file.readlines())
file.close()

md = []

#' Convert script to markdown format 

def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield g
    
script_split = list(group(script, "'''#"))

for i in script_split:
    i = list(group(i, "#'''"))
    
    if len(i) > 1:
        res = [x for x in i[0] if x != '' and x != "'''#"]
        print(res)

    
#' ---

#print(*md,sep="\n")

#md2 = []
#        
#for l in md:
#    if l.find("#'") != -1:
#        l_format = re.sub("#'\s*", '', l)
#        md2.extend(l_format)
#    else:
#        md2.extend(l)
#
#print(md2)





#for i,l in enumerate(md):
#    if l.find("#'") != -1:
#        md[i] = re.sub("#'\s*", '', l)
#        
#print(*md,sep="\n")
