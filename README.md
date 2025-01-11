Ce projet permet de gérer un équipage d'un vaisseau spatial, avec différents types de membres (personnes civiles, opérateurs et mentalistes), des vaisseaux et des actions associées à ces membres.

Fonctionnalités principales
1. Ajout de membres à l'équipage

L'équipage peut être composé de trois types de membres :

    Personne civile : Une personne générique sans rôle spécifique. Son nom, prénom, genre et âge sont demandés lors de l'ajout.
    Opérateur (Pilote / Technicien) : Un membre avec un rôle spécialisé. Un opérateur peut être soit un pilote, soit un technicien, et leur rôle doit être spécifié lors de l'ajout. De plus, il y a des restrictions d'âge : un pilote doit avoir plus de 25 ans, un technicien doit avoir plus de 18 ans.
    Mentaliste : Un membre avec des capacités spéciales. Son nom, prénom, genre et âge sont demandés lors de l'ajout.

2. Gestion des membres et des actions

Les membres de l'équipage peuvent effectuer des actions :

    Piloter : Les opérateurs de type pilote peuvent piloter le vaisseau.
    Maintenance : Les opérateurs de type technicien peuvent effectuer des tâches de maintenance.
    Agir : Les Mentalistes peuvent utiliser leur pouvoir spécial pour interagir avec les autres membres du vaisseau.
        Si le Mentalist a plus de 19 points de mana, il peut utiliser l'action "act" pour affecter un pilote ou un technicien.
        Si un Mentalist agit sur un pilote ou un technicien, celui-ci perd 1 point d'expérience (à condition qu'il en ait).
        Si le Mentalist a moins de 20 mana, il ne pourra pas agir et devra recharger son mana.

3. Gestion des vaisseaux et de la flotte
Fonctionnalités principales
1. Ajout de membres à l'équipage

L'équipage peut être composé de trois types de membres :

    Personne civile : Une personne générique sans rôle spécifique. Son nom, prénom, genre et âge sont demandés lors de l'ajout.
    Opérateur (Pilote / Technicien) : Un membre avec un rôle spécialisé. Un opérateur peut être soit un pilote, soit un technicien, et leur rôle doit être spécifié lors de l'ajout. De plus, il y a des restrictions d'âge : un pilote doit avoir plus de 25 ans, un technicien doit avoir plus de 18 ans.
    Mentaliste : Un membre avec des capacités spéciales. Son nom, prénom, genre et âge sont demandés lors de l'ajout.

2. Gestion des membres et des actions

Les membres de l'équipage peuvent effectuer des actions :

    Piloter : Les opérateurs de type pilote peuvent piloter le vaisseau.
    Maintenance : Les opérateurs de type technicien peuvent effectuer des tâches de maintenance.
    Agir : Les Mentalistes peuvent utiliser leur pouvoir spécial pour interagir avec les autres membres du vaisseau.
        Si le Mentalist a plus de 19 points de mana, il peut utiliser l'action "act" pour affecter un pilote ou un technicien.
        Si un Mentalist agit sur un pilote ou un technicien, celui-ci perd 1 point d'expérience (à condition qu'il en ait).
        Si le Mentalist a moins de 20 mana, il ne pourra pas agir et devra recharger son mana.

3. Gestion des vaisseaux et de la flotte

    Ajouter un vaisseau : On peut ajouter un vaisseau à la flotte avec un nom, un type (transport, guerre, marchand) et une condition (opérationnel, endommagé).
    Ajouter un membre à un vaisseau : Après avoir ajouté un membre à l'équipage, il peut être assigné à un vaisseau spécifique. L'équipage du vaisseau est mis à jour et le membre est retiré de l'équipage au sol.

4. Vérification de la préparation de la flotte

Avant de partir en mission, vous pouvez vérifier si la flotte est prête. Un vaisseau est considéré comme prêt si :

    Il y a au moins un pilote.
    Il y a au moins un technicien.
    Il y a au moins un Mentalist avec suffisamment de mana (au moins 50 mana).

5. Sauvegarde et chargement des données

Le programme permet de sauvegarder et de charger les données de l'équipage et des vaisseaux sous forme de fichiers JSON. Cela permet de reprendre la gestion des membres et des vaisseaux entre différentes sessions.
Fonctionnement du programme
Menu principal

Le programme propose un menu interactif avec les options suivantes :

    Ajouter une personne civile à l'équipage
    Ajouter un opérateur (pilote ou technicien) à l'équipage
    Ajouter un Mentalist à l'équipage
    Afficher l'équipage
    Effectuer une action sur un membre du vaisseau
    Ajouter un vaisseau à la flotte
    Ajouter un membre à un vaisseau
    Vérifier la préparation de la flotte
    Quitter le programme et sauvegarder les données

Gestion des actions du Mentalist

Si un Mentalist souhaite effectuer l'action act :

    Si le Mentalist a plus de 19 mana, il peut choisir un pilote ou un technicien pour leur faire perdre 1 point d'expérience.
    Si le Mentalist a 19 mana ou moins, il ne pourra pas utiliser l'action act et devra recharger son mana via l'action recharge.

Gestion de l'expérience

    Les pilotes et techniciens peuvent perdre 1 point d'expérience lorsqu'ils sont ciblés par un Mentalist.
    Si un pilote ou technicien a déjà 0 d'expérience, il ne perdra pas d'expérience supplémentaire.
    Ajouter un vaisseau : On peut ajouter un vaisseau à la flotte avec un nom, un type (transport, guerre, marchand) et une condition (opérationnel, endommagé).
    Ajouter un membre à un vaisseau : Après avoir ajouté un membre à l'équipage, il peut être assigné à un vaisseau spécifique. L'équipage du vaisseau est mis à jour et le membre est retiré de l'équipage au sol.

4. Vérification de la préparation de la flotte

Avant de partir en mission, vous pouvez vérifier si la flotte est prête. Un vaisseau est considéré comme prêt si :

    Il y a au moins un pilote.
    Il y a au moins un technicien.
    Il y a au moins un Mentalist avec suffisamment de mana (au moins 50 mana).

5. Sauvegarde et chargement des données

Le programme permet de sauvegarder et de charger les données de l'équipage et des vaisseaux sous forme de fichiers JSON. Cela permet de reprendre la gestion des membres et des vaisseaux entre différentes sessions.
Fonctionnement du programme
Menu principal

Le programme propose un menu interactif avec les options suivantes :

    Ajouter une personne civile à l'équipage
    Ajouter un opérateur (pilote ou technicien) à l'équipage
    Ajouter un Mentalist à l'équipage
    Afficher l'équipage
    Effectuer une action sur un membre du vaisseau
    Ajouter un vaisseau à la flotte
    Ajouter un membre à un vaisseau
    Vérifier la préparation de la flotte
    Quitter le programme et sauvegarder les données

Gestion des actions du Mentalist

Si un Mentalist souhaite effectuer l'action act :

    Si le Mentalist a plus de 19 mana, il peut choisir un pilote ou un technicien pour leur faire perdre 1 point d'expérience.
    Si le Mentalist a 19 mana ou moins, il ne pourra pas utiliser l'action act et devra recharger son mana via l'action recharge.

Gestion de l'expérience

    Les pilotes et techniciens peuvent perdre 1 point d'expérience lorsqu'ils sont ciblés par un Mentalist.
    Si un pilote ou technicien a déjà 0 d'expérience, il ne perdra pas d'expérience supplémentaire.