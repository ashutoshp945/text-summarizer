from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from text_summarizer.logging import logger

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e