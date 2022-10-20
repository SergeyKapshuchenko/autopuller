import json
from pathlib import Path


def load_json(filename: Path | str) -> dict:
    with open(filename, mode='r') as file:
        config = json.load(file)
    return config
