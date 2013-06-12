#!/usr/bin/python
"""Parse NCBI Gene Info file into smaller list of human genes.

Downloaded from 
ftp://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz

Gene_info format
#Format: tax_id GeneID Symbol LocusTag Synonyms dbXrefs chromosome map_location description type_of_gene Symbol_from_nomenclature_authority Full_name_from_nomenclature_authority Nomenclature_status Other_designations Modification_date (tab is used as a separator, pound sign - start of a comment)

human tax_id: 9606

python parse_raw_ncbi_dump.py > human_gene_list.txt
"""
import gzip
import sys
#import hugo_gene_symbols
#H = hugo_gene_symbols.load()
#H.find_sym("MySym")

fp = gzip.open("gene_info.gz")


human_genes = []
for i,line in enumerate(fp):
  if i % 100000 == 0:
    print >>sys.stderr, "Reading line %d..." %i
  line = line.strip('\n\r')
  if not line or line[0] == "#": continue
  row = line.strip('\n\r').split('\t')
  if row[0] != "9606": continue
  human_genes.append((row[1], row[2], row[4]))

for tup in human_genes:
  print "\t".join(tup)
  
  
  
