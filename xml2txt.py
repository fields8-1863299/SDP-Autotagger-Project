# Author: Travis Le
# A method to convert from XML to TXT.

def convert(input1, input2):
  line_tags = []
  file = open(input1)
  lines = file.readlines()
  file.close()
  file2 = open(input2, "w")
  for i in range(0, len(lines)):
    current = lines[i].strip()
    arabic_start = "<emph>"
    arabic_end = "</emph>"
    head_start = "<head>"
    head_end = "</head>"
    if current.startswith("<") and current.endswith(">"):
      if arabic_start in current:
        file2.write(current[current.find(arabic_start) + 6 : current.find(arabic_end)] + "\n")
      elif head_end in current:
        filtered1 = current.replace(head_end, "")
        if len(filtered1) != 0:
          file2.write(filtered1[filtered1.find(">") + 1 : len(filtered1) - 1] + "\n")
        else:
          file2.write("\n\n")
      elif "head" in current:
        file2.write("\n")
      else:
        file2.write("\n")
    else:
      file2.write(current)
  
  file2.close()



def test(input1):
  
  file = open(input1)
  lines = file.readlines()
  file.close()

  for i in range(0, len(lines)):
    no_space = lines[i].strip()
    current = lines[i].strip()
    arabic_start = "<emph>"
    arabic_end = "</emph>"
    head_start = "<head>"
    head_end = "</head>"
    if no_space.startswith("<") and no_space.endswith(">"):
      if arabic_start in current:
        file2.write(current[current.find(arabic_start) + 6 : current.find(arabic_end)])
      elif head_end in current:
        filtered1 = current.replace(head_end, "")
        if len(filtered1) != 0:
          file2.write(filtered1[filtered1.find(">") + 1 : len(filtered1) - 1])
        # print(filtered1)
      elif "head" in current:
        file2.write("\n")
      else:
        file2.write("\n")
    else:
      file2.write(current)
  

# test("texts/test_txt.txt")

convert("texts/d51.xml", "texts/result_txt.txt")




