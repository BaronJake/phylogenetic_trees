#!/bin/bash

cd output_files/alignments

for file in *.fasta
do
    if [ ! -f ../alignments/$file.treefile ]; then
        iqtree -s $file -nt AUTO
    fi
done
