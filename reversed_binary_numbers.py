from sys import exit

val = raw_input()
try:
    val = int(val)
except ValueError as e:
    exit(e)
try:
    if val <= 1000000000 and val >=1:
        print int(bin(val)[:1:-1], 2)
    else:
        raise Exception("Value not within 1 and 1,000,000,000")
except Exception as e:
    exit(e)