#!/usr/bin/python

'''#

---
title: SrctoMarkdown.py
subtitle: Convert script to markdown document
author: Jose Alquicira Hernandez
---


# Description
 
This program takes a script written in **python**, **perl**, **javascript**, **R** or **shell**
and generates a markdown document with comments processed as markdown and code embedded in
markdown code tags.


# Requirements
 
## Pandoc
 
This program requires [Pandoc](http://pandoc.org/) to convert the markdown output generated
with this program to any other format.

Download Pandoc from the [installing webpage](http://pandoc.org/installing.html). 

## pypandoc

In order to use pandoc within python, pypandoc wrapper is required.

Install `pypandoc` via `pip`:

```bash
sudo pip install pypandoc
```

> See [pip webpage](https://pip.pypa.io/en/stable/installing/) if you do not use `pip` yet


# Parameter description


| Parameters |                  Description                   |
|:----------:|:----------------------------------------------:|
| -s         | script file (with comments in markdown style)  |
| -o         |      output format (html, pdf, rst, ...)       |
| -c         |                    css file                    |
| -md        |            Write markdown output               |
| -pandoc    |Path to pandoc. Default `/usr/local/bin/pandoc` |

# Usage example

```shell
python SrctoMarkdown.py -s functions.js -o html -c kult.css -md
```

#'''

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
        md_comm = re.match("#'", l)
        
        # Currrent line is a comment
        if md_comm != None:
            # Previous line was code
            if prev_line_code:
                md.append("```\n")
            # Previous line was not code
            if l != '':
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
                
        if md_comm != None:
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

Splits a list according to a string pattern.


### Parameters

| Parameters |                  Description                              |
|:----------:|:---------------------------------------------------------:|
| seq        |     list corresponding to script file                     |
| sep        |    pattern used to split the list                         |


### Usage example 

```python
script_split = group(script, "\'''#")
```

### Output

- `g`: a list of lists separated by provided string pattern

#'''

def group(seq, sep):
    g = []
    for el in seq:
        if re.match(sep, el) != None :
            yield g
            g = []
        g.append(el)
    yield list(g)



'''#
## format_multiple_line_comment

### Description

This function takes a list where each item corresponds to one single line of 
the script file. All items are ordered according to original script.

### Parameters

| Parameters |                  Description                              |
|:----------:|:---------------------------------------------------------:|
| script     |     list corresponding to script file                     |
| lang       | programming language tag: python, perl, shell, javascript |
| comment_tag_start | Tag to indicate markdown multiple-line comment start(\'\'\'# or /*) |
| comment_tag_end | Tag to indicate markdown multiple-line comment end (#\'\'\' or */) |

### Usage example 

```python
format_single_comment(file, "python")
```

### Output

- `markdown`: a list corresponding to script file with formatted single-line 
comments, multiple-line comments and code tags added to code chunks.

#'''



def format_multiple_line_comment(script, lang, 
                                 comment_tag_start, comment_tag_end):

    markdown = []
    script_split = group(script, comment_tag_start)

    for l in script_split:
        i = list(group(l,comment_tag_end))
        if len(i) > 1:
            res = [re.sub("^\s*", '', x).rstrip("\n") for x in i[0] if re.match(comment_tag_start, x) == None ]
            markdown.extend(res)

            
            res_2 = [x for x in i[1] if  re.match(comment_tag_end, x) == None]
            res_2 = format_single_comment(res_2, lang)
            markdown.extend(res_2)
            
        else:
            res_3 = format_single_comment(i[0], lang)
            markdown.extend(res_3)
    
    return(markdown)
    

#' # Code starts

#' ## Import libraries

#' Import `re` to use regular expressions
import re

#' Import `argparse` to handle command-line arguments
import argparse

#' Import pandoc wrapper
import pypandoc

#' Import `sys` library
import sys

#' Set path to pandoc
import os

#' Get parameters 
parser = argparse.ArgumentParser(description='Gets parameters.')
parser.add_argument("-s", required=True)
parser.add_argument("-o", required=True)
parser.add_argument("-c", required=False)
parser.add_argument("-md", required=False, action="store_true")
parser.add_argument("-pandoc", required=False)

args = parser.parse_args()


#' Set path to `pandoc`

if args.pandoc:
    os.environ.setdefault('PYPANDOC_PANDOC', args.pandoc)
else:
    os.environ.setdefault('PYPANDOC_PANDOC', '/usr/local/bin/pandoc')


#' Validate output format

valid_formats= ["asciidoc", "beamer", "commonmark", "context", "docbook", "docx", 
 "dokuwiki", "dzslides", "epub", "epub3", "fb2", "haddock", "html", "html5", 
 "icml", "json", "latex", "man", "markdown", "markdown_github", "markdown_mmd", 
 "markdown_phpextra", "markdown_strict", "mediawiki", "native", "odt", "opendocument", 
 "opml", "org", "pdf", "plain", "revealjs", "rst", "rtf", "s5", "slideous", "slidy", 
 "tei", "texinfo", "textile"]
 
if args.o not in valid_formats:
    sys.exit("ERROR: Invalid output format. Expected one of these:\n" + 
    ', '.join(valid_formats))

#' Validate if input file exists

if not os.path.isfile(args.s):
    sys.exit("ERROR: no '" + args.s + "' file exists")

if args.c:
    if not os.path.isfile(args.c):
        sys.exit("ERROR: no '" + args.c + "' file exists")

#' Get filename and language program
script_info = args.s.split(".")
filename = script_info[0]
extension = script_info[1]


#' Open file
file = open(args.s, 'r')
script = file.readlines()
file.close()

#' Convert script to markdown format 

if extension == "pl":
    md_doc = format_single_comment(script, "perl")
elif extension == "sh":
    md_doc = format_single_comment(script, "bash")
elif extension == "R" or extension == "r":
    md_doc =  format_single_comment(script, "R")
elif extension == "py":
    md_doc = format_multiple_line_comment(script, "python", "'''#", "#'''")
elif extension == "js":
    md_doc = format_multiple_line_comment(script, "js", "/**", "**/")
elif extension == "java":
    md_doc = format_multiple_line_comment(script, "java", "/**", "**/")

#' Join list of lines
md = '\n'.join(md_doc)

#' Write raw markdown file
md_file = open(filename + ".md", "w")
md_file.write(''.join(md))
md_file.close()

#' # Convert markdown to output format

if args.c and args.o == "html":
    pandoc_args=['-c' + args.c, '--toc', '-N', '--self-contained', '--standalone']
    
    output = pypandoc.convert(filename + ".md", 'html', outputfile = filename + '.html', 
                              extra_args = pandoc_args)
    assert output == ""
else:
    output = pypandoc.convert(filename + ".md", 'html', outputfile = filename + '.html')
    assert output == ""


if args.o != "html":
    output = pypandoc.convert(filename + ".md", args.o, outputfile = filename + "." +args.o)
    assert output == ""

#' Remove markdown output file?
if not args.md:
    os.remove(filename + ".md")