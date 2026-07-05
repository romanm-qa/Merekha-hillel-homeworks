import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("DEBUG message")
logging.info("INFO message")
logging.warning("WARNING message")
logging.error("ERROR message")
logging.critical("CRITICAL message")