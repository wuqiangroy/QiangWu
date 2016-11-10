#!/usr/bin/env python
# -*- coding: utf-8 -*-

from person import person
import time

class choice(object):
    def __init__(self):
        pass
    def choice1(self):
        John = person('John')
        c1 = raw_input("1.做网管，工资2000 \n2.做洗碗工，工资1800\n>>>  ")
        if c1 == 1:
            print "{0}选择做一名网管，工资每月2000元。" .format(John.name)
        else:
            print "{0}选择做一名洗碗工，工资每月1800元。" .format(John.name)

    def choice2(self):
        John = person('John')
        Liz = person('Liz')
        Peter = person('Peter')
        print "是否选择质问{0}约了谁？" .format(Liz.name)
        c1 = int(raw_input("1.问一下吧，最近感觉她一直不正常。\n2.情侣间相互的信任都没有了么？不问 \n>>>  "))
        if c1 == 1:
            John.talk("约了谁啊？")
            time.sleep(2)
            print"{0}说：“{1},就是我们CEO，人又高又帅，今晚说带我去一家很棒的餐厅。”" .format(Liz.name, Peter.name)
            time.sleep(2)
            print "{0}说：“{1},你！你！你！……为什么不告诉我？为什么选择他？”" .format(John.name, Liz.name)
            time.sleep(2)
            Liz.talk("五年的感情，我怕伤害你。在北京，没钱的日子我过怕了，我渴望钱。")
            time.sleep(2)
            Liz.talk("我渴望名牌化妆品、渴望名牌包包、渴望名牌鞋子，光靠咱俩这辈子都不可能。")
            time.sleep(2)
            print "{0}说：“然而，{1}能带给我，他能快速让我享受这一切。对不起，我……”" .format(Liz.name, Peter.name)
            time.sleep(2)
            print '''
            {0}还说了些什么，{1}没有听清，他只知道，他给不了{0}所要的一切，他痛苦、迷茫。
            世界真的要塌了。
            没有了{0}，{1}的世界也没了。
            ''' .format(Liz.name, John.name)
        else:
            pass

    def choice3(self):
        John = person('John')
        Liz = person('Liz')
        print "是否选择和{0}在一起？" .format(Liz.name)
        c3 = int(raw_input("1.依旧忘不了曾经的她，在一起。\n2.劈腿的女人不值得，还有更好的。\n>>>  "))
        if c3 == 1:
            John.talk("这么多年，我心里一直有你，一直等你回来。")
            time.sleep(2)
            print "{0}和{1}幸福的在一起。" .format(John.name, Liz.name)
        else:
            John.talk("我的伤痛依旧，对不起，我们还是做朋友吧。")
            time.sleep(2)
            print "{0}转身离开，留下一身的骄傲。" .format(John.name)