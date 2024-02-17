from pybtex.database import BibliographyData, parse_file
from collections import OrderedDict

def remove_abstracts(bib):
  """Remove abstracts from bib."""
  bib_data = parse_file(bib)
  for entry in bib_data.entries.values():
      try:
          del entry.fields['abstract']
      except KeyError:
          print()
  BibliographyData.to_file(bib_data, bib)

def remove_file(bib):
  """Remove file paths from bib."""
  bib_data = parse_file(bib)
  for entry in bib_data.entries.values():
      try:
          del entry.fields['file']
      except KeyError:
          print()
  BibliographyData.to_file(bib_data, bib)


# Taken from Max Golla's bib validator
# https://github.com/m33x/MaxBib/blob/master/order_within.py

def readfile(filename):
    result = []
    with open(filename, 'r', encoding="utf8") as inputfile:
        for line in inputfile:
            line = line.rstrip('\r\n')
            result.append(line)
    return result


def get_bibitems(bib):
    """Where does a bibentry start, where does it end?"""
    result = OrderedDict()
    item = []
    entry_name = ''
    for line in bib:
        if line != '':
            item.append(line)
        if line.startswith('@'):
            entry_name = line
        if line.startswith('}'):
            result[entry_name] = item
            entry_name = ''
            item = []
    return result

def convert_to_bibentries(maxbib_items):
    entries = OrderedDict()
    for item in maxbib_items:
        entry = OrderedDict()
        entries[item] = entry
    return entries

def enforce_order(name, entry, order):
  """Parse the bib item to something meaningful, aka identify title, author, year etc."""
  for k, v in enumerate(entry):
    if v != order[k]:
        print(name)
        print("Wrong order", v, "!=",order[k])
        print(entry)
        print()



def main():
    # change file name for different file
    file = "./BIB Files/Accessible Security and Privacy/Visual Impairment/Visual Impairment.bib"
    remove_abstracts(file)
    remove_file(file)
            
            

if __name__ == '__main__':
    main()