
import random
import copy

# 分数
score = 0
# 开始界面
def start():
    list_2048 = [['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    ']]
    i = 0
    while i < 2:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if list_2048[y][x] == '    ':
            list_2048[y][x] = '%4d'%2
            i += 1
    return list_2048

# 将列表打印出游戏界面的效果
def print_number(li):
    for row in li:
        for number in row:
            print(number,end='|')
        print()

# down_step1 是将游戏界面里面所有的元素堆在下面，使中间没有空隙
def down_step1(old_list):
    while True:
        for x in range(3):
            for y in range(4):
                if old_list[x][y] != '    ' and old_list[x+1][y] == '    ':
                    old_list[x][y],old_list[x+1][y] = old_list[x+1][y],old_list[x][y]
        count = 0
        for y in range(4):
            judge_list = []
            for x in range(4):
                judge_list.append(str(old_list[x][y]))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old_list

# down_step2 是将上下相邻且相同的数字合并，因为是向下移动，故判断的时候是从下像上判断，这点很重要。
def down_step2(old_list):
    global score
    for x in range(4):   # 将前面处理好，挨着紧凑的数据来判断最后两项是否相同，若相同就将两项合并
        if old_list[3][x] != '    ' and old_list[3][x] == old_list[2][x]:
            old_list[3][x] = '%4d'%(int(old_list[3][x]) * 2)
            old_list[2][x] = '    '
            score += int(old_list[3][x])
            if old_list[1][x] != '    ' and old_list[1][x] == old_list[0][x]:
                old_list[1][x] = '%4d'%(int(old_list[1][x]) * 2)
                old_list[0][x] = '    '
                score += int(old_list[1][x])
        elif old_list[2][x] != '    ' and old_list[2][x] == old_list[1][x]:
            old_list[2][x] = '%4d'%(int(old_list[2][x]) * 2)
            old_list[1][x] = '    '
            score += int(old_list[2][x])
        elif old_list[1][x] != '    ' and old_list[1][x] == old_list[0][x]:
            old_list[1][x] = '%4d'%(int(old_list[1][x]) * 2)
            old_list[0][x] = '    '
            score += int(old_list[1][x])
    return old_list
