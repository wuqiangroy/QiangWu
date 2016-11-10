#!/usr/bin/env python
# -*- coding: utf-8 -*-

class person(object):
    def __init__(self, name):
        self.name = name

    def talk(self, words):
        print "{0}: \"{1}\"" .format(self.name, words)
