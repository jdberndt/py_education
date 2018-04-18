x = [1,2,3,4,5,6]
y = []

for num in x:
	if num >3:
		y.append(num) 
	
print(x)
print(y)
f = open('myfile.txt', 'w')
f.write(str(x)+'\n'+str(y))
f.close()

g = open('myfile.txt')
h = g.readlines()
print(g)
print(h)
