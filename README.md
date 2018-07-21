# vikinghome
Customized home control app for the Viking Homestead.

## Intended use

This code is intended to run on a Raspberry Pi with a Touchscreen, running semi-permanently as a full-screen application in order to supply access to:

* A webcam view (TyCam), which we're using as a supplemental baby monitor
* Sonos music controls
* Philips Hue lighting controls

## Setup & Dependencies

1. Install python3 (3.7 at time of writing)
2. Create a virtual development environment:

```shell
$ python -m venv env
```

3. Activate the environment:

```shell
$ source ./env/bin/activate
```

4. Install pyglet (1.3.2 at time of writing):

```shell
$ pip install pyglet
```

5. Install requests (2.19.1 at time of writing):

```shell
$ pip install requests
```

### Mac OS X

I used http://brew.sh to install python.

## Deployment & Running

Follow the development environment requirements, but you can skip the virtual environment, and just install the pip packages globally.

Then just run:

```shell
$ python3 src/main.py
```

Use 'q' to quit.
