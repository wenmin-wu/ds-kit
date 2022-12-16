import logging
import colorlog

_DEFAULT_LOG_FMT = "%(log_color)s[%(levelname)s %(asctime)s.%(msecs)03d %(name)s]:%(reset)s %(message)s"
_DEFAULT_LOG_DATE_FMT = "%Y-%m-%d %H:%M:%S"


def get_logger(
    name: str, fmt: str = None, dt_fmt: str = None
) -> logging.Logger:
    if fmt is None:
        fmt = _DEFAULT_LOG_FMT
    if dt_fmt is None:
        dt_fmt = _DEFAULT_LOG_DATE_FMT

    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(fmt, dt_fmt))
    logger = colorlog.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger

