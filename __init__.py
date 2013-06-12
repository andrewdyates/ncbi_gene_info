import os
DIR = os.path.abspath(os.path.dirname(__file__))
FNAME = os.path.join(DIR, "human_gene_list.txt")

def load_list(fname=FNAME):
  genes = []
  for line in open(fname):
    genes.append(line.strip('\n\r').split('\t'))
  return genes
  
def sym_to_entrez_dicts(glist=None):
  if glist is None:
    glist = load_list()

  sym_to_entrez = {}
  alias_to_entrez = {}
  for r in glist:
    entrez, sym, alias_s = r
    aliases = alias_s.split('|')
    for a in aliases:
      if a and a != '-':
        alias_to_entrez.setdefault(a,set()).add(entrez)
    sym_to_entrez.setdefault(sym,set()).add(entrez)

  return sym_to_entrez, alias_to_entrez
  
