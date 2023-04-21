# Exemple pour l'ajout d'une fonction au robot francaster

## Etape 1: Ajout de la fonction
Dans cette exemple la fonction sera ajoutée au fichier **robot/controller/francaster_controller.py**

Un exemple de fonction est donné ci-dessous:
```py
def francaster_do_yes(self) -> None:
    """Do a yes gesture"""
    sleep(.5)
    MOTORS["HEAD_YAW"].set_motor_position(60)
    sleep(.5)
    MOTORS["HEAD_YAW"].set_motor_position(120)
```

## Etape 2: Ajout de la fonction au html
Une fois la fonction ajoutée au fichier **robot/controller/francaster_controller.py**, il faut l'ajouter au fichier **index.html**.

Dans cette exemple, la fonction sera ajoutée dans la section **Francaster**.

```html
<category id="catFrancaster" name="Francaster">
    ...
    <block type="francaster_do_yes"></block>
</category>
```

## Etape 3: Ajout de la fonction au blocs
Pour cette étape nous allons nous rendre dans le fichier **blockly/blocks/francaster.js**.

La fonction est ajoutée comme suit:
```js
Blockly.Blocks['francaster_do_yes'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Dire ")
            .appendField(new Blockly.FieldDropdown([["oui", "o"], ["non", "n"]]), "MOVE")
            .appendField("de la tete")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
```

## Etape 4: Ajout de la fonction au code js
Pour cette dernière étape nous allons nous rendre dans le fichier **blockly/generators/javascript/francaster.js**.

La fonction est ajoutée comme suit:
```js
Blockly.JavaScript['francaster_do_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    return dropdown_motor === "o" ? `runPiRobotCommand("francaster_do_yes");` : `runPiRobotCommand("francaster_do_no");`;
};
```

## Fin
Une fois toutes les étapes effectuées, il suffit de redémarrer le serveur pour que les modifications soient prises en compte.