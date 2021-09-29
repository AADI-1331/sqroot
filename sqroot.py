#Hints:
#If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
#In case of input data being supplied to the question, it should be assumed to be a console input. 


#!/usr/bin/env python
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]

for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)
