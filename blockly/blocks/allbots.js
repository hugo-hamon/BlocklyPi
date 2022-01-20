var ALLBOTS_COLOR = 0;

Blockly.Blocks['allbots_shift_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("faire")
            .appendField(new Blockly.FieldDropdown([["avancer", "av"], ["reculer", "re"]]), "MOVE")
        this.appendValueInput("POWER2").setCheck("Number").appendField(
            new Blockly.FieldDropdown([
                ["le moteur 0 de", "0"],
                ["le moteur 1 de", "1"],
                ["le moteur 2 de", "2"],
                ["le moteur 3 de", "3"],
                ["le moteur 4 de", "4"],
                ["le moteur 5 de", "5"],
                ["le moteur 6 de", "6"],
                ["le moteur 7 de", "7"],
                ["le moteur 8 de", "8"]]),
            "MOTOR2");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};