
# Projet O9 : Implémentation d'un système de régulation dynamique de vitesses basé sur les véhicules connectés
## Préambule : Installation de Sumo
<a href = "https://github.com/licit-lab/ITSProjects/blob/415797d33cd19d347c11a93686661d55a7af4943/Projet09-VSL/SUMO_installation/notice_installation"> Pour installer SUMO et vérifier le bon fonctionnement des simulations <a/>
## Introduction 

<p align="center">
  <img src="https://github.com/licit-lab/ITSProjects/blob/bc9f7715036f5477dbb52d34f2447863a14cb2a6/Projet09-VSL/images/Capture%20d%E2%80%99%C3%A9cran%202021-12-15%20%C3%A0%2013.18.00.png">
</p>


Les systèmes de régulation dynamiques consistent à:
  1) détecter dynamiquement une zone de congestion sur une voie rapide
  2) donner une consigne de limitation de vitesse en amont de cette zone
  
<p align="center">
  <img src="https://github.com/licit-lab/ITSProjects/blob/d1a9542a1551a1d77dae1b51503c3b283d9c1ec0/Projet09-VSL/images/Capture%20d%E2%80%99%C3%A9cran%202021-12-15%20%C3%A0%2013.31.13.png">
</p>

Le but est ainsi de limiter le flux arrivant sur la zone de congestion pour limiter sa propagation voir même la dissiper.

Le système détermine donc à partir de quelle distance et pour combien de temps il est nécessaire que les véhicules appliquent la limitation de vitesse pour que la congestion soit dissipée lorsque ces derniers entre sur la zone de ralentissement.
  
## Objectifs du projet
Le projet a pour objectifs : 
  1) Prendre en main les outils de simulation SUMO/TRACI
  2) Implémenter un système de régulation dynamique des vitesses simplifié et basé sur les véhicules connectés
  3) Appréhender la sensibilité d'un tel système au taux de pénétration (nombre de véhicules connectés/nombre total de véhicules
  4) Explorer le potentiel des véhicules connectés pour 1) assurer l'efficacité du système de contrôle même à taux de pénétration réduit 1bis) combiner différentes stratégies de contrôle pour en assurer une inédite et plus efficace.

## TP 
Présentation du réseau.
<p align="center">
  <img src="https://github.com/licit-lab/ITSProjects/blob/eccc2893c04f549d760106183d820d9bf9614af8/Projet09-VSL/images/scenario.png">
</p>
  
<a href = "https://github.com/licit-lab/ITSProjects/blob/7f741b3e599073e9f100c87ce424868b322bbc0b/Projet09-VSL/Projet09-VSL.ypnb.ipynb"> Le sujet du TP est un jupyter notebook. <a/> La version complétée de ce jupyter (comprenant vos réponses) constituera votre rendu.
<a href = "https://github.com/licit-lab/ITSProjects/blob/84ce81ab236960da50563422684ba01f02a958e1/Projet09-VSL/TP_simulation/run_simulation"> Vous pouvez récupérer les fichiers de simulation et le  script python à compléter ici. <a/> Votre script python complété est également attendu dans votre rendu final.
  
## Outils pour traiter les fichiers de sortie
Lien vers fichier de traitement. Pour vous aider à analyser les fichiers de sortie vous pouvez aller voir ici.
## Liens utiles 
<a href ="https://sumo.dlr.de/docs/"> Pour aller voir la documentation SUMO <a/>  
<a href ="https://sumo.dlr.de/docs/TraCI.html"> Pour aller voir la documentation TRACI <a/>  
