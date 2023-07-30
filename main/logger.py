import logging
import os
from functools import lru_cache
from rich.console import Console
from rich.logging import RichHandler

console = Console(color_system="256", width=150, style="blue")


@lru_cache
def get_logger(module_name):
    logger = logging.getLogger(module_name)
    handler = RichHandler(rich_tracebacks=True, console=console, tracebacks_show_locals=False, enable_link_path=False,
                          locals_max_string=150, locals_max_length=10)
    handler.setFormatter(logging.Formatter("[ %(threadName)s:%(funcName)s:%(lineno)d ] - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger



