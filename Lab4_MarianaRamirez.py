"""
Lab 4 - Code Refactoring
(100 marks in total)

Name: MARIANA RAMIREZ
Due Data: Jan. 30, 2023, 17:00pm

"""

import turtle

#Exercise 1:

def draw_circles(t, size, decrease):
    for _ in range(4):
        t.circle(size)
        size = size - decrease



#Exercise 2:

def draw_special(t, size, repeat, decrease):
    for _ in range(repeat):
        draw_circles(t, size, decrease)
        t.right(360 / repeat)


#Exercise 3:


def draw_picture_nice():
    Albert = turtle.Turtle()
    Albert.speed(6)

    colors = ['white','blue', 'yellow', 'pink', 'red']
    decrease = [4 , 5, 10, 19, 20]

    for i in range(len(colors)):
        Albert.color(colors[i])
        draw_special(Albert, 100, 10, decrease[i])



if __name__ == '__main__': 
    drawing_screen = turtle.Screen()
    drawing_screen.bgcolor('black')
    draw_picture_nice()
    #draw_picture()
    drawing_screen.mainloop() 




"""
After finishing your lab, please upload the file to GitHub and copy paste the link
to your e-learn.

Hope this lab is helpful to your project 1 - Artistic Turtle Drawing. Have fun!
"""

