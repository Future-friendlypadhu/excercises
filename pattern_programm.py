def pattern(row):
    for i in range(0,row):
        for j in range(i):
            print('@',end="")
        print(" ")
pattern(5)        
