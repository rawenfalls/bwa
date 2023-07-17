import time
import os

def str_to_arr(word):
	a_arr=[]
	for i in range(0,len(word),1):
		a_arr.append(word[i])
	return(a_arr)


start_time = time.time()
interval = 20
counter = 0
counter1 = 0
counter_flags = 0
counter_x=0
str_counter = 0
A_arr=[]
B_arr=[]
print('введите количество несовпадений')
x=int(input())
with open('./a/sequence1.fasta') as a_file:
	with open('./b/sequence2.fasta') as b_file:
		with open('./c.txt','w+') as c_file:
			print(a_file.readline().rstrip()[1:] + ' vs ' + b_file.readline().rstrip()[1:])
			counter = 0
			while 1:
				str_counter+=1
				a = a_file.readline().rstrip()
				b = b_file.readline().rstrip()
				A_arr = A_arr+str_to_arr(a)
				B_arr = B_arr+str_to_arr(b)
				if a == '' and b== '': break
				c_file.write(a+'\n')
				for i in range(0,len(a),1):
					if a[i] == b[i]:
						c_file.write('|')
						counter+=1
						counter_x=0
					else:
						c_file.write('x')
						counter1+=1
						counter_x+=1
				c_file.write('\n'+b)
				if (counter_x>=x):
					counter_flags+=1
					print(str_counter)
					c_file.write('<-------------------')
				c_file.write('\n')
			print('совпадение '+str(counter))
			print('не совпадение '+str(counter1))
			print(str(x)+' и более несовпадений '+str(counter_flags))
print("--- %s seconds ---" % int(time.time() - start_time),end='')
os.system('start c.txt')
