list1 = []
swappedlist = []
n=int(input("I'll give you an list to fill in. You can put inside this list whatever you want. However, first of all, how big do you want this list to be in size (that would be better if you could make it less than 5 :) "))

for i in range(0,n):
 list1.append(input("Please enter your input: "))
 
list1=list1[::-1]
print("This is the list that you've entered to the console in swapped order")
print(list1)

n=int(input("Now please enter a single digit number "))
print(f'Great you have entered {n}. Then I give you all the even numbers from 0 to {n}. They are:')
for i in range (0,n+1):
 
 if i%2==0:
  print(i)
