
# Projet O9 : Implémentation d'un système de régulation dynamique de vitesses basé sur les véhicules connectés
## Préambule : Installation de Sumo
Pour installer SUMO et vérifier le bon fonctionnement des simulations, cliquer
<a href = "https://github.com/licit-lab/ITSProjects/blob/1c6f270fec0ab690d6284fe3ccc3c709c10cecb4/Projet09-VSL/SUMO_installation/Fiche_installation_SUMO.pdf">  ici </a>

Au terme de l'installation de SUMO, n'oubliez pas de la tester. 
Pour ce faire, procédez par étape en s'appuyant sur le contenu du dossier SUMO_installation :
1. Ouvrir avec NetEdit le fichier `init_network.net.xml`, il fournit une description du réseau routier et de l'agencement des routes
2. Vérifier le bon fonctionnement de SUMO en lançant la simulation contenue dans le fichier `init_simulation.sumocfg`. Il suffit d'ouvrir le fichier de simualtion depuis l'interface GUI de SUMO.
3. Vérifier le bon fonctionnement de TraCI en exécutant le fichier Python `init_TP_ITS.py`:
 - Ouvrer le fichier Python `init_TP_ITS.py`pour i) changer le WorkingDirectory (au début du fichier Python) et mettre le lien vers le votre et  ii) Verifier que vous lancer la bonne simulation (à la fin du fichier Python), ici `init_simulation.sumocfg`.
 - Exécuter le fichier python depuis votre console de commande (```python your/path/to/working/directory/SUMO_installation/init_TP_ITS.py```). Vous pouvez alors observer que l'interface SUMO s'active et que les étapes de simulation défilent dans l'invite de commande de SUMO ou même celle de votre machine.

N'oubliez pas de créer l'environnment associé au projet : `environment_P07-10.yml`.

## Introduction 

Des incidents sur le réseau (accidents, conditions météréologiques dégradées, etc) ou des contraintes propres à celui-ci (réduction du nombre de voies, voie d'insertion) peuvent entrainer des conditions de trafic dégradées, voire des ondes de congestion qui se propagent sur le réseau. Pour contrer ces phénomènes, les gestionnaires d'infrastructures mettent en place des stratégies de régulation de trafic qui consistent à 
1) détecter un évènement sur le réseau, 
2) le caractériser et 
3) anticiper sa propagation spatiale et temporelle.  

Les stratégies de régulations ont pour objectif d'améliorer le trafic, que ce soit en termes d'efficacité (réduction des temps de parcours des usagers, augmentation du flux de véhicules, etc), de sécurité (en réduisant les différences de vitesses entre les véhicules par exemple) ou d'environnement (en réduisant les émissions de CO2 par exemple). 
 
  
<p align="center">
  <img src=https://github.com/licit-lab/ITSProjects/blob/ee12aa059e0ff7ddcdd0b11ed0bda60bc9350e1d/Projet09-VSL/images/Capture%20d%E2%80%99%C3%A9cran%202021-12-15%20%C3%A0%2013.18.00.png width="800">
</p>


De nouvelles stratégies de contrôle, associées au développement des Systèmes de Transport Intelligent (STI) et notamment des Véhicules Connectés (VC), ont été développées à partir des années 90. Les systèmes de régulation dynamique de vitesses font ainsi partie des plus populaires d'entre elles dans la littérature. Ils  consistent à:
  1) détecter dynamiquement une zone de congestion sur une voie rapide
  2) donner une consigne de limitation de vitesse en amont de cette zone.
  
Le but est ainsi de limiter le flux arrivant sur la zone de congestion pour limiter sa propagation, voire même la dissiper.

Les systèmes déterminent donc à partir de quelle distance et pour combien de temps il est nécessaire que les véhicules appliquent la limitation de vitesse pour que la congestion soit dissipée lorsque ceux-ci arrivent sur la zone de ralentissement.
 
Si, en premier lieu, ces systèmes reposaient sur les données issues des boucles électromagnétiques pour trouver la distance et le temps optimum de limitation de vitesse et sur les Panneaux à Messages Variables (PMV) pour délivrer le contrôle, certains reposent désormais  entièrement sur les Véhicules Connectés (VCs) et la communication I2V (Infrastructure-Véhicule), notamment en s'appuyant sur des Unités de Bords de Route (UBR) pour assurer des relais à courte-portée ou directement les TMS (Traffic Management Systems) en s'appuyant sur le réseau cellulaire longue-portée.

<p align="center">
  <img src=https://github.com/licit-lab/ITSProjects/blob/05e6a1fa86d3e3550ce92b921415096289104123/Projet09-VSL/images/Capture%20d%E2%80%99%C3%A9cran%202021-12-15%20%C3%A0%2013.31.13.png width="600">
</p>

Ici, on fera abstraction du protocole de communication et on ne s'intéressera qu'à l'usage des VCs pour délivrer le contrôle et leur impact réel sur le trafic global et les émissions de polluants associées.
  
## Objectifs du projet
Le projet a pour objectifs : 
  1) Prendre en main les outils de simulation SUMO/TRACI;
  2) Implémenter un système de régulation dynamique des vitesses simplifié et où le contrôle est basé sur les véhicules connectés;
  3) Appréhender la sensibilité d'un tel système au taux de pénétration (nombre de véhicules connectés/nombre total de véhicules;
  4) Explorer le potentiel des véhicules connectés pour 
      1) assurer l'efficacité du système de contrôle même à taux de pénétration réduit 
      2) ou combiner différentes stratégies de contrôle pour en implémenter une nouvelle, inédite et plus efficace.

## TP 
Le réseau d'étude est présenté dans le schéma ci-dessous.
<p align="center">
  <img src=https://github.com/licit-lab/ITSProjects/blob/05e6a1fa86d3e3550ce92b921415096289104123/Projet09-VSL/images/scenarioITS.png width="700">
</p>
  
<a href = "https://github.com/licit-lab/ITSProjects/blob/7f741b3e599073e9f100c87ce424868b322bbc0b/Projet09-VSL/Projet09-VSL.ypnb.ipynb"> Le sujet du TP est un jupyter notebook. </a> La version complétée de ce jupyter (comprenant vos réponses) constituera votre rendu.

Vous pouvez récupérer les fichiers de simulation et le  script python à compléter 
<a href = "https://github.com/licit-lab/ITSProjects/blob/84ce81ab236960da50563422684ba01f02a958e1/Projet09-VSL/TP_simulation/run_simulation"> ici. </a> Votre script python complété est également attendu dans votre rendu final.
  
## Outils pour traiter les fichiers de sortie
Pour vous aider à analyser les fichiers de sortie, vous pouvez aller voir 
<a href = "https://github.com/licit-lab/ITSProjects/blob/13b5563437d8c0f3f47b7006e9955b382b85f398/Projet09-VSL/Outils_analyses.ipynb">   ici. </a>
Pour convertir vos fichiers xml en fichiers csv, vous pouvez utiliser la commande suivante dans votre terminal : python tools/xml/xml2csv.py nom_fichier.xml
 
## Liens utiles 
Pour aller voir la documentation
<a href ="https://sumo.dlr.de/docs/"> SUMO </a> 

Pour aller voir la documentation 
<a href ="https://sumo.dlr.de/docs/TraCI.html">  TRACI </a>  
