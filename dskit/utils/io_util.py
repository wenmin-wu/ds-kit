import pickle
from typing import Callable
from smart_open import open as sopen
from .logging_util import get_logger

logger = get_logger('IO')

def get_open_fn(file_path: str) -> Callable:
    if file_path.startswith('s3://'):
        return sopen
    else:
        return open

def load_pkl(file_path: str) -> object:
    open_fn = get_open_fn(file_path)
    logger.info(f'Loading object from {file_path} ...')
    with open_fn(file_path, 'rb') as fin:
        obj = pickle.load(fin)
        logger.info(f'Loaded object from {file_path}.')
        return obj

def dump_pkl(obj: object, file_path: str) -> None:
    open_fn = get_open_fn(file_path)
    logger.info(f'Dumping object to {file_path} ...')
    with open_fn(file_path, 'wb') as fout:
        pickle.dump(obj, fout)
    logger.info(f'Dumped object to {file_path}.')
