import time
spaces=' '*50
s =' '*50

print(' \r' +s + 'CAUTION --->Launching Jarvis', end='')
time.sleep(1)
for i in range(3,-1,-1):
    print(' \r' +s +  f"{i}" + spaces, end='')
    time.sleep(1)

print(' \r' +s + 'Hello, I am Jarvis' + spaces, end='')

time.sleep(2)

print(' \r' +s + 'Welcome Here'+ spaces, end='')

# time.sleep(1.5)

# print(' \r' +s + 'Here' + spaces, end='')

