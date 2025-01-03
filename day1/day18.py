from turtle import Turtle, Screen

# Create a turtle object named 'tim'
tim = Turtle()

# Function to draw a shape with 'num_sides' sides
def draw_shape(num_sides):
    angle = 360 / num_sides  # Calculate the angle between each side
    for _ in range(num_sides):
        tim.forward(100)  # Move forward by 100 units
        tim.right(angle)  # Turn right by the calculated angle

# Draw shapes with sides ranging from 3 to 10
for shape_size_n in range(3, 11):
    draw_shape(shape_size_n)

# Set up the screen and keep it open
screen = Screen()
screen.mainloop()
