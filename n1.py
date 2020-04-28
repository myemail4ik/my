def appender(old,current):
	if current>1:
		return str(old)+str(current)+' '
	else:
		return str(old)+' '

def func(input_str):
	old=input_str[0]
	counter=0
	out_str=''
	for i in input_str:
		if str(i)==str(old):
			counter+=1
			old=i
		else:
			out_str=out_str+appender(old,counter)
			counter=1
			old=i

	out_str=out_str+appender(old,counter)
	return out_str			



input_str='AAAABBYKYYBBBBAAAAAAAAAAAAAAB' # преобразовать в 'A4 B2 Y K Y2 B4 A14 B'
print(func(input_str))
print('otvet')
print('A4 B2 Y K Y2 B4 A14 B')