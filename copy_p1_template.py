from tkinter import Canvas, Tk, Event
import p1_utilities
import random
import time
import typing
import traceback
gui = Tk()
gui.title('My Terrarium')

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
the_canvas = Canvas(gui, width=1000, height=800, background='skyblue')
the_canvas.pack()

########################## YOUR CODE BELOW THIS LINE ##############################

### MAKE CREATURE SECTION (put your function defs here ) ##########################

# Here's a delightful smiley face as an example (feel free to delete it)
# def make_creature(a_canvas, center, primary_color="red", secondary_color="blue", size=100, my_tag=""):
#     radius = size / 2

#     # just a demo of how you might think about making your creature:
#     left_eye_pos = (center[0] - radius / 4, center[1] - radius / 5)
#     right_eye_pos = (center[0] + radius / 4, center[1] - radius / 5)
#     eye_width = radius / 10
#     eye_height = radius / 10

#     p1_utilities.make_circle(a_canvas, center, radius,
#                           fill_color=primary_color, tag=my_tag)
#     p1_utilities.make_oval(a_canvas, left_eye_pos, eye_width,
#                         eye_height, fill_color="red", tag=my_tag)
#     p1_utilities.make_oval(a_canvas, right_eye_pos, eye_width,
#                         eye_height, fill_color="green", tag=my_tag)
#     p1_utilities.make_line(a_canvas, [
#         (center[0] - radius / 2, center[1] + radius / 3),
#         (center[0], center[1] + radius / 1.2),
#         (center[0] + radius / 2, center[1] + radius / 3)
#     ], curvy=True, tag=my_tag)

def make_creature(a_canvas, center, primary_color="red", secondary_color="blue", size=100, my_tag=""):
    r = size / 2
    x = center[0]
    y = center[1]

    p1_utilities.make_circle(a_canvas, center, r, fill_color=primary_color, tag=my_tag)
    p1_utilities.make_line(a_canvas, [(x - r + 5, y + 15), (x + r - 5, y + 15)], curvy=False, fill_color="black", tag=my_tag) 
    p1_utilities.make_line(a_canvas, [(x - r + 5, y + 15), (x - r + 10, y + 2*r)], curvy=False, fill_color="black", tag=my_tag)
    p1_utilities.make_line(a_canvas, [(x + r - 5, y + 15), (x + r - 10, y + 2*r)], curvy=False, fill_color="black", tag=my_tag)
    p1_utilities.make_rectangle(a_canvas, (x - r + 10, y + 2*r), 80, r, fill_color=secondary_color, tag=my_tag)

####################################################################################


### MAKE LANDSCAPE OBJECT SECTION (put your function defs here ) ###################
# Note: if you're going to use shapes that ALSO were part of your creature, no need
# to copy those function definitions twice!
def make_landscape_object(a_canvas, center, size=100, my_tag="", primary_color='blue'):
    p1_utilities.make_car(a_canvas, center, fill_color=primary_color, my_tag=my_tag)

####################################################################################


def __my_delete(canvas: Canvas, tag: typing.Union[str, None]):
    if tag is None:
        return

    if p1_utilities.does_tag_exist(canvas, tag):
        p1_utilities.delete(canvas, tag)

def __my_get_right(canvas: Canvas, tag: typing.Union[str, None]):
    if tag is None:
        return

    if p1_utilities.does_tag_exist(canvas, tag):
        p1_utilities.get_right(canvas, tag)

def __my_get_left(canvas: Canvas, tag: typing.Union[str, None]):
    if tag is None:
        return

    if p1_utilities.does_tag_exist(canvas, tag):
        p1_utilities.get_left(canvas, tag)

## EVENT HANDLERS HERE ##############################################################

hotairballoon_counter = 5
def click_handle(event: Event):
    # print(event.x, event.y)
    global hotairballoon_counter
    # new_tag = "hotairballoon_" + str(counter)
    # p1_utilities.make_cloud(
    #     the_canvas, (event.x,event.y), fill_color="white", my_tag=new_tag)
    make_creature(
        the_canvas, 
        (event.x, event.y), 
        p1_utilities.random_color(), 
        "orange", 
        100, 
        f"hotairballoon_{hotairballoon_counter}"
    )
    print(f"hotairballoon_{hotairballoon_counter}")
    hotairballoon_counter += 1

def double_click_handle(event):
    print(event)
    tag = p1_utilities.get_tag_from_event(the_canvas, event)
    __my_delete(the_canvas, tag)

the_canvas.bind('<Button-1>', click_handle)
the_canvas.bind('<Button-2>', double_click_handle)

####################################################################################


## Initial Terarium Setup Here ####################################################

p1_utilities.make_rectangle(
    the_canvas,
    (0, 500),
    1100,
    350,
    "gray")

for i in range(5):
    make_landscape_object(
        the_canvas,
        (random.randint(0, 10), random.randint(450, 700)),
        random.randint(80, 120),
        f"car_{i}",
        primary_color=p1_utilities.random_color(),
    )
    # print(f"car_{i}")

for i in range(10):
    p1_utilities.make_cloud(
        the_canvas, 
        (random.randint(100, 900), random.randint(0, 300)), 
        fill_color="white", 
        my_tag=f"cloud_{i}")

# sample code to make a creature:
for i in range(5):
    make_creature(
        the_canvas, 
        (random.randint(0, 799), random.randint(0, 300)), 
        p1_utilities.random_color(), "orange", 
        100, 
        f"hotairballoon_{i}")


####################################################################################

## ANIMATION LOOP HERE ####################################################
# Note, you will only have ONE animation loop

car_speed_values = [random.randint(2, 10) for _ in range(5)]
cloud_speed_val = [random.randint(1, 3) for _ in range(10)]

cloud_directions = list()
for _ in range(10):
    if random.random() >= 0.5:
        cloud_directions.append(1)
    else:
        cloud_directions.append(-1)

while True:
    try:
        for i in range(hotairballoon_counter):
            tmp_tag = f"hotairballoon_{i}"
            if not p1_utilities.does_tag_exist(the_canvas, tmp_tag):
                continue
            p1_utilities.update_position(the_canvas, tmp_tag, x=0, y=-2)
        for i in range(5):
            p1_utilities.update_position(the_canvas, f"car_{i}", x=car_speed_values[i])
        for i in range(10):
            tmp_tag = f"cloud_{i}"
            p1_utilities.update_position(the_canvas, tmp_tag, x=(cloud_speed_val[i] * cloud_directions[i]))
            try:
                curr_cloud_right = __my_get_right(the_canvas, tmp_tag)
                curr_cloud_left = __my_get_left(the_canvas, tmp_tag)
                if curr_cloud_right >= 1000 or curr_cloud_left <= 0:
                    p1_utilities.flip(the_canvas, tmp_tag)
                    cloud_directions[i] = -cloud_directions[i]
            except TypeError as e:
                pass

        gui.update()
        time.sleep(1 / 60.0)
    except Exception as e:
        print(traceback.format_exc())
        exit(0)


########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
