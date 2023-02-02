class Adam(Optimizer):
  def __init__(self, lr: float, beta: float):
    super().__init__(lr=lr)
    self.beta = beta