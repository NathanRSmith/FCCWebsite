make a Python virtualenv

    pip install -r requirements.txt
    nodeenv -p
    npm install -g bower
    bower install
    env ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future" pip install fabric

To build:

    python build.py

Built site is in build directory.

    open build/index.html

To push to gh-pages

    ghp-import -np build

To deploy to server after building and pushing to gh-pages

    fab remote deploy


Notes

Revolution Slider Docs: http://catapultthemes.com/documentation/documentation.html