import torch

# Example taken from first few lines of https://people.sc.fsu.edu/~jburkardt/data/cnf/aim-50-1_6-yes1-4.cnf
## Main source: https://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.htm
# a b d 0
# -b c d 0
# -b -c d 0
A = [[1,1,0,1,0],
	 [0,-1,1,1,1],
	 [0,-1,-1,1,2],
	 [1,0,0,0,0],
	 [0,0,0,0,1]]
A = [[1,1,0,1,0],
	 [0,-1,1,1,1],
	 [0,-1,-1,1,2],
	 [0,0,0,-1,1],
	 [0,0,0,0,1]]
A = [[1,0,0,0],
	 [1,1,0,0],
	 [0,0,1,0],
	 [1,1,1,1]]
# B = [[1],[1],[1]]
def is_decimal(tensor):
	if(torch.all(tensor.long()==tensor)):
		return False
	else:
		return True
A = torch.Tensor(A)

# C = [[1],[1],[1],[1],[1]]
C = [[1]]*A.shape[0]
def getRanges(row):
	global A
	return range(1,torch.sum(A[row]!=0)+1)
# B = torch.Tensor(B)
C = torch.Tensor(C)

# vals = range(1,3)
# print(getRanges(0))
# print(getRanges(1))
# print(getRanges(2))
# print(getRanges(3))
# print(getRanges(4))
# quit()
def calcVal(mat):
	cnt = 0
	for x in mat:
		if(x==0.0 or x==1.0):
			continue
		cnt+=max(0-x,1-x)
	return int(cnt)
def DiffRet(a,b):
	return torch.sum((b-a))
def printMe(a,b,c,d):
	C = [[a],[b],[c],[d]]
	C = torch.Tensor(C)
	# print(torch.mm(B,A))
	# print(torch.inverse(A))
	ret = (torch.mm(torch.inverse(A),C))
	# if(not is_decimal(ret)):
	print(a,b,c,d)
	print(ret)
	print("Val",calcVal(ret))
	return ret
	# print(list(x for x in ret))
	# print(is_decimal(ret))
ret2 = printMe(1,1,1,1)
ret3 = printMe(1,2,1,1)
ret3 = printMe(1,3,1,1)
print(DiffRet(ret2,ret3))