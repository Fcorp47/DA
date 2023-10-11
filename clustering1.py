import random
lt = [2, 5, 3, 12, 4, 8, 17, 19, 15, 13, 21]
lt2 = []
lt3 = []
lt4 = []
#num2 = input("Enter Number into: ")
#num2 = int(num2)
#for j in range(num2):
#    n = input("Enter the Number: ")
#    n = int(n)
#    lt.append(n)
print(lt)
k = input("Enter the number of k you want: ")
k = int(k)
random.shuffle(lt)
for i in range(0,len(lt),k):
    lt1 = lt[i:i + k]
    total = sum(lt[i:i+k])
    mean = total/ len(lt[i:i+k])
    lt2.append(lt1)
    lt3.append(mean)
lt3 = tuple(lt3)
print(lt2)
print(lt3)
print("----------------------------------------------------------------------------------------")
for j in range(len(lt3)):
    for i in range(len(lt2)):
        if(lt3[i]+3>=lt[i] and lt3[j]-3<=lt[i]):
            lt4.append(lt2[i])
            lt2 = []
print(lt4)
