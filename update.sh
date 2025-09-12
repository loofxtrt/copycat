#!/usr/bin/bash
# script to update the documentation files
source venv/bin/activate
python3 python/readme/writer.py
python3 python/track/writer.py