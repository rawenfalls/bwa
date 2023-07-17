from difflib import SequenceMatcher
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()
interval = 20
counter = 0
with open('./a/sequence1.fasta') as a_file:
	with open('./a/sequence1.fasta') as b_file:
		print(a_file.readline().rstrip()[1:] + ' vs ' + b_file.readline().rstrip()[1:])
		first_str_a = a_file.readline().rstrip()
		second_str_a = a_file.readline().rstrip()
		first_str_b = b_file.readline().rstrip()
		second_str_b = b_file.readline().rstrip()
		for i in range(0,len(first_str_a)-interval,1):
			a_str = first_str_a[i:interval+i:1]
			print (a_str + " " + first_str_b + " "+str(i))
			if not(a_str in first_str_b):
				print(a_str)
				counter+=1
		print(counter)







		# print(round(similar(first_str, second_str),2))
		# print(first_str)
		# a = 0
		# for i in range(0,len(first_str),1):
		# 	if first_str[i] == second_str[i]:
		# 		print('|',end='')
		# 		a+=1
		# 	else:
		# 		print('x',end='')
		# print('\n'+second_str)
		# print(str(a))
