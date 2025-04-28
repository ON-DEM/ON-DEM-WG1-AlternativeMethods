# Contributing guidelines

Thank you for your interest in contributing!

Please follow these guidelines to ensure consistency across the project:

## Folder structure

Your model folder should follow the structure below:
```
example_model/
    ├── data/                  # Local data folder (DO NOT push any data to GitHub)
    │   ├── raw/                # Raw, unprocessed data
    │   └── processed/          # Processed, cleaned data
    │
    ├── notebooks/              # Data exploration and model training notebooks
    │
    ├── scripts/                # Generic scripts: data processing, plotting, job submission (e.g., HPC)
    │
    ├── output/                 # Persisted model weights, results (plots, reports, literature reviews)
    │
    ├── api/                    # Scripts for serving the model via an API
    │
    ├── requirements.txt        # List of dependencies (or requirements.in if using pip-tools)
    ├── README.md               # Project overview and instructions (include your contact information)
    └── Dockerfile              # (Optional) Dockerfile to containerize your model
```

## Contribution process

- Before starting, check if a similar model or project already exists.
- **Branching**: Create a branch or fork the repository before making changes. Open a pull request when you're ready.
- **Naming**: Choose a clear and descriptive name for your folder and model.
- **Attribution**: Only include code that you have the right to use. If you use third-party code, check the license and cite appropriately.
- **Data sources**: If your data is public, include links to the original repositories or sources.
- **Dependencies**:
    - List all necessary packages in a `requirements.tx`t file (consider version pinning).
    - Avoid using Git submodules for dependencies; prefer listing external packages in requirements.txt unless necessary.
- **Environment Export (Optional)**: You can export your conda environment with:

```bash
conda env export > my_environment.yml
```

Include the `environment.yml` file in your project to help others replicate your setup.
