import logging
import sys
import os, shutil, fnmatch
import argparse
import re
from pathlib import Path

def parse_arguments():
    """ Parse command-line arguments
    Exemple : python m3u_to_mp3\m3u_to_mp3.py
              -i ./m3u_dir
              -o ./mp3_dir
    """
    description = \
        'Read M3U files and copy the mp3 files listed.\n' \
        'Ex: python m3u_to_mp3\m3u_to_mp3.py' \
        '    -i ./m3u_dir \
        '    -o ./mp3_dir'
    parser = argparse.ArgumentParser(
        description=\
            description,
        formatter_class=\
            argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i", "--input"
                        , help="M3U directory."
                        , dest="m3u_dir"
                        , required=True)

    parser.add_argument("-o", "--output"
                        , help="MP3 directory."
                        , dest="mp3_dir"
                        , required=True)

    return parser.parse_args()

logger = logging.getLogger('m3u_to_mp3')
logger.setLevel(logging.DEBUG)
logger.handlers = []
logger.propagate = False
console_hdlr = logging.StreamHandler()
console_hdlr.setLevel(logging.INFO)
logger.addHandler(console_hdlr)
loghdlr = logging.FileHandler(\
            'm3u_to_mp3.log'
            , mode='w'
            , encoding = "utf-8")
loghdlr.setFormatter(
    logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s'))
loghdlr.setLevel(logging.DEBUG)
logger.addHandler(loghdlr)

args = parse_arguments()
