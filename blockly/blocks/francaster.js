const FRANCASTER_COLOR = 60;

function getMotorDropdownFrancaster() {
    return new Blockly.FieldDropdown([
        ["inconnue", "0"],
        ["inconnue", "1"],
        ["inconnue", "2"],
        ["Epaule gauche 1", "3"],
        ["Epaule droite 1", "4"],
        ["Epaule droite 2", "5"],
        ["Epaule droite 3", "6"],
        ["Coudre droit", "7"],
        ["Hanche gauche", "8"],
        ["Genou gauche", "9"],
        ["Pied gauche", "10"],
        ["Hanche droite", "11"],
        ["Genou droit", "12"],
        ["Pied droit", "13"],
        ["Nuque", "14"],
        ["Tete", "15"]
    ]);
}

Blockly.Blocks['francaster_set_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Mettre le moteur")
            .appendField(getMotorDropdownFrancaster(), "MOTOR_NB");
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

Blockly.Blocks['francaster_shift_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Faire")
            .appendField(new Blockly.FieldDropdown([
                ["avancer", "FORWARD"],
                ["reculer", "BACKWARD"]
            ]), "DIRECTION")
            .appendField("le moteur")
            .appendField(getMotorDropdownFrancaster(), "MOTOR_NB");
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

Blockly.Blocks['francaster_sleep'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Dormir pendant ")
            .appendField(new Blockly.FieldTextInput("1"), "NB_SEC")
            .appendField(" secondes");
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster_walk_n_steps'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Avancer de ")
            .appendField(new Blockly.FieldTextInput("1"), "NB_STEPS")
            .appendField(" pas");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster_do_hi'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Dire bonjour ")
            .appendField(new Blockly.FieldTextInput("1"), "NB_HI")
            .appendField(" fois");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster_walk_n_steps_with_knee_lift'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Avancer de ")
            .appendField(new Blockly.FieldTextInput("1"), "NB_STEPS")
            .appendField(" pas avec levés de genoux");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

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

Blockly.Blocks['francaster_reset_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Remettre a la position initiale")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

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

Blockly.Blocks['francaster_answer_question'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Demander")
            .appendField(new Blockly.FieldTextInput("comment tu t'appelles?"), "QSTN");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("Pose une question au robot");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['francaster_listen_and_answer'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Pose moi une question");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(FRANCASTER_COLOR);
        this.setTooltip("Parle et le robot te répondra");
        this.setHelpUrl("");
    }
};
