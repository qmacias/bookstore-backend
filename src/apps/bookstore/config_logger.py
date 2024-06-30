from logging import Logger, getLogger, DEBUG, Formatter, StreamHandler


def config_logger(name: str) -> Logger:
    logger = getLogger(name)

    logger.setLevel(DEBUG)

    formatter = Formatter('%(levelname)s:%(message)s')

    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
