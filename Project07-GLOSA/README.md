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

<h3 align="center">Equipement des véhicles</h3>

<br/> 
<div align="justify">
Pour équiper les véhicles d'un <a href="https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#devices">dispositif</a> d'information existant dans SUMO, ils existent principalement deux manières:
<br/>   
  <ul>
    <li>Soit nous ciblons le type de véhicules pour lequelle nous voulons équiper le dispositifs. Dans ce cas il faut modifier la structure des fichier d'entrée des véhicles pour integrer la commande: </li>

</ul>
  
 ```xml 
  <param key="has.glosa.device" value="true"/>
  ```
 <ul>
  <dd> Cette commende peut être inclues dans les vTypes ou bien directement dans la discription individuelles du véhicles.</dd> 
  </ul> 
  <ul>
    <li>Soit nous ciblons la probabilité d'insertion du véhicles sans entréer dans les fichiers d'entréer. Au quel cas, il faut spécifier la commande suivante lors du lancement de la simulation par le terminale:
    </li>
    
  ```
  --device.fcd.probability 100
  ```
</ul>
<ul>
  <dd> Ici le 100 illustre que 100% des véhicules sont équipés du GLOSA, pour changer la probabilité, changer le nombre...</dd> 
  </ul> 

    
  <ul>
    <li>D'autres approches existent également, comme l'implantation deterministe ou nommer la liste d'identifiant des véhicules dans la commande, mais pour ce projet, il ne sera pas utile de l'utiliser.
    </li>
    </ul>
A noter que cette approche est similaire pour d'autres équipement en remplacant glosa par l'équipement présent dans SUMO.

</div>  

<h1 align="center">Bibliographie</h1>

[1] https://ieeexplore.ieee.org/document/6728552
