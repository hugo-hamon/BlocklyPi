# Personnalisation du projet BlocklyPi

Ce projet est très similaire au projet Blocklino des Francas de Seine Maritime. Pour savoir comment le personnaliser à
vos besoins, veuillez vous référer à la documentation de Blocklino, dans le
document [personnalisation.md](https://github.com/antoinelabard/blocklino/blob/demo/personnalisation.md) de la branche
demo. ce document reprend son squelette en ne modifiant que les éléments particuliers à Blockly.

## Ajout d'une nouvelle catégorie à la boîte à outils

Modifiez le fichier [index.html](index.html), entre les balises `<xml>`.

## Création d'un bloc

### Ajout du bloc au projet

Modifiez le fichier [blockly/blocks/pirobot.js](blockly/blocks/pirobot.js), à la racine du fichier.

### Personnalisation du générateur de code

Modifiez le fichier [blockly/generators/javascript/pirobot.js](blockly/generators/javascript/pirobot.js)

Inutile ici d'adapter le code comme décrit dans
la [documentation originale](https://github.com/antoinelabard/blocklino/blob/demo/personnalisation.md#personnalisation-du-g%C3%A9n%C3%A9rateur-de-code)
. L'entête doit donc ressembler à ceci :

```js
Blockly.JavaScript['francas_block'] = function(block) {
    // ...
}
```

