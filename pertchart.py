# Requirements
#! pip uninstall graphviz
#! conda install python-graphviz


from graphviz import Digraph, nohtml
import ast

# Data
# Provide tasks as list of tuples like:("Task id", "start", "duration", "end", "responsible", "predecessor)
# For the first tasks, predecessor will be "START", 
#   e.g., ("Task id", "start", "duration", "end", "responsible", "START")
# For the final tasks preced "END", 
#   e.g., ("END", "start", "duration", "end", "responsible", "Task id4"), ("END", "start", "duration", "end", "responsible", "Task id5")

filename = "datafile.txt"

task_list = []
with open(filename) as f:
    for line in f:
        values = ast.literal_eval(line)
        task_list.append(values)
        
a = task_list

# Graph Instance
g = Digraph('g', 
            filename='PERT.gv',
            node_attr={'shape': 'Mrecord', 
                       'height': '.1'})

# configurations
fill_color = 'grey93'

g.attr(rankdir='LR')
g.attr('node', shape='record')

# Nodes

for i in range(len(a)):
    if a[i][0] == "END":
            continue
    g.node(a[i][0], 
           nohtml('<f0>' + 
                  a[i][0] + 
                  ' |{' + a[i][1] + '|' + a[i][2] + '|' + a[i][3] + '}|<f2>' + 
                  a[i][4]), 
           fillcolor=fill_color, 
           style='filled',
           color='red'
          )

# Edges
'''
g.edge('node0:f2', 'node4:f1') # connect edges with connetion points <f2> and <f1>
g.edge('node0', 'node1')
'''

try:
    for i in a:
        #g.edge(i[3] + ':f2', i[0] + ':f0')
        if i[0] == "END":
            g.edge(i[5], "FINISH")
        else:
            g.edge(i[5], i[0])
except:
    print("Unexpected error. Check your inputs")
finally:
    print("PERT chart generated successfully")

g.view()

# Credits and References
# btree.py - http://www.graphviz.org/pdf/dotguide.pdf Figure 13
''' https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
https://www.programcreek.com/python/example/104476/graphviz.Digraph
https://graphviz.readthedocs.io/en/stable/examples.html#structs-py
'''