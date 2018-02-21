#!/bin/sh
echo "Using summarize.py\n"
python src/summarize.py examples/input.txt

echo "\n\nUsing summarize2.py\n"
python src/summarize2.py examples/input.txt
