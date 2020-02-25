# Author: Sam Fields
# A method for outputting the xml encoding of a txt transcriptiom file

import autotagger
from config import AutotaggerConfiguration

# follows the most basic process to read in a txt file and print out a tei xml file
def print_tei(input):
    # cfg -> configuration
    cfg = AutotaggerConfiguration()
    file = open(input, encoding="utf-8")
    lines = file.readlines()
    file.close()
    # lines is a big (collection of) string(s)
    tf = autotagger.TranscriptionFile(lines)
    document = autotagger.setup_DOM(cfg)
    # autotagger.run() -> builds the xml file
    document = autotagger.run(tf, cfg)
    print(document.toprettyxml('\t', '\n', None))

print_tei("texts/Test2020_NoSubsection.txt")