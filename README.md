# mkfilename
Utility to generate filenames for archiving.

## Why?
I wanted to archive quick notes for easy retrieval.
Over time I found a naming convention that proved to be useful.
In order to quickly generate matching names, I wrote this utility.
Over time this neatly sorts your notes.

I use this quite some time now and thought about releasing it to public.

## How
You copy a heading to clipboard and call this utility.
As a result, you will receive a proper filename in your clipboard.

I generate a portable executeable for Linux, Windows and Mac and usually
distribute that on my workstations. Then I create a shortcut and whenever
I need to generate a filename from a selected heading, I click the link.

The script `freeze.sh` creates a standalone version.

## Example

1. Copy `Python is a high-level, interpreted, general-purpose programming language` to clipboard.
2. Run `./mkfilename.py --clipboard`
3. Paste you clipboard contents. 
   You should get `220812-python-is-a-high-level-interpreted-general-purpose-programming-language.md`

## License
This code is released under MIT license.