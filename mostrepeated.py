string="engineering"
list1=[]
list2=[]
for i in string:
    if i not in list1:
        list1.append(i)
        list2.append(string.count(i))
occ=min(list2)
ele=list1[list2.index(occ)]
print(ele.occ)
