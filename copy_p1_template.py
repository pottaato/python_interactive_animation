import math
import random
import string
import time
import traceback
from tkinter import Canvas, Event, Tk

import p1_utilities

gui = Tk()
gui.title("My Terrarium")

# initialize canvas:
window_width = gui.winfo_screenwidth()
window_height = gui.winfo_screenheight()
the_canvas = Canvas(gui, width=1000, height=800, background="skyblue")
the_canvas.pack()

FPS = 60

########################## YOUR CODE BELOW THIS LINE ##############################


def random_tag(prefix: str) -> str:
    return "{}{}".format(
        prefix,
        "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(128)
        ),
    )


### MAKE CREATURE SECTION (put your function defs here ) ##########################

# hotairbaloon
def make_creature(
    a_canvas, center, primary_color="red", secondary_color="blue", size=100, my_tag=""
):
    r = size / 2
    x = center[0]
    y = center[1]

    p1_utilities.make_circle(a_canvas, center, r, fill_color=primary_color, tag=my_tag)
    p1_utilities.make_line(
        a_canvas,
        [(x - r + 5, y + 15), (x + r - 5, y + 15)],
        curvy=False,
        fill_color="black",
        tag=my_tag,
    )
    p1_utilities.make_line(
        a_canvas,
        [(x - r + 5, y + 15), (x - r + 10, y + 2 * r)],
        curvy=False,
        fill_color="black",
        tag=my_tag,
    )
    p1_utilities.make_line(
        a_canvas,
        [(x + r - 5, y + 15), (x + r - 10, y + 2 * r)],
        curvy=False,
        fill_color="black",
        tag=my_tag,
    )
    p1_utilities.make_rectangle(
        a_canvas, (x - r + 10, y + 2 * r), 80, r, fill_color=secondary_color, tag=my_tag
    )


####################################################################################


### MAKE LANDSCAPE OBJECT SECTION (put your function defs here ) ###################
# Note: if you're going to use shapes that ALSO were part of your creature, no need
# to copy those function definitions twice!

# car
def make_landscape_object(a_canvas, center, size=100, my_tag="", primary_color="blue"):
    p1_utilities.make_car(a_canvas, center, fill_color=primary_color, my_tag=my_tag)


def make_sun(a_canvas, center, size=100, my_tag="", primary_color="yellow"):
    p1_utilities.make_poly_circle(
        a_canvas, center, size, fill_color="yellow", tag=my_tag
    )


####################################################################################

hotairballoon_tagset = set()
car_tagset = set()
cloud_tagset = set()


def __my_delete(canvas: Canvas, tag: str):
    if tag in ["sun", "road"]:
        return

    p1_utilities.delete(canvas, tag)
    for tagset in [hotairballoon_tagset, car_tagset, cloud_tagset]:
        if tag in tagset:
            tagset.remove(tag)


## EVENT HANDLERS HERE ##############################################################


def click_handle(event: Event):
    tag = random_tag("hotairballoon")
    make_creature(
        the_canvas,
        (event.x, event.y),
        p1_utilities.random_color(),
        "orange",
        100,
        tag,
    )
    hotairballoon_tagset.add(tag)


# delete function: delete [hotairballoon] when double clicked


def double_click_handle(event):
    tag = p1_utilities.get_tag_from_event(the_canvas, event)
    __my_delete(the_canvas, tag)


the_canvas.bind("<Button-1>", click_handle)
the_canvas.bind("<Button-2>", double_click_handle)

####################################################################################


## Initial Terarium Setup Here ####################################################

make_sun(the_canvas, (100, 100), 100, "sun")

# road
p1_utilities.make_rectangle(the_canvas, (0, 500), 1100, 350, "gray", "road")

# generate 5 cars
for i in range(5):
    tmp_tag = random_tag("car")
    make_landscape_object(
        the_canvas,
        (random.randint(0, 10), random.randint(450, 700)),
        random.randint(80, 120),
        my_tag=tmp_tag,
        primary_color=p1_utilities.random_color(),
    )
    car_tagset.add(tmp_tag)

