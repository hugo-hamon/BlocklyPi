Blockly.Blocks['avancer'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Avancer le Robot ");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("");
 this.setHelpUrl("");
  }
 };
 
 Blockly.Blocks['reculer'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Reculer le Robot ");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("");
 this.setHelpUrl("");
  }
 };
 
Blockly.Blocks['tourner_a_gauche'] = {
  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("Tourner à gauche");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['tourner_a_droite'] = {
  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("Tourner à droite");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['angle_motor'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Tourner le moteur ")
        .appendField(new Blockly.FieldDropdown([["01","0"], ["02","1"], ["03","2"], ["04","3"],
                                                ["05","4"],["06","5"],["07","6"],["08","7"]]), "motor")
        .appendField("de ");
    this.appendValueInput("angle")
        .setCheck("Number");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(180);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['reset_position'] = {
  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("Réinitialiser la position");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(315);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['coucou_motor'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Faire coucou avec la patte ")
        .appendField(new Blockly.FieldDropdown([["gauche","0"], ["droite","1"]]), "motor");
        
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(180);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
Blockly.Blocks['allbot_sleep'] = {
    init: function () {
        this.appendValueInput("NBR_SEC").appendField("Dormir pendant");
        this.appendDummyInput().appendField("secondes");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(220);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

