Blockly.Blocks['robot_motor_power'] = {
	init : function() {
		this.setHelpUrl('http://www.example.com/');
		this.setColour(0);
		this.appendValueInput("POWER").setCheck("Number").appendField(
				new Blockly.FieldDropdown([
						[ "Set the power of the left motor to", "LEFT" ],
						[ "Set the power of the right motor to", "RIGHT" ] ]),
				"MOTOR");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
		this.setTooltip('');
	}
};

Blockly.Blocks['control_key_down'] = {
	init : function() {
		this.setHelpUrl('http://www.example.com/');
		this.setColour(210);
		this.appendDummyInput().appendField(new Blockly.FieldDropdown([
                        [ "On ↓ key", "DOWN" ],	[ "On ↑ key", "UP" ], 
                        [ "On ← key", "LEFT" ],	[ "On → key", "RIGHT" ] ]), "KEY")
            .appendField(new Blockly.FieldDropdown([ [ "up", "UP" ], [ "down", "DOWN" ] ]), "TYPE");
        
		this.appendStatementInput("STATEMENTS");
		this.setTooltip('');
	}
};
//  francas_bloc : Fait clignoter la led de la carte Arduino le nombre de fois indiqué par l'utilisateur. Ce bloc est à
//      titre d'exemple et devrait être supprimé pour la mise en production.
//      Lien vers la sauvegarde Blockly Factory :
//      https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#jkn7oz
Blockly.Blocks['francas_block'] = {
  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("Francas Bloc")
        .appendField(
            new Blockly.FieldImage("https://www.bafa-lesfrancas.fr/sites/default/files/2017-08/logo-francas_0.png",
            100, 50, { alt: "*", flipRtl: "FALSE" }));
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