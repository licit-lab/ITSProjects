
<h1 align="center">Description du projet</h1>


<h2 align="center">Analyse des impacts du GLOSA sur le trafic</h2>

<div align="justify">
<br/> Le principal objectif de ce projet est de comprendre l'impact du GLOSA sur le trafic, notamment à l'approche d'un feu de circulation dans un milieu urbain. 
</div>

<br>
<br>
<h2 align="center" id="GLOSA?">Qu'est-ce que le GLOSA ?</h2>
<br/> 
<div align="justify">
Le <i>Green Light Optimal Speed Advice</i> (GLOSA) est un service basé sur un système de communication Infrastructure-to-Vehicles (I2V). Il permet d'envoyer des informations relatives à l'état du feu de circulation (appelées SPATEM en Europe) vers les véhicules connectés en approche. L'objectif de cette communication est de permettre au véhicule connecté de tirer parti des informations relatives au statut des feux de circulation pour l'aider à optimiser sa vitesse d'approche de l'intersection [1]. Ce cas d'utilisation des ITS n'est pas une problématique récente [2,3,4] et est, de fait, déjà intégré dans certaines villes [5].
</div>
<br/>

<img src="https://s3-prod.autonews.com/OEM06_301239829_AR_-1_BOMDZEXWACYH.jpg">
<br>
<br>
<h3 align="center">Comment ça marche ?</h3>
<br/> 
<div align="justify">
Le GLOSA informe le conducteur du véhicule de la présence d'un feu de circulation, de son état actuel (phase) et de la durée restante pour la phase courante. À l'approche de cette intersection, il est tout à fait possible que l'état du feu soit distinct sur chacune des voies. Deux cas peuvent se produire:
<ul>
  <li>soit le feu est rouge : dans ce cas, le feu de circulation indique si oui ou non, il pourra passer à la phase verte pour un changement de vitesse donnée, </li>
  <li>soit la phase est déjà verte : dans ce cas, l'information concerne si oui ou non le véhicule pourra passer en considérant une vitesse donnée.</li>
</ul>

 
Mathématiquement, il est possible de traduire ce procédé selon la formulation du monosegment de 
<a href="https://ieeexplore.ieee.org/document/6728552">Seredynski et al.</a>:

"Soit un segment <i>s</i> de longueur <i>l</i>  connu, soit les vitesses minimales et maximales sur le segment [v<sup>min</sup>,v<sup>max</sup>], ainsi que la fonction <i>t<sub>s</sub></i> lisant à tout instant <i>t</i> la table horaire associée aux feux de circulation en extrémité de section, <i>t<sub>s</sub>(t)={GREEN,YELOW,RED}</i>. 

L'objectif consiste à trouver la vitesse minimale <i>v</i> pour que le véhicule puisse passer au vert":
 
<p align="center"> 
  <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/Screenshot%202021-12-14%20at%2013-14-48%20Comparison%20of%20Green%20Light%20Optimal%20Speed%20Advisory%20approaches.png" width="600">
  </p>
On peut généraliser cette approche à des réseaux de multisegment:
  
"Soit une liste de n segments S={s<sub>1</sub>,...,s<sub>n</sub>}, avec leur longueur l<sub>i</sub> où 1<i<n, les vitesses minimums et maximums du segment i, [v<sub>i</sub><sup>min</sup>, v<sub>i</sub><sup>max</sup>], sont connues.


L'horaire des feux de circulation t<sub>si</sub> à la fin du segment i définissant l'etat du feu de circulation à l'instant t, <i>t<sub>si</sub>(t)={GREEN,YELOW,RED}</i>. L'objetif est de trouver la vitesse conseillée sur chacun des segments, v={v<sub>1</sub>,...,v<sub>n</sub>} qui minimisera un certain objectif f(v)":


<p align="center">   
   <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/Screenshot%202021-12-14%20at%2013-14-40%20Comparison%20of%20Green%20Light%20Optimal%20Speed%20Advisory%20approaches.png" width="600">
   </p>


Usuellement, on peut traduire cette notion avec les images 1 et 2. 

La première image montre un scénario, où une voiture s'approche d'un feu de circulation n'étant pas équipé d'un GLOSA. Comme aucune information n'est transmise au conducteur, la vitesse qu'il maintient l'obligera à s'arrêter au feu rouge, puis à redémarrer lorsque le cycle passe au vert. 

