import logging
import os
import datetime

from task3.config import settings
from task3.framework.singleton import Singleton


class Logger(metaclass=Singleton):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger(__name__)

        if not os.path.isdir(settings["log_dir_name"]):
            os.mkdir(settings["log_dir_name"])

        file_handler = logging.FileHandler(
            settings["log_dir_name"]
            + settings["log_filename_prefix"]
            + datetime.datetime.now().strftime(settings["log_time_format"])
            + settings["log_file_extension"],
            mode=settings["log_mode"]
        )

        formatter = logging.Formatter(
            fmt=settings["log_msg_format"],
            datefmt=settings["log_date_format"])

        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

        if settings["log_level"] == settings["log_level_debug"]:
            self._logger.setLevel(logging.DEBUG)
        elif settings["log_level"] == settings["log_level_info"]:
            self._logger.setLevel(logging.INFO)
        elif settings["log_level"] == settings["log_level_warning"]:
            self._logger.setLevel(logging.WARNING)
        elif settings["log_level"] == settings["log_level_error"]:
            self._logger.setLevel(logging.ERROR)
        else:
            self._logger.setLevel(logging.CRITICAL)

    def get_logger(self):
        return self._logger
