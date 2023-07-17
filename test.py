with open('./a/sequence1.fasta','r') as a_file:
	with open('./c.txt','w') as c_file:
		a_file.readline()
		while 1:
			a = a_file.readline().rstrip()
			if a == '': break
			c_file.write(a)
		print('Done')
