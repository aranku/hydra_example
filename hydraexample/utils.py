from typing import Callable
import functools
import hydra

def instantiate(config):
    # Case 1: no config
    if config is None:
        return None
    # Case 2b: grab the desired callable from name
    else:
        _target_ = config.pop("_target_")

    # Retrieve the right constructor automatically based on type
    if isinstance(_target_, str):
        fn = hydra.utils.get_method(path=_target_)
    elif isinstance(_target_, Callable):
        fn = _target_
    else:
        raise NotImplementedError("instantiate target must be string or callable")

    obj = functools.partial(fn, **config)

    # Restore _name_
    if _target_ is not None:
        config["_target_"] = _target_

    return obj()
