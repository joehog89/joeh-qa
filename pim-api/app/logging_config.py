import logging
from pathlib import Path


def configure_logging():
    log_folder = Path("logs")
    log_folder.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                log_folder / "pim_api.log",
                encoding="utf-8",
            ),
        ],
        force=True,
    )