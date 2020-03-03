import numpy

def s(N):
	s_out=0
	for i in range(0,N):
		i=i+1
		s=((i+1)/i)
		print('intermediate value: '+str(s))
		s_out=s+s_out
	return s_out

print("programm is start...")
try:
	N=int(input())
except ValueError:
	print("ERR")

print("Out value: "+str(s(N)))