import random
for i in range (1,100000):
    x = random.randint(0,30)
    y = random.randint(0,30)
    error = random.randint(-1,1)
    op = random.randint(6,7)
    def eval(x,op,y):
        if op == 6:
            return x + y
        if op == 7:
            return x - y
    result = eval(x,op,y) + error
    if op == 6:
        print(str(x) + ' + ' + str(y) + ' = ' + str(result))
    if op == 7:
        print(str(x) + ' - ' + str(y) + ' = ' + str(result))
    answer = int(input("Nhập 0 nếu đây là phép tính sai, 1 nếu đây là phép tính đúng: "))
    if answer == 1 and error == 0:
        print("Đúng rồi, điểm của bạn là: ", i)
        continue
    elif answer == 0 and error != 0:
        print("Đúng rồi, điểm của bạn là: ", i)
    else:
        print("Game over, điểm của bạn là ", i)
        break

