from hydraexample.optimizer.optimizer import Optimizer
from hydraexample.dataset.dataset import Dataset
from flax import linen as nn
from dataclasses import dataclass

@dataclass
class Trainer:
    optimizer: Optimizer
    dataset: Dataset
    model: nn.Module
