
------------------------------
## 🍎 Guide de survie des Ports sur macOS
## 1. Trouver qui utilise un port
Si Docker te dit que le port est déjà pris, tape ceci dans ton terminal :

lsof -i :5555


* COMMAND : Le nom de l'application (ex: python3.1, postgres).
* PID : Le numéro d'identification unique à utiliser pour fermer l'app.

## 2. Forcer la fermeture du processus (Kill)
Remplace <PID> par le numéro trouvé à l'étape précédente :

kill -9 <PID>


* Note : Si tu as plusieurs lignes, utilise le PID de la ligne où il est écrit LISTEN.

## 3. Libérer les ports "fantômes" de Docker
Parfois, macOS croit qu'un port est utilisé par Docker alors que le conteneur est arrêté.

# Arrête proprement tous les services du projet
docker-compose down
# Si ça persiste, redémarre le réseau Docker
docker network prune -f

## 4. Vérifier les connexions actives
Pour voir rapidement tous les ports en écoute sur ton Mac :

netstat -an | grep LISTEN

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
C'est une réaction très saine ! Voir une cinquantaine de ports ouverts peut donner l'impression que ton Mac est "encombré" ou vulnérable.
Cependant, attention : la plupart de ces ports sont utilisés par macOS lui-même pour fonctionner (AirPlay, iCloud, PyCharm, Bluetooth). Si tu tentes de tous les arrêter, ton système ou tes logiciels risquent de planter.
Voici comment faire le tri intelligemment.
------------------------------
## 🛡️ Ce que tu peux arrêter sans risque
Tu ne dois te concentrer que sur ce que tu as lancé, c'est-à-dire les ports liés à tes tests Docker et Python.

   1. Nettoyer Docker (Le plus important)
   Pour fermer les ports 5555, 5433 et tous les autres liés à tes essais, tape :
   
   docker stop $(docker ps -q)
   
   Cette commande éteint tous les conteneurs qui tournent actuellement.
   2. Nettoyer les "fantômes"
   Parfois, même après un stop, Docker garde des traces.
   
   docker system prune -f
   
   
------------------------------
## 🚫 Ce que tu ne dois PAS arrêter
Sur ta capture d'écran, certains ports sont normaux et vitaux pour ton Mac :

* Port 5000 : Utilisé par macOS pour AirPlay / Control Center.
* Port 7000 : Souvent utilisé par le système pour le partage de fichiers ou AirPlay.
* Ports 445 / 88 : Services système pour les réseaux et la sécurité (Kerberos/SMB).
* Ports très élevés (ex: 63342) : Ce sont des ports temporaires ouverts par PyCharm pour communiquer avec ton navigateur ou ses propres extensions.

------------------------------
## 💡 La règle d'or pour un Data Analyst
Ne t'occupe que du port que tu as défini dans ton fichier docker-compose.yml.
Le plan d'action pour repartir sur une base propre :

   1. Ferme PyCharm.
   2. Ouvre ton Terminal et tape : docker-compose down (dans le dossier de ton projet).
   3. Redémarre Docker Desktop.
   4. Relance uniquement ton projet : docker-compose up -d.

À ce moment-là, si tu refais un lsof ou netstat, tu ne devrais voir qu'un seul port (ex: 5433) lié à ton travail. Tous les autres appartiennent au système et tu peux les ignorer.
------------------------------
## 📝 Note pour ton fichier .md

Conseil de sécurité/propreté :
Avant de commencer une session de travail, faire un docker ps pour voir ce qui tourne. Si trop de choses sont présentes, utiliser docker stop $(docker ps -q) pour faire le vide et ne relancer que le nécessaire.

