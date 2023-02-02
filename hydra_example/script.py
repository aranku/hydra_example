from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import instantiate

@hydra.main(version_base=None, config_path="../configs", config_name="config")
def my_app(cfg):
    print(OmegaConf.to_yaml(cfg))
    trainer = instantiate(cfg)
    print(trainer)

if __name__ == "__main__":
    my_app()