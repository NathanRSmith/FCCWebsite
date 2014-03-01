make a Python virtualenv

    pip install -r requirements.txt
    nodeenv -p
    npm install -g bower
    bower install

To build:

    python build.py

Built site is in build directory.

    cd build
    python -m SimpleHTTPServer