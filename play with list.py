L = [4, 5, 1, 2, 9, 7, 10, 8]
print(f"Original List : {L}")

count = 0 

for i in L:
    count = count + i
    
avg = count/len(L)

print("Sum = ", count)
print("Average =", avg)

L.sort()
print(L)

print("Smallest element is:", L[0])

print("Largest element is:", L[-1])