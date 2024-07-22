# codewithmpia

Bienvenue sur le dépôt GitHub de mon blog personnel ! Dans ce dépôt, vous trouverez le code source et les ressources nécessaires utlisées pour coder codewithmpia.

Vous pouvez visitez ce blog ici: [codewithmpia.pythonanywhere.com/](https://codewithmpia.pythonanywhere.com/)

## Aperçu

![Capture d'écran de la page d'accueil](/contents/assets/static/images/screenshots/screenshot-lg.png)

codewithmpia est un site web personnel où je partage mes réflexions, mes idées et mes projets. Il est construit à l'aide de Flask, un micro-framework web Python, et utilise MYSQL comme base de données. Le site comprend les fonctionnalités suivantes :

* Une page d'accueil qui affiche tous les articles publiés
* Une barre de recherche pour rechercher des articles par mot-clé
* Une page pour chaque article, avec la possibilité de laisser des commentaires

## Installation

Pour installer et exécuter codewithmpia localement, suivez les étapes suivantes :

1. Clonez ce dépôt GitHub sur votre ordinateur local :
```
git clone https://github.com/votre-nom-utilisateur/mon-blog.git
```

2. Créez un environnement virtuel Python et activez-le :
```bash
python3 -m venv env

source env/bin/activate
```

3. Installez les dépendances requises à l'aide de pip :
```
pip install -r requirements.txt
```

4. Créez un fichier `.env` dans le répertoire racine du projet et définissez les variables d'environnement nécessaires :

```makefile
SECRET_KEY=votre-clé-secrète

DATABASE_URI=mysql+pymysql://utlisateur:mot-de-passe@host:3306/base-de-donnee

ou si vous préferez le sqlite:
DEV_DB = f"sqlite:///{BASE_DIR}/db.sqlite3"
```

5. Exécutez l'application Flask en utilisant la commande suivante :
```python run_app.py 
```
6. Accédez à `http://localhost:5000` dans votre navigateur web pour afficher codewithmpia.

## Déploiement

Pour le déploiement, le choix est libre. Vous pouvez choisir n'importe quel hébergeur selon vos moyens mais à une seule condition: la prise en charge de Python. 

## Licence

codewithmpia est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

Merci d'avoir visité codewithmpia !

## Quelques captures:

![Capture d'écran de la page de detail d'un article](/contents/assets/static/images/screenshots/screenshot-lg-2.png)

![Capture d'écran de la page d'accueil pour mobile](/contents/assets/static/images/screenshots/screenshot-sm.png)

