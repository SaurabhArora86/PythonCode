import logging
import logging.config
import pathlib
import json
import atexit


def setup_logging():
    config_path = pathlib.Path(__file__).parent.parent / \
        'configs/logging_config.json'

    with open(config_path, 'r') as f:
        config = json.load(f)

    logging.config.dictConfig(config)

    # Get the handler correctly from the root logger
    root_logger = logging.getLogger()

    # Find the queue handler
    for handler in root_logger.handlers:
        if isinstance(handler, logging.handlers.QueueHandler):
            if hasattr(handler, 'listener'):
                handler.listener.start()
                atexit.register(handler.listener.stop)

    return root_logger


# Example usage
if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Logging system initialized successfully")
