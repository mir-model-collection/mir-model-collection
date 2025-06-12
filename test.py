from mir_model_collection.env import PROJECT_NAME
from mir_model_collection.models.dummy import DummyModel, DummyModelConfig

model = DummyModel(config=DummyModelConfig())

model.save_pretrained(model.get_model_cache_dir())

model.push_to_hub(f"{PROJECT_NAME}/{model.get_model_name()}")

model = DummyModel.from_pretrained(f"{PROJECT_NAME}/{DummyModel.get_model_name()}")

print(model)
