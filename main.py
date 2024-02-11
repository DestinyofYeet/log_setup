import logging
import pathlib
from datetime import datetime
import sys

from modules import test


def setup_logging(
    log_root_folder=None,
    parent_multiplier=1,
    dir_name="logs",
    log_name="log - ",
    log_suffix="txt",
    use_timestamp=True,
    strftime_format="%d.%m.%y - %H:%M:%S",
    logging_level=logging.DEBUG,
    logging_format="%(asctime)s [%(threadName)s] %(name)s:%(lineno)d %(levelname)s - %(message)s",
):
    if log_root_folder is None:
        log_root_folder = pathlib.Path(__file__).absolute()

        for i in range(parent_multiplier):
            log_root_folder = log_root_folder.parent

    log_formatter = logging.Formatter(logging_format)

    logging_folder = pathlib.Path(f"{log_root_folder.absolute()}/{dir_name}")
    logging_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(strftime_format)
    filename = f"{log_name}{timestamp if use_timestamp else ''}.{log_suffix}"

    file_handler = logging.FileHandler(f"{dir_name}/{filename}")
    file_handler.setFormatter(log_formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)

    logging.basicConfig(
        level=logging_level,
        encoding="utf-8",
        format=logging_format,
        handlers=[
            console_handler,
            file_handler
        ],
    )


def log_traceback():
    logging.getLogger(__name__)
    logging.exception("An exception has occurred:", exc_info=True)


def main():
    setup_logging()

    logger = logging.getLogger(__name__)

    logger.info("main")
    logger.error("error")

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Division failed", exc_info=True)

    test.test()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_traceback()
        raise
