

Version-0.1

<br/>

<p align="center">
 <h2 align="center">Log management</h2>
 <h3 align="center">With Python3.8 and syslog-ng</h3>
</p>

</br>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built with</a></li>
      </ul>
    </li>
    </br>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        </br>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#usage">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
<li><a href="#contact">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

<p align="center">
 <h4 align="center">About The Project</h4>
</p>

Hey, pour mon premier projet publique j'ai décidé de créer un script python permettant d'automatiser la gestions de logs cisco(router et switch) basé sur syslog-ng.

Je compte créer 2 scripts différents, le premier sera en cli et le second sera en GUI.

Ces derniers serviront afficher les logs socké par syslog-ng avec différentes fonctions facilitant l'affichage des logs. (Trier par date, trier par niveau de logs..)

<!-- BUILT WITH -->

<p align="center">
 <h4 align="center">Built with</h4>
</p>

Pour l'instant j'utilise seulement Syslog-ng et Python 3.8, je n'ai pas encore utilisé de librairie particulière pour ce dernier, pour ma part j'ai utilisé les distribution linux Ubuntu 20.04 et Debian 10. 

Avoir des appareils cisco pour récuprer ses propres logs. (Si vous n'en avez pas à disposition j'ai déposé quelques fichiers logs dans le fichier cisco).

* [Syslog-ng](https://www.syslog-ng.com/)
* [Python](https://www.python.org/)
* [Ubuntu](https://ubuntu.com/)/[Debian](https://www.debian.org/)

<!-- GETTING STARTED -->

<p align="center">
 <h4 align="center">Getting Started</h4>
</p>

Pour l'utilisation du script:

 1. Cloner de dépôt.

 2. Installer les paquets.

 3. Suivre l'installation plus bas.

    

    <!-- PREREQUISITES -->

<p align="center">
 <h4 align="center">Prerequisites</h4>
</p>

Avoir des appareils cisco pour récuprer ses propres logs

Installer la version 3 de Python.

* Python
  ```sh
  apt install python3
  ```

* Syslog-ng

  ```sh
  apt install syslog-ng
  ```

  <!-- INSTALLATION -->

  <p align="center">
   <h4 align="center">Installation</h4>
  </p>

  Pour récuperer des logs cisco remplacer le fichier syslog-ng.conf dans le repertoir /etc/syslog-ng/ par celui du dépôt.

  ```sh
  mv syslog-ng.conf etc/syslog-ng/syslog-ng.conf
  ```

  Si vous n'avez pas d'appareils cisco déplacé le dossier cisco dans /var/log/

  ```sh
  mv cisco/ /var/log/
  ```

  Ajouter le droit d'éxecution sur le script log.py

  ```sh
  chmod +x log.py
  ```

<!-- USAGE  -->

<p align="center">
 <h4 align="center">Usage</h4>
</p>

Futur vidéo de l'utilisation du script.

<!-- CONTRIBUTING -->
<p align="center">
 <h4 align="center">Contributing</h4>
</p>

Je reste ouvert à tout type d'idée, de fonction à ajouter, ou de l'optimisation de code en pull request.

<!-- CONTACT -->
<p align="center">
 <h4 align="center">Contact</h4>
</p>

Ethost - [LinkedIn](https://www.linkedin.com/in/morin-julien/)

Project Link: https://github.com/Ethost/python_log

<!-- ACKNOWLEDGEMENTS -->

<p align="center">
 <h4 align="center">Acknowledgements</h4>
</p>

* [GitHub README-TEMPLATE](https://github.com/othneildrew/Best-README-Template)




