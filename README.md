# autonomous-driving-dqn-carla
Experimentation on Carla Simulator for running DQN RL agents for Autonomous Driving

## What is Carla?
Carla is an open-source simulator for autonomous driving research!
It has been developed from the ground up to support development, training, and validation of autonomous driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites, environmental conditions, full control of all static and dynamic actors, maps generation and much more.

[CARLA Documentations](https://carla.readthedocs.io/en/latest/)



## Requirments
At time of this experiment [CARLA 0.9.8](https://github.com/carla-simulator/carla/releases/tag/0.9.8) was used.

* Server side. A 4GB minimum GPU will be needed to run a highly realistic environment. A dedicated GPU is highly advised for machine learning.
* Client side. Python is necessary to access the API via command line. Also, a good internet connection and two TCP ports (2000 and 2001 by default).
* System requirements. Any 64-bits OS should run CARLA.
* Other requirements. Two Python modules: Pygame to create graphics directly with Python, and Numpy for great calculus.

Windows users need two other requirments to run CARLA:
* [DirectX Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=35)
* [Open GL 3.3 or above](https://developer.nvidia.com/opengl-driver)

Note: CARLA 0.9.8 only works with python 3.7

Run **reuirments.txt** to get all dependencies installed.

The machine used was [Windows] 64-bit, 16GB RAM | intel(R) Core(TM) i7-8650U CPU @ 1.90GHz 2.11GHz | NVIDIA GeForce GTX 1050
* Download and install [CARLA 0.9.8 for windows](https://carla-releases.s3.eu-west-3.amazonaws.com/Windows/CARLA_0.9.8.zip)
* Download and install [CARLA Additional Maps 0.9.8](https://carla-releases.s3.eu-west-3.amazonaws.com/Windows/AdditionalMaps_0.9.8.zip)

## Installation
Extract downloaded package

Open a terminal in the main CARLA folder. Run the following command to execute the package file and start the simulation:
run carla
```
> CarlaUE4.exe
```
You can use your W, A, S and D to moved arround and mouse left click + drag to look arround

Run the following conmmand to add vehicles and pedestrians

```
> python3 spawn_npc.py -n <number-of-units>
```

## Using CARLA in python

Note that you need to have carla running (the shell or .exe) in order to run scripts.

If you attempt to import carla you'll face the error ```ModuleNotFoundError: No module named 'carla'```

You either need to write your script dirercty where you extracted carla. In that case the part ```sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg'...``` will detect carla path in your environment variables.

Or change the path in ```sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg'...``` to directrly point to where you extracted carla.

A cleaner way would be to copy ```'../carla/dist/carla-*%d.%d-%s.egg'``` in your python site pachkages, then you can import it normally anywhere you are developing your script. Just make sure site packages are accesible form your environment variables.


## Repo agenda
* Controlling the Car and getting Camera Sensor Data
	* Spawn the car in its environment
	* Controll the car in its environment
	* Get sensory data back from that car
		* Hood camera
		* Collision sensor
* Reinforcement Learning to train a self-driving car