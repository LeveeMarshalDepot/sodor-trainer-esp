import logging
from pathlib import Path


def get_logger(name: str) -> logging.Logger:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    logger = logging.getLogger(name)
    if not logger.handlers:
        fh = logging.FileHandler(log_dir / "sodor-trainer.log", encoding="utf-8")
        fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
        logger.addHandler(fh)
        logger.setLevel(logging.DEBUG)
    return logger