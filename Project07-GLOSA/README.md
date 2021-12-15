
<h1 align="center">Description du projet</h1>


<h2 align="center">Analyse des impacts du GLOSA sur le traffic</h2>

<div align="justify">
<br/> Le principale objectif de ce proket est de comprendre l'impactes du GLOSA sur le traffic, notamment à l'approche d'un feux de circulation dans un millieu urbain. 
</div>

<h2 align="center" id="GLOSA?">Qu'est-ce que le GLOSA ?</h2>
<br/> 
<div align="justify">
Le <i>Green Light Optimal Speed Advice</i> (GLOSA) est un système de communication infrastructure-to-vehicles (I2V) qui permets d'envoier des informations rélatifs à l'état du feux de circulation vers les véhicules connectées. L'objectif de cette communication est d'utiliser les informations sur le temps des feux de circulation pour optimiser la vitesse des véhicules à leurs passages [1]. Ce cas d'utilisation des ITS n'est pas une problèmatiques récentes [2,3,4] et fait déjà integréer dans certaines villes [5]. 
</div>
<br/>
<img src="https://s3-prod.autonews.com/OEM06_301239829_AR_-1_BOMDZEXWACYH.jpg">
<h3 align="center">Comment ça marche ?</h3>
<br/> 
<div align="justify">
Le GLOSA informe le conducteur du véhicle de la présence d'un feux de circulation en approche en lui informant de l'état du feux, il se peut que l'état soit différents à chaque voie. Deux cas peuvent se produire, soit le feux est rouge est dans ce cas le feux de circulation indique si oui ou non il pourra passer à la phase vert pour un changement de vitesse donnée. Soit la phase est déjà verts et dans ce cas, l'information concernet si oui ou non le véhicule pourra passer et selon une vitesse donnée. 

Mathématique, il est possible de le traduire selon la formulation du mono-segment de <a href="https://ieeexplore.ieee.org/document/6728552">Seredynski et al.</a>:

"Soit un segment <i>s</i> de longueur <i>l</i>  connue ainsi que la vitesse minimal et maximale sur le segment [v<sup>min</sup>,v<sup>max</sup>] et l'horaire des feux de circulation <i>t<sub>s</sub></i> à la fin du segment qui définie l'état du feux de circulation à l'instant <i>t</i>, <i>t<sub>s</sub>(t)={GREEN,YELOW,RED}</i>. Le but est de trouver la vitesse minimal <i>v</i> pour que le vehicules passer au vert":
 
<p align="center"> 
  <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/Screenshot%202021-12-14%20at%2013-14-48%20Comparison%20of%20Green%20Light%20Optimal%20Speed%20Advisory%20approaches.png" width="600">
  </p>
On peut generaliser cette approches par des reseaux de multi-segment:
  
"Soit une liste de n segment S={s<sub>1</sub>,...,s<sub>n</sub>}, avec leurs longueur l<sub>i</sub> où 1<i<n, le vitesse minimun et maximun du segment i, [v<sub>i</sub><sup>min</sup>,v<sub>i</sub><sup>max</sup>], sont connue. L'horraire des feux de circulation t<sub>si</sub> à la fin du segment i définissant l'etat du feu de circulation à l'instant t, <i>t<sub>si</sub>(t)={GREEN,YELOW,RED}</i>. L'objetif est de trouver la vitesse conseiller sur tout les segment, v={v<sub>1</sub>,...,v<sub>n</sub>} qui minimisera un certain objectif f(v)":

<p align="center">   
   <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/Screenshot%202021-12-14%20at%2013-14-40%20Comparison%20of%20Green%20Light%20Optimal%20Speed%20Advisory%20approaches.png" width="600">
   </p>