# generate 10 clouds
for i in range(10):
    tmp_tag = random_tag("cloud")
    p1_utilities.make_cloud(
        the_canvas,
        (random.randint(100, 900), random.randint(0, 300)),
        fill_color="white",
        my_tag=tmp_tag,
    )
    cloud_tagset.add(tmp_tag)

# sample code to make a creature:

# generate 5 hotairballoons
for i in range(5):
    tmp_tag = random_tag("hotairballoon")
    make_creature(
        the_canvas,
        (random.randint(0, 799), random.randint(0, 300)),
        p1_utilities.random_color(),
        "orange",
        100,
        my_tag=tmp_tag,
    )
    hotairballoon_tagset.add(tmp_tag)


####################################################################################

## ANIMATION LOOP HERE ####################################################
# Note, you will only have ONE animation loop

car_tag_speed_mapping = {tag: random.randint(2, 10) for tag in car_tagset}

cloud_tag_speed_mapping = {tag: random.randint(1, 3) for tag in cloud_tagset}
cloud_tag_direction_mapping = dict()
for tag in cloud_tagset:
    if random.random() >= 0.5:
        cloud_tag_direction_mapping[tag] = 1
    else:
        cloud_tag_direction_mapping[tag] = -1

hotairballoon_angle_mapping = dict()

while True:

    try:
        # make every generated hotairballoon "fly up" and change color
        for tmp_tag in hotairballoon_tagset:
            # if not p1_utilities.does_tag_exist(the_canvas, tmp_tag):
            #     continue
            if tmp_tag not in hotairballoon_angle_mapping or random.random() < 0.05:
                hotairballoon_angle_mapping[tmp_tag] = math.pi * random.random()
            p1_utilities.update_position(
                the_canvas,
                tmp_tag,
                x=(
                    2 * random.random() * math.cos(hotairballoon_angle_mapping[tmp_tag])
                ),
                y=(
                    -2
                    * random.random()
                    * math.sin(hotairballoon_angle_mapping[tmp_tag])
                ),
            )
            if random.random() < (2 / FPS):
                p1_utilities.update_fill(
                    the_canvas, tmp_tag, p1_utilities.random_color()
                )

        # make every car move different speed
        for tag in car_tagset:
            p1_utilities.update_position(the_canvas, tag, x=car_tag_speed_mapping[tag])

        # make cloud move different speed and direction, bounce when hit edge of canvas
        for tag in cloud_tagset:
            p1_utilities.update_position(
                the_canvas,
                tag,
                x=cloud_tag_speed_mapping[tag] * cloud_tag_direction_mapping[tag],
            )
            cloud_right = p1_utilities.get_right(the_canvas, tag)
            cloud_left = p1_utilities.get_left(the_canvas, tag)

            # print(cloud_right, cloud_left)
            if cloud_right >= 1000 or cloud_left <= 0:
                p1_utilities.flip(the_canvas, tag)
                cloud_tag_direction_mapping[tag] = -cloud_tag_direction_mapping[tag]

        # has a possibility (~1/1s) to generate a new car
        if random.random() <= (1 / FPS):
            tmp_tag = random_tag("car")
            make_landscape_object(
                the_canvas,
                (random.randint(0, 10), random.randint(450, 700)),
                random.randint(80, 120),
                my_tag=tmp_tag,
                primary_color=p1_utilities.random_color(),
            )
            car_tagset.add(tmp_tag)
            car_tag_speed_mapping[tmp_tag] = random.randint(2, 10)

        gui.update()
        time.sleep(1 / FPS)

    except Exception as e:
        print(repr(e))
        print(traceback.format_exc())
        exit(0)

########################## YOUR CODE ABOVE THIS LINE ##############################

# makes sure the canvas keeps running:
the_canvas.mainloop()
