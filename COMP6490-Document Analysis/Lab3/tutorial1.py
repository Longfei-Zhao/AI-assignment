# necessary imports
import csv
#import urllib2
import networkx as nx
import matplotlib.pyplot as plt
#%matplotlib inline

# opening a local CSV file
to_read = open("./dataset.csv")  #use this line for a locally downloaded file
# or reading it directly from the specified URL
# url = 'http://rizoiu.eu/sna-lab-ipython/dataset.csv'
# to_read = urllib2.urlopen(url)
reader = csv.reader(to_read)

#  construct the networkx graph
G = nx.Graph()
# G.add_nodes_from([node for line in reader for node in line])
# G.add_edges_from(*reader)
for line in reader:
    G.add_nodes_from(line)
    G.add_edge(*line)


# determine the spring layout
pos = nx.spring_layout(G)
print("The social graph contains %s users." % G.number_of_nodes())
print("The social graph contains %s relations." % G.number_of_edges())
# draw the graph
# plt.figure(figsize=(19,12))
# plt.axis('off')
# nx.draw_networkx_nodes(G, pos, node_size=50)
# nx.draw_networkx_edges(G, pos, width=0.75, arrows=True)
no_hops = min([len(nx.shortest_path(G, source = '137056623', target = x)) - 1 for x in G.nodes() if x not in ['137056623']])
print("Using %d introductions, '137056623' can reach anyone in the network" % no_hops)
ec = nx.eccentricity(G)
print(ec)
G.graph
