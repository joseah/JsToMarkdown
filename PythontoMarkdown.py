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


#' Open file via a connection
file = open("/Users/joseah/Documents/lab_collado/github/SrcToMarkdown/test.py", 'r')
script = map(str.strip,file.readlines())
file.close()

md = []

#' Convert script to markdown format 

def format_single_comment(script):
    md = []
    prev_line_code = False
    
    for l in script:  
        l = l.strip('\n')
        md_comm = l.find("#'")   
        
        # Currrent line is a comment
        if md_comm != -1:
            # Previous line was code
            if prev_line_code:
                md.append("```")
            # Previous line was not code
            l_format = re.sub("#'\s*", '', l)
            md.append(l_format)
            
        # Current line is not a comment        
        else:
            # Previous line was not code
            if not prev_line_code and l != '':
                md.append("\n```python")
                md.append(l)
            # Previous line was code
            elif l != '':
                md.append(l)
                
        if md_comm != -1:
            prev_line_code = False
        elif l != '':
            prev_line_code = True

    if prev_line_code:
        md.append("```")
    return(md)    

def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield g
    
script_split = list(group(script, "'''#"))

#print(*script_split, sep="\n")

for l in script_split:
    i = list(group(l, "#'''"))

    if len(i) > 1:
        res = [x for x in i[0] if x != "'''#"]
        print(*res, sep="\n")
        res_2 = [x for x in i[1] if  x != "#'''"]
        res_2 = format_single_comment(res_2)
        print(*res_2, sep="\n")
        
    else:
        i[0] = format_single_comment(i[0])
        print(*i[0], sep="\n")

    



#format_single_comment(md)

