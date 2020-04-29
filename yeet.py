# Author: Travis Le
# Attempt to figure the header notes and print out the pages in the right format

import autotagger
from config import AutotaggerConfiguration


attemp to print out the page
def print_bod(document, tf, marginheaders, footnotes):
      body = document.getElementsByTagName('body')[0]
      count = 0
      for page in tf.pages:
            for l in page:
                  count += 1
                  print(l)
                  print(count)