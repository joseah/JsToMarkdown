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


#' # Define functions

'''#
## format_single_comment

### Description

This function takes a list where each item corresponds to one single line of 
the script file. All items are order according to original script.

### Parameters

| Parameters |                  Description                              |
|:----------:|:---------------------------------------------------------:|
| script     |     list corresponding to script file                     |
| lang       | programming language tag: python, perl, shell, javascript |


### Usage example 

```python
format_single_comment(file, "python")
```

### Output

- `md`: a list corresponding to script file with formatted single-line comments 
and code tags added to code chunks.

#'''

def format_single_comment(script, lang):
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
                md.append("\n```" + lang)
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


#' ---


'''#
## group

### Description

Splits a list according to a provided string pattern.


### Parameters

| Parameters |                  Description                              |
|:----------:|:---------------------------------------------------------:|
| seq        |     list corresponding to script file                     |
| sep        |    pattern used to split the list                         |


### Usage example 

```python
script_split = group(script, "\'\'\'#")
```

### Output

- `g`: a list of lists separated by provided string pattern

#'''

def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        g.append(el)
    yield list(g)



#' # Code starts

#' ## Import libraries

import re


#' Open file via a connection
file = open("/Users/joseah/Documents/lab_collado/github/SrcToMarkdown/test.py", 'r')
script = map(str.strip,file.readlines())
file.close()

markdown = []

#' Convert script to markdown format 

   


    
script_split = group(script, "'''#")


for l in script_split:
    i = list(group(l, "#'''"))

    if len(i) > 1:
        res = [x for x in i[0] if x != "'''#"]
        markdown.extend(res)
        
        res_2 = [x for x in i[1] if  x != "#'''"]
        res_2 = format_single_comment(res_2, "python")
        markdown.extend(res_2)

        
    else:
        res_3 = format_single_comment(i[0], "python")
        markdown.extend(res_3)

    

print(*markdown, sep="\n")
