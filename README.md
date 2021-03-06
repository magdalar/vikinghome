# vikinghome
Customized home control app for the Viking Homestead.

## Intended use

This code is intended to run on a Raspberry Pi with a Touchscreen, running semi-permanently as a full-screen application in order to supply access to:

* A webcam view (TyCam), which we're using as a supplemental baby monitor
  * Assumes use of https://elinux.org/RPi-Cam-Web-Interface
* Sonos music controls
* Philips Hue lighting controls

## Setup & Dependencies

1. Install python3 (3.8 at time of writing)
2. Create a virtual development environment:

```shell
$ python3 -m venv env
```

This creates a directory 'env', where the project-specific development environment will live. This directory is excluded by `.gitignore`, so will not be checked in or version-controlled.

3. Activate the environment:

```shell
$ source ./env/bin/activate
```

This will put the environment at the front of your `PATH`, et al. It also provides a `deactivate` function to run if you wish to re-use the shell without logging out.


4. Install dependencies:

| Name | Version | Description | URL |
| pyglet | 1.3.2 | The 'game' library we're using for running the main app | http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/ |
| requests | 2.23.0 | HTTP Fetching | http://requests.readthedocs.io/en/master/ |
| pyzbar | 0.1.8 | QRCode reader. Also install zbar on your system (`brew install zbar`). | https://pypi.org/project/pyzbar/ |
| opencv-python | 4.2 | Computer-Vision library, for image processing. | https://pypi.org/project/opencv-python/ |


```shell
brew install zbar
pip install pyglet requests pyzbar opencv-python
```

### Mac OS X

I used http://brew.sh to install python.

## Deployment & Running

Follow the development environment requirements, but you can skip the virtual environment, and just install the pip packages globally.

Then just run:

```shell
$ python3 src/main.py
```

Or use the `run.sh` script provided. If you cloned your repository somewhere other than $HOME/code/vikinghome/, you'll need to update the `VIKINGHOME` environment variable in the script.

Use 'q' to quit.
