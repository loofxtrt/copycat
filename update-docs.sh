#!/usr/bin/bash

# script to update the documentation files

# activates python venv
source venv/bin/activate

# defines the repository root and pass it to the scripts
ROOT=/mnt/seagate/workspace/coding/projects/icons/copycat/
python3 ./scripts/readme/writer.py $ROOT
python3 ./scripts/track/writer.py $ROOT