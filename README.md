# Shrink Map

## Tool to shrink the world/map size of the techage survival server

In order to prevent the size of the world ('map.sqlite' currently almost 50 GB) from growing unnecessarily, I installed the mapcleaner tool.

Mapcleaner deletes unused areas of the map. Since this is very computationally intensive, Mapcleaner is set to only process a thin slice of the world each night after the backup. It takes over 2 years for the complete card.

Link to [mapcleaner](https://github.com/minetest-go/mapcleaner)

## How it works

Mapcleaner removes map blocks based on a nodename whitelist. The nodename whitelist defines which nodes should be retained.
The used whitelist includes almost all “unnatural” blocks.
If one of these blocks is found in a chunk (or in the neighboring chunks), it will not be deleted. (A chunk is a square of 80x80x80 meters/blocks)

That means:

Simple dirt towers without further decorative blocks, or dug caves without torches, protective blocks or similar will be deleted.
