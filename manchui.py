import random

manchui = 10007
surveyor = '권예원 김기빈 소정욱 현도도 조원경 정보경 김수현 오새윤 심은아'.split()
print(surveyor)
for i in range(manchui):
    r = random.randint(0,8)
    if i==manchui-1:
        print('*********축 당첨*********')
    print(surveyor[r])

