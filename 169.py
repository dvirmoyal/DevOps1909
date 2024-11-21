import requests
from  time import sleep
try:
 responses = requests.get("httt/.bklakl")
except BaseException as e:
    print(f"something went wrong: {e.args}")
except ValueError:
    print("Value Error")
time_to_sleep = input("time to sleep in seconds: ")
sleep(time_to_sleep)

a = int(input("first: "))
b = int(input("second: "))
res = (a / b )
print(res)