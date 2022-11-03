from calendar import c
from itertools import combinations
import re

fasta_delimiter = ">"
with open("input_files/sequence.fasta") as file:
    sequences = file.read().split(fasta_delimiter)
sequences = [fasta_delimiter + sequence.replace("PREDICTED: ", "") for sequence in sequences if sequence]

pattern = re.compile(r">[XN]M_\d*\.\d*\W+(\w+\W+\w+).*")
fasta_to_species_dict = {sequence:pattern.match(sequence).group(1) for sequence in sequences}
species_to_common_name_dict = {
    "Homo sapiens": "Human",
    "Gorilla gorilla": "Gorilla",
    "Pan troglodytes": "Chimpanzee",
    "Choloepus didactylus": "Sloth",
    "Panthera leo": "Lion",
    "Felis catus": "Cat",
    "Balaenoptera musculus": "Whale",
    "Tursiops truncatus": "Dolphin",
    "Vulpes lagopus": "Fox",
    "Ictidomys tridecemlineatus": "Squirrel",
    "Cervus canadensis": "Elk",
    "Canis lupus": "Dog",
    "Loxodonta africana": "Elephant",
    "Eptesicus fuscus": "Bat",
    "Mus musculus": "Mouse",
    "Ornithorhynchus anatinus": "Platypus",
    "Danio rerio": "Fish",
    "Vombatus ursinus": "Wombat",
    "Gekko japonicus": "Gekko",
    "Crotalus tigris": "Snake",
}
sequences = [fasta_delimiter + re.sub(pattern,species_to_common_name_dict[fasta_to_species_dict[sequence]], sequence) for sequence in sequences]


combinations = list(combinations(sequences,10))
length_combinations = len(combinations)
for count,combo in enumerate(combinations):
    print(f"writing {count + 1} file / {length_combinations}")
    file_name = ''.join([fasta.split("\n")[0][1:] for fasta in combo])
    with open(f"output_files/fasta_combinations/{file_name}.fasta", "w")as outfile:
        outfile.write("".join(combo))
