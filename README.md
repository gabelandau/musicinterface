# Music Interface
This application is a Vue.js/Flask user interface for an in-home audio system that doesn't have a nice looking web interface.

## Installation Instructions
The `app/` directory of this repository contains a production-ready build of the `interface/` source directory. `api.py` is the entire flask application, which needs to be modified to include your commands for the audio system.

To get started, do the following:
1. Run `pip install flask` and `pip install -U flask_cors`
2. Run `python api.py` to start the application.