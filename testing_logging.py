from utils.logger import setup_logging
import logging

logger = setup_logging()


def test_logging():
    logger.debug("Debug message - should not appear (INFO level set)")
    logger.info("Info message - should appear")
    logger.warning("Warning message - should appear")
    logger.error("Error message - should appear")
    logger.critical("Critical message - should appear")

    try:
        1 / 0  # Simulate an error
    except Exception as e:
        logger.error("An error occurred", exc_info=True)


if __name__ == "__main__":
    test_logging()
