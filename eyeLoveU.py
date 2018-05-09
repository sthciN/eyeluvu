# --*-- encoding: utf-8 --*--
from easygui import msgbox
import time
import DWords
import random
def eyeloveu():
    # words, meanings = DWords.text_get()
    wordDict = DWords.text_get()
    while True:
        time.sleep(800)
        word = random.choice(wordDict.keys())
        meaning = wordDict[word]
        msgbox(msg='Liebe deine Augen!\n\n\n{}\n\n{}'.format(str(word), str(meaning)), title='EyeLoveU', ok_button='OK', image=None, root=None)

eyeloveu()
