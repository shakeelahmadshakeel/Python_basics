# a=[]

def prime_ck(nums):
    # counter=0 gives diff ans empty list
    a = []  # no change
    b = []
    for num in range(1, nums + 1):
        counter = 0
        # a=[] gives empty list
        for i in range(1, num + 1):
            # counter=0 gives empty list
            if num % i == 0:
                counter = counter + 1
                # print(i)
                # a.append(i)
                # i+=1
        if counter == 2:
            a.append(num)
            print("num is Prime", i)
            # print(a)
        else:
            b.append(num)
            print("num is not Prime", i)
    print("numbers are prime in list", a)
    print(len(a))


prime_ck(100)




