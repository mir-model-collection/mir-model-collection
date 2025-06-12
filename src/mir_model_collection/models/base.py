from pathlib import Path

import torch.nn as nn
from huggingface_hub import PyTorchModelHubMixin

from mir_model_collection.env import get_cache_dir


class BaseModel(nn.Module, PyTorchModelHubMixin):
    @classmethod
    def get_model_name(cls) -> str:
        from mir_model_collection.models.register import get_model_name

        return get_model_name(cls)

    def get_model_cache_dir(self) -> Path:
        cache_dir = get_cache_dir()
        model_dir = cache_dir / self.get_model_name()
        model_dir.mkdir(exist_ok=True)
        return model_dir
