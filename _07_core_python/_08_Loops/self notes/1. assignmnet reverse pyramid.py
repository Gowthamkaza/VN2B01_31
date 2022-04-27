x=6
# Downward loop for inverse loop  
for i in range(0,x):
      # assign value to n of i after each iteration
    for j in range(i):
        # print reduced value in each new line  
        print(j, end=' ')
    print()
print("------------------------------")

x=6
# Downward loop for inverse loop
for i in range(x,0,-1):
    n = i   # assign value to n of i after each iteration
    for j in range(0, n):
        # print reduced value in each new line
        print(n, end=' ')
    print()