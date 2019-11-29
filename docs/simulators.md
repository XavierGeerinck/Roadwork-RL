# Simulators

The supported simulators out of the box are situated in `src/SimulatorIntegrations`. The code existing here is the code that is being utilized to hook the simulator onto a [GRPC.io](https://grpc.io) communication server.

## OpenAI

> **Note:** we recommend using Linux or Mac OS X to run the system, windows is known to cause issues under certain simulators (see: "exception: access violation reading 0x000..."). If you have windows, please utilize WSL.

### Prerequisites

- Python 3 (sudo apt install python3)
- Python 3 Pip (sudo apt install python3-pip)
- Python 3 OpenGL (sudo apt install python3-opengl)
- Ffmpeg

- [Box2D] Swig - `sudo apt install swig`
- [Box2D] Box2D - `pip3 install box2d`
- [Box2d] Box2D Kengz - `pip3 install box2d-kengz`

> **Note:** when utilizing Windows, install ["xming"](https://sourceforge.net/projects/xming/) and export the following variable in your WSL shell: `export DISPLAY=localhost:0.0`, you can also add this to the startup script with: `echo "export DISPLAY=localhost:0.0" >> ~/.bashrc`.

> **Note 2:** If you receive the error `AttributeError: 'ImageData' object has no attribute 'data'`, then install 

> **Note 3:** It seems that on **WSL 2** things are a bit more complex and you have to use `export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0`. Next to that you also have to edit the Xming `X0.hosts` file (see installation directory - e.g. `C:\Program Files (x86)\Xming`) and add your WSL ip (see ifconfig inet address). For a more permanent but unsecure option, edit the desktop launch icon to include `-ac` in the startup options

When running on a Ubuntu terminal only server, install a screen by running `sudo apt install xvfb` and starting it up with `xvfb-run -s "-screen 0 1400x900x24" bash`

### Installation

```bash
pip3 install -r requirements.txt
```

> **Note:** we utilize pyglet 1.3.2 since a more recent version breaks the OpenAI gym (more information: [https://github.com/tensorflow/agents/issues/163](https://github.com/tensorflow/agents/issues/163))

### Running the example

```bash
# Start the server
python3 server.py

# <open new window>
# Run the nodejs example
node ../../SDKs/nodejs/test.js
```

## Custom

To integrate your own custom simulator, a couple of steps have to be followed. As a high level overview, the following has to be done:

1. Installation of the simulator
2. Coding a handler that interacts with the simulator based on the `OpenAI` API
3. A serializer has to be written 