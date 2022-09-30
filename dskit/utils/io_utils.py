import re
import pickle
import time
import ujson as json
from smart_open import open as sopen
from typing import Tuple, Callable


def get_path_and_open_fn(path: str) -> Tuple[str, Callable]:
    path = re.sub("^s3.://", "s3://", path)
    open_fn = sopen if path.startswith("s3://") else open
    return path, open_fn


def pickle_load(path: str) -> object:
    path, open_fn = get_path_and_open_fn(path)
    with open_fn(path, "rb") as f:
        return pickle.load(f)


def pickle_dump(obj: object, path: str):
    path, open_fn = get_path_and_open_fn(path)
    with open_fn(path, "wb") as f_out:
        pickle.dump(obj, f_out)


def json_load(path: str) -> dict:
    path, open_fn = get_path_and_open_fn(path)
    with open_fn(path, "r") as f:
        return json.load(f)


def json_dump(obj: object, path: str):
    path, open_fn = get_path_and_open_fn(path)
    with open_fn(path, "w") as f_out:
        json.dump(obj, f_out)
