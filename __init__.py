#!/usr/bin/env python
# -*- coding: utf-8 -*-
from story import story
from person import person
from choice import choice
import time
import sys



if __name__ == '__main__':

    story = story('John')
    choice = choice()
    John = person('John')
    Liz = person('Liz')
    story.intro()
    story.begin()
    choice.choice1()
    story.interview()
    story.before_break_out()
    choice.choice2()
    story.break_out()
    story.study_further()
    story.meet()
    choice.choice3()



