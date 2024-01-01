#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime

"""
Map Slices
==========

Max. coordinates (x,y,z): -30912 to 30927
In mapblock positions:    -30912 to 30912
Mapblocks (16x16x16):     -1932 to 1932
Chunks: (5x5x5):          -386 to 386

This makes 773 slices in z direction.

See: https://github.com/minetest-go/mapcleaner
"""

templ = """{
  "chunk_x":-386,
  "chunk_y":-386,
  "chunk_z":_idx_,
  "removed_chunks":0,
  "retained_chunks":0,
  "processed_chunks":0,
  "from_x":-386,
  "from_y":-386,
  "from_z":_idx_,
  "to_x":386,
  "to_y":386,
  "to_z":_idx_,
  "delay":0
}
"""

def get_time():
    """
    Get date/time of day as string
    """
    current = datetime.now()
    time = current.strftime("%d/%m/%Y %H:%M:%S")
    return time

def get_index(seconds=None):
    """
    Get slice index (from -386 to 386) based on days since epoch
    """
    now = datetime.now()
    seconds = seconds or now.strftime("%s") # seconds since epoch
    days = int(int(seconds) / 86400) # days since epoch
    return (days % 773) - 386

def get_filesize():
    """
    Return size of file 'map.sqlite' in MB
    """
    return int(os.stat("./map.sqlite").st_size / 1000000)

def shrink_map():
    """
    Shrink the map slice by slice
    """
    idx = get_index()
    s = templ.replace("_idx_", str(idx))
    open("mapcleaner.json", "wt").write(s)

    open("./shrink_map.log", "at").write(f"{get_time()}: Work on slice {idx} (-386 to 386)\n")

    size1 = get_filesize()
    os.system("./mapcleaner")
    os.system("sqlite3 map.sqlite \"VACUUM INTO './map2.sqlite';\"")
    os.renames('./map2.sqlite', './map.sqlite')    
    size2 = get_filesize()

    open("./shrink_map.log", "at").write(f"{get_time()}: File size [MB] of 'map.sqlite' is (old -> new) {size1} -> {size2}\n")


if __name__ == "__main__":
    shrink_map()
