# mtb-deep-leaarning

### 1. Data Retrieval

### 2. Create tree cluster

This can be accomplished through:

a. Installing TreeCluster through following the instructions outlined in https://github.com/niemasd/TreeCluster

b. Running the following in command line:

TreeCluster.py -i <filepath to phylogenetic tree> -t <desired Hamming distance threshold, in my case 0.001> -m <desired clustering method, in my case max_clad> | paste -sd ' ' >> <filepath to output file (csv)>

c. Separating the TreeCluster csv file into a folder of files containing the samples for each cluster through running the create_to_keep_files.py script in this repository (update the country variable to match the desired phylogeny):

python create_to_keep_files.py

d. Reconstructing subtrees for each of the clusters through running the prune_tr.R file in this repository:

Rscript --vanilla prune_tr.R <filepath to the origincal phylogenetic tree> <path to one of the files outputted in step c>

### 3. Model inferences

Run the phylodeep_script.py file from this repository to generate a csv containing all of the phylodeep predicitions. Make sure to set the path_to_tree variable in the script to represent the path to the desired tree at any iteration of the loop.

python phylodeep_script.py
