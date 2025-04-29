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

To add your own model, create a new folder with a structure similar to `example_model`.

## Setting up an model development environment
 
First things first, we presume that all models will be developed in `python`. So, to setup our dev tech stack we will use `conda` as our environment manager and `pip` as our package manager. We will especially 
use miniconda, which is lighter than anaconda.

### Miniconda setup 

Feel free to skip the setup in case `conda` is already installed. You can check this by trying `conda --version` at the command line.

#### On Windows

Install miniconda by following the steps [here](https://docs.anaconda.com/free/miniconda/)

#### On MacOS (via command line)

Given the architectural variations, the steps below should help you install `conda` on your local machine.

**M1 machine (arm64)**

- Download miniconda installer script\
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh`
- Install using the script\
`sh ./Miniconda3-latest-MacOSX-x86_64.sh`
- Accept all the defaults the installer suggests

**Intel machine (x86_64)**

- Download miniconda installer script\
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`
- Install using the script\
`sh ./Miniconda3-latest-MacOSX-x86_64.sh`
- Accept all the defaults the installer suggests

If you would like both the arm64 and x86_64 installations on your M1 machine, check out this [medium article](https://towardsdatascience.com/how-to-install-miniconda-x86-64-apple-m1-side-by-side-on-mac-book-m1-a476936bfaf0).

### Creating a conda environment via the command-line

Environments allow for good isolation of stacks (containerisation not virtualisation). 
Here we use `conda` to create virtual environments in the same way as explained [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html). 
Following these same steps, we will create an environment for our project as follows

- Create a python-based environment for our project\
`conda create --name saxflux python=<version_number>`
- Activate the environment\
`conda activate saxflux`
- Adding the api-key as an environment variable\
`conda env config vars set apikey=<your_api_key>`
- Delete the environment\
`conda env remove --name saxflux`

*Note that, when a python-based conda-environment is created, by default, it installs `pip` in our environment.*

## Installing the packages in your environment

### Installing packages
- Go to the local directory where you have cloned this repository.
- Once there, you can install the required packages listed in the `requirements.txt` using `pip install -r requirements.txt`. This will install the packages in your activated environment, for example, `saxflux`.

For folks interested in using `conda` and `poetry` together instead of `pip`, checkout these nice articles
- [Conda or Poetry?](https://medium.com/semantixbr/getting-started-with-conda-or-poetry-for-data-science-projects-1b3add43956d)
- [Setting up Conda+Poetry](https://ealizadeh.com/blog/guide-to-python-env-pkg-dependency-using-conda-poetry)

### Get started

With a conda environment setup, you can run your model notebooks/scripts by choosing the right kernel.

## Useful references

- [Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/index.html)
