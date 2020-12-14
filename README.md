# College Track Cookie Cutter Template

_A logical, reasonably standardized, but flexible project structure for doing and sharing College Track work._


#### [Project homepage](https://github.com/College-Track/cookieCutterSimple)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```



### To start a new project, run:
------------

    cookiecutter https://github.com/College-Track/cookieCutterSimple


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```

    ├── LICENSE
    ├── README.md           <- The top-level README for developers using this project.
    ├── data
    │   ├── interim         <- Intermediate data that has been transformed.
    │   ├── processed       <- The final, canonical data sets for modeling.
    │   └── raw             <- The original, immutable data dump.
    │
    ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    ├── src                 <- Contains all python code
    │   ├── 1_data_prep.py  <- Initial script to load and prep data
    │   ├── 2_analysis.py   <- If needed, script to run analysis or run more complicated processes
    │   └── helpers.py      <- Contains helper functions that are used in main scripts
    │   └── variables.py    <- For any set variables that will be used - empty by default
    │   └── soql_queries.py <- To store any needed SOQL querires
    │
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── notebooks           <- any Jupyter notebooks used for developing ideas
```

