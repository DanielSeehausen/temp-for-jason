#!/usr/bin/env python3
from .helpers import *
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())


def get_track_canonical_urls(track_id):
    track_dict = get("track", track_id)

    urls = []

    print("Fetching...\n\n")
    print(track_dict["title"])

    for topic in track_dict["children"]:
        print("\n\t", topic["title"])
        for unit in topic["children"]:
            print("\t\t", unit["title"])
            for lesson in unit["children"]:
                full_lesson_data = get("lesson", lesson["id"])
                print("\t\t\t - ", lesson["title"], end="...")
                try:
                    url = get_url(full_lesson_data)
                    urls.append(url)
                except:
                    print("<---- BAD DATA HERE. LESSON OBJECT FOLLOWED BY ERROR:")
                    print(lesson)
                    raise
                print("success")

    return (urls)

def get_track(track_id):
    track_dict = get("track", track_id)

    found_lessons = set([])
    rows = []

    track_title = track_dict["title"]
    print("Fetching...\n\n")
    print(track_title)

    for topic in track_dict["children"]:
        topic_title = topic["title"]
        print("\n\t", topic_title)
        for unit in topic["children"]:
            unit_title = unit["title"]
            print("\t\t", unit_title)
            for lesson in unit["children"]:
                full_lesson_data = get("lesson", lesson["id"])
                print("\t\t\t - ", lesson["title"], end="...")
                try:
                    get_url(full_lesson_data)
                    found_lessons.add(full_lesson_data["canonical_id"])
                    parent_data = [track_title, topic_title, unit_title, len(rows)]
                    lesson_data = parse_lesson_to_row(full_lesson_data)
                    rows.append(parent_data + lesson_data)
                except:
                    print("<---- BAD DATA HERE. LESSON OBJECT FOLLOWED BY ERROR:")
                    print(lesson)
                    raise
                print("success")

    return (rows, found_lessons)


def get_online_redux_react():
    track_dict = get("track", 31303)

    found_lessons = set([])
    rows = []

    track_title = track_dict["title"]
    print("\n\nFetching...\n\n")
    print(track_title)

    for topic in track_dict["children"][-2:]: #only react and redux?
        topic_title = topic["title"]
        print("\n\t", topic_title)
        for unit in topic["children"]:
            unit_title = unit["title"]
            print("\t\t", unit_title)
            for lesson in unit["children"]:
                full_lesson_data = get("lesson", lesson["id"])
                print("\t\t\t - ", lesson["title"], end="...")
                try:
                    found_lessons.add(full_lesson_data["canonical_id"])
                    parent_data = [track_title, topic_title, unit_title, len(rows)]
                    lesson_data = parse_lesson_to_row(full_lesson_data)
                    rows.append(parent_data + lesson_data)
                except:
                    print("<---- BAD DATA HERE. LESSON OBJECT FOLLOWED BY ERROR:")
                    print(lesson)
                    raise
                print("success")

    return (rows, found_lessons)
