import logging


def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Function to set up a logger with specified name, log file, and logging level.

    Args:
        name (str): The name of the logger.
        log_file (str): The file path where logs will be saved.
        level (int, optional): The logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)  # ok done

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger