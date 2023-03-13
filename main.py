# import colorgram

# extracted_colors = colorgram.extract('image\image.jpg', 30)

# def format_colors():
#     color_list = []
#     for colors in extracted_colors:
#         rgb_tuple = colors.rgb
#         r, g, b = rgb_tuple
#         formatted_rgb = (r, g, b)
#         color_list.append(formatted_rgb)
#     return color_list
    
# color = format_colors()
# print(color)

import turtle as t
import random

my_turtle = t.Turtle()
t.colormode(255)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), 
 (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
 (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), 
 (19, 86, 89), (82, 148, 129), (147, 17, 19), (12, 70, 64), (107, 127, 153), (168, 99, 102)]


"""REQUIREMENTS
Paint a 10 by 10 rows of spot
Each of the dot should be around 20 and 50 as gap
"""

my_turtle.speed(0)
my_turtle.hideturtle()
vertical_repeat = 0
gap = 40
while vertical_repeat < 10:
    my_turtle.penup()
    my_turtle.setheading(225)
    my_turtle.forward(300)
    my_turtle.setheading(0)
    horizontal_repeat = 0
    while horizontal_repeat < 10:
        colors = random.choice(color_list)
        my_turtle.dot(20, colors)
        my_turtle.penup()
        my_turtle.forward(30)
        my_turtle.penup()
        my_turtle.forward(30)
        
        horizontal_repeat += 1
        
    my_turtle.penup()
    my_turtle.setposition(0, gap)
    my_turtle.penup()   
    gap += 40
    vertical_repeat +=1 

my_screen = t.Screen()
my_screen.exitonclick()














# import turtle as t
# import random

# my_turtle = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, g, b)
#     return color_tuple


# my_turtle.speed(0)
# my_turtle.pensize(1)

# complete_pattent = 0
# while complete_pattent < 8.5:
#     colors = random_color()
#     direction = complete_pattent
#     my_turtle.color(colors)
#     my_turtle.circle(100)
#     my_turtle.left(direction)
#     my_turtle.circle(100)
    
#     complete_pattent += 0.1




# directions = [0, 90, 180, 270]

# max_attempt = 0
# my_turtle.pensize(10)
# my_turtle.speed(0)
# while max_attempt < 500:
#     colors = random_color()
#     my_turtle.color(colors)
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(directions))
#     max_attempt += 1


# shape = 3
# distance = 100
# max_attempt = 0
# while max_attempt < 8:
#     angle = 360 / shape
#     colors = ["blue", "green", "black", "red", "purple", "orange"]
#     random_color = random.choice(colors)
#     my_turtle.color(random_color)
#     for _ in range(shape):
#         my_turtle.forward(distance)
#         my_turtle.right(angle)
#     shape += 1
#     max_attempt += 1


# for _ in range(10):
#     my_turtle.pendown()
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)

    # my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)


# screan = t.Screen()
# screan.exitonclick()
