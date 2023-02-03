from hydraexample.optimizer.optimizer import Optimizer
from hydraexample.dataset.dataset import Dataset
from flax import linen as nn

class Trainer:
    def __init__(self, optimizer: Optimizer, dataset: Dataset, model: nn.Module) -> None:
        self.optimizer = optimizer
        self.dataset = dataset
