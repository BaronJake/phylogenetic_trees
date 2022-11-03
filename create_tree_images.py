from ete3 import Tree
from ete3.treeview import TreeStyle
from os import listdir

list_of_tree_files = [file_name.split(".")[0] for file_name in listdir("output_files/alignments") if file_name.split(".")[-1] == "treefile"]
len_of_input_files = len(list_of_tree_files)

for index,file in enumerate(list_of_tree_files):

    print(f"Working on file #{index + 1} out of {len_of_input_files}")
    tree_images_already_created = listdir("output_files/tree_images")
    tree_images_already_created_and_used = listdir("output_files/tree_image_used")
    if f"{file}.png" in tree_images_already_created or f"{file}.png" in tree_images_already_created_and_used:
        print("File already created, Skipping!")
        continue

    with open(f"output_files/alignments/{file}.fasta.treefile") as treefile:
        tree_string = treefile.read()

    tree = Tree(tree_string)
    style = TreeStyle()
    style.show_leaf_name = True
    style.mode = "c"
    style.arc_start = -180
    style.arc_span = 360
    style.show_border = True
    tree.render(f"output_files/tree_images/{file}.png",tree_style=style)

for image in tree_images_already_created:
    if image in tree_images_already_created_and_used:
        print(f"{image} is in both used and unused directories.")
