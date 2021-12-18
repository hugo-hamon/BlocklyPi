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

Blockly.Blocks['block_drt'] = {
  init: function() {
    this.appendValueInput("NBR_SEC").appendField("Dormir pendant");
    this.appendDummyInput().appendField("secondes");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(185);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['block_move_forward'] = {
  init: function() {
    this.appendValueInput("NBR_PAS_FORWARD").appendField("Avancer de");
    this.appendDummyInput().appendField("pas");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['block_hi'] = {
  init: function() {
    this.appendValueInput("NBR_HI").appendField("Saluer")
    this.appendDummyInput().appendField("fois");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['block_move_forward_gn_cd'] = {
  init: function() {
    this.appendValueInput("NBR_PAS_FORWARD").appendField("Avancer de");
    this.appendDummyInput().appendField("pas avec lever de genoux");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['block_motor_dc'] = {
  init: function() {
  	this.appendDummyInput()
  		.appendField("faire tourner vers")
        .appendField(new Blockly.FieldDropdown([["l'avant","av"], ["l'arrière","re"]]), "MOVE")
  	this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['block_yes'] = {
  init: function() {
  	this.appendDummyInput()
  		.appendField("dire ")
        	.appendField(new Blockly.FieldDropdown([["oui","o"], ["non","n"]]), "MOVE")
		.appendField("de la tete")
  	this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['block_init'] = {
  init: function() {
  	this.appendDummyInput()
		.appendField("remettre a la position initiale")
  	this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['dire'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Dire")
        .appendField(new Blockly.FieldTextInput("Bonjour"), "TEXT");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("Fait parler le robot");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['repete'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Répète après moi");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("Parle et le robot répètera ce que tu dis");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['question'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Demande")
        .appendField(new Blockly.FieldTextInput("comment tu t'appelles?"), "QSTN");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("Pose une question au robot");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['question_vocale'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Demande")
        .appendField(new Blockly.FieldTextInput("comment tu t'appelles?"), "QSTN");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("Pose une question au robot");
 this.setHelpUrl("");
  }
};
