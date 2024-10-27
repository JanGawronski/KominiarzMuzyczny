#!/bin/bash
python -m venv .
source ./bin/activate
pip install "py-cord[voice]" "py-cord[speed]" yt-dlp pyshorteners requests spotipy sponsorblock