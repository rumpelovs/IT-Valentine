import time
from colorama import init, Fore

import time

def love_confession():
    message = "Ты знаешь, я всегда нахожу удовольствие в программировании, поэтому сегодня я решил использовать Python, чтобы кое что сказать тебе и удивить тебя!"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.04)
    

    message2 = " Ты - самая прекрасная и удивительная девушка, которую я когда-либо встречал."
    for char in message2:
        print(char, end='', flush=True)
        time.sleep(0.06)
   

    message3 = " Твоя улыбка заставляет мое сердце биться быстрее, а твой голос звучит как мелодия."
    for char in message2:
        print(char, end='', flush=True)
        time.sleep(0.06)
    
    message4 = " Когда я вижу тебя, моя душа наполняется радостью, а мои мысли о тебе заполняют каждый уголок моего разума. Ты - воплощение красоты и нежности, и я не могу удержаться от того, чтобы не сказать тебе правду - ты безумно мне нравишься!"
    for char in message4:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    message5 = " Каждый момент, проведенный с тобой, становится незабываемым!"
    for char in message5:
        print(char, end='', flush=True)
        time.sleep(0.06)
  
love_confession()
