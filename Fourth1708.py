lt = [["Laptop","Printer","Tablet","Headset"],
      ["Printer","Moniter","Tablet"],
      ["Laptop","Printer","Tablet","Headset"],
      ["Laptop","Moniter","Tablet","Headset"],
      ["Printer","Moniter","Tablet","Headset"],
      ["Printer","Tablet","Headset"],
      ["Moniter","Tablet"],
      ["Laptop","Printer","Moniter"],
      ["Laptop","Tablet","Headset"],
      ["Printer","Tablet"]]
lt1 = []
lt2 = []
#list of uniqe item and their feq
for i in lt:
    for j in i:
        if j not in lt1:
            lt1.append(j)
            lt2.append(1)
        else:
            ind = lt1.index(j)
            lt2[ind] += 1
print(lt1)
print(lt2)
print("------------------------------------------------------------------------------------------")
#Remove the non feq items

for r in lt2:
    if (r <= 3):
        lt1.remove(lt1[r])
        lt2.remove(lt2[r])
print(lt1)
print(lt2)
print("------------------------------------------------------------------------------------------")
#comibination
lt3 = []
lt4 = []
x=0
while(x<len(lt1)):
    y = x+1
    while(y<len(lt1)):
        lt4.append(lt1[x])
        lt4.append(lt1[y])
        y = y + 1
        lt3.append(lt4)
        lt4 = []
    x = x + 1
print(lt3)
print("------------------------------------------------------------------------------------------")
#count comibination
ct = 0
lt5 = []
for i in lt3:
    n1 = i[0]
    n2 = i[1]
    for j in lt:
       if((n1 in j) and (n2 in j)):
            ct = ct + 1
    lt5.append(ct)
    ct = 0
print(lt5)
print("------------------------------------------------------------------------------------------")
#final list
flt = []
fltc = []
k = 0
while(k<len(lt5)):
    if(lt5[k]>3):
        flt.append(lt3[k])
        fltc.append(lt5[k])
    k= k+1
print(flt)
print(fltc)
print("------------------------------------------------------------------------------------------")
