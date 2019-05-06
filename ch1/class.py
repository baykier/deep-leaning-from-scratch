# coding: utf-8

class man:

    def __init__(self, name=None):
        self.name = name
        print('__init__')
    def hello(self):
        print("hello {}!".format(self.name))
    
    def goodbye(self):
        print("goodbye {}!".format(self.name))
        
bot = man('jack')
bot.hello()
bot.goodbye()