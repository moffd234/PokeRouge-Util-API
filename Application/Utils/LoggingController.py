import logging
import sys
from logging import StreamHandler, Formatter, basicConfig


def setup_logging() -> None:
    console_handler = StreamHandler(sys.stdout)
    formatter: Formatter = Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    console_handler.setFormatter(formatter)

    basicConfig(level=logging.DEBUG, handlers=[console_handler])
    logging.getLogger("data.seed").setLevel(logging.INFO)
    logging.getLogger("api").setLevel(logging.INFO)
    logging.getLogger("utils.extractor").setLevel(logging.INFO)
