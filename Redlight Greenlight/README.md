# Red light Green light
## Inspired by squidgame
A homework assignment. 

The assignment (also [here](https://github.com/vvabi-sabi/PAC/blob/main/Lesson6.ipynb#Лабораторная-работа-6.-Красный-свет-/-зелёный-свет) — scroll all the way down): create a program, that detects motion from a video feed.

## Gameplay
### Start screen
* Press `SPACE` to start the countdown
### Countdown screen
* 3 second countdown to get into position
### Gameplay screen

### Endgame screen
* Press `Y` to play again
* Press `N` to quit the game

Press `ESCAPE` or `Q` at any point to also quit the game.

## Known issues
* Key inputs are not registered right away. Has to do with the way I implemented key detection: `key = cv2.waitKey(50)` — not a great way (for ...reasons).
* If person is far away — motion detection might not work as well.
* If the user is playing, and somebody walks in the background — the game will still register motion and falsly end the game.
* 
## Sources
* Doll image source [here](https://www.yankodesign.com/images/design_news/2021/11/how-to-make-your-own-squid-game-toy-using-an-ipad-and-a-3d-pen/3d_pen_squid_game_toy_26.jpg).
* Doll music: not mine, but I lost the source.
* Gun shot sound: [From SampleFocus By Jacob Liotine](https://samplefocus.com/samples/ak47-machine-gun-spray-fx).
