# Did I Pass? Grader

This package takes two CSV and checks what your grade can be if you give your expected grade on an assignment.

## Installation
```pip install -e .```

## Usage
```bash
usage: grader [-h] -g GRADEFILE -s SYLLABUS -t TYPE -n NEWGRADE

optional arguments:
  -h, --help            show this help message and exit
  -g GRADEFILE, --gradefile GRADEFILE
                        the file containing grades
  -s SYLLABUS, --syllabus SYLLABUS
                        the file containing the syllabus grade breakdown
  -t TYPE, --type TYPE  input grade type
  -n NEWGRADE, --newgrade NEWGRADE
                        input grade as number out of 100
```