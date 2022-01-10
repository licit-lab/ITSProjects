
# Projet O9 : Implémentation d'un système de régulation dynamique de vitesses basé sur les véhicules connectés
## Préambule : Installation de Sumo
<a href = "https://github.com/licit-lab/ITSProjects/blob/415797d33cd19d347c11a93686661d55a7af4943/Projet09-VSL/SUMO_installation/notice_installation"> Pour installer SUMO et vérifier le bon fonctionnement des simulations <a/>
## Introduction 

Des incidents sur le réseau (accidents, conditions météréologiques dégradées, etc) ou des contraintes propres à celui-ci (réduction du nombre de voies, voie d'insertion) peuvent entrainer des conditions de trafic dégradées voir des ondes de congestion qui se propagent sur le réseau. Pour contrer ces phénomènes, les gestionnaires d'infrastructures mettent en place des stratégies de régulation de trafic qui consistent à 1) détecter un évènement sur le réseau, 2) le caractériser et 3) anticiper sa propagation spatiale et temporelle.  Les stratégies de régulations ont pour objectif d'améliorer le trafic, que ce soit en terme d'efficacité (réduction des temps de parcours des usagers, augmentation du flux de véhicules, etc), de sécurité (en réduisant les différences de vitesses entre les véhicules par exemple) ou d'environnement (en réduisant les émissions de CO2 par exemple). 
 
  
<p align="center">
  <img src=https://github.com/licit-lab/ITSProjects/blob/ee12aa059e0ff7ddcdd0b11ed0bda60bc9350e1d/Projet09-VSL/images/Capture%20d%E2%80%99%C3%A9cran%202021-12-15%20%C3%A0%2013.18.00.png width="800">
</p>


De nouvelles stratégies de contrôle, associés au développement des Systèmes de Transport Intelligent (STI) et notamment des Véhicules Connectés (VC), ont été développées à partir des années 90. Les systèmes de régulation dynamiques de vitesses font ainsi partie des plus populaires d'entre elles dans la littérature. Ils  consistent à:
  1) détecter dynamiquement une zone de congestion sur une voie rapide
  2) donner une consigne de limitation de vitesse en amont de cette zone.
  
Le but est ainsi de limiter le flux arrivant sur la zone de congestion pour limiter sa propagation voir même la dissiper.

Les systèmes déterminent donc à partir de quelle distance et pour combien de temps il est nécessaire que les véhicules appliquent la limitation de vitesse pour que la congestion soit dissipée lorsque ceux-ci arrivent sur la zone de ralentissement.
 
Si en premier lieu, ces systèmes reposaient sur les données issus des boucles électromagnétiques pour trouver la distance et le temps optimum de limitation de vitesse et sur les Panneaux à Messages Variables (PMV) pour délivrer le contrôle, certains reposent désormaisne  entièrement sur les VC et la communication I2V( Infrastructure-Véhicule) (à l'aide d'Unités de Bords de Route (UBR)).

<p align="center">
  <img src=https://github.com/licit-lab/ITSProjects/blob/05e6a1fa86d3e3550ce92b921415096289104123/Projet09-VSL/images/Capture%20d%E2%80%99%C3%A9cran%202021-12-15%20%C3%A0%2013.31.13.png width="600">
</p>

Ici, on ne s'intéressera qu'à l'impact des VC pour délivrer le contrôle. 
  
## Objectifs du projet
Le projet a pour objectifs : 
  1) Prendre en main les outils de simulation SUMO/TRACI;
  2) Implémenter un système de régulation dynamique des vitesses simplifié et où le contrôle est basé sur les véhicules connectés;
  3) Appréhender la sensibilité d'un tel système au taux de pénétration (nombre de véhicules connectés/nombre total de véhicules;
  4) Explorer le potentiel des véhicules connectés pour 1) assurer l'efficacité du système de contrôle même à taux de pénétration réduit 1bis) combiner différentes stratégies de contrôle pour en implémenter une nouvelle, inédite et plus efficace.

## TP 
Le réseau d'étude est présenté dans le schéma ci-dessous.
<p align="center">
  <img src=https://github.com/licit-lab/ITSProjects/blob/84ce81ab236960da50563422684ba01f02a958e1/Projet09-VSL/images/scenarioITS.png width="600">
</p>
  
<a href = "https://github.com/licit-lab/ITSProjects/blob/7f741b3e599073e9f100c87ce424868b322bbc0b/Projet09-VSL/Projet09-VSL.ypnb.ipynb"> Le sujet du TP est un jupyter notebook. <a/> La version complétée de ce jupyter (comprenant vos réponses) constituera votre rendu.
<a href = "https://github.com/licit-lab/ITSProjects/blob/84ce81ab236960da50563422684ba01f02a958e1/Projet09-VSL/TP_simulation/run_simulation"> Vous pouvez récupérer les fichiers de simulation et le  script python à compléter ici. <a/> Votre script python complété est également attendu dans votre rendu final.
  
## Outils pour traiter les fichiers de sortie
<a href = "https://github.com/licit-lab/ITSProjects/blob/13b5563437d8c0f3f47b7006e9955b382b85f398/Projet09-VSL/Outils_analyses.ipynb">  Pour vous aider à analyser les fichiers de sortie, vous pouvez aller voir ici. <a/>
Pour convertir vos fichiers xml en fichiers csv, vous pouvez utiliser la commande suivante dans votre terminal : python tools/xml/xml2csv.py nom_fichier.xml
 
## Liens utiles 
<a href ="https://sumo.dlr.de/docs/"> Pour aller voir la documentation SUMO <a/>  
<a href ="https://sumo.dlr.de/docs/TraCI.html"> Pour aller voir la documentation TRACI <a/>  
