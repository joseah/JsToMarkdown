#' ---
#' title:        Get strand from fasta file
#' author:       Jose Alquicira Hernandez
#' ---


#' # Overview
#' This program takes a fasta file and extracts strand information for each sequence.
#'

#' | Parameters |                  Description                  |
#' |:----------:|:---------------------------------------------:|
#' | -f         |                FASTA file                     |
#' | -h         |              displays help                    |




#' # Usage example
#'
#' ```bash
#' perl perl_example.pl -f ecoli.fa
#' ```
#''

#' Code starts

# Import required libraries
use strict;
use Getopt::Long;
my %opts = ();
GetOptions (\%opts,'f=s');             
if(scalar(keys(%opts))==0)
{
        print "Parameters:\n";
        print "-f       FASTA file\n";
        print "-h | -help        Ayuda\n";
        exit;
}
if($opts{'h'})                 
        &PrintHelp;
}
sub PrintHelp
{
        system "pod2text -c $0 ";
        exit();
}
# Open fasta file
open (DATOS, $opts{f});
my $sequence;
my $title;
while (my $line = <DATOS>)
{
        if ($line =~ /^>.+\[gene=(\w+)\].+\[location=(complement)?\(?(\d*)\.\.(\d*)\)?\]/)
        {
                print "\n$1\t$3\t$4\t";
                if ($2) 
                {
                        print "reverse\t";
                }else
                {
                        print "forward\t";
                }
   
        
        }
        if ($line =~ /^[ATCG]+/)
        {
                $line =~ s/\n//;
                print "$line";
        }
}
close (DATOS);