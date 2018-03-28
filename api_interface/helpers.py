#!/usr/bin/env python3
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

import requests
from json import loads
import csv

endpoints = {
    "root": "https://learn.co/api/v1/",
    "lesson": "https://learn.co/api/v1/curriculums/",
    "track": "https://learn.co/api/v1/tracks/",
    "batch": "https://learn.co/api/v1/batches/"
}

def to_csv(rows, output="temp.csv"):
    with open(output, 'w') as f:
        writer = csv.writer(f, delimiter='|', quotechar='"')
        writer.writerows(rows)

def get(tier, id):
    return requests.get(f"{endpoints[tier]}{id}").json()

def parse_lesson_to_row(lesson):
    cid = lesson["canonical_id"]
    title = lesson["title"]
    c_name = lesson["canonical_name"]
    content_type = lesson["content_type"]
    github = "https" + lesson["github_url"] if lesson["github_url"] else "MISSING DATA!"
    return [cid, title, c_name, content_type, github]
