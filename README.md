# autonomous-driving-dqn-carla
Experimentation on Carla Simulator for running DQN RL agents for Autonomous Driving

## What is Carla?
Carla is an open-source simulator for autonomous driving research!
It has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites, environmental conditions, full control of all static and dynamic actors, maps generation and much more.



## Requirments
At time of this experiment [CARLA 0.9.8](https://github.com/carla-simulator/carla/releases/tag/0.9.8) was used.

* Server side. A 4GB minimum GPU will be needed to run a highly realistic environment. A dedicated GPU is highly advised for machine learning.
* Client side. Python is necessary to access the API via command line. Also, a good internet connection and two TCP ports (2000 and 2001 by default).
* System requirements. Any 64-bits OS should run CARLA.
* Other requirements. Two Python modules: Pygame to create graphics directly with Python, and Numpy for great calculus.

Run **reuirments.txt** to get all dependencies installed.

The machine used was [Windows] 64-bit, 16GB RAM | intel(R) Core(TM) i7-8650U CPU @ 1.90GHz 2.11GHz | NVIDIA GeForce GTX 1050
* Download and install [CARLA 0.9.8 for windows](https://carla-releases.s3.eu-west-3.amazonaws.com/Windows/CARLA_0.9.8.zip)
* Download and install [CARLA Additional Maps 0.9.8](https://carla-releases.s3.eu-west-3.amazonaws.com/Windows/AdditionalMaps_0.9.8.zip)

