""" 
# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

```text
file file image file image data
```

### Output:

```text
file file(1) image file(2) image(1) data
```

"""
n=input("Input:")
a=n.split()

rep=""

for i in range(len(a)):
    count = 0
    for j in range(0,i):
        if a[i]==a[j]:
            count +=1
    if count>0:
        rep = rep + a[i] +"("+ str(count) +")" + " "
    else:
        rep = rep + a[i] + " "


print(rep)