# EU Cost Action Open Network on DEM Simulations (ON-DEM)

- [Link to COST Action page](https://www.cost.eu/actions/CA22132/)
- [Link to ON-DEM Confluence page](https://on-dem.atlassian.net/)

## WG 1 Alternative Methods (DEM-ML)

[Link to WG1 page](https://on-dem.atlassian.net/wiki/spaces/WG1/overview)

**Contributors(s)**: 

## Repository directory structure

A basic repository structure has been created by default, but you are free to define your own DS structure.

The repository structure is the following.
```
GitHub-Repository
│   README.md
|
|   License
|
|   example_model
    └───data - Folder containing your (do not push any data to GitHub. This is for you local use alone.)
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
