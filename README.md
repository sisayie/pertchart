# pertchart

[![Build](https://github.com/sisayie/pertchart/actions/workflows/python-publish.yml/badge.svg)](https://github.com/sisayie/pertchart/actions/workflows/python-publish.yml)

The purpose of his application is to automatically generate pert chart from tasks in json file.

## Installation
```pip install pertchart```

## Usage
```
from pertchart import PertChart

pc = PertChart()
tasks = pc.getInput(path_to_inputfile)
pc.create_pert_chart(pc.calculate_values(tasks))
```

### Example Input Data File
The data file contains task tuples one per line as in the following sample:
```
{
  "T1.1": {
    "Tid": "T1.1",
    "start": 0,
    "duration": 1,
    "end": 0,
    "responsible": "Responsible1",
    "pred": ["START"]
  },
  "T1.2": {
    "Tid": "T1.2",
    "start": 0,
    "duration": 3,
    "end": 0,
    "responsible": "Responsible2",
    "pred": ["T1.1"]
  },
  "T1.3": {
    "Tid": "T1.3",
    "start": 0,
    "duration": 3,
    "end": 0,
    "responsible": "Responsible3",
    "pred": ["T1.1"]
  },
  "T1.4": {
    "Tid": "T1.4",
    "start": 0,
    "duration": 2,
    "end": 0,
    "responsible": "Responsible4",
    "pred": ["T1.2"]
  },
  "T1.5": {
    "Tid": "T1.5",
    "start": 0,
    "duration": 2,
    "end": 0,
    "responsible": "Responsible5",
    "pred": ["T1.3"]
  },
  "T1.6": {
    "Tid": "T1.6",
    "start": 0,
    "duration": 1,
    "end": 0,
    "responsible": "Responsible6",
    "pred": ["T1.4"]
  },
  "T1.7": {
    "Tid": "T1.7",
    "start": 0,
    "duration": 3,
    "end": 0,
    "responsible": "Responsible7",
    "pred": ["START"]
  },
  "T1.8": {
    "Tid": "T1.8",
    "start": 0,
    "duration": 0,
    "end": 0,
    "responsible": "Responsible8",
    "pred": ["T1.5","T1.6","T1.7"]
  },
  "END": {
    "Tid": "END",
    "start": 0,
    "duration": 0,
    "end": 0,
    "responsible": "Responsible",
    "pred": ["T1.8"]
  }
}
```

## Exacmple Output PERT chart for th eabove input data
![PERT Output](https://github.com/sisayie/pertchart/blob/master/pert_v0.4.png "PERT output")

### Credits and References
- http://www.graphviz.org/pdf/dotguide.pdfbtree.pyFigure13
- https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
- https://www.programcreek.com/python/example/104476/graphviz.Digraph
- https://graphviz.readthedocs.io/en/stable/examples.html#structs-py
