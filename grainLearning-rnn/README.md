# Model: GrainLearning RNN

This repository contains an example surrogate model, **GrainLearning RNN**, which predicts macroscopic stress and void ratio based on a given load sequence and contact parameters.

📘 For detailed model structure, input/output formats, and architecture, please refer to the [GrainLearning RNN documentation](https://grainlearning.readthedocs.io/en/latest/rnn.html#the-rnn-model).

## 🚀 Installation

### 🔹 Option 1: Manual Setup

```python
# Go to grainLearning-rnn folder
cd grainLearning-rnn
# create an environment
conda create --name grainlearning-rnn python=3.10
conda activate grainlearning-rnn
# install the requirements
pip install -r requirements.txt
```

### 🔹 Option 2: Environment file

Use the provided conda environment file to set up everything in one step:
```python
conda env create -f envs/macos_arm.yml
```

### More details

For further, more detailed instructions take a look at the [grainLearning/rnn instructions](https://github.com/GrainLearning/grainLearning/blob/main/grainlearning/rnn/README.md).

⚠️ **TensorFlow Note**: `GrainLearning/rnn` uses TensorFlow. You may need to follow specific installation steps depending on your system (e.g., macOS ARM, GPU support).

⚠️ **Python Version**: Please use Python 3.10 or earlier, as later versions are not guaranteed to be compatible.

## Get started

A minimal working example for training the model is available in the [train_rnn.ipynb notebook](notebooks/train_rnn.ipynb).

In the folder `scripts`, you can find the python scripts to run a training of the model.

## Data

Details about the datasets used for training and evaluation are available in [`data/README.md`](data/README.md).

## Results

📄 **Paper**: A description of a surrogate model for triaxial compression tests have been published in [*Towards scientific machine learning for granular material simulations -- challenges and opportunities*](https://arxiv.org/pdf/2504.08766).

📦 **Models**: Check out trained models for triaxial simulations [here](https://github.com/GrainLearning/grainLearning/tree/main/grainlearning/rnn/trained_models).

## Resources

- [Documentation of GrainLearning/rnn](https://grainlearning.readthedocs.io/en/latest/rnn.html)
