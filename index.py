#!/usr/bin/env python3
import sys
print(sys.version)
from api import *

def main():
    l1_lectures = get_track_canonical_urls(40234)
    print(li_lectures)

if __name__ == '__main__':
    main()
