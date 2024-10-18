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


## Installation Guide

### Prerequisites
1. **Python 3.x** and **pip** installed on your system.
2. Basic understanding of using the command line.

### Step 1: Download the Directory

Download the required files either manually (reqomended) or with `git clone`:

```bash
git clone https://github.com/LessVegetables/Little-Projects.git
```

Then navigate to the `Redlight-Greenlight` folder:

```bash
cd Little-Projects/Redlight-Greenlight
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
To avoid dependency conflicts, it's recommended to create a virtual environment. Run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
```

### Step 3: Install Required Dependencies
All necessary dependencies are listed in the `requirements.txt` file. Install them by running:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Program
Once the dependencies are installed, you can run the program by executing the following command:

```bash
python game.py
```
---

## Troubleshooting

- **Issue with Dependencies:** Make sure you have installed all the required libraries from the `requirements.txt`. You can also try running `pip freeze` to verify installed packages.
  
- **Missing Assets:** If any asset is missing, recheck the repository structure or download the required files from the repository manually.

---
