import os
from text_summarizer.logging import logger
from text_summarizer.entity import DataTransformationConfig
from datasets import load_dataset, load_from_disk
from transformers import AutoTokenizer

class DataTranformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config,
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        self.data_path = config.data_path
        self.root_dir = config.root_dir
    
    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length = 1024, truncation = True)

        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(example_batch['summary'], max_length = 1024, truncation = True)
        
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encoding['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.data_path)
        data_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched= True)
        data_samsum_pt.save_to_disk(os.path.join(self.root_dir, "samsum_dataset"))