<h1 align="center">Bienvenue dans Résidences CROUS Notifier <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px"> </h1>
<p align="center">

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
![](https://img.shields.io/badge/OS-Linux-informational?style=flat&logo=linux&logoColor=white&color=40c640)
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=40c640)
![](https://img.shields.io/badge/Automation-Cron-informational?style=flat&logo=linux&logoColor=white&color=blue)
    
## Description 
Résidences CROUS Notifier est un bot Telegram conçu pour surveiller et notifier en temps réel les logements disponibles dans les résidences CROUS à Strasbourg. Ce bot envoie des mises à jour automatiques toutes les 15 minutes avec le nombre total de logements disponibles par résidence et vous permet de rester informé(e) sans effort.

✨ **Fonctionnalités principales** :
- 🔔 Notifications automatiques pour chaque résidence sélectionnée.
- 🏢 Possibilité de choisir des résidences spécifiques ou toutes les résidences.
- 🚫 Commande pour se désabonner des notifications à tout moment.
- ⚡ Interface simple et rapide pour rester informé des disponibilités.

---

## Installation <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30">

1. **Clonez ce projet**
```
git clone https://github.com/Ali-Mahdiyanjoo/CrousResidenceNotifier
cd CrousResidenceNotifier
```

2. **Créez un environnement virtuel et installez les dépendances**
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. **Configurer les identifiants du bot**
   - Récupérez un jeton Telegram via le [BotFather](https://core.telegram.org/bots#botfather).
   - Ajoutez votre jeton dans le fichier `main.py` et `sender.py` comme valeur de `TELEGRAM_BOT_TOKEN`.

4. **Définir un Cron Job**
   Configurez un cron job pour exécuter `sender.py` toutes les 15 minutes :
   ```
   crontab -e
   ```
   Ajoutez la ligne suivante :
   ```
   */15 * * * * /usr/bin/python3 /path/to/your/project/sender.py >> /path/to/your/project/cron.log 2>&1
   ```

5. **Exécuter le bot**
   Démarrez le bot en arrière-plan pour gérer les commandes `/start`, `/stop` et `/help` :
   ```
   nohup python3 main.py &
   ```

---

##  <img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60"> Contributing

Les contributions, problèmes et demandes de fonctionnalités sont les bienvenus.<br />
N'hésitez pas à vérifier la [page des problèmes](https://github.com/Ali-Mahdiyanjoo/CrousResidenceNotifier/issues) pour contribuer.

---

## 🖥 👨‍💻 Author 👨‍💻 🖥 
 
👤 **Ali Mahdiyanjoo**

- Github: [@Ali-Mahdiyanjoo](https://github.com/Ali-Mahdiyanjoo)
- LinkedIn: [@Ali-Mahdiyanjoo](https://ir.linkedin.com/in/ali-mahdiyanjoo-1452101b6)

---

## 📝 License

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT). Consultez le fichier LICENSE pour plus d'informations.
