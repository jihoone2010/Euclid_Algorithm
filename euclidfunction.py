print("\n")

a, b = map(int, input("I shall tell you the gcd of two integers a and b. You shall type your a,b: ").split(','))

print("\n")

small = a
big = b
if a>b:
    small = b
    big = a

def euclidal(a, b):
    small = a
    big = b
    if a>b:
        small = b
        big = a
    
    ablist = []
    rd = 1

    while True:
        pastrd = rd
        pastbig = big
        rd = big%small
        multiple = int((big-rd)/small)
        big = small
        small = rd

        ablist.append([pastbig, big, rd, multiple])

        if rd == 0:
           return ablist, pastrd
        
process, gcd = euclidal(a, b)

print("\n")



print("gcd process: ")

print("\n")

for i in process:
    print(i[0], "=", i[1],"*",i[3], "+", i[2])

print("\n")

print(f"the gcd of {a} and {b} is {gcd}")

print("\n")








   

