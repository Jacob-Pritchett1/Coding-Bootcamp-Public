for i in range(0,151):
    print(i)

for index in range(5,1001,5):
    print(index)

for i in range(1,101):
    if i%5==0:
        print("Coding")
    else:
        print("Coding Dojo")

sum = 0
for i in range(0,500000):
    if i%2==1:
        sum = sum+i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum = 6
highNum = 600
mult = 100
for i in range(lowNum,highNum,mult):
    if i%mult==0:
        print(i)