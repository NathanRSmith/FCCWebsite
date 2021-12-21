make a Python virtualenv

    pip install -r requirements.txt
    nodeenv -p --prebuilt
    npm install -g bower
    bower install
    env ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future" pip install fabric

To build:

    python build.py

Built site is in build directory.

    open build/index.html

To push to gh-pages

    ghp-import -np build


--------------------------
Deploying to the Live Site
--------------------------

Follow the standard workflow.  Make changes, `python build.py` and preview locally from `build/`.
When ready, `ghp -np build/` & `git commit -am '<comment>'`.
Preview on GitHub (http://nathanrsmith.github.io/FCCWebsite/).
If everything looks ok, deploy to the server `fab remote deploy` and enter the hosting username/password when prompted.


-----
Notes
-----

Revolution Slider Docs: http://catapultthemes.com/documentation/documentation.html
