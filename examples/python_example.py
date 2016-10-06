#' ---
#' title:        set-region.py
#' author:       Jose Alquicira Hernandez
#' ---


#' # Description 
#' 
#' This program takes a relationship and `.evec` file (output from smartPCA) in order to set regions to each individual.
#'

'''#
| Parameters |                  Description                  |
|:----------:|:---------------------------------------------:|
| 1st        | relationship file (id and region)             |
| 2nd        |              `.evec` file                     |
#'''


'''#

- Relationship file is built using ids from PLINK file and population metadata
- `.evec` file is obtained running a PCA usig `smartPCA`

#'''



#' # Usage example
#'
#' ```shell
#' python set-region.py genotypes.pop genotypes.evec
#' ```
#'

#' # Code starts

# Import `sys` library for managing command parameters
import sys

# Import `sys library for using regular expressions
import re

data = sys.argv[1] # relationship file
data_2 = sys.argv[2] # *ind file

eth = {}

# Open file via a connection
rs = open(data, 'r')
for l in rs:
        l = l.rstrip('\n')
        l = l.rsplit('\t')
        eth[l[0]] = l[1] + '\t' + l[2]
rs.close()

rs = open(data_2, 'r')
for l in rs:
        if not re.match(".+#.+", l):
                l = l.rstrip('\n')
                # Regular expression for 4 eigenvectors
                ide = re.findall("^\s+(\w+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(\W+|\w+)$", l)
                ncol = int(len(ide[0]))
                for i in xrange(0,ncol-1):
                        print ide[0][i] + "\t",
                request = eth.get(ide[0][0],None)
                print request

# Close file connection
rs.close()
