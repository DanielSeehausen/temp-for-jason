ROOT:   "https://learn.co/api/v1/"
LESSON: "https://learn.co/api/v1/curriculums/:id"
TRACK:  "https://learn.co/api/v1/tracks/:id"
BATCH:  "https://learn.co/api/v1/batches/:id"

Hierarchy:
Track -> Topic -> Unit -> Lessons

------------------------------------------------------------------------

JSON response track structure is as follows:

track.children : [ topics.children : [ units.children => lessons ] ]

i.e.:

```json
track: {
  id: 25783,
  title: 'Module 4 – Web Development Immersive 2.0',
  depth: 0,
  published_batch_ids: [],
  track_id: 25783,
  children: [topics]
}

topic: {
  id: 27733,
  title: 'Discussion Questions',
  depth: 1,
  published_batch_ids: [],
  track_id: 25783,
  children: [subSections]
}

unit: {
  id: 31058,
  title: 'Mod4: Useful tools for React',
  depth: 2,
  published_batch_ids: [],
  track_id: 25783,
  children: [ {LAB!} },
}

lesson: {
  id: 31059,
  title: 'Some Useful Tools for Writing React',
  depth: 3,
  published_batch_ids: [ 502 ],
  track_id: 25783,
  children: [],
  github_url: '//github.com/learn-co-curriculum/some-useful-tools-for-writing-react'
}
```

------------------------------------------------------------------------

Lesson Structure (is this from lesson endpoint then?):

```json
Specific Lesson: {
  "content_type": "Lab",
  "created_at": "2017-02-24T16:35:01.116-05:00",
  "parent_title": "An Intro to Hashes",
  "canonical_id": 7436,
  "child_order": [],
  "depth": 3,
  "github_url": "//github.com/learn-co-curriculum/my-first-hash",
  "has_lab": true,
  "id": 25449,
  "parent_id": 25447,
  "published_batch_ids": [
    477,
    484
  ],
  "readme_markdown": "# My First Hash\n\n## Objectives\n\n1. Create hashes...",
  "readme_markdown_as_html": "<h2 id=\"objectives\">Objectives</h2>\n\n<ol...",
  "slug": "first-hash",
  "title": "First Hash",
  "track_id": 25054,
  "track_title": "Module 1 – Web Development Immersive 2.0",
  "type": "Lesson",
  "updated_at": "2018-01-26T14:40:25.285-05:00",
  "is_readme": false,
  "canonical_name": "my-first-hash",
  "completed_progresses_count": 2310,
  "open_issue_count": 0,
  "open_pr_count": 0,
  "tracks": [
    {
      "id": 11897,
      "title": "Teacher Training - Web Development Fundamentals"
    },
    {
      "id": 8303,
      "title": "QA Testing Track"
    },
    {
      "id": 5309,
      "title": "Web Development with Ruby on Rails"
    }
  ]
}
```
