import numpy

def s(N):
	s_out=0
	for i in range(1,N):
		s=(((-1)**i)*(1/(2**i)))
		print('intermediate value: '+str(s))
		s_out=s+s_out
	return s_out+1
	
print("programm is start...")
try:
	N=int(input())
except ValueError:
	print("ERR")

print("Out value: "+str(s(N)))