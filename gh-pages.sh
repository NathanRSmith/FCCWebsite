python build.py
git clone https://github.com/NathanRSmith/FCCWebsite.git .gh-pages --branch=gh-pages
cd .gh-pages/
git rm -r .
cp -r ../build/* .
cp -r ../build/.* .
git add .
git commit -m 'built site'
git push origin
cd ..
rm -rf .gh-pages/