Used for migrating files from an Apple file server using HFS to a Windows server running NTFS. 

Based on a post by Jacob Viljm which can be found at:
https://askubuntu.com/questions/671320/how-to-rename-file-names-to-avoid-conflict-in-windows-or-mac

I extended this to rename all directories as well

Removes <, >, :, ", /, \\, |, ? and * from file and directory names.

use:
python3 scrubber.py .
or
python3 scrubber.py /path/to/some/folder
