#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVE_DIR="archive"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created archive directory."
fi

NEW_NAME="grades_${TIMESTAMP}.csv"
mv grades.csv "$ARCHIVE_DIR/$NEW_NAME"
echo "Moved grades.csv to $ARCHIVE_DIR/$NEW_NAME"

touch grades.csv
echo "Created new empty grades.csv"

echo "$TIMESTAMP | grades.csv | $NEW_NAME" >> organizer.log
echo "Logged to organizer.log"
