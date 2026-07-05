import logging

# Настройка логирования
logging.basicConfig(
    filename='example.log',  # файл, куда будут записываться логи
    level=logging.ERROR,  # минимальный уровень логирования
    format='%(asctime)s - [%(levelname)s] - %(message)s'  # формат записи
)

logging.debug("DEBUG message")
logging.info("INFO message")
logging.warning("WARNING message")
logging.error("ERROR message")
logging.critical("CRITICAL message")
