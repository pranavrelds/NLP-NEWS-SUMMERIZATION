import os

ARTIFACTS_DIR: str = "artifacts"
SOURCE_DIR_NAME: str = 'src'

# constants related to data ingestion
DATA_INGESTION_ARTIFACTS_DIR: str = "data_ingestion_artifacts"
RAW_DATA_DIR_NAME: str = "raw_data"
DATA_INGESTION_TRAIN_DIR: str = "train"
DATA_INGESTION_TEST_DIR: str = "test"

# constants related to pipeline
COLUMNS_NAME =  ['text', 'ctext']
PRETRAINED_MODEL_NAME = "t5-small"

# constants related to model training
MODEL_TRAINING_ARTIFACTS_DIR: str = "model_training_artifacts"
TRAINED_MODEL_NAME: str = 'model.pt'
CHECKPOINT_DIR: str = 'checkpoint'
LEARNING_RATE: float = 2e-5
EPOCHS: int = 1
BATCH_SIZE = 4
NUM_WORKERS = 0