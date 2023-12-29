import sys

instance_type = sys.argv[1]

if instance_type == 't2.micro':
    print("you will be charged 1$ per hour")
elif instance_type == 't3.micro':
    print("you will be cahrged 2$ per hour")
elif instance_type == 't2.large':
    print("you will be charged 3$ per day")
else:
    print("invalid input")