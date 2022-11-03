# phylogenetic_trees

Just a little project to generate a bunch of phylogenetic trees from FASTA format sequesnces from NCBI

split_fasta.py creates a bunch of fasta files with different mixes of 10 phylogenetic sequences from the input fasta file

run_msa.sh runs MUSCLE msa on fasta files to get multisequence alignment for all sequences in FASTA file

create_trees.sh takes a multisequence alignment file and creates a phylogenetic tree image

create_tree_images.py create png images of phylogenetic tree images