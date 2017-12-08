# SmartHome
An IoT and smart home project using a raspbery PI
## Modules
Temperature Module -> detect room temperature and control the heating system
Movement sensor module -> detect movements and switch on the lights
## How to manage the front-end

Donc faut installer node-red qui est un outil hyper pratique pour justement
effectuer du traitement sur IoT qui fonctionne comme un drag and drop pour
l'installer => "sudo npm install -g --unsafe-perm node-red"
Une fois que c'est installé il suffit de taper "node-red" dans le terminal et ça démarre, faut ensuite copier/coller l'url indiqué dans le terminal dans
un navigateur web et là t'auras accès à l'outil
J'ai pas préciser mais tout ça faut le faire directement sur le raspberry

### First steps
Mais faut rajouter des éléments car là l'outil est brut sans add-on donc faut
aller dans "manage palette" présent dans le menu à droite
en haut il y aura 2 onglets: "Nodes" et "Install", faut aller dans instal et
rechercher 2 utilitaires: "node-red-contrib-ds18b20-sensor" et
"node-red-dashboard"
Si tout fonctionne correctement si tu veux test:
Ce tuto est court est vraiment bien pour se faire la main avec les led sur raspberry
https://www.youtube.com/watch?v=CiIQ3BTI7aw

### Heating system:
part1: https://www.youtube.com/watch?v=M0Mjo0J1X_Q
part2: https://www.youtube.com/watch?v=UKv4_jvPtr4

## Install Node.js
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
