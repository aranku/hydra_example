from flax import linen as nn

class MLP(nn.Module):
  def setup(self, features: int):
    # Submodule names are derived by the attributes you assign to. In this
    # case, "dense1" and s"dense2". This follows the logic in PyTorch.
    self.dense1 = nn.Dense(features)
    self.dense2 = nn.Dense(features)

  def __call__(self, x):
    x = self.dense1(x)
    x = nn.relu(x)
    x = self.dense2(x)
    return x
