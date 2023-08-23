import time
import os
start_time = time.time()

def str_to_arr(arr_name, string):
	for i in range(0,len(string),1):
		arr_name.append(string[i])
	return(arr_name)

def file_in_arr(file_name):
	arr = []
	while 1:
		string = file_name.readline().rstrip()
		if string == '': break
		arr=str_to_arr(arr, string)
	return(arr)

def max_len(lena, lenb):
	if lena> lenb:return(lena)
	return(lenb)

def append_min_arr(dop_len, min_arr):
	while dop_len:
		min_arr.append('X')
		dop_len-=1
	return(min_arr)

def print_file(A_arr, B_arr, C_arr, c_file, max_len):
	len = 70
	flag = 0
	flags = 0
	i=0
	while(i<max_len):
		counter = 0
		while counter <= len and i+counter<max_len:
			c_file.write(A_arr[counter+i])
			counter+=1
		counter = 0
		c_file.write('\n')
		while counter <= len+flag and i+counter<max_len+flag:
			if C_arr[counter+i+flags] == '*':
				flag += 1
			else:
				c_file.write(C_arr[counter+i+flags])
			counter+=1
		c_file.write(' '+str(counter+i))
		if flag >0:
			flags += flag
			flag =0
			c_file.write('<-------------')
			print(str(i//70+1)+' строка')
		counter = 0
		c_file.write('\n')
		while counter <= len and i+counter<max_len:
			c_file.write(B_arr[counter+i])
			counter+=1
		c_file.write('\n')
		i+=70
	print('поиск можно осуществить по указателю (<-------------)')
	return()

start_time = time.time()
interval = 20
counter = 0
counter1 = 0
counter_flags = 0
counter_x=0
str_counter = 0
A_arr=[]
B_arr=[]
C_arr=[]
len_A_arr=0
len_B_arr=0
print('введите количество несовпадений')
x=int(input())
with open('./a/sequence1.fasta') as a_file:
	with open('./b/sequence2.fasta') as b_file:
		with open('./c.txt','w+') as c_file:
			name_A=a_file.readline().rstrip()
			name_B=b_file.readline().rstrip()
			A_arr=file_in_arr(a_file)
			B_arr=file_in_arr(b_file)
			len_A_arr=len(A_arr)
			len_B_arr=len(B_arr)
			max_len=max_len(len_A_arr, len_B_arr)
			if max_len==len_A_arr:
				B_arr = append_min_arr(max_len-len_B_arr, B_arr)
			else:
				A_arr = append_min_arr(max_len-len_A_arr, A_arr)
			for i in range(0,max_len,1):
				if A_arr[i] == B_arr[i]:
					C_arr.append('|')
					counter+=1
					counter_x=0
				else:
					C_arr.append('x')
					counter1+=1
					counter_x+=1
				if counter_x>=x and i<=len_A_arr and i<=len_B_arr:
					counter_flags+=1
					counter_x=0
					C_arr.append('*')
			print(str(len_A_arr)+" "+str(len_B_arr))
			print('совпадение '+str(counter))
			print('не совпадение '+str(counter1))
			print(str(x)+' и более несовпадений подряд нашлось:'+str(counter_flags))
			print_file(A_arr, B_arr, C_arr, c_file, max_len)
print("--- %s seconds ---" % int(time.time() - start_time),end='')
os.system('start c.txt')
