python build.py
git clone https://github.com/NathanRSmith/FCCWebsite.git .gh-pages --branch=gh-pages
cd .gh-pages/
git rm -r .
cp -r ../build/* .
touch .nojekyll
git add .
git commit -m 'built site'
git push origin gh-pages && cd .. && rm -rf .gh-pages/