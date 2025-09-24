#!/usr/bin/bash

# script to update the documentation files

# activates python venv
source venv/bin/activate

# defines the repository root and pass it to the scripts (hardcoded path)
ROOT=/mnt/seagate/workspace/coding/projects/icons/copycat/

python3 ./scripts/readme/writer.py "."
python3 ./scripts/track/writer.py $ROOT