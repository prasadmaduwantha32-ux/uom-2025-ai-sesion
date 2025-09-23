def get_product(num):
    for x in range(2,num//2+1):
        for y in range(2,num//2+1):
            if x**2+y**2==(num-x-y)**2:
                return x*y*(num-x-y)
            
    return

print(get_product(1000))
