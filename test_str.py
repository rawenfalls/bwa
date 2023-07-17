import time
import os
start_time = time.time()
interval = 20
counter = 0
counter1 = 0
# with open('./a/sequence1.fasta') as a_file:
# 	with open('./b/sequence2.fasta') as b_file:
# 		with open('./c.txt','w+') as c_file:
# 			print(a_file.readline().rstrip()[1:] + ' vs ' + b_file.readline().rstrip()[1:])
# 			counter = 0
# 			while 1:
# 				a = a_file.readline().rstrip()
# 				b = b_file.readline().rstrip()
# 				if a == '': break
# 				c_file.write(a+'\n')
# 				for i in range(0,len(a),1):
# 					if a[i] == b[i]:
# 						c_file.write('|')
# 						counter+=1
# 					else:
# 						c_file.write('x')
# 						counter1+=1
# 				c_file.write('\n'+b+'\n')
# 			print('совпадение '+str(counter))
# 			print('не совпадение '+str(counter1))
# print("--- %s seconds ---" % int(time.time() - start_time),end='')
# os.system('start c.txt')

with open('./a/sequence1.fasta') as a_file:
	a = a_file.readline().rstrip()
	print(len(a))
	a = a_file.readline().rstrip()
	print(len(a))
	a = a_file.readline().rstrip()
	print(len(a))
	# with open('./b/sequence2.fasta') as b_file:
	# 	a_str= ''
	# 	b_str= ''
	# 	while 1:
	# 		a = a_file.readline().rstrip()
	# 		b = b_file.readline().rstrip()
	# 		if a == '': break
	# 		a_str = a_str+a
	# 		b_str = b_str+b
	# 	with open('./cq.txt','w+') as c_file:
	# 		c_file.write(a)
	# 		c_file.write(b)