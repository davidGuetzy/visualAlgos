# Visualizing Algorithms

This repository contains the code to visualize some common algorithms in computer science using the python manim library. 

There is a possibility that I create a YouTube Channel to display some of the work I do here.


## Installation

Contained within the repo there is a Vagrantfile which will construct a virtual machine capable of doing development and execution of manim files. See **Using the Virtual Machine** below. 

If you don't want to use virtualbox, you can visit the [Manim Community Page](https://docs.manim.community/en/stable/installation.html) and follow their instructions to install Manim on your machine. You should be able to interact with the code after forking the repo and following the instructions.


## Using the Virtual Machine

1. Install [Vagrant](https://www.vagrantup.com/) if you do not have it already.
2. Install some flavor of X windows server
    1. For Mac there is [xQuartz](https://www.xquartz.org/)
    2. For Windows I know of [xMing](https://sourceforge.net/projects/xming/)
3. Clone/Fork the repository to some directory
4. Run vagrant up and the box should provision
5. Connect with the box via an ssh connection
    - This is very easy with VSCode's Remote - SSH Extension
    - You can also set up a config file to ssh in it is important to include ForwardX11 yes
6. Once connected, you can see the repo contents in ~/visualAlgos
 



