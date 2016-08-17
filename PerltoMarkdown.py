#!/usr/bin/python

'''
Title:        Convert perl scripts to markdown and html
Author:       Jose Alquicira Hernandez <alquicirajose at gmail.com>
Status:       Active
Type: Process
Created:      09-Mar-2016
Post-History: 16-Mar-2016
Python version: 2.6.6
'''

# Parameters:
# 1st = .js file
# 2nd = .output file format
# 3rd (Optional)= css file

#' Usage example
#'
#' ```shell
# python PerltoMarkdown.py -s example.pl -o html -c kult.css 
#' ```

#' Import "sys" library for managing command parameters
import sys

#' Import "re" library for using regular expressions
import re

#' Import "io" to deal with text enconding
import io

# Import pandoc wrapper

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
filename = args.s.replace(".pl", "")

md = []
#' Open file via a connection
file = open(args.s, 'r')
for l in file:
        l = l.strip('\n')
        md_comm =  re.match(".*^[#]{1}[']{1}.*", l)
        # print(md_comm)


        #' If a comment has started it means that the chunk of code has finished. End chunk of code and indicate
        #' that there is no code anymore.
        if(md_comm != None and code):
            md.append("```\n")
            code = 0

        #' If we are within a markdown comment, format line and append
        if(md_comm):
            l_format = re.sub("#'\s*", '', l)
            md.append(l_format)

        #' If a comment has not started it means that there is a chunk of code. 
        #' Print markdown code label and indicate that code has started

        if(md_comm == None and code == 0):
            if(l != ''):
                md.append("\n```perl")
                code = 1    

        #' If a comment has not started, there is code we want to append
        if(md_comm == None and code):
            if(l != ''):
                md.append(l)


      
file.close()

if(code):
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
