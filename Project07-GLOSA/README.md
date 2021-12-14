<h1 align="center">Description du projet</h1>

<h2 align="center">Analyse des impacts du GLOSA sur le traffic</h2>

<div align="justify">
<br/> Le principale objectif de ce proket est de comprendre l'impactes du GLOSA sur le traffic, notamment à l'approche d'un feux de circulation dans un millieu urbain. 
</div>

<h2 align="center" id="GLOSA?">Qu'est-ce que le GLOSA ?</h2>
<br/> 
<div align="justify">
Le <i>Green Light Optimal Speed Advice</i> (GLOSA) est un système de communication infrastructure-to-vehicles (I2V) qui permets d'envoier des informations rélatifs à l'état du feux de circulation vers les véhicules connectées. L'objectif de cette communication est d'utiliser les informations sur le temps des feux de circulation pour optimiser la vitesse des véhicules à leurs passages [1]. Ce cas d'utilisation des ITS n'est pas une problèmatiques récentes et fait déjà integréer dans certaines villes. 
</div>
<br/>
<img src="https://s3-prod.autonews.com/OEM06_301239829_AR_-1_BOMDZEXWACYH.jpg">


<h2 align="center">GLOSA dans SUMO</h2>
<br/> 
<div align="justify">
Contrairement à d'autres systèmes de transport intelligent qui nécessite l'utilisation de <a href="https://sumo.dlr.de/docs/TraCI.html">TraCi</a> dans SUMO, des modules de <a href="https://sumo.dlr.de/docs/Simulation/GLOSA.html">GLOSA</a>  ont été créé dans SUMO depuis la version 1.9.1. Comme nous l'avons vu dans la section <i><a href="#GLOSA?">Qu'est-ce que le GLOSA ?</a></i>, la fonction GLOSA informe les véhicles de deux manière. La première manière est une information de realentissement, dans ce cas l'infrastructure informe si le vehicule doit ralentir au vu d'un arret par faute de temps ou pour un passage lors d'un changement de phase. La deuxième manière est une information d'accélération, le feux de circulation informe le véhicles qu'il doit augmenter sa vitesse pour pouvoir passer au vert. Pour mettre en place ce module, il faut à la fois équiper les véhicles et les feux de circulation ciblé. 
</div>   

<h2 align="center">Equipement des véhicles</h2>

Pour équiper les véhicles d'un <a href="https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#devices">dispositif</a> d'information existant dans SUMO, ils existent principalement deux manières. 

<h1 align="center">Bibliographie</h1>

[1] https://ieeexplore.ieee.org/document/6728552