Dans le deuxième scénario, on suppose cette fois que la voiture et le feu de circulation sont équipés du système GLOSA et que le feu de circulation peut transmettre cette information à une distance fixe (double flèche de communication). Tant que le véhicule ne se trouve pas dans cette zone, il "maintient" sa vitesse en espérant passer au vert. Lorsqu'il entre dans la zone de communication, le feu de circulation envoie une information indiquant la vitesse à adopter et/ou une instruction, en l'occurrence "ralentir" dans ce cas. Avec la nouvelle vitesse adoptée, le conducteur n'aura pas besoin de s'arrêter et pourra continuer son itinéraire après avoir franchi le feu de circulation.

 
<p align="center">   
 <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/explication_sans_glosa.png" width="450">
   <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/explication_glosa_active.png" width="450">
   </p>
 

De manière similaire, les deux images suivantes représentent le cas, où le feu de circulation indique au conducteur d'augmenter sa vitesse pour pouvoir passer au rouge, en respectant les limites de vitesse bien évidemment. 
 
<p align="center">   
   <img src="https://github.com/licit-lab/ITSProjects/blob/dev/Project07-GLOSA/image/explication_glosa_vert.png" width="450">
   </p>
 
 


<br>
</div>
<h3 align="center">Problématique du sujet ?</h3>
<br/> 
<div align="justify">
La mise en place de ce cas d'utilisation suscite quelques questionnements et n'est pas sans enjeux:
<ul>
  <li> Quels sont les impacts en termes d'efficacité du trafic ? Ce cas d'usage permet-il de réduire la congestion aux abords d'un feu de circulation ? </li>
  <li> Quels sont les impacts en termes d'émissions de polluants? Peut-on réduire les émissions relatives au trafic ? etc... </li>
</ul>
Toutes ces questions sont au centre du GLOSA et le but de ce sujet est précisément de mener des analyses pour qualifier ces impacts. Avant d'aborder les concepts liés à la recherche, nous allons voir comment le GLOSA peut-être intégré et étudié dans l'outil de simulation SUMO (Simulation of Urban MObility).
</div>
<br>
<br>

<h2 align="center" id="GLOSASUMO">GLOSA dans SUMO</h2>
<br/> 
<div align="justify">
Contrairement à d'autres systèmes de transport intelligent qui nécessitent l'utilisation d'une interface comme  <a href="https://sumo.dlr.de/docs/TraCI.html">TraCi</a> pour développer de nouveaux services dans SUMO, des modules de <a href="https://sumo.dlr.de/docs/Simulation/GLOSA.html">GLOSA</a>  ont été spécialement implémentés directement dans le cœur de simulation de SUMO depuis sa version 1.9.1. 

Comme nous l'avons vu dans la section <i><a href="#GLOSA?">Qu'est-ce que le GLOSA ?</a></i>, la fonction GLOSA informe les véhicules de deux manières. 

La première manière est une information de ralentissement, dans ce cas l'infrastructure transmet une instruction au véhicule en lui informant de ralentir du fait d'une phase de feu déjà au "rouge" ou d'un délai trop court pour franchir l'intersection durant le vert restant.

La deuxième manière est une information d'accélération, le feu de circulation informe le véhicle qu'il doit augmenter sa vitesse pour pouvoir passer au vert. 

Pour mettre en place ce module, il faut à la fois équiper les véhicules et l'infrastructure (et les feux de circulation). 
</div>   

<br>
<h3 align="center">Équipement des véhicules</h3>

<br/> 
<div align="justify">
Pour équiper les véhicules d'un <a href="https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#devices">dispositif</a> d'information existant dans SUMO, il existe principalement deux manières:
<br/>   
  <ul>
    <li>Soit nous ciblons le type de véhicules, que nous voulons équiper du dispositif. Dans ce cas, il faut modifier la structure des fichiers d'entrée de SUMO visant à décrire les véhicules pour y intégrer la commande: </li>
<br/>

  
 ```xml 
  <param key="has.glosa.device" value="true"/>
  ```
 </ul>

 <ul>
  <dd> Cette commande peut être incluse dans les <b>vTypes</b> ou bien directement dans la description individuelle du véhicule. L'avantage de cette approche est qu'elle permet de cibler le type de véhicule ayant un équipement.
  </dd> 
  </ul> 

  <ul>
    <li>Soit nous ciblons la probabilité d'insertion d'un véhicule de type GLOSA, en précisant uniquement la probabilité qu'un tel véhicule apparaisse sur le réseau. La compétence GLOSA pourra alors être ajoutée à n'importe quel type de véhicule lors de son apparition sur le réseau routier de SUMO. Il n'est dès lors pas nécessaire de modifier les fichiers d'entrée et de configuration du scénario de SUMO. Dans un tel cas, il faut spécifier l'option de commande suivante lors du lancement de la simulation depuis le terminal de commande:
    </li>
    <br/>
    
  ```
  --device.glosa.probability 100
  ```
