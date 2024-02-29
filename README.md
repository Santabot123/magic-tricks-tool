# What is magic-trick-tool

It`s a free demo of my ~~AI cheats~~ 🪄magic🪄. It detects persons in the specified area of the screen and directs your crosshair to the person who is closest to the crosshair.

# Minimum system requirements
- OS: Windows 10/11 64-bit
- Memory: 16GB RAM
- Graphics: **Nvidia GPU** with at least 4 GB VRAM

**Note:** Minimum system requirements may vary depending on the game in which you will use 🪄magic🪄.

# Installation 
Video guide: 
Steps:
1. Download this repository and unzip it.
2. Install  [Anaconda](https://www.anaconda.com/download).
3. Open Aanaconda Navigator.
4. Open the "Environment" tab.
5. Press "Create" and enter any name in "New environment name" field and choose python 3.9.18. After this step Anaconda will create new virtual enviroment.
6. Click the play button(▶) next to the newly created virtual environment and choose "Open in Terminal".
7. In the terminal, you must install the necessary libraries using the following commands:
```pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121```
```pip install ultralytics```
```pip install dxcam```
```pip install pydirectinput-rgx```
```pip install shapely```
```pip install sahi```
```pip install chardet```
8. Open the "Home" tab in  Aanaconda Navigator and install JupyterLab if it not.

# Usage

1.Launch your game; go to settings and switch full screen to window mode.
2. Open the "Home" tab in  Aanaconda Navigator and launch JupyterLab.
3. In JupyterLab find folder where you saved this repository and open ```run.ipynb```
4. Run it by clicking run all sells button next button (⏩). 
5. Now you should go into your game and try it!!!
6. 🪄Magic🪄 would be active only while Right mouse button is preessed (of you whant to change it-read **Fine-tuning** paragraph).

To stop program you can press "Restart the kernel" button ( ⟳) or F1 button.

### Fine-tuning
If you want to change some settings go to ```run.ipynb``` and find 𝙐𝙎𝙀𝙍 𝘾𝙊𝙉𝙁𝙄𝙂 section.
- To change the area for target detection modify LEFT, TOP, RIGHT, BOTTOM parameters.
- To change the key that should be pressed to activate 🪄magic🪄 modify ACTIVATE_KEY (you can also make it always active by changing ALWAYS_ACTIVE=False to ALWAYS_ACTIVE=True)
- To change speed of your crosshair modify SCALE variable 
- Tou can also choose where to aim if 



# Demonstration of work



 
