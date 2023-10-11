num = input("Enter number: ")
lt = []
n1 = int(num)
count = 0
for i in range(n1):
    n = input("Enter the Name: ")
    lt.append(n)
c = input("Enter the char: ")
for j in range(len(n)):
    if(c == n[j]):
        count = count + 1
print(count)
