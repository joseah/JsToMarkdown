#!/usr/bin/python

#' ---
#' title:        bash2markdown
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
#' python BashtoMarkdown.py -s example.sh -o html -c kult.css 
#' ```
#'

#' Import `re` library for using regular expressions
import re

#' Import `io` to deal with text enconding
import io

# Import pandoc wrapper

import pypandoc
###############################
## Install pypandoc via:      #  
## "sudo pip install pypandoc"#
###############################



#' Import `argparse` to handle command-line arguments
import argparse

parser = argparse.ArgumentParser(description='Gets parameters.')
parser.add_argument("-s", required=True)
parser.add_argument("-o", required=True)
parser.add_argument("-c", required=False)
args = parser.parse_args()


#' Open output markdown file
filename = args.s.replace(".sh", "")

#' Open file via a connection
file = open(args.s, 'r')

#' Open file via a connection
#file = open("/Users/joseah/Documents/lab_collado/github/SrcToMarkdown/test.sh", 'r')
script = map(str.strip,file.readlines())
file.close()


#' Convert script to markdown format 

md = []
prev_line = ''
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
            md.append("\n```sh")
            md.append(l)
        # Previous line was code
        elif l != '':
            md.append(l)
            
    if md_comm != -1:
        prev_line_code = False
    elif l != '':
        prev_line_code = True
    
    prev_line = l

if prev_line_code:
    md.append("```")
    
#print(*md,sep="\n")


#' Join list of lines
md = '\n'.join(md)

#' Write raw markdown file
md_file = open(filename + ".md", "w")
md_file.write(''.join(md))
md_file.close()

#' # Convert markdown to output format

if args.c:
    output_file = pypandoc.convert(md, args.o, format = "md", extra_args=['-c' + args.c, '--toc', '-N', '--self-contained', '--standalone'])
else:
    output_file = pypandoc.convert(md, args.o, format = "md")


#' # Write html output
output = io.open(filename + "." + args.o, "w", encoding='utf8')
output.write(output_file)
output.close()