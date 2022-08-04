def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    easy_oper = ["+", "-", "*"]
    msg_local = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg_local += msg[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg_local += msg[7]
    if (v1 == 0 or v2 == 0) and v3 in easy_oper:
        msg_local += msg[8]
    if msg_local != "":
        print(msg[9] + msg_local)


msg = [
    "Enter an equation\n",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):\n",
    "Do you want to continue calculations? (y / n):\n",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)\n",
    "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
    "Last chance! Do you really want to embarrass yourself? (y / n)\n"
    ]

memory = 0

while True:
    calc = input(msg[0])
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg[1])
        continue

    check(x, y, oper)

    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        if y == 0:
            print(msg[3])
            continue
        else:
            result = x / y
    else:
        print(msg[2])
        continue

    print(result)

    answer = input(msg[4])
    while answer not in ["y", "n"]:
        answer = input(msg[4])
    if answer == "y" and is_one_digit(result):
        msg_index = 10
        while msg_index < 13:
            answer = input(msg[msg_index])
            while answer not in ["y", "n"]:
                answer = input(msg[msg_index])
            if answer == "y":
                msg_index += 1
            else:
                break
        if msg_index == 13:
            memory = result
    elif answer == "y":
        memory = result

    answer = input(msg[5])
    while answer not in ["y", "n"]:
        answer = input(msg[5])
    if answer == "y":
        continue
    else:
        break
