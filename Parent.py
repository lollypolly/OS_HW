#!/usr/bin/python3

# Mokeeva Polina 11-902

import os
import sys
import random

if(len(sys.argv) < 2):
        print("Error!");
        os._exit(1);

n = int(sys.argv[1]);
for i in  range (0, n):
        child = os.fork();
        if (child > 0):
                if(i == 0):
                        print("The Parent process is PID = %d" % (os.getpid()));        
        else:
                os.execl('./Child.py', 'Child.py', str(random.randint(5, 10)))
                break;
for i in range (0, n):
        answer = os.wait();
        print("The Child procces (PID = %d) was completed" % (answer[0]));
        print("Status: %d" % (answer[1]));


 	
 	

