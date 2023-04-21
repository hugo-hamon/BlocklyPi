# Personnalisation du projet BlocklyPi

Ce guide permet de définir la procédure pour personnaliser ce fork du projet BlocklyPi, à savoir ajouter des blocs, des boîtes à outils et permettre à ces composants d'interagir avec le port GPIO du Raspberry Pi. Ces instructions sont spécifiques au projet actuel et servent de mémo pour faciliter sa personnalisation, dans le cadre des missions réalisées par les Francas de Seine-Maritime.

Si vous êtes débutant avec ce projet, lisez le guide de [Blockly](https://developers.google.com/blockly/guides/overview) pour avoir un guide faisant le tour des principaux concepts. Les notions de programmation en bloc, toolbox, workspace ou autres demandent à être comprises pour suivre ce guide, et ne seront pas redéfinies ici.

## Contribution
### Architecture du projet

Le projet est constitué de 2 parties :
- Un frontend écrit en JavaScript qui fournit une interface à l'utilisateur pour communiquer avec son robot.
- Un backend écrit en Python qui permet de communiquer avec le port GPIO du Raspberry Pi.

Ces 2 composants utilisent un serveur XML-RPC pour communiquer. Il doit être instancié en exécutant la commande python3 server.py à la racine du projet.

Pour ce qui nous intéresse concernant l'ajout d'actions à nos robots, voici l'arborescence du projet :
```
BlocklyPi/
    blockly/
        blocks/
            allbots.js : Le script contenant le code de définition des blocs pour le robot Allbots.
            francaster.js : Le script contenant le code de définition des blocs pour le robot Francaster.
        generators/
            allbots.js : Le script contenant les générateurs de code des blocs associés au robot Allbots.
            francaster.js : Le script contenant les générateurs de code des blocs associés au robot Francaster.
    robot/
        controller/
            allbotsController.py : Le module contenant toutes les actions qu'un robot Allbots est capable d'exécuter.
            francasterController.py : Le module contenant toutes les actions qu'un robot Francaster est capable d'exécuter.
            controller.py : Le module regroupant les actions communes à tous les robots.
        robotMotor.py : Une classe contenant tout le code de base permettant de contrôler un servomoteur donné.
    server.py : Le script où nous allons instancier notre serveur XML-RPC et définir l'ensemble des fonctions qu'il peut interpréter.
```
### Ajout d'une nouvelle catégorie à la boîte à outils
La boîte à outils par défaut utilisée par le projet est dans le fichier index.html. Chaque nouvelle catégorie doit être placée dans ce fichier, dans la balise <xml>.

Une catégorie a la syntaxe suivante :
```html
<category id="robot_id" name="robot_name">
   <block type="robot_name_action_name1"></block>
   <block type="robot_name_action_name2"></block>
   <!---etc.-->
</category>
```

### Ajout d'un nouveau bloc
Le code décrivant un bloc a 3 composantes :

- La déclaration du bloc dans la **boîte à outils** : Elle permet de rendre visible le bloc dans la catégorie de son choix.
- La déclaration de l'interface utilisateur du bloc : L'apparence et toutes les possibilités d'interaction de l'utilisateur avec le bloc :
  - Sa couleur.
  - Ses éléments descriptifs (textes, images, etc).
  - Ses paramètres (entrées de valeurs, déclarations d'autres blocs, etc).
  - Le générateur de code associé au bloc : Le composant chargé d'appeler la fonction liée à l'action que l'utilisateur souhaite exécuter, en prenant en compte les paramètres de l'utilisateur.

Par convention, le nom des blocs et de toutes les fonctions qui leur sont associées doivent respecter le format suivant : **"robot_name_action_name"**. Tous les blocs d'une même catégorie devront avoir la même teinte, qui pourra être définie par une constante ROBOT_COLOR dans le script de définition des blocs de cette catégorie, dans **blockly/blocks/**.

#### Définition et générateur de code du bloc
Pour faciliter l'écriture du code définissant le comportement de notre bloc, nous pouvons utiliser l'outil [Blockly Factory](https://blockly-demo.appspot.com/static/demos/blockfactory/index.html).

La syntaxe pour les blocks dans le dossier **blockly/blocks/** est la suivante :
```js
Blockly.Blocks['francaster_repeat'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Répète après moi");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("Parle et le robot répètera ce que tu dis");
        this.setHelpUrl("");
    }
};
```

Pour le dossier **blockly/generators/**, la syntaxe est la suivante :
```js
Blockly.JavaScript['francaster_repeat'] = function (block) {
    return `runPiRobotCommand("francaster_repeat");`;
};
```

`runPiRobotCommand` est la commande utilisée pour communiquer avec le serveur XML-RPC. Ses arguments sont le nom de la
fonction appelée dans le backend, ainsi que la liste des valeurs de ses paramètres.

Une fois le bloc créé, différents morceaux de code sont à insérer dans le projet de la manière suivante :

- La définition du bloc : [`blockly/blocks`](../blockly/blocks).
- Le générateur de code du bloc : [`blockly/generators/javascript`](../blockly/generators/javascript).
- La ligne `<block type="robot_name-action_name"></block>` : [`index.html`](../index.html), au sein de la catégorie
  voulue.

Ne pas oublier de faire appel à ces scripts, en ajoutant dans la balise `<head>` de [`index.html`](../index.html):

- `<script src="blockly/blocks/francaster.js"></script>`
- `<script src="blockly/generators/javascript/francaster.js"></script>`

## Déclaration et description d'une fonction côté backend

Toutes les fonctions relatives à un robot doivent être décrites dans un module `robot_name_controller.py` dans `robot/controller/`.
Chaque action que le robot peut exécuter est décrite par une fonction de la manière suivante :

```Python
def robot_name_action_name(self, arg1: str, arg2: str) -> None:
# actions...
```
Si un nouveau robot est ajouté, assurez-vous de l'importer dans le fichier `robot/controller/controller.py` et de l'ajouter à ses parents.

### Configuration du matériel

Le Raspberry Pi utilise une carte de commande
nommée [pca9685](https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/) pour pouvoir piloter les moteurs du robot depuis son port GPIO. Chaque moteur est nommé selon le numéro du connecteur sur lequel il est branché sur cette carte. C'est le numéro à indiquer lorsque l'on instancie un moteur dans le module de contrôle du robot à l'aide de la classe `RobotMotor`, dans le champ `id`.

### Déploiement

Le dossier du projet peut simplement être placé dans le répertoire personnel de l'utiliser (`~/BlocklyPi`). Des informations plus détaillées sont déjà présentes dans le [README](../README.md) du projet. Si le code est mis à jour vers une nouvelle version, il peut arriver que les changements soient mal pris en compte. La meilleure solution dans ce cas est de redémarrer le système et de relancer le serveur XML-RPC.

### Francaster
![](res/photo-francaster.jpg)

Francaster est le nom donné au robot dont le modèle est celui d'Aster, un androïde dont les différentes parties du corps
sont imprimables en 3D.

Liens utiles :
- [Thingiverse](https://www.thingiverse.com/thing:3992150)
- [GitHub](https://github.com/poppy-project/poppy-humanoid)
- [poppy-project.org](https://www.poppy-project.org/en/robots/poppy-humanoid/)

### Allbots
![](res/photo-allbots.jpg)

Allbots est un robot à quatre pattes imprimable en 3D, dont l'apparence peut faire penser à une araignée ou à un crabe.

Liens utiles :
- [Thingiverse](https://www.thingiverse.com/thing:1434665)
- [Manuel](https://manuals.whadda.com/category.php?id=85)

## Ajout de questions / réponses et événements pour le robot Francaster

### Ajout de questions / réponses

Afin de rendre le robot plus interactif, il est possible d'ajouter des questions et des réponses. Pour ce faire, if suffit de suivre les étapes suivantes :

1. Ajoutez la question et la réponse dans le fichier `robot/speech/json/questions.json`.
2. Une fois le fichier modifié, un script Python se trouve dans le dossier `robot/speech` permettant de générer le fichier `normalized_questions.json`. Ce fichier a pour objectif de normaliser les questions et les réponses. Pour exécuter ce script, placez-vous dans le dossier `robot/speech` et lancez la commande `python3 normalize_questions.py`.

### Ajout d'événements

L'ajout d'événements au robot permet de lui donner des réactions spécifiques lorsqu'il détecte un mot-clé ou une partie de phrase. Pour ce faire, suivez les étapes ci-dessous :

1. Ajoutez l'événement dans le fichier `robot/speech/event_handler.py`, au sein de la fonction `process_question`.
2. Ajoutez la fonction qui sera appelée lors de l'événement dans le fichier `robot/speech/event_handler.py`.

Voici un exemple d'événement :

```Python
def process_question(self, question: str) -> None:
    ...
    elif "blague" in question:
        self.process_joke()
    ...
```

Et un exemple de fonction associée :

```Python
def process_joke(self) -> None:
    """Traite l'événement blague"""
    joke = random.choice(list(self.jokes.items()))
    self.francaster.speak(joke[0])
    time.sleep(2)
    self.francaster.speak(joke[1])
```

Les questions étant normalisées, les mots-clés ne doivent pas contenir de majuscules, d'accent ou de caractères spéciaux.