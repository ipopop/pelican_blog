##### My Live test : 🚀 [pelican_blog](https://ipopop.github.io/pelican_blog/)

##### Official Pelican

[getpelican.com](https://getpelican.com/)

![](Screenshot-blog.jpg)

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

##### List of themes :

```markdown

|'BT3-Flat' | (https://github.com/KenMercusLai/BT3-Flat.git)  | 'BT3-Flat' |
|'Casper2Pelican' | (https://github.com/abr4xas/Casper2Pelican.git)  | 'Casper2Pelican' |
|'Flex' | (https://github.com/alexandrevicenzi/Flex.git)  | 'Flex' |
|'MinimalXY' | (https://github.com/petrnohejl/MinimalXY.git)  | 'MinimalXY' |
|'Nuja' | (https://github.com/allenskd/Nuja.git)  | 'Nuja' |
|'Papyrus' | (https://github.com/aleylara/Papyrus)  | 'Papyrus' |
|'Responsive-Pelican' | (https://github.com/ir193/Responsive-Pelican.git)  | 'Responsive-Pelican' |
|'alchemy' | (https://github.com/nairobilug/pelican-alchemy.git)  | 'alchemy' |
|'apricot' | (https://github.com/livibetter-backup/apricot.git)  | 'apricot' |
|'attila' | (https://github.com/arulrajnet/attila)  | 'attila' |
|'blue-penguin' | (https://github.com/jody-frankowski/blue-penguin.git)  | 'blue-penguin' |
|'blue-penguin-dark' | (https://github.com/tcarwash/blue-penguin-dark.git)  | 'blue-penguin-dark' |
|'bluegrasshopper' | (https://github.com/gregseth/pelican-bgh.git)  | 'bluegrasshopper' |
|'bold' | (https://github.com/demianbrecht/pelican-bold.git)  | 'bold' |
|'brutalist' | (https://github.com/mamcmanus/brutalist.git)  | 'brutalist' |
|'bulrush' | (https://github.com/textbook/bulrush.git)  | 'bulrush' |
|'burrito' | (https://github.com/fly/burrito.git)  | 'burrito' |
|'buruma' | (https://github.com/ivanhercaz/buruma.git)  | 'buruma' |
|'chameleon' | (https://github.com/yuex/pelican-iliork.git)  | 'chameleon' |
|'chunk' | (https://github.com/tbunnyman/pelican-chunk.git)  | 'chunk' |
|'cid' | (https://github.com/hdra/Pelican-Cid.git)  | 'cid' |
|'clean-blog' | (https://github.com/gilsondev/pelican-clean-blog.git)  | 'clean-blog' |
|'crowsfoot' | (https://github.com/porterjamesj/crowsfoot.git)  | 'crowsfoot' |
|'dev-random3' | (https://github.com/22decembre/dev-random3.git)  | 'dev-random3' |
|'eevee' | (https://github.com/kura/eevee.git)  | 'eevee' |
|'elegant' | (https://github.com/Pelican-Elegant/elegant.git)  | 'elegant' |
|'free-agent' | (https://github.com/callmefish/pelican-free-agent.git)  | 'free-agent' |
|'fresh' | (https://github.com/jsliang/pelican-fresh.git)  | 'fresh' |
|'genus' | (https://github.com/vaiski/genus.git)  | 'genus' |
|'html5-dopetrope' | (https://github.com/PierrePaul/html5-dopetrope.git)  | 'html5-dopetrope' |
|'hyde' | (https://github.com/jvanz/pelican-hyde.git)  | 'hyde' |
|'irfan' | (https://github.com/erfaan/pelican-theme-irfan.git)  | 'irfan' |
|'iris' | (https://github.com/slok/iris.git)  | 'iris' |
|'jesuislibre' | (https://github.com/badele/pelican-theme-jesuislibre.git)  | 'jesuislibre' |
|'jojo' | (https://github.com/dokelung/jojo.git)  | 'jojo' |
|'lannisport' | (https://github.com/siovene/lannisport.git)  | 'lannisport' |
|'lazystrap' | (https://github.com/lazycoder-ru/lazystrap.git)  | 'lazystrap' |
|'lovers' | (https://github.com/chdoig/pelican-bootstrap3-lovers.git)  | 'lovers' |
|'maggner-pelican' | (https://github.com/kplaube/maggner-pelican.git)  | 'maggner-pelican' |
|'martin-pelican' | (https://github.com/cpaulik/martin-pelican.git)  | 'martin-pelican' |
|'material' | (https://github.com/greizgh/pelican-material.git)  | 'material' |
|'materialistic' | (https://github.com/eswarm/materialistic-pelican.git)  | 'materialistic' |
|'mediumfox' | (https://github.com/cprieto/pelican-mediumfox.git)  | 'mediumfox' |
|'medius' | (https://github.com/onuraslan/medius.git)  | 'medius' |
|'mg' | (https://github.com/lucachr/pelican-mg.git)  | 'mg' |
|'neat' | (https://github.com/BYK/pelican-neat.git)  | 'neat' |
|'nest' | (https://github.com/molivier/nest.git)  | 'nest' |
|'nice-blog' | (https://github.com/guilherme-toti/nice-blog.git)  | 'nice-blog' |
|'nikhil-theme' | (https://github.com/gunchu/nikhil-theme.git)  | 'nikhil-theme' |
|'niu-x2' | (https://github.com/wilbur-ma/niu-x2.git)  | 'niu-x2' |
|'octopress' | (https://github.com/MrSenko/pelican-octopress-theme)  | 'octopress' |
|'pelican-b-side' | (https://gitlab.com/jhauh/pelican_b_side.git)  | 'pelican-b-side' |
|'pelican-blue' | (https://github.com/Parbhat/pelican-blue.git)  | 'pelican-blue' |
|'pelican-cait' | (https://github.com/hdra/pelican-cait.git)  | 'pelican-cait' |
|'pelican-fh5co-marble' | (https://github.com/claudio-walser/pelican-fh5co-marble.git)  | 'pelican-fh5co-marble' |
|'pelican-hss' | (https://github.com/laughk/pelican-hss.git)  | 'pelican-hss' |
|'pelican-mockingbird' | (https://github.com/wrl/pelican-mockingbird.git)  | 'pelican-mockingbird' |
|'pelican-simplegrey' | (https://github.com/fle/pelican-simplegrey.git)  | 'pelican-simplegrey' |
|'pelican-sober' | (https://github.com/fle/pelican-sober.git)  | 'pelican-sober' |
|'pelican-twitchy' | (https://github.com/ingwinlu/pelican-twitchy.git)  | 'pelican-twitchy' |
|'pelicanthemes-generator' | (https://github.com/badele/pelicanthemes-generator.git)  | 'pelicanthemes-generator' |
|'pjport' | (https://github.com/xm3ron/pjport.git)  | 'pjport' |
|'plumage' | (https://github.com/kdeldycke/plumage.git)  | 'plumage' |
|'pujangga' | (https://github.com/habibillah/pujangga.git)  | 'pujangga' |
|'relapse' | (https://github.com/wamonite/relapse.git)  | 'relapse' |
|'resume' | (https://github.com/suheb/resume.git)  | 'resume' |
|'semantic-ui' | (https://github.com/ellisonleao/pelican-semantic-ui.git)  | 'semantic-ui' |
|'simplify-theme' | (https://github.com/vuquangtrong/simplify-theme.git)  | 'simplify-theme' |
|'smoothie' | (https://github.com/kdheepak89/pelican-smoothie.git)  | 'smoothie' |
|'sora' | (https://github.com/if1live/pelican-sora.git)  | 'sora' |
|'stirring' | (https://github.com/hansliu/pelican-stirring.git)  | 'stirring' |
|'storm' | (https://github.com/redVi/storm.git)  | 'storm' |
|'sundown' | (https://github.com/keningle/pelican-sundown.git)  | 'sundown' |
|'svbhack' | (https://github.com/gfidente/pelican-svbhack.git)  | 'svbhack' |
|'svbtle' | (https://github.com/wting/pelican-svbtle.git)  | 'svbtle' |
|'taman' | (https://github.com/karambir/taman.git)  | 'taman' |
|'twenty-html5up' | (https://github.com/frankV/twenty-pelican-html5up.git)  | 'twenty-html5up' |
|'voce' | (https://github.com/limbenjamin/voce.git)  | 'voce' |
|'voidy-bootstrap' | (https://github.com/robulouski/voidy-bootstrap.git)  | 'voidy-bootstrap' |
|'w3-personal-blog' | (https://github.com/samael500/w3-personal-blog.git)  | 'w3-personal-blog' |
|'water-iris' | (https://github.com/jarv/water-iris.git)  | 'water-iris' |
|'yapeme' | (https://github.com/kplaube/yapeme.git)  | 'yapeme' |
```
