import logging
import sys
import glob
import os, shutil, fnmatch
import argparse
import re
import chardet
from pathlib import Path

pid = os.getpid()
print("PID is '{}'".format(pid))
log_directory = os.path.join(os.getcwd(), 'log')
os.makedirs(log_directory, exist_ok=True)
log_file = os.path.join(log_directory, 'm3u_to_mp3.log')
print ("log file is {}".format(log_file))

logger = logging.getLogger('m3u_to_mp3')
logger.setLevel(logging.DEBUG)
logger.handlers = []
logger.propagate = False
console_hdlr = logging.StreamHandler()
console_hdlr.setLevel(logging.INFO)
logger.addHandler(console_hdlr)
loghdlr = logging.FileHandler(log_file, mode='w', encoding = "utf-8")
loghdlr.setFormatter(
    logging.Formatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s'))
loghdlr.setLevel(logging.DEBUG)
logger.addHandler(loghdlr)

def parse_arguments():
    """ Parse command-line arguments
        Example : python m3u_to_mp3/m3u_to_mp3.py
              -i ./m3u_dir
              -o ./mp3_dir
    """
    description = \
        'Read M3U files and copy the mp3 files listed.\n' \
        'Ex: python m3u_to_mp3/m3u_to_mp3.py' \
        '    -i ./m3u_dir' \
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

    parser.add_argument("-p", "--prefix"
                        , help="M3U files prefix."
                        , dest="prefix"
                        , default=None
                        , required=False)

    parser.add_argument("-c", "--check"
                        , help="Check only MP3 files in M3U files."
                        , dest="check"
                        , action='store_true'
                        , default=False
                        , required=False)

    return parser.parse_args()

class M3U2MP3():
    ''' Class to read M3U files and copy the mp3 files listed '''
    def __init__(self, input_dir, output_dir, prefix=None, check=False):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.prefix = prefix
        self.check = check

    def parse_playlists(self):
        m3u_file_name_list = fnmatch.filter(os.listdir(self.input_dir), '*.m3u')
        if self.prefix is not None:
            m3u_file_name_list = fnmatch.filter(os.listdir(self.input_dir), '{}*.m3u'.format(self.prefix))
        logger.debug("M3U file list is '{}'".format(m3u_file_name_list))
        for m3u_file_name in m3u_file_name_list:
            logger.debug("M3U file is '{}'".format(m3u_file_name))
            m3u_file_full_path = os.path.join(self.input_dir, m3u_file_name)
            m3u_file_path = Path(m3u_file_full_path)
            blob = m3u_file_path.read_bytes()
            detection = chardet.detect(blob)
            logger.debug(detection)
            encoding = detection["encoding"]
            # logger.debug(m3u_file_path.decode(encoding))
            mp3_dir = os.path.join(self.output_dir, m3u_file_name.replace(".m3u", ""))
            if not self.check:
                os.makedirs(mp3_dir, exist_ok=True)
            with open(m3u_file_full_path, 'r', encoding=encoding) as m3u_file:
                m3u_file_lines = m3u_file.readlines()
                count = 0
                for m3u_file_line in m3u_file_lines:
                    count += 1
                    # logger.debug("Line{}: {}".format(count, m3u_file_line.strip()))
                    mp3_file_name = m3u_file_line.strip()
                    mp3_file_name = mp3_file_name.replace("\\", os.sep)
                    mp3_file_name = mp3_file_name.replace("/", os.sep)
                    mp3_file_path = os.path.join(self.input_dir, mp3_file_name)
                    check_mp3_file = os.path.isfile(mp3_file_path)
                    if check_mp3_file:
                        if self.check:
                            logger.debug("File {} exists".format(mp3_file_path))
                        else:
                            logger.debug("Copy {} to {} directory".format(mp3_file_path, mp3_dir))
                            shutil.copy2(mp3_file_path, mp3_dir)
                    else:
                        logger.warning("Playlist:{}. File '{}' NOT exists.".format(m3u_file_name, mp3_file_path))


if __name__ == "__main__": # pragma: no cover
    args = parse_arguments()

    m3u_to_mp3 = M3U2MP3(args.m3u_dir, args.mp3_dir, args.prefix, args.check)
    m3u_to_mp3.parse_playlists()