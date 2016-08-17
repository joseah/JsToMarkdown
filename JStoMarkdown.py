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

#' Open output markdown file
filename = args.s.replace(".js", "")

md = []
#' Open file via a connection
file = open(args.s, 'r')
for l in file:
        l = l.strip('\n')
        comment_begins  =  re.match(".*[/]+[*]+.*", l)
        comment_ends  =  re.match(".*[*]+[/]+.*", l)
        
        #' If a comment ends, indicate that a comment has finished
        if(comment_ends != None):
            comment = 0

        #' If we are within a comment, print all lines
        if(comment == 1):
             md.append(l)

        #' If a comment begins, indicate that there is a comment
        if(comment_begins != None):
            comment = 1

        #' If a comment ends, indicate that a comment has finished
        if(comment_ends != None):
            md.append('\n')
            comment = 0

        #' If a comment has not started and has not ended it means that there is a chunk of code. 
        #' Print markdown code label and indicate that code has started
        if(comment == 0 and code == 0):
            if(l != '' and l != "*/"):
                md.append("\n```js")
                code = 1

        #' If a comment has not started and has not ended it and there is code we want to print all lines
        if(comment == 0 and code):
            if(l != '' and l != "*/"):
                md.append(l)

        #' If a comment has started it means that the chunk of code has finished. End chunk of code and indicate
        #' that there is no code anymore.
        if(comment_begins != None and code):
            md.append("```")
            code = 0
      
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
