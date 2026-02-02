Comparaison CI-TEX SIRIUS 2025
###################################
La comparaison des données CI-TEX & SIRIUS est prescrite par la démarche qualité de la DiRIF. La formulation de l'indicateur est :  

**Nombre d'évènements renseignés dans Sytadin/nombre d'évènements signalés**, 

avec l'objectif de 75%.

On propose une reformulation de l'indicateur : 

**Nombre d'interventions enregistrées dans CI-TEX qui correspondent à un événement enregistré dans SIRIUS
divisé par le nombre total d'interventions enregistrées dans CI-TEX**.

**Le résultat du calcul, présenté ci-dessous, est de 59%**.

Le présent document contribue à la traçabilité de la méthode de calcul.

Cette page rend compte des traitements réalisés pour effectuer la comparaison des données sur les onze premiers mois de l'année 2025.
On s'est arrêté en novembre car l'exploitation a été faite en décembre 2025.

On a intégré des éléments techniques qui pourront servir à reproduire les traitements l'an prochain pour avoir un résultat comparable.

Extraction des données d'interventions
****************************************
On a fait une extraction des données à cette adresse : https://dirif.akelio.com/intervention/list   
**Télécharger fiches complètes**    période : 1-11/2025   

La table contient de nombreuses colonnes dont on ne garde que la liste suivante : 

* 'CEI', 
* "Date d'appel", 
* "Heure d'appel",
* "Horaire d'arrivée sur le lieu d'intervention",
* "Horaire du départ du lieu d'intervention"
* "Origine de l'appel",
* 'Axe', 
* 'Sens',
* 'Localisation',  
* "Type d'intervention",

On remplace les données manquantes par :

* "00:01" pour  "Heure d'appel" & "Horaire d'arrivée sur le lieu d'intervention"
* "23:59" pour "Horaire du départ du lieu d'intervention"

Pou le champ *Heure d'appel* qui intervient dans la liaison, seulement 28 valeurs sont nulle, l'impact sur l'indicateur est donc négligeable.

On remplace certains noms d'axe comme N385 -> A86.

Pour cette exploitation, on n'a pas travaillé sur le champ Localisation dont la valorisation est complexe (voir travaux de 2024) car il n'est pas renseigné de la même manière par tous les utilisateurs.

La table obtenue comporte environ 41 000 lignes.

Doublons de fiches d'interventions
****************************************
L'élimination des doublons n'est pas un sujet simple car il faudrait :

* Ne pas conserver plus d'une fiche correspondant à une seule intervention,
* Ne pas supprimer une fiche qui rend compte d'une intervention à part entière, même si celle-ci partage plusieurs caractéristiques (Heure d'appel, CEI, Axe, Sens) avec une autre intervention.
* Ne pas mettre en place un traitement trop complexe, difficile à maintenir et à contrôler

On ignore si , dans les principes d'utilisation de CI-TEX, la présence de plusieurs véhicules doit donner lieu à autant d'enregistrements d'interventions différentes 
ou s'il doit s'agir d'une seule intervention. 
Dans le cas de SIRIUS, il y aura en général un seul événement.

En dehors des doublons manifestes dont les principales caractéristiques sont identiques, on trouve les cas suivants :

Même axe, même sens, même CEI, un faible écart des heures d'appel  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On peut supposer qu'un écart des heures enregistées inférieur à 30 munutes, pour des intervenions du même CEI sur les mêmes axe et sens, traduit deux enregistrements de la même  intervention. 
Quoi qu'il en soit la mise en relation avec SIRIUS ne pouvant pas se faire sur l'heure exacte, 
les deux interventions seront associées au même événement SIRIUS s'il en existe un.

* 900 interventions sont enregistrées avec une heure d'appel inférieur à **10 mn** après une intervention du même CEI sur les mêmes axe et sens.
* 2300 interventions sont enregistrées avec une heure d'appel inférieur à **30 mn** après une intervention du même CEI sur le même axe.

Ce type de doublons potentiel est significatif puisqu'il porte sur plus de 5% des interventions.

Dans le calcul du taux de correspondance, on n'a pas supprimé ces doublons. 

Même heure, même axe, CEI différents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Il peut s'agir des interventions de 2 CEI sur le même événement ou sur deux événements différents.  
La seconde hypothèse est la plus plausible quand les CEI ne sont pas voisins et cela se produit surtout avec l'axe A86 sur lequel il est courant que plusieurs interventions aient la même heure (et minute) d'appel.

On ne supprime pas ces doublons (environ 220), mais on s'attend à ce qu'un seul événement SIRIUS corresponde aux deux interventions.

Même heure, même CEI, axes différents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
On trouve généralement cette situation avec des axes qui sont voisins :  

* A86 & A3
* A86 & A4
* A86 & A15
* A6a & A4b
* A104 & N2

Il peut s'agir d'événements au niveau des bretelles d'échange entre les deux axes.

On ne supprime pas ces doublons (environ 280), mais on s'attend à ce qu'un seul événement SIRIUS corresponde aux deux interventions AGER.

Ce sujet mériterait d'être clarifié avec les utilisateurs de CI-TEX.

Extraction des événements SIRIUS
***********************************
Les données SIRIUS sur les événements sont utilisées par Marc Koenig pour produire des statistiques publiées chaque mois.  
Marc partage les fichiers mensuels sur COSMOSE au format Excel. Ces fichiers étant partiellement traités à la main, il peut y avoir des différences de format.
Par exemple, pour le mois de juillet 2025, les données brutes sont sur la seconde feuille du classeur, laquelle porte le nom feuille 1 !  

Les données étant produites par un système informatique et traitées dans un but statistique, elles sont plus *propres* que les données d'intervention.

Désignation des axes et sens
*******************************
Certains **axes** ne sont pas désignés de la même manière par SIRIUS et par CI-TEX; il faut dont, pour la liaison, établir une correspondance entre les noms des axes dans SIRIUS et dans CI-TEX, au moins pour les principaux axes dont les noms diffèrent.  

Correspondances utilisées : [['A6A','A6a'],['A6B','A6b'],['N118N','N118'],['N104N','N104'],['A104N','A104'],['N_1104','N1104'],['N_1013','N1013'],['CD77N4','CD77'],['N186B','N186'] ]

Le **sens** n'est pas toujours renseigné dans CI-TEX ou plusieurs sens sont indiqués. Cette dernière situation porte sur un faible nombre et on a retenu le premier sens indiqué.

Les cas où le sens n'est pas renseignés représentent moins de 2% des interventions et on ne les a pas pris en compte dans le calcul du taux de correspondance. 
Ce choix conduit à un résultat plus élevé.  C'est un choix discutable car il signifie que l'absence d'information sur le sens, un élément sur lequel la DiRIF 
est susceptible de s'améliorer, n'a pas d'impact sur l'indicateur.

Liaison entre les tables
***************************
On fait la liaison sur les champs **date, heure, Axe, Sens**. 

Pour les évènements SIRIUS, on étend la période prise en considération à 30 minutes, avant et après l'heure considérée.

On constate que 59% des interventions ont un correspondant dans la base SIRIUS pour cette liaison. Cette valeur est celle que l'on propose pour l'indicateur recherché.

Ce résultat dépend de nombreuses hypothèses que l'on a fait ressortir, autant que possible, dans les explications ci-dessus.







