
# Projet O9 : Implémentation d'un système de régulation dynamique de vitesses basé sur les véhicules connectés
## Préambule : Installation de Sumo
<a href = "https://github.com/licit-lab/ITSProjects/blob/415797d33cd19d347c11a93686661d55a7af4943/Projet09-VSL/SUMO_installation/notice_installation"> Pour installer SUMO et vérifier le bon fonctionnement des simulations <a/>
## Introduction 

  
<img src=" https://github.com/Ifsttar/PedSim/blob/master/docs/images/rapports/figure%204.2%20%5B1%5D%20p%2076.png">

   
Les systèmes de régulation dynamiques consistent à:
  1) détecter dynamiquement une zone de congestion sur une voie rapide
  2) donner une consigne de limitation de vitesse en amont de cette zone

Le but est ainsi de limiter le flux arrivant sur la zone de congestion pour limiter sa propagation voir même la dissiper.

Le système détermine donc à partir de quelle distance et pour combien de temps il est nécessaire que les véhicules appliquent la limitation de vitesse pour que la congestion soit dissipée lorsque ces derniers entre sur la zone de ralentissement.
  
## Objectifs du projet
Le projet a pour objectifs : 
  1) Prendre en main les outils de simulation SUMO/TRACI
  2) Implémenter un système de régulation dynamique des vitesses simplifié et basé sur les véhicules connectés
  3) Appréhender la sensibilité d'un tel système au taux de pénétration (nombre de véhicules connectés/nombre total de véhicules
  4) Explorer le potentiel des véhicules connectés pour 1) assurer l'efficacité du système de contrôle même à taux de pénétration réduit 1bis) combiner différentes stratégies de contrôle pour en assurer une inédite et plus efficace.

## TP 
<a href = "https://github.com/licit-lab/ITSProjects/blob/7f741b3e599073e9f100c87ce424868b322bbc0b/Projet09-VSL/Projet09-VSL.ypnb.ipynb"> Le sujet du TP est un jupyter notebook. <a/> La version complétée de ce jupyter (comprenant vos réponses) constituera votre rendu.
<a href = "https://github.com/licit-lab/ITSProjects/blob/84ce81ab236960da50563422684ba01f02a958e1/Projet09-VSL/TP_simulation/run_simulation"> Vous pouvez récupérer les fichiers de simulation et le  script python à compléter ici. <a/> Votre script python complété est également attendu dans votre rendu final.
  
## Outils pour traiter les fichiers de sortie
Lien vers fichier de traitement. Pour vous aider à analyser les fichiers de sortie vous pouvez aller voir ici.
## Liens utiles 
<a href ="https://sumo.dlr.de/docs/"> Pour aller voir la documentation SUMO <a/>  
<a href ="https://sumo.dlr.de/docs/TraCI.html"> Pour aller voir la documentation TRACI <a/>  
