


# s = input("Enter string = ")

# s1 = ""


# for i in range(len(s)):
    
#     count = 0
#     if s[i] not in s1:
#         s1 = s1 + s[i]
#         for j in range(len(s)):
#             if s[i] == s[j]:
#                 count = count+1
                
#         else:
#             print(s[i]," ->",count,end=", ")

# arr = [11,3,5,5,11]

# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if arr[i]==arr[j]:
#             del arr[j]
#             break
        
# print(arr)

arr = [11,17,26,87,87,17]

largest = 0
secLargest = 0

for ch in arr:
    if ch> largest:
        largest = ch

for ch in arr:
    if ch > secLargest and ch != largest:
        secLargest = ch

print(secLargest)

                

