from hydraexample.optimizer.optimizer import Optimizer
from hydraexample.dataset.dataset import Dataset

class Trainer:
    def __init__(self, optimizer: Optimizer, dataset: Dataset) -> None:
        self.optimizer = optimizer
        self.dataset = dataset