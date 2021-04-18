#algoritmo de euclides

def mdc(a,b):
	r = a % b
	while (r!=0):
		a = b
		b = r
		r = a % b
	return b

print("Digite o valor de a:")
a = int(input())
print("Digite o valor de b:")
b = int(input())

print("O mdc({:d}, {:d}) = {:d}".format(a,b,mdc(a,b)))
