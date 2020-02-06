#引入module后也可以调用module内的变量
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics#使用self来明确内部的变量，防止与外部变量混淆
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# happy_bday = Song(['happy birthday to u','I donnot want to get sued','so I will stop right there'])
# bulls_on_parade = Song(['they rally around the family','with pockets full of shells'])
#
# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()
a = ['happy birthday']
happy = Song(a)
happy.sing_me_a_song()