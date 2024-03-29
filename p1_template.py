from tkinter import Canvas, Tk, Event
import p1_utilities
import random
import time
gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
the_canvas = Canvas(gui, width=800, height=800, background='white')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

### MAKE CREATURE SECTION (put your function defs here ) ##########################

# Here's a delightful smiley face as an example (feel free to delete it)
def make_creature(a_canvas, center, primary_color="red", secondary_color="blue", size=100, my_tag=""):
    radius = size / 2
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - radius / 4, center[1] - radius / 5)
    right_eye_pos = (center[0] + radius / 4, center[1] - radius / 5)
    eye_width = radius / 10
    eye_height = radius / 10

    p1_utilities.make_circle(a_canvas, center, radius,
                          fill_color=primary_color, tag=my_tag)
    p1_utilities.make_oval(a_canvas, left_eye_pos, eye_width,
                        eye_height, fill_color="red", tag=my_tag)
    p1_utilities.make_oval(a_canvas, right_eye_pos, eye_width,
                        eye_height, fill_color="green", tag=my_tag)
    p1_utilities.make_line(a_canvas, [
        (center[0] - radius / 2, center[1] + radius / 3),
        (center[0], center[1] + radius / 1.2),
        (center[0] + radius / 2, center[1] + radius / 3)
    ], curvy=True, tag=my_tag)

####################################################################################


### MAKE LANDSCAPE OBJECT SECTION (put your function defs here ) ###################
# Note: if you're going to use shapes that ALSO were part of your creature, no need
# to copy those function definitions twice!
def make_landscape_object(a_canvas, center, size=100, my_tag="", primary_color='blue'):
    p1_utilities.make_car(a_canvas, center, fill_color=primary_color)

####################################################################################

## EVENT HANDLERS HERE ##############################################################

counter = 0
def click_handle(event: Event):
    # print(event.x, event.y)
    global counter
    new_tag = "square_" + str(counter)
    p1_utilities.make_cloud(
        the_canvas, (event.x,event.y), fill_color="gray", my_tag=new_tag)
    counter = counter + 1

def double_click_handle(event):
    print(event)
    print(p1_utilities.get_tag_from_event(the_canvas, event))

the_canvas.bind('<Button-1>', click_handle)
the_canvas.bind('<Button-2>', double_click_handle)

####################################################################################


## Initial Terarium Setup Here ####################################################
for _ in range(5):
    make_landscape_object(
        the_canvas,
        (random.randint(0, 799), random.randint(400, 700)),
        random.randint(80, 120),
        "landscape",
        primary_color=p1_utilities.random_color(),
    )

# sample code to make a creature:
for _ in range(5):
    make_creature(
        the_canvas,
        (random.randint(0, 799), random.randint(0, 599)),
        p1_utilities.random_color(),
        p1_utilities.random_color(),
        random.randint(30, 180),
        "creature"
    )
####################################################################################

## ANIMATION LOOP HERE ####################################################
# Note, you will only have ONE animation loop

while True:
    p1_utilities.update_position(the_canvas, "creature", x=2, y=-2)
    # print("top:", p1_utilities.get_top(the_canvas, "test"))
    # print("bottom:", p1_utilities.get_top(the_canvas, "test"))
    gui.update()
    time.sleep(0.1)


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
