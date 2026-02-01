---
title: "À propos d'Eclipse SW360"
linkTitle: À propos
menu:
    main:
        weight: 10

---

{{< blocks/cover image_anchor="top" height="sm" color="primary" >}}
{{< page/header >}}
{{< /blocks/cover >}}

<div class="container l-container--padded">


<div class="row">
<div class="col-12 col-lg-8">

Aujourd'hui, dans la plupart des cas, les logiciels ne sont pas créés à partir de zéro, mais plutôt assemblés à partir de divers composants logiciels tiers préemballés. Par conséquent, les organisations sont confrontées aux défis suivants :

* Vérifier différents aspects de la conformité lors de l'utilisation de composants logiciels tiers : conformité des licences, contrôles ECC, évaluations de propriété intellectuelle, etc.
* Partager les connaissances sur les composants logiciels et leurs qualités. Par exemple, quels composants logiciels devraient être recommandés, lesquels devraient être abandonnés selon quels critères ?
* Fournir une vue d'ensemble des composants utilisés : une organisation et sa gestion de la chaîne d'approvisionnement doivent disposer d'informations sur les actifs intégrés dans quels produits ou solutions.

Ces trois cas d'utilisation principaux ciblent différents rôles dans une organisation : responsables qualité, développeurs de logiciels, conseillers juridiques, architectes logiciels, responsables R&D, etc. Cependant, tous ces cas d'utilisation partagent un besoin commun d'un hub central qui gère les informations sur les composants logiciels.

SW360 est un projet logiciel open source sous licence EPL-2.0 qui fournit à la fois une application web et un référentiel pour collecter, organiser et rendre disponibles les informations sur les composants logiciels. Il établit un hub central pour les composants logiciels dans une organisation. SW360 permet de :

* suivre les composants utilisés par un projet/produit,
* évaluer les vulnérabilités de sécurité,
* maintenir les obligations de licence,
* appliquer des politiques, et
* générer des documents juridiques.

Par exemple, SW360 peut déclencher un processus de vérification dans l'outil de conformité open source FOSSology et importer le rapport de vérification résultant. Les données sont soit stockées dans la base de données de SW360, soit importées à la volée depuis des sources externes. À l'avenir, nous prévoyons d'avoir des fédérations d'instances SW360 qui partagent des informations sélectionnées. Outre son interface utilisateur web, toutes les fonctionnalités de SW360 sont disponibles via une API qui permet une intégration dans les outils devops existants.
</div>

</div>
</div>