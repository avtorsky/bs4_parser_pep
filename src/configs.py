import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import BASE_DIR

DT_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_DIR = 'logs'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
PARSER_CACHE_FLAGS = (
    '-c',
    '--clear-cache',
)
PARSER_CACHE_HELP = 'Очистка кеша'
PARSER_DESC_HELP = 'Парсер документации Python'
PARSER_MODE_FLAGS = ('mode',)
PARSER_MODE_HELP = 'Режимы работы парсера'
PARSER_OUTPUT_FLAGS = (
    '-o',
    '--output',
)
PARSER_OUTPUT_HELP = 'Дополнительные способы вывода данных'


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(description=PARSER_DESC_HELP)
    parser.add_argument(
        PARSER_MODE_FLAGS[0],
        choices=available_modes,
        help=PARSER_MODE_HELP,
    )
    parser.add_argument(
        PARSER_CACHE_FLAGS[0],
        PARSER_CACHE_FLAGS[1],
        action='store_true',
        help=PARSER_CACHE_HELP,
    )
    parser.add_argument(
        PARSER_OUTPUT_FLAGS[0],
        PARSER_OUTPUT_FLAGS[1],
        choices=('pretty', 'file'),
        help=PARSER_OUTPUT_HELP,
    )
    return parser


def configure_logging():
    log_dir = BASE_DIR / LOG_DIR
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser.log'

    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10**6, backupCount=5
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()),
    )
