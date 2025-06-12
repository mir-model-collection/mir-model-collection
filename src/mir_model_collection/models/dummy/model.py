from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Type, Union

import torch.nn as nn
from safetensors.torch import save_model

from ..base import BaseModel
from ..register import register


@dataclass
class DummyModelConfig:
    dim_in: int = 5
    dim_out: int = 17


@register("dummy-model")
class DummyModel(BaseModel):
    def __init__(self, config: DummyModelConfig):
        super().__init__()
        self.config = config
        self.model = nn.Linear(config.dim_in, config.dim_out)

    def _save_pretrained(self, save_directory: Path) -> None:
        save_model(
            self.model,
            str(save_directory / "model.safetensors"),
        )

    @classmethod
    def _from_pretrained(
        cls: Type["DummyModel"],
        *,
        model_id: str,
        revision: Optional[str],
        cache_dir: Optional[Union[str, Path]],
        force_download: bool,
        proxies: Optional[Dict],
        resume_download: Optional[bool],
        local_files_only: bool,
        token: Optional[Union[str, bool]],
        **model_kwargs: Any,
    ) -> "DummyModel":
        model = cls(**model_kwargs)
        return model