</ul>
<ul>
  <dd> Ici le 100 illustre que 100% des véhicules sont équipés du GLOSA, pour changer la probabilité, il suffit de changer la valeur du nombre... L'avantage de cette méthode est qu’elle permet de construire des fichiers automatiquement sans interventions humaines. Elle permet également de répliquer un grand nombre de fois une simulation en changeant des paramètres, par exemple en utilisant des boucles dans des fichiers <a href="https://fr.wikihow.com/%C3%A9crire-un-fichier-batch">BACH</a>.
  </dd> 
  </ul> 

    
  <ul>
    <li>D'autres approches existent également, comme l'implantation déterministe ou l'établissement d'une liste d'identifiants des véhicules à équiper lors du lancement de scénario en ligne de commande, mais, pour ce projet, il ne sera pas utile de les utiliser.
    </li>
    </ul>
Toutes les approches se valent, il suffit de choisir le plus facile à utiliser pour vous. À noter que cette approche est similaire pour d'autres équipements en remplaçant le GLOSA par l'<a href="https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#devices">équipement</a> présent dans SUMO.
</div>  

<br>
<br>
<h3 align="center">Équipement des feux de circulation</h3>
<br/>
<div align="justify">
Il existe différentes manières de bâtir une simulation du trafic dans SUMO. Les scénarios faisant appel au GLOSA ne font pas exception. 

Pour implémenter le GLOSA dans SUMO, il est possible de modifier le fichier ```.net```, mais ceci peut perturber et fausser les résultats en cas de mauvaise manipulation. 

Dans notre cas et comme le préconise la documentation de SUMO, nous allons spécifier les paramètres du GLOSA du feu de circulation cible dans un fichier d'entrée additionnel. Pour activer la fonction GLOSA, il suffit de spécifier les paramètres:
<ul>
  <li>distance de communication, </li>
  <li>id du feux de circulation, et</li>
  <li>le programID.</li>
</ul> 
On procède alors de la façon suivante:
<br/>
  
```xml
<tlLogic id="C" programID="0">
        <param key="device.glosa.range" value="60"/>
</tlLogic>
```

Cette approche à l'avantage de cibler le feu de circulation du réseau. 

<br>
<br>
</div> 
<h3 align="center">Aperçu global du GLOSA dans SUMO</h3>
<br/>
</div>  
Il existe 4 paramètres GLOSA dans SUMO:

  <ul>
    <li>device.glosa.range : spécifie la distance de communication du feu de circulation,il s'applique sur le feux de circulation et SUR LA VOITURE et il est par défaut égal à 100 mètres</li>
    <li>device.glosa.min-speed : indique la vitesse minimum pour effectuer la manœuvre, il s'applique au paramètre du véhicule et il est par défaut égal à 5m/s soit 18 km/h</li>
    <li>device.glosa.max-speedfactor : indique le speedfactor lors de la communication, il s'applique au paramètre du véhicule et il est par défaut égal à 1.1</li>
    <li>jmDriveAfterYellowTime : indique la volonté de continuer à rouler au jaune en fonction de la durée de fonctionnement de la phase jaune (par défaut 0). La valeur sera prise en compte lors de la vérification de la faisabilité d'une manœuvre d'accélération</li>
    <br/>
</div>  

<h2 align="center">Partie I : Mise en place du GLOSA</h2>
<br/> 
<div align="justify">
L'objectif de cette première partie est d'intégrer un système GLOSA à l'aide des explications produites dans la section <a href="#GLOSASUMO">GLOSA dans SUMO</a>. 

Pour ce faire, des fichiers sont présents dans le dossier simulation_sumo. Ce répertoire comprend 
<ul>
  <li>un reseau (fichier ```.net```), </li>
  <li>un fichier de demande (```.rou```) qui contient la demande en transport, ainsi que la distribution des types de véhicules (phase de génération de la demande par type de véhicule),</li>
  <li>un fichier additionnel comprenant les paramètres du GLOSA pour le feu de circulation, et</li> 
  <li>un fichier ```.sumocfg``` qui est le fichier permettant l'exécution de la simulation. </li>
</ul>
À noter encore que cette configuration de la simulation n'est pas exclusive. Plusieurs types d'imbrication sont possibles, libres à vous, de la modifier pour proposer d'autres structures. 
 
<br>
Quelques caractéristiques de la simulation:
 
 - Cycle de feux : 90s
 - Demande total : 1800veh/h
 - Longueur de l'artère principale avant le feu de circulation : 1000 m
 - Nombre de voies du tronçon principal : 2
 - Distance de communication du GLOSA : 500 m
 - Facteur de vitesse lors de la communication avec le GLOSA: 1.1
 <br/>

 <br>
  
  
