from turtle import Turtle, Screen
import random

# Create a turtle object named 'tim'
tim = Turtle()
tim.speed("fastest")  # Set the turtle speed to the fastest

# Function to draw a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.random(), random.random(), random.random())  # Random color
        tim.circle(100)  # Draw a circle with a radius of 100 units
        tim.setheading(tim.heading() + size_of_gap)  # Adjust the heading by the gap

# Draw a spirograph with a gap size of 10 degrees
draw_spirograph(5)

# Set up the screen and keep it open
screen = Screen()
screen.mainloop()
