##### Memo :
 
```sh
pip install pelican
pip install --upgrade pip
pip install pelican
pelican-quickstart
pelican content
pelican --listen
mkdir -p static/admin
touch static/admin/config.yml
pelican content
pelican --listen
git init
git remote add origin git@github.com:<your_repo_name_here>/pelican_blog.git
git branch -M main
git push -u origin main
cp ~/.gitignore_global ./.gitignore
git branch -M master main
git push --set-upstream origin main
pip install pelican markdown ghp-import
ghp-import output -b gh-pages\ngit push origin gh-pages\n
mkdir ./content/images
pelican content -s publishconf.py
git status
git add -a && git commit -m 'deploy on gh-pages'
python -m pip install invoke
pelican content -s publishconf.py
pelican --listen
ghp-import output -b gh-pages\ngit push origin gh-pages\n
```
