#!/usr/bin/env python3

from api_interface import *

def main():
    mod4_rows, mod4_lessons = get_track(25783)
    redux_rows, redux_lessons = get_track(23286)
    in_person_rows, in_person_ids = get_online_redux_react()
    all_rows = mod4_rows + redux_rows + in_person_rows

    # in_person_ids = mod4_lessons.union(redux_lessons)
    # unique_online_rows, online_ids = temper(in_person_ids)
    # overlap_ids = in_person_ids.intersection(online_ids)
    # all_rows = mod4_rows + redux_rows + unique_online_rows
    #
    # for row in all_rows:
    #     if row[4] in overlap_ids:
    #         row.insert(0, 'B')
    #     elif row[4] in in_person_ids:
    #         row.insert(0, 'I')
    #     else:
    #         row.insert(0, 'O')

    HEADERS = ["Track", "Topic", "Unit", "Position", "CID", "Title", "CName", "Content Type", "Github", "ReviewStatus", "Action", "Merge Status", "Owner", "Reviewer A", "Reviewer B"]
    header_and_rows = [HEADERS] + all_rows
    to_csv(all_rows)

if __name__ == '__main__':
    main()
