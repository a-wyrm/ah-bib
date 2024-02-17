from pybtex.database import BibliographyData, parse_file
from collections import OrderedDict
import sys


def remove_abstracts(bib):
  bib_data = parse_file(bib)
  for entry in bib_data.entries.values():
      try:
          del entry.fields['abstract']
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
  for k, v in enumerate(entry):
    if v != order[k]:
        print(name)
        print("Wrong order", v, "!=",order[k])
        print(entry)
        #sys.exit(1)
        print()



def main():
    # change file name for different file
    file = "./BIB Files/Password Policies.bib"
    remove_abstracts(file)

    bib = readfile(file)
    bib_items = get_bibitems(bib)
    bib_entries = convert_to_bibentries(bib_items)
    for entry in bib_items:
        order = []
        if entry.startswith("@inproceedings"):
            order = ['author', 'title', 'booktitle', 'year', 'series', 'pages', 'address', 'month', 'publisher']
        elif entry.startswith("article"):
            order = ['author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'month', 'publisher']
        else:
            order = ['author', 'title', 'note', 'month', 'year']
        
        enforce_order(entry, bib_entries[entry], order)

            
            

if __name__ == '__main__':
    main()