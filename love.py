import time
import turtle
import math

import time

def love_confession():
    message = "Ты знаешь, я всегда нахожу удовольствие в программировании, поэтому сегодня я решил использовать Python, чтобы кое что сказать тебе и удивить тебя!"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.04)
    

    message2 = " Ты - самая прекрасная и удивительная девушка, которую я когда-либо встречал."
    for char in message2:
        print(char, end='', flush=True)
        time.sleep(0.04)
   

    message3 = " Твоя улыбка заставляет мое сердце биться быстрее, а твой голос звучит как мелодия."
    for char in message3:
        print(char, end='', flush=True)
        time.sleep(0.04)
    
    message4 = " Когда я вижу тебя, моя душа наполняется радостью, а мои мысли о тебе заполняют каждый уголок моего разума. Ты - воплощение красоты и нежности, и я не могу удержаться от того, чтобы не сказать тебе правду - ты безумно мне нравишься!"
    for char in message4:
        print(char, end='', flush=True)
        time.sleep(0.03)
    
    message5 = " Каждый момент, проведенный с тобой, становится незабываемым!"
    for char in message5:
        print(char, end='', flush=True)
        time.sleep(0.06)
  
love_confession()

def xt(t):
    return 16 * math.sin(t) ** 3
def yt(t):
    return 13 * math.cos(t) - 5 \
    * math.cos(2 * t) - 2 * \
    math.cos(3 * t) - math.cos(4 * t)
t = turtle.Turtle()
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 * i) // 2 % 255)
    t.goto(0, 0)
t.hideturtle()
turtle.update()
turtle.mainloop()
