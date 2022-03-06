/**
 *  francas_bloc : Fait clignoter la led de la carte Arduino le nombre de fois indiqué par l'utilisateur. Ce bloc est à
 *  titre d'exemple et devrait être supprimé pour la mise en production.
 *      Lien vers la sauvegarde Blockly Factory :
 *      https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#jkn7oz
 * @type {{init: Blockly.Blocks.francas_block.init}}
 */
Blockly.Blocks['francas_block'] = {
    init: function () {
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Francas Bloc")
            .appendField(new Blockly.FieldImage(
                "https://www.bafa-lesfrancas.fr/sites/default/files/2017-08/logo-francas_0.png",
                100,
                50,
                {
                    alt: "*",
                    flipRtl: "FALSE"
                }));
        this.appendDummyInput()
            .appendField("Un bloc pour faire des tests");
        this.appendDummyInput()
            .appendField("Faire clignoter la led de la carte ")
            .appendField(new Blockly.FieldTextInput("3"), "nbBlinks")
            .appendField(" fois.");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(30);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};