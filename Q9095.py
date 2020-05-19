a = int(input())

def cal(num):
    case = []
    count = 1
    for i in range(num):
        case.append(1)
    pop = []
    print(case)

    while (True):
        temp = case.pop()
        print(case)
        pop.append(temp)

        if num < 4:
            if len(pop) == 1:
                count += len(case)
            if len(pop) == 2:
                count += (len(case) * 2)
            if len(case) == 0:
                break
        else:
            if len(pop) == 1:
                count += len(case)
                print(count)
            else:
                if (len(case)*2) == num:
                    count += len(case)
                    print(count)
                elif (len(case) * 3) < num:
                        break
                else:
                    count += (len(case)*2)
                    print(count)


    return count

for k in range(a):
    num = int(input())
    print(cal(num))

