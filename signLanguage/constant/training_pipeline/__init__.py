import os

ARTIFACTS_DIR: str = "artifacts"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL: str = "https://github.com/anupkumarsahu/datasets/raw/main/Sign_language_data.zip"

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_STATUS_FILE:str = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16

BUCKET_NAME = "sign-lang-2024"
S3_MODEL_NAME = "best.pt"
