# -*- encoding: utf-8 -*-
# @Time    :   2024/02/10 12:58:16
# @File    :   main.py
# @Author  :   CYZ
# @Contact :   ciao_yizhen@163.com
# @Function:   刘谦魔术程序版

import random
from pydantic import BaseModel
from enum import Enum

class Sex(str, Enum):
    男 = "男"
    女 = "女"
    
class Area(str, Enum):
    南方人 = "南方人"
    北方人 = "北方人"
    不确定 = "不确定"

class InputParams(BaseModel):
    name:str
    sex:Sex
    area:Area
    
name = input("请输入你的名字:")
sex = input("请输入你的性别(请输入'男' or '女'):")
area = input("请输入你认为你是南方人或者北方人(请输入'北方人' or '南方人' or '不确定'):")

while True:
    input_params = {"name": name, "sex": sex, "area":area}
    try:
        InputParams(**input_params)
        break
    except:
        print("您的入参不正确，请重新输入")
        name = input("请输入你的名字:")
        sex = input("请输入你的性别(请输入'男' or '女'):")
        area = input("请输入你认为你是南方人或者北方人(请输入'北方人' or '南方人' or '不确定'):")

# 随机生成卡牌
card = [i for i in range(1, 14)]
random.shuffle(card)
card = card[:4]

# 撕一半 然后将一半放最下面
new_card = []
for index in range(1, 3):
    for item in card:
        new_card.append(str(item) + "_" + str(index))
assert len(new_card) == 8, "error"

def throwFirstCard(card:list) -> list:
    """_summary_
    丢出去最上方的卡牌

    Args:
        card (list): 当前的卡牌堆

    Returns:
        list: 返回处理后的卡牌
    """
    del card[0]
    return card

def pickFirstCardToEnd(card:list) ->list:
    """_summary_
    拿起最上方的一张卡 放到最后

    Args:
        card (list): 当前的卡牌堆

    Returns:
        list: 返回处理后的卡牌
    """
    first_card = card[0]
    card.append(first_card)
    del card[0]
    return card

def pickTopCardInsertCenter(n:int, card:list) -> list:
    """_summary_
    拿起上方的n张卡 插入到中间去

    Args:
        n (int): 上方几张卡
        card (list): 当前的卡牌堆

    Returns:
        list: 返回处理后的卡牌
    """

    top_card = card[:n]
    for i in range(n):
        del card[0]
    
    insert_index = random.randint(1, len(card) - 2)  # -2 是因为 一个是不能插入到尾巴(尼格买提失败的原因) 一个是因为0开始数的原因
    for i in range(n):
        temp = top_card.pop()  # 反着插入 这样insert_index不需要修改
        card.insert(insert_index, temp)
    return card

# 根据名字往下放几张拍
length = len(name)
for i in range(length):
    new_card = pickFirstCardToEnd(new_card)
    
    
# 拿起最上面三张,插入到中间序
new_card = pickTopCardInsertCenter(3, new_card)

# 收起最上面的一张卡
secret_card = new_card[0]
del new_card[0]

# 根据南方人拿起一张 北方人拿起两张
match area:
    case "南方人":
        n = 1
    case "北方人":
        n = 2
    case "不确定":
        n = 3
        
new_card = pickTopCardInsertCenter(n, new_card)

# 根据男生拿起一张 女生拿起两张
match sex:
    case "男":
        n = 1
    case "女":
        n = 2
        
# 卡牌丢出去
for i in range(n):
    throwFirstCard(new_card)
    
# 念咒语环节
incantation = "见证奇迹的时刻"
for item in incantation:
    print(item)
    new_card = pickFirstCardToEnd(new_card)
    

# 好运留下来 烦恼丢出去环节
while len(new_card) != 1:
    print("好运留下来")
    new_card = pickFirstCardToEnd(new_card)
    print("烦恼丢出去")
    new_card = throwFirstCard(new_card)

print("留下的最后两张牌是:")
print(new_card[0], secret_card)



    