'''
down 是中和两个步骤，然后在把处理完的元素堆在下面。
这里没有用循环处理，是因为要让玩家每操作一次，也只变动一次，
操作一次，而变动多次会使玩家捉摸不到游戏的规律性
'''
def down(old_list):
    judge_list = copy.deepcopy(old_list)
    old_list = down_step1(old_list)
    old_list = down_step2(old_list)
    old_list = down_step1(old_list)
    if judge_list == old_list:
        return old_list
    if old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0,3)
            y = random.randint(0,3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d'%2
                k += 1
    elif old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d'%2
                k += 1
    else:
        pass
    return old_list

def up_step1(old_list):
    while True:
        for x in range(3,0,-1):
            for y in range(4):
                if old_list[x][y] != '    ' and old_list[x-1][y] == '    ':
                    old_list[x][y],old_list[x-1][y] = old_list[x-1][y],old_list[x][y]
        count = 0
        for y in range(4):
            judge_list = []
            for x in range(4):
                judge_list.append(str(old_list[x][y]))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old_list
def up_step2(old_list):
    global score
    for x in range(4):   # 将前面处理好，挨着紧凑的数据来判断最后两项是否相同，若相同就将两项合并
        if old_list[0][x] != '    ' and old_list[0][x] == old_list[1][x]:
            old_list[0][x] = '%4d'%(int(old_list[0][x]) * 2)
            old_list[1][x] = '    '
            score += int(old_list[0][x])
            if old_list[2][x] != '    ' and old_list[2][x] == old_list[3][x]:
                old_list[2][x] = '%4d'%(int(old_list[2][x]) * 2)
                old_list[3][x] = '    '
                score += int(old_list[2][x])
        elif old_list[1][x] != '    ' and old_list[1][x] == old_list[2][x]:
            old_list[1][x] = '%4d'%(int(old_list[1][x]) * 2)
            old_list[2][x] = '    '
            score += int(old_list[1][x])
        elif old_list[2][x] != '    ' and old_list[2][x] == old_list[3][x]:
            old_list[2][x] = '%4d'%(int(old_list[2][x]) * 2)
            old_list[3][x] = '    '
            score += int(old_list[2][x])
    return old_list
def up(old_list):
    judge_list = copy.deepcopy(old_list)
    old_list = up_step1(old_list)
    old_list = up_step2(old_list)
    old_list = up_step1(old_list)
    if judge_list == old_list:
        return old_list
    if old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d'%2
                k += 1
    elif old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d'%2
                k += 1
    else:
        pass
    return old_list

def left_step1(old_list):
    while True:
        for x in range(4):
            for y in range(3,0,-1):
                if old_list[x][y] != '    ' and old_list[x][y-1]=='    ':
                    old_list[x][y],old_list[x][y-1] = old_list[x][y-1],old_list[x][y]
        count = 0
        for row in old_list:
            judge_list = []
            for number in row:
                judge_list.append(str(number))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old_list
def left_step2(old_list):
    global score
    for i in range(4):
        if old_list[i][0] != '    ' and old_list[i][0] == old_list[i][1]:
            old_list[i][0] = '%4d'%(int(old_list[i][0])*2)
            old_list[i][1] = '    '
            score +=int(old_list[i][0])
            if old_list[i][2] != '    ' and old_list[i][2] == old_list[i][3]:
                old_list[i][2] = '%4d'%(int(old_list[i][2])*2)
                old_list[i][3] = '    '
                score += int(old_list[i][2])
        elif old_list[i][1] != '    ' and old_list[i][1] == old_list[i][2]:
            old_list[i][1] ='%4d'%(int(old_list[i][1])*2)
            old_list[i][2] = '    '
            score += int(old_list[i][1])
        elif old_list[i][2] != '    ' and old_list[i][2] == old_list[i][3]:
            old_list[i][2] ='%4d'%(int(old_list[i][2])*2)
            old_list[i][3] = '    '
            score += int(old_list[i][2])
    return old_list
def left(old_list):
    judge_list = copy.deepcopy(old_list)
    old_list = left_step1(old_list)
    old_list = left_step2(old_list)
    old_list = left_step1(old_list)
    if judge_list == old_list:
        return old_list
    if old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d'%2
                k += 1
    elif old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d'%2
                k += 1
    else:
        pass
    return old_list

def right_step1(old_list):
    while True:
        for x in range(4):
            for y in range(3):
                if old_list[x][y] != '    ' and old_list[x][y+1]=='    ':
                    old_list[x][y],old_list[x][y+1] = old_list[x][y+1],old_list[x][y]
        count = 0
        for row in old_list:
            judge_list = []
            for number in row:
                judge_list.append(str(number))
            judge_str = ''.join(judge_list)
            judge_str = judge_str.strip()
            if '    ' in judge_str:
                break
            else:
                count += 1
        if count == 4:
            break
    return old_list
def right_step2(old_list):
    global score
    for i in range(4):
        if old_list[i][3] != '    ' and old_list[i][3] == old_list[i][2]:
            old_list[i][3] = '%4d'%(int(old_list[i][3])*2)
            old_list[i][2] = '    '
            score += int(old_list[i][3])
            if old_list[i][1] != '    ' and old_list[i][1] == old_list[i][0]:
                old_list[i][1] = '%4d'%(int(old_list[i][1])*2)
                old_list[i][0] = '    '
                score += int(old_list[i][1])
        elif old_list[i][2] != '    ' and old_list[i][2] == old_list[i][1]:
            old_list[i][2] ='%4d'%(int(old_list[i][2])*2)
            old_list[i][1] = '    '
            score += int(old_list[i][2])
        elif old_list[i][1] != '    ' and old_list[i][1] == old_list[i][0]:
            old_list[i][1] ='%4d'%(int(old_list[i][1])*2)
            old_list[i][0] = '    '
            score += int(old_list[i][1])
    return old_list
def right(old_list):
    judge_list = copy.deepcopy(old_list)
    old_list = right_step1(old_list)
    old_list = right_step2(old_list)
    old_list = right_step1(old_list)
    if judge_list == old_list:
        return old_list
    if old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') >= 2:
        k = 0
        while k < 2:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d' % 2
                k += 1
    elif old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') == 1:
        k = 0
        while k < 1:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if old_list[y][x] == '    ':
                old_list[y][x] = '%4d' % 2
                k += 1
    else:
        pass
    return old_list

# 启动游戏

old_list = start()
print_number(old_list)

while True:
    # 根据用户输入做出相应的移动
    print()
    user_input = input('请输入你要移动的方向[上(w)下(s)左(a)右(d)]:')
    print()
    if user_input == 'w':
        old_list = up(old_list)
        print_number(old_list)
        print()
        print('目前得分：%d 分'%score)
    elif user_input == 's':
        old_list = down(old_list)
        print_number(old_list)
        print()
        print('目前得分：%d 分' % score)
    elif user_input == 'a':
        old_list = left(old_list)
        print_number(old_list)
        print()
        print('目前得分：%d 分' % score)
    elif user_input == 'd':
        old_list = right(old_list)
        print_number(old_list)
        print()
        print('目前得分：%d 分' % score)
    else:
        print()
        print('输入错误！请输入正确的方向！')
        print_number(old_list)
    # 游戏的终止条件
    # 判断界面是否还有空位
    if old_list[0].count('    ') + old_list[1].count('    ') + old_list[2].count('    ') + old_list[3].count('    ') == 0:
        # 判断每一个数相邻是否还有相同的数字
        count = 0
        for i in range(4):          # 判断横排
            for j in range(3):
                if old_list[i][j] == old_list[i][j+1]:
                    count += 1
        for x in range(4):
            for y in range(3):
                if old_list[y][x] == old_list[y+1][x]:
                    count += 1
        if count == 0:
            print('很遗憾，游戏结束！')
            print('您的最终得分：%d 分' % score)
            break