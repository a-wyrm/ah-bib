from pybtex.database import BibliographyData, parse_file

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


def main():
    # change file name for different file
    file = "./BIB Files/Misc. Accessibility Papers/Misc. Accessibility Papers.bib.bib"
    remove_abstracts(file)
    remove_file(file)

            
            

if __name__ == '__main__':
    main()