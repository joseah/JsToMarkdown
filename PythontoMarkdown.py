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

md = []
#' Open file via a connection
file = open("/Users/joseah/Documents/lab_collado/github/SrcToMarkdown/SrctoMarkdown.py", 'r')

script = map(str.strip,file.readlines())

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


for line in script_split:
    
    x = list(map(lambda x: x.find("'''#"), line))
    
    if 0 not in x:
        print("```python")
        print(*line, sep='\n')
        print("```")
    else:
        comment_ends = list(group(line, "'''"))
        print(*comment_ends[0][1:], sep="\n")
        print(*comment_ends[1][1:], sep="\n")