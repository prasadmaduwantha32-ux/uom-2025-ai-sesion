def m_of_3and5(number):
    summ=0
    for x in range(1,number):
        if x%3==0 or x%5==0:
            summ+=x
    return summ
print(m_of_3and5(1000))
