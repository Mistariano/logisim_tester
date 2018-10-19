import logging


class LoggerMgr:
    _LOGGER = None

    def __init__(self):
        if self._LOGGER is None:
            self._LOGGER = logging.getLogger('LogisimT')
            self._LOGGER.setLevel(logging.DEBUG)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(logging.Formatter('%(name)s: [%(levelname)s]%(message)s'))
            self._LOGGER.addHandler(stream_handler)

    @staticmethod
    def get_logger():
        manager = LoggerMgr()
        return manager._LOGGER
