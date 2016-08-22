#!/usr/bin/python

'''
---
title:        source2markdown
author:       Jose Alquicira Hernandez
---


# Description
 
This program takes a script written in **python**, **perl**, **javascript** or **shell**
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


| Parameters |                  Description                  |
|:----------:|:---------------------------------------------:|
| -s         | script file (with comments in markdown style) |
| -o         |              output format (html)             |
| -c         |                    css file                   |

# Usage example

```shell
python SrctoMarkdown.py -s functions.js -o html -c kult.css 
```

'''

#' # Program starts

#' Import `sys` library for managing command parameters
import sys

#' Import `re` library for using regular expressions
import re

#' Import `io to deal with text enconding
import io

# Import pandoc wrapper



import pypandoc

#' Import `argparse` to handle command-line arguments
import argparse

parser = argparse.ArgumentParser(description='Gets parameters.')
parser.add_argument("-s", required=True)
parser.add_argument("-o", required=True)
parser.add_argument("-c", required=False)
args = parser.parse_args()

