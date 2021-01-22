# pertchart

[![Build Status](https://travis-ci.com/sisayie/pertchart.svg?branch=master)](https://travis-ci.com/github/sisayie/pertchart)

The purpose of his application is to automatically generate pert chart from tasks in text file.

## Requirement
`pip install graphviz`

## Data File
The data file contains task tuples one per line as in the following sample:
```
("Task id", "start", "duration", "end", "responsible", "START")
("Task id1", "start", "duration", "end", "responsible", "Task id")
("Task id2", "start", "duration", "end", "responsible", "Task id1")
("Task id3", "start", "duration", "end", "responsible", "Task id1")
("Task id4", "start", "duration", "end", "responsible", "Task id3")
("Task id5", "start", "duration", "end", "responsible", "Task id2")
("END", "start", "duration", "end", "responsible", "Task id4")
("END", "start", "duration", "end", "responsible", "Task id5")
```

### Credits and References
- btree.py - http://www.graphviz.org/pdf/dotguide.pdf Figure 13
- https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
- https://www.programcreek.com/python/example/104476/graphviz.Digraph
- https://graphviz.readthedocs.io/en/stable/examples.html#structs-py
