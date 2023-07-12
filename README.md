# IT-Valentine
![Header](https://github.com/rumpelovs/IT-Valentine/blob/main/assets/image%20(1).png)




____

##### This code will gradually print a message that you are in love with a girl and want to spend every minute with her. This is an original and romantic way to express your feelings using programming.

___
### ⚙️ How does the code work? ⚙️

##### Easy and simple, in order to create it, you need to import a specific library and write an easy function. After that, you need to come up with the text that you want the program to write!
___

### Here's what the code looks like:

``` Python
import time

message = ""
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.1)
```

![Python](https://img.shields.io/badge/-PYTHON-000?style=for-the-badge&logo=python&logoColor=EBFF19)
____

## The second part of the code!

### The second part of the code uses drawing the heart with stripes. Here is an example of the code:


``` Python
import turtle
import math

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
``` 
![Python](https://img.shields.io/badge/-PYTHON-000?style=for-the-badge&logo=python&logoColor=EBFF19)
#### 📫 Follow me 📫

[![github](https://img.shields.io/badge/-GITHUB-000?style=for-the-badge&logo=github&logoColor=911515)](https://github.com/rumpelovs)