Usuellement on peut traduire cette notion avec les images 1 et 2. La premier image montre un scenario où une voiture s'approche d'un feu de circulation n'étant pas équiper d'un GLOSA. Comme aucune information n'est transmisse au conducteur, la vitesse qu'il m'entiends l'obligera à s'arreter au vu rouge et redemarrer lorsque que le cycle repasse au vert. Dans le deuxieme scénario, on suppose cette fois que la voiture et le feux de circulation sont équipe de systèmes GLOSA et que le feux de circulation peut transmettre cette information à un distance fixe (double fleche communication). Tant que le vehicule ne se trouve pas dans cette zone, il "mientient" sa vitesse en espèrant passer au vert. Lorsqu'il rentre dans la zones de communication, le feux de circulation envoie une information indiquant la vitesse à adopter, en laucurence ralentir dans ce cas. Avec la nouvelle vitesse adopter, le conducteur n'aura pas besoin de s'arreter et pourra continuer son iterraire après avoir passer le feux de circulation.
 
<p align="center">   
 <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/explication_sans_glosa.png" width="450">
   <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/explication_glosa_active.png" width="450">
   </p>
 
 De manière similaire les deux images suivantes representes le cas au le feux de circulation indique au conducteur d'augmenter sa vitesse pour pouvoir passer au rouge, en respectant les limites de vitesses vien évidamment. 
 
<p align="center">   
   <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/explication_glosa_vert.png" width="450">
   </p>
 
 
  
De manière plus complexe il est possible de formuler cette problèmatique dans l'obtique d'un étude de voie verte (ref ?).
</div>
<h3 align="center">Problèmatique du sujet?</h3>
<br/> 
<div align="justify">
Un enjeux de la mise en place de ce cas d'utilisations sucistes quelques questionnement. Quelles est sont impactes sur le traffic ? Ce type permets t-il de réduire la congestion au bords d'un feux de circulation ? Peut-il reduire les émissions relatif au traffic ? ect... Toutes ces questions sont au centre du GLOSA et le but de ce sujet et d'analyser ces impacts. Avant d'aborder les préceptives de recherches, nous allons voir comme elle s'ingre dans l'outil de simulation SUMO (Simulation of Urban MObility).
</div>


<h2 align="center" id="GLOSASUMO">GLOSA dans SUMO</h2>
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
    <li>device.glosa.range : spécifier la distance de communication du feux de circulation,il s'applique sur le feux de circulation et SUR LA VOITURE et il est par defaut égale à 100 mètres</li>
    <li>device.glosa.min-seed : indique la vitesse minimun pour effectuer la manoeuvre, il s'applique au paramètre du véhicles et il est par defaut égale à 5m/s soit 18 km/h</li>
    <li>device.glosa.max-speedfactor : indique le speedfactor lors de la communication,i l s'applique au paramètre du véhicles et il est par defaut égale à 1.1</li>
    <li>jmDriveAfterYellowTime : Mouais</li>
    <br/>
</div>  

<h2 align="center">Partie I : Mise en place du GLOSA</h2>
<br/> 
<div align="justify">
L'objectif de cette premier partie est d'integrer un systèmes GLOSA à l'aide des explications énumérer dans la section <a href="#GLOSASUMO">GLOSA dans SUMO</a>. Pour ce faire des fichiers sont présents dans le dossier simulation_sumo. Ce repertoire comprends un reseau (fichier ```.net```), une fichier de la demande (```.rou```) qui contient la demande en transport ainsi que la distribution des types de véhicules. Puis un fichier additionel comprennant les paramètres du GLOSA pour le feux de circulation et finalement un fichier ```.sumocfg```qui est le fichier d'execution de la simulation. A noter encore que cette configuration de la simulation exclusif. Plusieurs types d'imbrication sont possible, libre à vous de la modifier pour proposer d'autres structures. 
 
 
Quelques caratèristiques du reseaux:
 
 - Cycle de feux : 90s
 - Demande total : 1800veh/h
 - Longueur de l'artaire principale avant le feux de circulation : 1000 m
 - Nombre de voie du tronçon principale : 2
 
Deux objectifs sont à faire dans cette parties
 - Avec un choix judicieux sur la demande, évaluer la différences les scénarios avec 0% et 100% de véhicules équiper de VAC
 
 
Deux points au minimun sont attendus pour cette partie, l'analyse sur l'impact sur le traffic et l'impact sur les emessions 
 
Ci dessous vous trouverez quelques sources utiles au traitement de cette partie:
 
 https://www.cerema.fr/system/files/documents/2020/08/evaluation_capacite_feux_france_2016_cle4e6dd3.pdf
 
