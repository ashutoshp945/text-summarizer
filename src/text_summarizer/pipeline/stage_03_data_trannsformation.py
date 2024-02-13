from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_transformation import DataTranformation
from text_summarizer.logging import logger


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_tranformation_config = config.get_data_transformation_config()
        data_tranformation = DataTranformation(config= data_tranformation_config)
        data_tranformation.convert()