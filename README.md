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
  2. [DONE] Make cars always move right, clouds moves left-right, "hotairballoon" moves up
  3. [DONE] Spawn new "hotairballoon" on-click
  4. [DONE] Make each cars and clouds move with different speed
  5. Make delete function that removes "hotairballoon" (by double-click)
  6. Make cars keep appearing from left
  7. [DONE] Make any objects constantly change color

Source: https://bain-cs110.github.io/assignments/p1#starter-files 