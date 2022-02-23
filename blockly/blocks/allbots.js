var ALLBOTS_COLOR = 0;

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
    ]);
}

Blockly.Blocks['allbots-set_motor_position'] = {
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
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-shift_motor_position'] = {
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
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-reset_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Remettre a la position initiale")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};