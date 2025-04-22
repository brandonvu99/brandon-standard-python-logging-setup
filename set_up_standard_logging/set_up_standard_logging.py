"""Module for set_up_standard_logging()."""

import logging
from datetime import datetime
from pathlib import Path


def set_up_standard_logging(
    logs_dirpath: Path = Path("/logs"),
    level: int = logging.NOTSET,
    new_log_file_every_run: bool = True,
    log_file_prefix: str = "",
    create_subdirs: bool = True,
):
    """
    Arguments:
        logs_dirpath (Path): path to the directory which will have the log file created in
        level (int): the log level from the {logging} module
        new_log_file_every_run (bool): If True, then a new log file (with the current datetime
                                       of this function call in the filename) will be created
                                       with each invocation of this function. For example,
                                       "2025-01-30-12-02-03.log".
                                       If False, then the filename will only be "logs.log".
        log_file_prefix (str): a prefix to add to the log filename. Used in either case of
                               {new_log_file_every_run} being True or False.
        create_subdirs (bool): if True, will create subdirs such that the final log path will
                               in a directory at a path something like "2025/01/30".
                               if False, the logs will be stored at the {logs_dirpath}.
    """
    now = datetime.now()
    if create_subdirs:
        logs_dirpath = logs_dirpath / f"{now.year:04d}/{now.month:02d}/{now.day:02d}"

    logs_dirpath.mkdir(parents=True, exist_ok=True)

    filename_prefix = f"{log_file_prefix}-" if log_file_prefix else ""
    log_filename = (
        f"{filename_prefix}{now.strftime('%Y-%m-%d-%H-%M-%S')}.log"
        if new_log_file_every_run
        else f"{filename_prefix}logs.log"
    )
    log_filepath = logs_dirpath / log_filename

    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s",
        level=level,
        handlers=[
            logging.FileHandler(
                filename=log_filepath,
                encoding="utf-16",
            ),
            logging.StreamHandler(),
        ],
    )
