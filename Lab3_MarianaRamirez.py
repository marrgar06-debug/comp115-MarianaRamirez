"""
Lab 3: Draw some basic shapes with Turtle Graphics, using loop algorithms.

Complete exercise 1-2 (each values 50 points, 100 points in total).

Author:  <Mariana Ramirez>
Due Date: This Friday (Jan. 23) 5:00pm.
    
"""

import turtle
drawing_screen = turtle.Screen()


Exercise 1 - To draw a regular hexagon:

You may have noticed that to draw a square is very similar 
to draw an equilateral triangle. We need to calculate 
the exterior angle of a square, which is the angle your turtle/pen/brush
will turn.

Now, similar as example 2 and 3, 
but draw a regular hexagon (6 sides) with side length 100.

Hint:
num_sides = 6
exterior_angle = 360 / num_sides
'''

# Code your exe 1 here

alex.clear()
alex.shape("circle")
alex.color("blue")
alex.up()
alex.goto(0, 0) 
alex.down()
num_sides = 6
side_length = 100
exterior_angle = 360 / num_sides 
for _ in range(6):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.shape("blank")




"""
Part 2

Understanding the following examples 4 and 5 is beneficial for you to move to the exercise 2 below.
"""

'''

Exercise 2 - To draw a rainbow (like this one https://elearn.capu.ca/mod/assign/view.php?id=3237843):
You can set your own initial radius and increment value.

Hint: You may need to use the functions below:
alex.circle(-radius, 180)
alex.backward()
'''

# Code your exe 2 here

num_circles = 7
rainbow_colors = ["violet", "indigo", "blue",
                    "green", "yellow", "orange", "red"]
radius = 200
radius_decrease = 10
alex.clear()  
alex.speed(5)
alex.pensize(15)
alex.up()
for rainbow_color in rainbow_colors:
     alex.color(rainbow_color)
     alex.backward(radius)
     alex.goto(-radius, 0)
     alex.setheading(90)
     alex.down()
     alex.circle(-radius, 180)
     alex.up()
     radius = radius - radius_decrease

alex.shape("blank")









drawing_screen.mainloop() 


"""
Well done! Now you've finished your lab3 successfully. Please upload it 
to your GitHub repository and submit your lab3 GitHub link on e-learn, 
as you did for lab1 and lab2. That's all.

Resource (optional): For exercise 1, feel free to review the concept of exterior angles of regular polygons from here:
https://www.teachoo.com/8592/2789/Exterior-Angles-of-Regular-Polygons/category/Sum-of-Exterior-Angles-of-Polygons/
"""
