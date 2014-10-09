import u12
import time
import numpy as np


d = u12.U12()

for i in range(0,10,1):
    if np.mod(i,2) == 0:
        d.eAnalogOut(analogOut0=0,analogOut1=3)
    else:
        d.eAnalogOut(analogOut0=3,analogOut1=0)
    time.sleep(1)
d.eAnalogOut(analogOut0=0,analogOut1=0)