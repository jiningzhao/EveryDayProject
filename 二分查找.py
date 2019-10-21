def binary_searth(list,item):
    low = 0
    high = len(list)-1

    while high >= low :
        mid = (high+low)//2
        guess = list[mid]

        if guess == item:
            print(guess)
            return guess
        elif guess > item:
            print(guess)
            high = mid - 1
        else:
            print(guess)
            low = mid + 1

def list(num):
    k = []
    for i in range(num):
        k.append(i)
    print(k)
    return k

item=int(input("请输入一个数："))
num=int(input("请输入要查找的范围："))
print(binary_searth(list(num),item))