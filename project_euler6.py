def GDSS(num):
    total=0
    ssum=0
    for dig in range(1,num+1):
        total+=dig
        ssum+=dig**2

    return total**2-ssum

print(GDSS(100))

