# interactive_animation

## General_guidance:
  * Canvas is separated into 2 parts: sky (blue), and road (gray)
  `Note: Road part is made by p1_utilities.make_rectangle (refer to ## Initial Terarium Setup Here ##)`
  * Sky filled with clouds `p1_utilities.make_cloud` and will move **inside** the frame. `something to do with p1_utilities.flip()`
  * Road filled with cars `p1_utilities.make_cars` and will **keep moving** to the right. `keep respawning on left then go right`
  * Creature is tagged "hotairballoon", move up `y=-2`, and can be spawned everywhere with single click
  * Two click on the Creature will make the Creature disappear 

## TODO:
  * Make car endlessly appear on the "Road" from left to right
  * Make cloud move in the "Sky", make cloud bounces off the canvas
