from typing import Dict, Type

from .base import BaseModel

_MODEL_REGISTRY: Dict[str, Type[BaseModel]] = {}
_REVERSE_REGISTRY: Dict[Type[BaseModel], str] = {}


def register(name: str):
    """Register a model class with a given name.

    Args:
        name: The name to register the model under

    Returns:
        A decorator that registers the model class

    Raises:
        ValueError: If a model is already registered under the given name
    """

    def decorator(model_cls: Type[BaseModel]) -> Type[BaseModel]:
        if name in _MODEL_REGISTRY:
            raise ValueError(f"Model name '{name}' is already registered")
        _MODEL_REGISTRY[name] = model_cls
        _REVERSE_REGISTRY[model_cls] = name
        return model_cls

    return decorator


def get_model(name: str) -> Type[BaseModel]:
    """Get a registered model class by name.

    Args:
        name: The name of the registered model

    Returns:
        The registered model class

    Raises:
        KeyError: If no model is registered under the given name
    """
    return _MODEL_REGISTRY[name]


def get_model_name(model_cls: Type[BaseModel]) -> str:
    """Get the registered name for a model class.

    Args:
        model_cls: The model class to look up

    Returns:
        The registered name for the model class

    Raises:
        KeyError: If the model class is not registered
    """
    return _REVERSE_REGISTRY[model_cls]
