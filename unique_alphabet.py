s='abcada'
seen =""
count =0
for char in s:
    if char not in seen:
        seen += char
        count +=1
   # print(seen)
    else:
        pass
print(len(seen))
print(count)
