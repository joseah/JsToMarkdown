#!/usr/bin/python

#' ---
#' title:        javascript2markdown
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
#' python JStoMarkdown.py -s functions.js -o html -c kult.css 
#' ```
#'



#' Import "sys" library for managing command parameters
import sys

#' Import "re" library for using regular expressions
import re

#' Import "io" to deal with text enconding
import io

#' Import pandoc wrapper

###############################
## Install pypandoc via:      #  
## "sudo pip install pypandoc"#
###############################

import pypandoc

#' Import "argparse" to handle command-line arguments
import argparse

parser = argparse.ArgumentParser(description='Gets parameters.')
parser.add_argument("-s", required=True)
parser.add_argument("-o", required=True)
parser.add_argument("-c", required=False)
args = parser.parse_args()

#' Flag variables
comment = 0
code = 0
prev_ends = 0

filename = args.s.replace(".js", "")

md = []

#' Open file via a connection

file = open(args.s, 'r')


#' Convert script to markdown format 

for l in file:
    l = l.strip('\n')

    # Identify when a comment is starting
    comment_begins  =  l.find("/*")

    # Identify when a comment is finishing
    comment_ends  =  l.find("*/")

    # We want to know when a commend has ended in the previous iteration
    prev_ends = comment_ends

    # If a comment begins, set flag variable as 1 and continue with next iteration
    # (When the "\*" is found, no action is needed)
    if(comment_begins != -1):
        comment = 1
        continue

    # If a comment finishes, set flag variable as 0 and continue with next iteration
    # (When the "\*" is found, no action is needed)
    if(comment_ends != -1):  
        comment = 0
        continue


    # If code variable is `1` (previous iteration) but there is a comment in current
    # iteration, add markdown tag to end block of code and set code flag variable to `0`  
    if(code and comment):
        md.append("```")
        code = 0

    # If a comment starts, save those lines
    if(comment == 1):
        md.append(l)

    # If there is no code and no comment in present iteration, add markdown flag to 
    # start code. Set variable code to `1` to indicate that following lines are code
    if(not code and not comment):
        if(l != ''):
            md.append("\n```js")
            code = 1

    # If there is code and not a comment, save all code
    if(code and not comment):
        if(l != ''):
            md.append(l)   
     
    
file.close()

if(comment == 0 and code):
    md.append("```")


#' Join list of lines
md = '\n'.join(md)

#' Write raw markdown file
md_file = open(filename + ".md", "w")
md_file.write(''.join(md))
md_file.close()


#' # Convert markdown to output format

if args.c:
    output_file = pypandoc.convert(md, args.o, format = "md", extra_args=['-c' + args.c, '--toc', '-N'])
else:
    output_file = pypandoc.convert(md, args.o, format = "md")


#' # Write html output
output = io.open(filename + "." + args.o, "w", encoding='utf8')
output.write(output_file)
output.close()
