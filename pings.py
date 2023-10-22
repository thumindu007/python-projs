import os

hostname = input("What is the website to be pinged? ")

number_of_pings = int(input("How many times would this be pinged? "))

responce = os.system(f"ping -n {number_of_pings} {hostname}")

if responce == 0:
    print(f"\n\n{hostname} is up\n")
else:
    print(f"\n\n{hostname} is down\n")