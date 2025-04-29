from grainlearning.rnn import preprocessor
import grainlearning.rnn.train as train_rnn

# define configuration
my_config = {
    'raw_data': 'data/triaxial_compression_variable_input.hdf5',
    'pressure': 'All',
    'experiment_type': 'drain',
    'window_size': 20,
    'window_step': 1,
    'patience': 25,
    'epochs': 300,
    'learning_rate': 5.21e-5,
    'lstm_units': 250,
    'dense_units': 10,
    'beta_1': 0.850845257610267,
    'beta_2': 0.8221020617320791,
    'epsilon': 8.597964850283817e-06,
    'batch_size': 512,
    'standardize_outputs': True,
    'add_e0': True,
    'add_pressure': True,
    'add_experiment_type': False,
    'save_weights_only': False,
    'standardize_outputs': True,
    'train_frac': 0.7,
    'window_size': 4,
    'window_step': 1
}

# define preprocessor
preprocessor_TC = preprocessor.PreprocessorTriaxialCompression(**my_config)

# train
train_rnn.train_without_wandb(preprocessor_TC, config=my_config)