# Write a program using a for loop that calculates 
# the sum of even numbers between 1 and 100.
answer=0
for i in range(1,100,1):
    if i%2==0 and i<100:
        answer+=i

print("Sum of EVEN numbers between 1 & 100: ",answer)
        