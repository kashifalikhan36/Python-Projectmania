def add(num_1, num_2):
    return num_1+num_2


def sub(num_1, num_2):
    return num_1-num_2


def mul(num_1, num_2):
    return num_1*num_2


def dev(num_1, num_2):
    return num_1/num_2


def calc(num_1, num_2,fun):
    if fun == "add":
        return add(num_1, num_2)

    elif fun == "sub":
        return sub(num_1, num_2)

    elif fun == "mul":
        return mul(num_1, num_2)

    elif fun == "dev":
        return dev(num_1, num_2)


while True:
    fun = input("Choose that what do u want to do (add,sub,mul,dev) --->").lower()
    num_1 = int(input("The First No.--->"))
    num_2 = int(input("The Second No.--->"))
    print(calc(num_1,num_2,fun))
    end = input("do u want to do again(Yes/No) ---->").lower()
    if end == "yes":
        continue
    elif end == "no":
        break
