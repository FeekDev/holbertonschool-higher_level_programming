#!/usr/bin/python3
# obtained range and iteration and separated
for i in range(0, 100):
    if i != 99:
        print(f"{int(i/10)}{i%10}", end=", ")
# not separated the last number
    else:
        print(f"{int(i/10)}{i%10}")
