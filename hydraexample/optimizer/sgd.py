from hydraexample.optimizer.optimizer import Optimizer

class SGD(Optimizer):
  def __init__(self, lr: float):
    super().__init__(lr=lr)