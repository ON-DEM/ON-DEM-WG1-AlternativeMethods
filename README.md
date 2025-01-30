# Template data science project

## Project name

For example, MOOI - Energy Control Businesspark

### About the project

Briefly introduce the project. If available, provide related links to the project, e.g., a webpage

### Team

**Internal project manager(s)**: 

**Researcher(s)**: 

## Repository directory structure

A basic repository structure has been created by default, but you are free to define your own DS structure.

The repository structure is the following.
```
GitHub-Repository
│   README.md
│
└───data - Folder containing your (versioned)
    │
    └───raw
    └───processed
│
└───notebooks - Folder containing your data exploration and model training notebooks 
│
└───scripts - Generic scripts folder
│
└───output - Output folder containing persisted model weights and results such as plots, literature reviews
│
└───api - Folder containing an api script for your model
│
│   requirements.txt or requirements.in (if using pip-tools)
│
│   dockerfile
```

## Setting up an DS environment

[Click here for instructions using miniconda](notebooks). Note that when using `miniconda`, we utilise `conda` as a 
virtual environment manager alone. That is, we do not use `conda` as a package manager. For that, we will use `pip`.
