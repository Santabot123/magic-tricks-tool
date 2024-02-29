# What is magic-trick-tool

It`s a free demo of my ~~AI cheats~~ 🪄magic🪄. It detects persons in the specified area of the screen and directs your crosshair to the person who is closest to the crosshair. In theory, this should work in any shooter game, but in practice, you'll have to test it yourself. Сurrently the 🪄magic🪄 works in in Fortnite, PUBG, and Apex Legends.

![f](https://github.com/Santabot123/magic-tricks-tool/assets/56690519/61458ba0-acc2-4021-bf61-055326fb9385)

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
7. In the terminal, you must install the necessary libraries using the following commands:  <br>
```pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121```  <br>
```pip install ultralytics``` <br>
```pip install dxcam``` <br>
```pip install pydirectinput-rgx``` <br>
```pip install shapely``` <br>
```pip install sahi``` <br>
```pip install chardet``` <br>
 <br>
8. Open the "Home" tab in  Aanaconda Navigator and install JupyterLab if it not.

# Usage

1.Launch your game; go to settings and switch full screen to window mode. <br>
2. Open the "Home" tab in  Aanaconda Navigator and launch JupyterLab. <br>
3. In JupyterLab find folder where you saved this repository and open ```run.ipynb```. <br>
4. Run it by clicking run all cells button next button (⏩). <br>
5. Now you should go into your game and try it!!! <br>
6. 🪄Magic🪄 would be active only while Right mouse button is preessed (of you whant to change it-read **Fine-tuning** paragraph). <br>
<br>
To stop program you can press "Restart the kernel" button ( ⟳) or F1 button.

### Fine-tuning
If you want to change some settings for fine tuning, go to ```run.ipynb``` and find 𝙐𝙎𝙀𝙍 𝘾𝙊𝙉𝙁𝙄𝙂 section.
- To change the area for target detection modify LEFT, TOP, RIGHT, BOTTOM parameters.
- To change the key that should be pressed to activate 🪄magic🪄 modify ACTIVATE_KEY (you can also make it always active by changing ALWAYS_ACTIVE=False to ALWAYS_ACTIVE=True)
- To change speed of your crosshair modify SCALE variable 
- You can also choose where to aim(head/body/random)
- You can also try to enable sahi - this will improve the recognition of small objects, but it will significantly reduce the number of frames it can process in one second


# Demonstration of work

https://github.com/Santabot123/magic-tricks-tool/assets/56690519/0e67ceb4-cf11-44f0-9121-3aaf655f21af






 
