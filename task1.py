from subprocess import*
import datetime
import numpy as np

commands = [
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
]

durations=[];

for cmnd in commands:
    #collecting srart time
    start = datetime.datetime.now()
    #execute one specific command
    pid = Popen(cmnd)
    pid.poll()
    #collecting end time
    e = datetime.datetime.now()
    #calculating execution time and store it in a list
    durations.append(end - start)
    
print('Average: %f' %(np.mean(durations)))
print('Maximum: %f' %max(durations))
print('Minimum: %f' %min(durations))
