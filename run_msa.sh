#!/bin/bash

cd output_files/fasta_combinations

for file in *
do
  if [ ! -f ../alignments/$file ]; then
    echo $file
    muscle -align "$file" -output ../alignments/$file
  fi
done
