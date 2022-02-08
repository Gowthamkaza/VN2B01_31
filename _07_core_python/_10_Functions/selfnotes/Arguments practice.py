print("--------3. Keyword arguments-------------")

def sum(n1,n2,n3):
    res1=n1+n2+n3
    print(res1)

sum(15,30,40)

def sum(n1=15,n2=25,n3=45):
    res2=n1+n2+n3
    return res2
sum()

