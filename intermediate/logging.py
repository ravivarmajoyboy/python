import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("debug msg")
logging.info("info msg")
logging.warning("warning msg")
logging.error("error msg")
logging.critical("critical msg")

logger = logging.getLogger("myapp")
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

logger.warning("this goes to app.log and console")
logger.info("this stays on console only")

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("something broke")
