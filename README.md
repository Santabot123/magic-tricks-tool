# What is magic-tricks-tool

It`s a free demo of my ~~AI cheats~~ 🪄magic🪄. It detects persons in the specified area of the screen and directs your crosshair to the person who is closest to the crosshair. In theory, this should work in any shooter game, but in practice, you'll have to test it yourself. Сurrently the 🪄magic🪄 tested in in Fortnite, PUBG, and Apex Legends.

![Знімок екрана 2024-03-26 111716](https://github.com/Santabot123/magic-tricks-tool/assets/56690519/8d4bb525-9759-4315-87a3-6a680c07ceba)
![f](https://github.com/Santabot123/magic-tricks-tool/assets/56690519/61458ba0-acc2-4021-bf61-055326fb9385)


# Minimum system requirements
- OS: Windows 10/11 64-bit
- Memory: 16GB RAM
- Graphics: **Nvidia GPU** with at least 4 GB VRAM

**Note:** Minimum system requirements may vary depending on the game in which you will use 🪄magic🪄.

# Installation 
Video guide:
<br>
Steps from video:
1. Download this repository and unzip it.
2. Install  [Anaconda](https://www.anaconda.com/download).
3. Open Aanaconda Navigator.
4. Open the "Environment" tab.
5. Press "Create" and enter any name in "New environment name" field and choose python 3.9.18. After this step Anaconda will create new virtual enviroment.
6. Open the "Home" tab in  Aanaconda Navigator and install JupyterLab if it not.

# Usage

1.Launch your game; go to settings and switch full screen to window mode. <br>
2. Open the "Home" tab in  Anaconda Navigator and launch JupyterLab.(Each time at a new launch, select in Anaconda Navigator exactly the same environment that you created. ) <br>
3. In JupyterLab find folder where you saved this repository and open ```UI.ipynb``` <br>
4. Run it by clicking run all sells button next button {⏩}(The first run will take much longer than usual because all the necessary libraries need to be loaded) <br>
5. After that a new settings window should open. <br>
6. To start the Magic press the RUN button  <br>
7. Now you should go into your game and try it!!!<br>
8. 🪄Magic🪄 would be active only while Right mouse button is preessed (if you whant to change it-read **Fine-tuning** paragraph).<br>
9. ☝️🤓 Actually if you don't need to change settings then you can run ```run.ipynb``` instead of ```UI.ipynb```. <br>
<br>
<br>

## Fine-tuning
When you hover over the settings menu item, you can read what it means.
**Note:**
- To change the area for target detection modify LEFT, TOP, RIGHT, BOTTOM parameters(if you run run.ipynb in the ```show_area``` section, you will see a screenshot of your screen with a rectangle that defines the area in which targets will be detected).
- Adjust the detection area in such a way that the image of your character does not get there, if it does get there, it can lead to the fact that the crosshair will always move in the same direction.
- The neural network will work more accurately if the detection zone is square
- To change speed of your crosshair movement modify SCALE variable 


# Demonstration of work

https://github.com/Santabot123/magic-tricks-tool/assets/56690519/0e67ceb4-cf11-44f0-9121-3aaf655f21af






 
