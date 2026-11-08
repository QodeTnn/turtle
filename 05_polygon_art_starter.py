import turtle
import random
from polygon_shape import Polygon

print("Starting program...")
screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Student Polygon Art")
screen.bgcolor("black")
screen.tracer(1) 

colors = ["cyan", "turquoise", "orange", "yellowgreen", "deepskyblue",
          "salmon", "plum", "lightgreen", "gold", "pink", "white"]
rng = random.Random(12)

polygons = [] 
for i in range(20):
    print(f"Drawing polygon {i+1}/20...")
    sides = rng.randint(3, 6)
    side_length = rng.randint(35, 120)
    x = rng.randint(-350, 260)
    y = rng.randint(-225, 180)
    color = rng.choice(colors)
    pen_size = rng.randint(1, 7)
    angle = rng.randint(0, 359)
    
    polygon = Polygon(x, y, sides, side_length, color, pen_size, angle)
    polygon.draw()
    polygons.append(polygon)


screen.update()
screen.mainloop()