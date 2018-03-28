def get_digested_track(track_id):
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

def temper(mod4_lessons):
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
                print("\t\t\t - ", lesson["title"], end="...")
                full_lesson_data = get("lesson", lesson["id"])
                found_lessons.add(full_lesson_data["canonical_id"])
                if not (full_lesson_data["canonical_id"] in mod4_lessons):
                    try:
                        parent_data = [track_title, topic_title, unit_title, len(rows)]
                        lesson_data = parse_lesson_to_row(full_lesson_data)
                        rows.append(parent_data + lesson_data)
                    except:
                        print("<---- BAD DATA HERE. LESSON OBJECT FOLLOWED BY ERROR:")
                        print(lesson)
                        raise
                    print("success")
                else:
                    print("mod4 already has!!!")
    return (rows, found_lessons)


mod4_rows, mod4_lessons = get_digested_track(25783)
redux_rows, redux_lessons = get_digested_track(23286)

in_person_ids = mod4_lessons.union(redux_lessons)

unique_online_rows, online_ids = temper(in_person_ids)

overlap_ids = in_person_ids.intersection(online_ids)

all_rows = mod4_rows + redux_rows + unique_online_rows

for row in all_rows:
    if row[4] in overlap_ids:
        row.insert(0, 'B')
    elif row[4] in in_person_ids:
        row.insert(0, 'I')
    else:
        row.insert(0, 'O')

HEADERS = ["Online/InPerson/Both", "Track", "Topic", "Unit", "Position", "CID", "Title", "CName", "Content Type", "Github", "ReviewStatus", "Action", "Merge Status", "Owner", "Reviewer A", "Reviewer B"]
header_and_rows = [HEADERS] + all_rows
to_csv(all_rows)
