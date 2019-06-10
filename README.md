# filenamescrubber
HFS to NTFS filename scrubber

Used for migrating files from an Apple file server using HFS
to a Windows server running NTFS.  

Removes <, >, :, ", /, \\, |, ? and * from file and directory
names.


use:
python3 scrubber.py .
or
python3 scrubber.py /path/to/some/folder
