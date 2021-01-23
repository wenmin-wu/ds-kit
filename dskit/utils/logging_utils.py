import logging
from logging.handlers import RotatingFileHandler

DEFAULT_LOG_FMT = "\x1b[1m\x1b[33m[%(levelname)s %(asctime)s.%(msecs)03d %(name)s]\x1b[0m: %(message)s"
DEFAULT_LOG_DATE_FMT = "%Y-%m-%d %H:%M:%S"


def get_logger(
    logger_name,
    file_name=None,
    fmt=None,
    dt_fmt=None,
    console_out=True,
    max_bytes=2000,
    backup_count=5,
):

    assert console_out or (file_name is not None), "no handler will be added"

    if fmt is None:
        fmt = DEFAULT_LOG_FMT
    if dt_fmt is None:
        dt_fmt = DEFAULT_LOG_DATE_FMT
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger_fmt = logging.Formatter(fmt, dt_fmt)

    if file_name is not None:
        fh = RotatingFileHandler(
            file_name, maxBytes=max_bytes, backupCount=backup_count
        )
        fh.setFormatter(logger_fmt)
        logger.addHandler(fh)

    if console_out:
        ch = logging.StreamHandler()
        ch.setFormatter(logger_fmt)
        logger.addHandler(ch)

    return logger
