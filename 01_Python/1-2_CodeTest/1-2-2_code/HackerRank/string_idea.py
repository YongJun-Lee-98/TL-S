# string의 특정 문자열을 추출

s = '11:15:00PM'
time, type_time = s[:-2], s[-2:]

# 24시간으로 할 경우 hh:mm:ss로 만들때 앞에 0을 붙여줘야함 이경우 zfill()을 사용
hour = int(time[:2])
print(hour)

hour = str(hour).zfill(2) # 05
print(type(hour))
other = "111J"

print(f"{hour} {other}")

"""
Answer code
---
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time, type_time = s[:-2], s[-2:]
    hour = int(time[:2])
    other = time[2:]
    
    if type_time == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    hour = str(hour).zfill(2)
    return f"{hour}{other}"
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

"""