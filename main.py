# imports
import uuid
import time

x = input('times: ')
x = int(x)

t0 = time.time()

with open('ids','w') as f:
	while x > 0:
		e = uuid.uuid4()
		print(str(e)+' created')
		f.write(str(e)+'\n')
		x -= 1

t1 = time.time()
total = t1-t0

if total > 1:
	print('\n completed in '+str(total)+' seconds')
else:
	print('\n completed in '+str(total * 1000)+' miliseconds')
