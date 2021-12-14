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
<h3 align="center">Comment ça marche ?</h3>
<br/> 

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
<br/>

  
 ```xml 
  <param key="has.glosa.device" value="true"/>
  ```
 </ul>
 <ul>
  <dd> Cette commende peut être inclues dans les vTypes ou bien directement dans la discription individuelles du véhicles.</dd> 
  </ul> 
  <ul>
    <li>Soit nous ciblons la probabilité d'insertion du véhicles sans entréer dans les fichiers d'entréer. Au quel cas, il faut spécifier la commande suivante lors du lancement de la simulation par le terminale:
    </li>
    <br/>
    
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


<h3 align="center">Equipement des feux de circulation</h3>
<br/>
<div align="justify">
Il existent différentes manières de batir un simulation du traffic dans SUMO et s'est le cas pour le GLOSA. Pour implanter le GLOSA dans SUMO, il est possible de modifier le fichier ```.net```, mais ceci peut pertuber et fausser les resultats en cas de mauvaise manipulation. Dans notre cas et comme le préconnisse la documentation de SUMO, nous allons spécifié les paramètres du GLOSA du feux de circulation cible dans un fichier additionnel d'entréer. Pour acctiver la fonction GLOSA, il suffit de spéfier le paramettre de distance de comminication et en spécifier le id du feux de circulation et le programID:
<br/>
  
```xml
<tlLogic id="C" programID="0">
        <param key="device.glosa.range" value="60"/>
</tlLogic>
```

Cette approche à l'avantage de cibler le feux de circulation du reseau, pour le faire sur directement sur la commande de simulation, il est possible de spécifier la distance de communication avec ```--device.glosa.range``` 
</div> 
<h3 align="center">Equipement des feux de circulation</h3>
<br/>
</div>  
Il existe 4 paramètres GLOSA dans SUMO:

  <ul>
    <li>device.glosa.range : spécifier la distance de communication du feux de circulation,il s'applique sur le feux de circulation et il est par defaut égale à 100 mètres</li>
    <li>device.glosa.min-seed : indique la vitesse minimun pour effectuer la manoeuvre, il s'applique au paramètre du véhicles et il est par defaut égale à 5m/s soit 18 km/h</li>
    <li>device.glosa.max-speedfactor : indique le speedfactor lors de la communication,i l s'applique au paramètre du véhicles et il est par defaut égale à 1.1</li>
    <li>jmDriveAfterYellowTime : Mouais</li>
    <br/>
</div>  



<h1 align="center">Bibliographie</h1>

[1] https://ieeexplore.ieee.org/document/6728552
