# Author: Travis Le
# A method to fix the format of diary 48 so that the auto-tagger can produce a good .xml output

import autotagger
from config import AutotaggerConfiguration

# fix the format of diary 48 (mainly add : after the page and fix subsection spacing)
def print_one(input1, input2):
  # cfg -> configuration
  cfg = AutotaggerConfiguration()
  file = open(input1)
  lines = file.readlines()
  file.close()
  file2 = open(input2, "w")
  for i in range(0, len(lines)):
    if (lines[i][0:4] == 'Page'):
      file2.write(lines[i].split("\n")[0] + ":" + "\n")
    elif ('Subsection:' in lines[i]):
      if (len(lines[i - 1]) < 4):
        file2.write(lines[i].split("\n")[0] + "\n")
      else:
        file2.write("\n" + lines[i].split("\n")[0] + "\n")
    else:
      file2.write(lines[i])
  file2.close()

print_one("texts/d48_new.txt", "texts/d48_fix.txt")