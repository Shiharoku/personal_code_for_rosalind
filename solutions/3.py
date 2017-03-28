#my code
seq = "ATCG"
dict_comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C':'G'}
comp = ''
for i in seq:
	comp += dict_comp[i]
print(comp[::-1])