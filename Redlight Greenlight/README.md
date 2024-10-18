# Red light Green light
## Inspired by squidgame
A homework assignment. 

This project is a homework assignment focused on creating a program that detects motion from a video feed. The full assignment can be found [here](https://github.com/vvabi-sabi/PAC/blob/main/Lesson6.ipynb#Лабораторная-работа-6.-Красный-свет-/-зелёный-свет) (scroll all the way down)

## Gameplay
### Start screen
* Press `SPACE` to begin the countdown.
### Countdown screen
* A 3-second countdown will give you time to get into position.
### Gameplay screen
* **Green light**: The doll is singing.
* **Red light**: The doll is looking at you.
* Press `SPACE` to win the game.
### Endgame screen
* Press `Y` to play again.
* Press `N` to quit the game.

At any point during the game, you can press `ESCAPE` or `Q` to quit.

## Known issues
###### Note: The main task was to create a motion-detection program, not necessarily a polished game. Be that as it may:
* **Key inputs** may not be registered immediately due to the current implementation of key detection using `key = cv2.waitKey(50)`. This approach has its drawbacks.
* **Motion detection** may struggle if the player is far away from the camera.
* **Background movement**: If someone walks behind the player while playing, the game may falsely detect motion and end.

## Improvements
* Add a time limit to press `SPACE` during gameplay to increase difficulty


## Sources
* Doll Image: [Source](https://www.yankodesign.com/images/design_news/2021/11/how-to-make-your-own-squid-game-toy-using-an-ipad-and-a-3d-pen/3d_pen_squid_game_toy_26.jpg).
* Doll Music: Not mine, but the source is lost.
* Gunshot Sound: [From SampleFocus By Jacob Liotine](https://samplefocus.com/samples/ak47-machine-gun-spray-fx).
