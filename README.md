# P12_FOSTER_Harris

##epic_events

Projet 12 OpenClassrooms

### epic_events Entity Relation Diagram
[ERD](ERD_epic_events.pdf)

## API RESTful (back-end) de gestion de clients/événements/contrats (CRM) qui permet aux utilisateurs de :
- S'authentifier grâce à leurs informations de compte 
- Créer/modifier/supprimer des clients selon leurs permissions 
- Créer/modifier/supprimer des contrats selon leurs permissions 
- Créer/modifier/supprimer des événements selon leurs permissions 
- Lire les informations associées aux utilisateurs/teams selon leurs permissions

L'API utilise des endpoints (points de terminaison) pour servir les données. L'Espace admin est le seul moyen de supprimer la plupart des données, ceci crée un niveau de sécurité supplémentaire pour les données.


### Documentation de l'API
- Documentation Postman disponible [ici](https://documenter.getpostman.com/view/14998980/UVkgwyh7)
- Tous les endpoints sont inclus et documentés

## Prérequis de base
- Une application de type 'terminal' - GitBash, Mintty, Cygwin (si vous êtes sur Windows) 
   ou les terminaux par défaut si vous utilisez Macintosh ou Linux. 
- Python 3.9
- Django 4.0.2

## Installation
### Pour les développeurs et utilisateurs (windows 10/11, mac, linux) :
#### Clonez la source de epic_events localement (en utilisant votre terminal) :
```sh
$ git clone https://github.com/harrisafoster/P12_FOSTER_Harris
$ cd P12_FOSTER_Harris
```
##### Dans votre terminal dans le dossier P12_FOSTER_Harris/ : Créer et activer un environnement virtuel avec (windows 10) :
```sh
$ python -m venv env
$ source ./env/Scripts/activate
```
##### Créer et activer un environnement virtuel avec (mac & linux) :
```sh
$ virtualenv venv
$ source venv/bin/activate
```
##### Installez les packages requis avec :
```sh
$ pip install -r requirements.txt
```
#### Générez votre propre SECRET_KEY :
Vous allez remarquer que vous n'avez pas de fichier secret_settings.py et c'est normal. Cette étape permet de
protéger la clé secrète de l'API. Pour créer, renseigner et utiliser votre nouvelle clé secrète veuillez suivre les 
étapes ci-dessous :
```sh
$ cd SoftDesk
$ touch secret_settings.py
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Une fois que vous aurez votre nouvelle clé secrète générée, mettez-la dans votre secret_settings.py exactement comme ceci:  
KEY = votre_nouvelle_clé

Après avoir fait cela, l'import de votre nouvelle clé secrète fonctionnera'

#### Créez et configurer votre DB PostGreSQL : 
- Installez PostgreSQL [ici](https://www.postgresql.org/download/)
- Utilisez l'application pgAdmin 4 pour créer votre base de données (object -> create -> database) et nommez-la comme vous le souhaitez (exemple : epic_db)
- Il vous sera demandé de créer un nom d'utilisateur pour votre DB ainsi qu'un mot de passe. Créez-les et notez-les
- Ensuite vous devrez renseigner ces informations dans votre secret_settings.py :
  - DB_USERNAME(votre nom d'utilisateur pour votre DB)
  - DB_PASSWORD(votre mot de passe pour ce même DB)
  - DB_NAME(ex. epic_db)
  - DB_HOST(par défaut : localhost)
  - DB_PORT(par défaut : 5432)

Une fois que vous aurez effectué ces étapes (ci-dessus), 
votre DB sera configuré et les imports relatifs au DB fonctionneront.

##### Après avoir configuré votre DB, faites les migrations nécessaires avec :
```sh
$ python manage.py migrate
```

#### Créez votre utilisateur admin avec :
```sh
$ python manage.py createsuperuser
```
## Utilisation
### Vous pouvez mettre l'API epic_events en route depuis votre terminal avec :
```sh
$ python manage.py runserver
```
Puis accédez à l'API via le port 8000 sur votre navigateur sur http://127.0.0.1:8000/

###Logging
- Veuillez vous référer au fichier errors.logs (racine/logging/errors.logs)

## Built with
Python 3.9 

Django 4.0.2

Django API REST - 3.13.1

Django JWT Authentication - 5.0.0

PostgreSQl 14
