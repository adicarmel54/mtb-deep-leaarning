import pandas as pd

country = "moldova"
dir = '/home/ac2445/mtb-transmission-project/' + country + '/'
clusters = pd.DataFrame(columns=["SequenceName", "ClusterNumber"])
with open(dir + country + '_tree_clusters.csv') as f:
    file = f.readlines()
    rows = file[0].split(' ')

    for row in rows[1:]:
        split = row.split('\t')
        clusters = clusters.append(
            {"SequenceName": split[0], "ClusterNumber": int(split[1])}, ignore_index=True)

max_cluster = clusters["ClusterNumber"].max()
for i in range(1, max_cluster + 1):
    to_keep = clusters[clusters["ClusterNumber"] == i]["SequenceName"].tolist()
    with open(dir + '/to_keep/A3_C' + str(i) + '.txt', 'w') as file:
        for item in to_keep:
            file.write("%s\n" % item)
