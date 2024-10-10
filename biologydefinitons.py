import random as r
biodic = {'Alleles': 'Different forms of a gene', 
'Anti-codon': 'Group of three bases on tRNA', 
'Codon': 'Group of three bases on mRNA', 
'Complementary Base Pairs': 'Each base has matching corresponding base', 
'Diploid':'A nucleus having two sets of chromosomes (NOT having pairs)',
'DNA Replication':'Making a copy of DNA',
'Evolution':'Inheritable change in a population (or species) in response to a change in the environment by natural selection over time',
'Expression':'The activation of a gene or the production of product',
'Gene':' Unit of inheritance. Length of DNA that codes for a protein',
'Gene expression':'When a gene is switched on and produces its characteristic or protein',
'Genetic Engineering':'Manipulation or alteration of an organisms genes or genotype',
'Genetic Screening':' Testing (people) for the presence or absence of a specific gene',
'Genotype':' Genetic make-up/combination of genes',
'Haploid':' A nucleus having one set of chromosomes',
'Heredity':' Passing of genetically controlled characteristics from parents to offspring',
'Heterozygous':' Alleles that are different',
'Homologous chromosomes':' Chromosomes which are the same size and shape containing genes for same traits',
'Homologous structures':' Same basic structure modified for different functions',
'Homozygous':' Identical alleles. Alleles are the same',
'Incomplete dominance':' Phenotype of heterozygous individual is intermediate between the two characteristics',
'Independent Assortment (Law of)': 'Either member of a pair of alleles can combine with either member of another pair of alleles in gamete formation',
'Isolation': 'Removal of a gene or piece of DNA or plasmid',
'Junk DNA': 'Non-coding DNA' ,
'Law':'Theory that has withstood long term testing'}
randitems = r.choice(list(biodic.values()))
print(randitems)
ans = input('Enter Keyword: ')
 