</div>

<h2 align="center">Partie II : Modification de la demande</h2>

Une des questions légitimes sur la mise en place des GLOSA est de connaitre sa limite en fonctionne de la demande. Ainsi dans cette partie, il est demande de:

- A demande total fixe, evaluter l'influence d'un taux de VAC augmentant sur le reseau
- A taux de VAC dans la flottes de vehicles évaluter les limites du GLOSA pour une demande augmentant

<h2 align="center">Partie II : Modification des facteurs</h2>


Un des questions légitimes sur la mise en places des GLOSA est de connaitre ses limites en fonction des indices de performances et du comportement du conducteur. Ainsi dans cette partie ouverte, il est demander de:

- A demande fixe et taux de VAC fixe, évaluer l'impact du GLOSA pour différentes plages de distances de communication du GLOSA.
- A demande fixe et taux de VAC fixe, évaluer l'impact du GLOSA pour différentes valeur du facteur de vitesse du conducteur. 

<h2 align="center">Partie II : Modification du reseau</h2>

Un des questions légitimes sur la mise en places des GLOSA est de connaitre ses limites en fonction du reseau étudiant. Ainsi dans cette partie ouverte, il est demander de:

- A demande fixe et taux de VAC fixe, évaluer l'impact du GLOSA pour différents nombre de voie sur le reseau.
- A demande fixe et taux de VAC fixe, évaluer l'impact du GLOSA pour différentes valeurs de cycle de feux. 


<h2 align="center">Modalités d'évaluation</h2>

Oral: Note: Je n'ai pas personnellement les questions pièges

Rapport: Le rapport doit être rédigé dans un français de qualité et de manière consise. Le rapport ne doit pas exéder les 10-15 pages, evitez donc trop de répétition et de divager sur certains points, notamment dans l'introduction et dans la conclusion. J'attends également une analyse sur la limite de vos démarches ainsi que des perspectives envisagables

Pour toutes questions éventuelles sur le projet, vous pouvez me contacter à l'adresse hugues.blache@entpe.fr ou bien poser des questions sur le Moodle. 



<h2 align="center">Bibliographie</h2>
<br/> 
<div align="justify">
<ul>
<dd> [1] M. Seredynski, B. Dorronsoro and D. Khadraoui, "Comparison of Green Light Optimal Speed Advisory approaches," 16th International IEEE Conference on Intelligent Transportation Systems (ITSC 2013), 2013, pp. 2187-2192, doi: 10.1109/ITSC.2013.6728552.</dd> 
<dd> [2] Stevanovic A, Stevanovic J, Kergaye C. Green Light Optimized Speed Advisory Systems: Impact of Signal Phasing Information Accuracy. Transportation Research Record. 2013;2390(1):53-59. doi:10.3141/2390-06</dd> 
<dd> [3] K. Katsaros, R. Kernchen, M. Dianati and D. Rieck, "Performance study of a Green Light Optimized Speed Advisory (GLOSA) application using an integrated cooperative ITS simulation platform," 2011 7th International Wireless Communications and Mobile Computing Conference, 2011, pp. 918-923, doi: 10.1109/IWCMC.2011.5982524.</dd> 
<dd> [4] Stebbins, S., Hickman, M., Kim, J., Vu, H.L., 2017. Characterising green light optimal speed advisory trajectories for platoon-based optimisation. Transport. Res. Part C:Emerg. Technol. 82, 43–62.</dd> 
<dd> [5] https://www.neogls.com/produit/glosa/</dd> 
</ul>
</div>
Ajouter les refs suivantes
https://www.researchgate.net/publication/259896470_Preparing_Simulative_Evaluation_of_the_GLOSA_Application

<p align="center">
<img src="https://www.entpe.fr/themes/custom/entpe/logo_entpe.png" width="450">
<img src="https://www.pole-emc2.fr/app/uploads/logos_adherents/be04eddc-e2fa-f150-aed4-53957cf64731.jpg" width="450">
</p>
<p align="center">
<img src="http://imu.universite-lyon.fr/wp-content/uploads/2015/08/LOGO-LICIT.png" width="450">
</p>


