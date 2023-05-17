# interactive_animation

## General_guidance:
  * Canvas is separated into 2 parts: sky (blue), and road (gray)
  `Note: Road part is made by p1_utilities.make_rectangle (refer to ## Initial Terarium Setup Here ##)`
  * Sky filled with clouds `p1_utilities.make_cloud` and will move **inside** the frame. `p1_utilities.flip() if reach canvas edges`
  * Road filled with cars `def make_landscape_object` and will **keep moving** to the right. `keep respawning on left moving in right direction`
  * Creature `def make_creature` is "hotairballoon", move up `y=-2`, and can be spawned everywhere on-click
  * Double click on the "hotairballoon" should deletes it

## TODO:
  1. [DONE] Make cloud do flip when hit the canvas's right or left edges.
     1. 1 	3 points 	Animate your creatures (and your environmental features if it makes sense to do so). If creatures / environmental features move off of the screen, recreate them on the other side or have them bounce off the side.
  2. [DONE] Make cars always move right, clouds moves left-right, "hotairballoon" moves up with random angle
     1. 2 	3 points 	Experiment with different kinds of motion. Instead of your creatures moving linearly at a constant speed, you can experiment with the math.sin and math.cos functions (or any others techniques) to make your creature oscillate, accelerate, decelerate, etc.
  3. [DONE] Spawn new "hotairballoon" on-click
     1. 3 	3 points 	Spawn a new creature or landscape object when the user either clicks or drags or right-clicks the screen (you can also use a keyboard event).
  4. [DONE] Make each cars and clouds move with different speed, hotairballoon diff speed & angle
     1. 4 	3 points 	Animate each of your creatures (all of your original 5) so that their movement is different (different speeds AND different movement patterns).
  5. [DONE] Make delete function that removes "hotairballoon" (by double-click)
     1. 7 	3 points 	When you click a creature, remove it from the screen (you can also assign a particular keyboard key to delete a creature (but it needs to be able to be hit more than once without causing an error))
  6. [DONE] Make cars keep appearing from left
     1. 6 	3 points 	Periodically (repeatedly) add or remove creatures and/or landscape objects to/from your scene.
  7. [DONE] Make any objects constantly change color
     1. 11 	3 points 	Make your creature or landscape feature periodically (repeatedly) change colors.

Source: https://bain-cs110.github.io/assignments/p1#starter-files
