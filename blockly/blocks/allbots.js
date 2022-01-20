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
                ["le moteur 8 de", "8"],
                ["le moteur 9 de", "9"],
                ["le moteur 10 de", "10"],
                ["le moteur 11 de", "11"],
                ["le moteur 12 de", "12"],
                ["le moteur 13 de", "13"],
                ["le moteur 14 de", "14"],
                ["le moteur 15 de", "15"]]),
            "MOTOR2");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};