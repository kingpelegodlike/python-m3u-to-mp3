import os
import argparse
import pytest
from mock import patch, Mock

from m3u_to_mp3.m3u_to_mp3 import parse_arguments, M3U2MP3

@patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(input_dir='input_dir', output_dir='output_dir'))
def test_parse_arguments(mock_args):
    parse_arguments()

def test_init():
    m3u_to_mp3 = M3U2MP3("input_dir", "output_dir", "playlist")

    assert hasattr(m3u_to_mp3, "input_dir"), "M3U2MP3 class does not have 'input_dir' attribute"

    assert hasattr(m3u_to_mp3, "output_dir"), "M3U2MP3 class does not have 'output_dir' attribute"

    assert hasattr(m3u_to_mp3, "prefix"), "M3U2MP3 class does not have 'prefix' attribute"

    assert m3u_to_mp3.input_dir == "input_dir", \
        "M3U2MP3 class 'input_dir' attribute habe value '{}' instead of 'input_dir'" \
        .format(m3u_to_mp3.input_dir)

    assert m3u_to_mp3.output_dir == "output_dir", \
        "M3U2MP3 class 'output_dir' attribute habe value '{}' instead of 'output_dir'" \
        .format(m3u_to_mp3.output_dir)

    assert m3u_to_mp3.prefix == "playlist", \
        "M3U2MP3 class 'prefix' attribute habe value '{}' instead of 'playlist'" \
        .format(m3u_to_mp3.prefix)

def test_parse_playlists():
    m3u_to_mp3 = M3U2MP3(os.path.join("testu", "data", "m3u_dir"), os.path.join("log", "mp3_dir"), "playlist")
    m3u_to_mp3.parse_playlists()