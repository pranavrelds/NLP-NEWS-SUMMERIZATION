import os, sys
from dataclasses import dataclass
from datetime import datetime
from from_root import from_root

from src.constants import *

@dataclass
class DataIngestionConfig:
    bucket_name: str = BUCKET_NAME
    file_name: str = FILE_NAME
    data_ingestion_artifacts: str = os.path.join(from_root(), training_pipeline_config.artifact_dir, DATA_INGESTION_ARTIFACTS_DIR)
    raw_data_dir: str = os.path.join(from_root(), data_ingestion_artifacts, RAW_DATA_DIR_NAME)
    train_file_path: str = os.path.join(data_ingestion_artifacts, DATA_INGESTION_TRAIN_DIR, TRAIN_FILE_NAME)
    test_file_path: str = os.path.join(data_ingestion_artifacts, DATA_INGESTION_TEST_DIR, TEST_FILE_NAME)

@dataclass
class ModelTrainerConfig:
    model_trainer_artifacts_dir: str = os.path.join(from_root(), training_pipeline_config.artifact_dir, MODEL_TRAINING_ARTIFACTS_DIR)
    trained_model_dir: str = os.path.join(model_trainer_artifacts_dir, 'trained_model', TRAINED_MODEL_NAME)
    epochs: int = EPOCHS
    checkpoint_dir: str = os.path.join(model_trainer_artifacts_dir, CHECKPOINT_DIR)
    checkpoint_fname: str = 'best_checkpoint'