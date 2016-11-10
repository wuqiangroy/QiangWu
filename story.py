#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from person import person
from choice import choice
class story(object):
    def __init__(self, name):
        self.name = name


    def wait(self, second):
        time.sleep(second)

    def intro(self):
        John = person('John')
        Liz = person('Liz')
        print "{0}和{1},就读于成都七中，同时，他们还是一对恩爱的恋人。" .format(John.name, Liz.name)

    def begin(self):
        John = person('John')
        Liz = person('Liz')
        print '''
        =============成都七中============
        '''
        Liz.talk('我收到清华录取通知书了。')
        time.sleep(2)
        John.talk("我没有考上……我和你一起去北京吧，我打工养你！")
        time.sleep(2)
        Liz.talk('嗯嗯，我爱你~')

    def interview(self):
        Peter = person('Peter')
        Liz = person('Liz')
        print '''
        =============4年过去了============
                     {0}毕业了
                ''' .format(Liz.name)
        Liz.talk('您好，这是我的简历。')
        time.sleep(2)
        Peter.talk('非常不错，很高兴你能加入我们公司！')
        time.sleep(2)
        Liz.talk('谢谢您，很高兴以后能够一起共事！')

    def before_break_out(self):
        Peter = person('Peter')
        Liz = person('Liz')
        John = person('John')
        print '''
        =============几个月之后============
              '''
        print '''下班前夕。
        '''
        print "{0} 说：“Hi,{1},今晚有空吗？我带你去一个很棒的餐厅。”" .format(Peter.name, Liz.name)
        time.sleep(2)
        Liz.talk("好啊，简直不能更棒！")
        time.sleep(2)
        print '''
        {0}打电话给{1}
        ''' .format(John.name, Liz.name)
        John.talk("亲爱的，咱们一起去看《复仇者联盟》吧。")
        time.sleep(2)
        Liz.talk("对不起亲爱的，我已经约人了，下次吧。")
        time.sleep(2)
    def break_out(self):
        Liz = person('Liz')
        John = person('John')
        print "{0}与{1}貌合神离，在{0}的悲痛之中他们分手了" .format(John.name, Liz.name)

    def study_further(self):
        John = person('John')
        print '''
        {0}异常难受，他决定要振作自己。
        {0}选择报名python学习班，
        每天早上7点开始学习，一直学习到晚上1点。
        终于他成功就职一家互联网公司。
        在互联网公司里面他顺风顺水，一直踏踏实实干活。
        ……
        ''' .format(John.name)
    def meet(self):
        John = person('John')
        Liz = person('Liz')
        Peter = person('Peter')
        print '''
        =============五年之后============
        {0}成功当上了IT总监，月薪5w。
        在北京买了车买了房。
        在一次逛街中，他偶遇了{1}
        ''' .format(John.name, Liz.name)
        print "{0}说：“Hi，{1}，好久不见！”" .format(Liz.name, John.name)
        time.sleep(2)
        print "{0}说：“{1},好久不见！最近好吗？”" .format(John.name, Liz.name)
        time.sleep(2)
        print "{0}说：“和你分手以后，我就和{1}在一起了，但是没想到他是一个结过婚的人。”" .format(Liz.name, Peter.name)
        time.sleep(2)
        Liz.talk("在矛盾和纠结中过了2年，我和他分手了。")
        time.sleep(2)
        Liz.talk("现在我在投行工作，累是累了一点，但是毕竟薪水还不错，过的还算很好。你呢？")
        time.sleep(2)
        John.talk("分手之后，在度过那段自我否定的时期之后，我报了一家互联网培训公司。")
        time.sleep(2)
        John.talk("现在在阿里做IT总监，也算过得很好吧。")
        time.sleep(2)
        print "{0}说：“看到你过的这么奋进，我真是为你感到高兴。这么多年，我对不起你……和{1}之后，我也没有再找了。”" .format(Liz.name, Peter.name)
        time.sleep(2)
        John.talk("虽然到现在我已经平淡了，但是老实说还是得感谢你，你把我刺激了，让我知道了要努力才能走到更高一步。")
        time.sleep(2)
        John.talk("我也单身，这么多年很忙没时间找。")
        time.sleep(2)
        Liz.talk("那咱们，我只是问一下，还可能吗？")
        time.sleep(2)



