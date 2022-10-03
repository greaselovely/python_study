#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  THEM: Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  """
  ME: Create a list to write to.
  Read the file and capture the text in the file.
  find the year in the file and append it to the list.
  """
  ranked_list = []
  with open(filename, 'r') as file:
    text = file.read()
  year_pattern = r'Popularity in (\d{4})'
  year = re.findall(year_pattern, text)[0]
  ranked_list.append(year)


  """
  ME:  This was work in understanding how to use named groups in regex.  This makes it useful for readability instead of 
  trying to understand / read either index (not really) or match groups.  For the digit below I recognize that the
  rank number cannot exceed 5 digits so for larger numbers using '\d+' would be 'better' (scalable).
  """
  rank_name_pattern = r'>(?P<rank>\d{1,4})<\/td><td>(?P<gname>\w+)<\/td><td>(?P<bname>\w+)<\/td>'
  matches = re.finditer(rank_name_pattern, text)
  for match in matches:
    ranked_list.append(f"{match.group('gname')} {match.group('rank')}")
    ranked_list.append(f"{match.group('bname')} {match.group('rank')}")

  ranked_list.sort()

  return ranked_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file  
  """
  ME: Iterate through all of the files presented in the args above.
  Capture the full path given to use in args minus the last 5 characters (.html) 
  so we can right a file to the same path and a file extension of .txt.  Has to be 
  cast to a str() to write to the file.
  """
  for file in args:
    output = f"{file[:-5]}.txt"
    with open(output, 'w') as f:
      f.write(str(extract_names(file)))
  
if __name__ == '__main__':
  main()
