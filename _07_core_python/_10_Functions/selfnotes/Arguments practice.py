print("--------3. Keyword arguments-------------")


def sum(n1, n2, n3):
    res1 = n1 + n2 + n3
    print(res1)


sum(15, 30, 40)


def sum3(n1=45, n2=25, n3=45):
    res2 = n1 + n2 + n3
    # return res2
    print(res2)


sum3()
