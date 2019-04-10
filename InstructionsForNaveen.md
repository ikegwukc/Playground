# OpenAI Instructions for Naveen.

I installed the latest version of ubuntu which at the time of writing this is: Ubuntu 18.04.02 LTS.

I open up terminal and then run the following commands:

```bash
# download latest version of Anaconda3
wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
```

```bash
# install latest version of anaconda3 python interactively

# I accepted the agreement and left the default install location
# as the default path, which should be: /home/$USER/anaconda3

bash Anaconda3-2019.03-Linux-x86_64.sh

# After installing Anaconda3 you will receive a prompt that
# asks if you want to initialize Anaconda3. Say yes

# Close the terminal and reopen it.
```


Create a anaconda environment for OpenAI gym
```bash
# create the environment
conda create --name universe python=3.7 anaconda

# initialize the environment
source activate universe

# Install required packges
apt install -y python3-dev zlib1g-dev libjpeg-dev cmake swig python-pyglet python3-opengl libboost-all-dev libsdl2-dev \
    libosmesa6-dev patchelf ffmpeg xvfb

# Then install gym
pip install gym
```

Now open up an anaconda3 shell with the following command `python` and then run the following command:
```python3
import gym
```
