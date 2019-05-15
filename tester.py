#!/usr/bin/env python3

from api_interface import *

def main():
    l1_lectures = get_track_canonical_urls(40234)
    l1_student_lessons = get_track_canonical_urls(40864)
    l1_teacher_training = get_track_canonical_urls(34621)
    print(l1_lectures, l1_student_lessons, l1_teacher_training)
    # HEADERS = ["Track", "Topic", "Unit", "Position", "CID", "Title", "CName", "Content Type", "Github", "ReviewStatus", "Action", "Merge Status", "Owner", "Reviewer A", "Reviewer B"]
    # header_and_rows = [HEADERS] + all_rows
    # to_csv(all_rows)

if __name__ == '__main__':
    main()