Définition élémentaire :
 
- MPR=0%: les véhicules/conducteurs ne sont pas connectés et ne disposent pas d'informations sur les
conditions de l'état du feu de circulation, à l'exception des informations résultant de leur expertise (c'est-à-dire qu'ils connaissent
sur les conditions habituelles) : cela équivaut à un taux de pénétration du marché (MPR) fixé à 0 %.
 
- MPR=100%: les véhicules/conducteurs disposent d'informations sur l'état du feux de circulation. Il permet au véhicule/conducteur de choisir la meilleure option
en termes de vitesse à l'approche d'un feu de circulation. Nous supposerons que tous les chauffeurs disposent
de l'information de la même manière lorsque l'information est disponible. Il correspond à un marché:
Taux de Pénétration de 100% des Véhicules connectés.


 
 <b>Question 1</b>
 
Pour cette question, il vous sera demandé d'évaluer et de comparer la mise en place du GLOSA pour deux scénarios, un scénario avec un taux de pénétration du marché (MPR) à 0% et un MPR=100%.
 
Pour l'analyse globale, vous devrez évaluer la différence en termes de:
 - Temps de parcours cumulé
 - Temps perdu 
 - Nombre de véhicules qui s'arrêtent
 - Volume des véhicules à l'arrêt et le pourcentage de véhicules à l'arrêt en fonction du taux de pénétration des VAC
 - Comparaison des deux diagrammes espaces-temps
 - Évaluation environnementale
 - Etc.
 
Vous pourrez utiliser le jupyter notebook pour vous aider dans les démarches et les figures disponibles. Néanmoins, la librairie plotly n'est qu'un outil, libre à vous d'en utiliser une autre. Également, les figures proposées dans ce juypternotebook ne sont pas forcément exactement les mêmes que celles demandées pour répondre aux questions. À vous de les adapter!
  
</div>

<h2 align="center">Partie II : Modification du réseau</h2>

Une des questions légitimes sur la mise en places des GLOSA est de connaitre ses limites en fonction du réseau étudiant. Ainsi dans cette partie ouverte, il est demandé de:

 - <b>Q2: </b> À demande fixe et taux de VAC fixe, évaluer l'impact du GLOSA pour différents nombres de voies sur le réseau. Par exemple nombre de voie=[1,2,3,4]
 - <b>Q3: </b> À demande fixe et taux de VAC fixe, évaluer l'impact du GLOSA pour différentes valeurs de cycle de feux.  Par exemple des cycles=[30,60,90,120,150]

Il serait bien dans cette partie de procéder à un plan d'expérience par quadrillage avec, en ordonnée et abscisse, les nombres de voies et les facteurs de cycles, en considérant un ou des indicateurs de performances. Comme dans la partie I, d'autres indicateurs sont bien à analyser.


<h2 align="center">Sources utiles</h2>

Ci-dessous vous trouverez quelques sources utiles au traitement du projet:

- <a href="https://sumo.dlr.de/docs/netconvert.html">Netconvert</a> sur SUMO
- <a href="https://www.cerema.fr/system/files/documents/2020/08/evaluation_capacite_feux_france_2016_cle4e6dd3.pdf">Cerema</a> Evaluation de la capacité aux feux retour d'observations en France: De la phase conception à l'épreuve du terrain
- <a href="https://sumo.dlr.de/docs/Simulation/GLOSA.html">GLOSA</a> sur SUMO

<h2 align="center">Modalités d'évaluation</h2>

Oral: Note: Je n'aime pas personnellement les questions pièges

Rapport: Le rapport doit être rédigé de manière concise. Le rapport ne doit pas excéder les 10-15 pages, évitez donc trop de répétition et de divaguer sur certains points, notamment dans l'introduction et dans la conclusion. J'attends également une analyse sur la limite de vos démarches ainsi que des perspectives envisageables.

Pour toutes questions éventuelles sur le projet, vous pouvez me contacter à l'adresse hugues.blache@entpe.fr ou bien poser des questions sur le Moodle. 

<h2 align="center">Modalités d'évaluation</h2>

Oral: Note: Je n'aime pas personnellement les questions pièges

Rapport: Le rapport doit être rédigé de manière concise. Le rapport ne doit pas excéder les 10-15 pages, évitez donc trop les répétitions et de divaguer sur certains points, notamment dans l'introduction et dans la conclusion. J'attends également une analyse sur la limite de vos démarches ainsi que des perspectives envisageables.

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


