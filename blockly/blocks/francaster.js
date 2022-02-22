var FRANCASTER_COLOR = 60;

function getMotorDropdown() {
    return new Blockly.FieldDropdown([
        ["0", "0"],
        ["1", "1"],
        ["2", "2"],
        ["3", "3"],
        ["4", "4"],
        ["5", "5"],
        ["6", "6"],
        ["7", "7"],
        ["8", "8"],
        ["9", "9"],
        ["10", "10"],
        ["11", "11"],
        ["12", "12"],
        ["13", "13"],
        ["14", "14"],
        ["15", "15"]
    ]);
}

Blockly.Blocks['francaster-set_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Mettre le moteur")
            .appendField(getMotorDropdown(), "MOTOR_NB");
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_RIGHT)
            .appendField("à")
            .appendField(new Blockly.FieldTextInput("0"), "ANGLE")
            .appendField("degrés.");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster-shift_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Faire")
            .appendField(new Blockly.FieldDropdown([
                ["avancer", "FORWARD"],
                ["reculer", "BACKWARD"]
            ]), "DIRECTION")
            .appendField("le moteur")
            .appendField(getMotorDropdown(), "MOTOR_NB");
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_RIGHT)
            .appendField("de")
            .appendField(new Blockly.FieldTextInput("0"), "SHIFT_ANGLE")
            .appendField("degrés");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster-sleep'] = {
    init: function () {
        this.appendValueInput("NBR_SEC").appendField("Dormir pendant");
        this.appendDummyInput().appendField("secondes");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster_walk_n_steps'] = {
    init: function () {
        this.appendValueInput("NBR_PAS_FORWARD").appendField("Avancer de");
        this.appendDummyInput().appendField("pas");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster-do_hi'] = {
    init: function () {
        this.appendValueInput("NBR_HI").appendField("Saluer");
        this.appendDummyInput().appendField("fois");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster_walk_n_steps_with_knee_lift'] = {
    init: function () {
        this.appendValueInput("NBR_PAS_FORWARD").appendField("Avancer de");
        this.appendDummyInput().appendField("pas avec lever de genoux");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster-do_yes'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("dire ")
            .appendField(new Blockly.FieldDropdown([["oui", "o"], ["non", "n"]]), "MOVE")
            .appendField("de la tete")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster-reset_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("remettre a la position initiale")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster-repeat'] = {
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

Blockly.Blocks['francaster-answer_question'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Demande")
            .appendField(new Blockly.FieldTextInput("comment tu t'appelles?"), "QSTN");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("Pose une question au robot");
        this.setHelpUrl("");
    }
};
