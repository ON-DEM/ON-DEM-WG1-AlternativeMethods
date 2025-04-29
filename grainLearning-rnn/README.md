# Model: GrainLearning RNN

This is an example of a surrogate model that given the load sequence and contact parameters would predict the macroscopic stress and void ratio.

Information about the structure of the model (including inputs and outputs) can be found [here](https://grainlearning.readthedocs.io/en/latest/rnn.html#the-rnn-model).

## Installation

### Option 1

```python
# Go to grainLearning-rnn folder
cd grainLearning-rnn
# create an environment
conda create --name grainlearning-rnn python=3.10
conda activate grainlearning-rnn
# install the requirements
pip install -r requirements.txt
```

### Option 2

You can also create the environment and install the requirements:
```python
conda env create -f envs/macos_arm.yml
```

### More details

Further, more detailed instructions take a look at the [grainLearning/rnn instructions](https://github.com/GrainLearning/grainLearning/blob/main/grainlearning/rnn/README.md).

⚠️ `GrainLearning/rnn` uses Tensorflow, you may have to follow specific instructions to install Tensorflow for you specific distribution and hardware.

⚠️ Use python versions <= 3.10

## Get started

A minimal example on how to train models can be found in this [notebook](notebooks/train_rnn.ipynb).

In the folder `scripts`, you can find the python scripts to run a training of the model.

## Data

Check more info about the data in [`data/README.md`](data/README.md).

## Results

📄 **Paper**: A description of a surrogate model for triaxial compression tests have been published in [*Towards scientific machine learning for granular material simulations -- challenges and opportunities*](https://arxiv.org/pdf/2504.08766).

📦 **Models**: Check out trained models for triaxial simulations [here](https://github.com/GrainLearning/grainLearning/tree/main/grainlearning/rnn/trained_models).

## Resources

- [Documentation of GrainLearning/rnn](https://grainlearning.readthedocs.io/en/latest/rnn.html)
