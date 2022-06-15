Blockly.JavaScript['allbots-set_motor_position'] = function (block) {
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var angle = block.getFieldValue('ANGLE');

    return `runPiRobotCommand("allbots-set_motor_position", "${dropdown_motor_nb}","${angle}");`;
};

Blockly.JavaScript['allbots-shift_motor_position'] = function (block) {
    var dropdown_direction = block.getFieldValue('DIRECTION');
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var shift_angle = parseInt(block.getFieldValue('SHIFT_ANGLE'));

    if (dropdown_direction === "BACKWARD") {
        shift_angle = -shift_angle
    }

    return `runPiRobotCommand("allbots-shift_motor_position", "${dropdown_motor_nb}", "${shift_angle}");`;
};

Blockly.JavaScript['allbots-reset_position'] = function (block) {
    return `runPiRobotCommand("allbots-reset_position");`;
};

Blockly.JavaScript['avancer'] = function(block) {
    var code = 'runPiRobotCommand("allbotsController.avancer");';
    return code;
};

Blockly.JavaScript['reculer'] = function(block) {
    var code = 'runPiRobotCommand("allbotsController.reculer");';
    return code;
};

Blockly.JavaScript['tourner_a_gauche'] = function(block) {
    var code = 'runPiRobotCommand("allbotsController.tourner_gauche");';
    return code;
};

Blockly.JavaScript['tourner_a_droite'] = function(block) {
    var code = 'runPiRobotCommand("allbotsController.tourner_droite");';
    return code;
};

Blockly.JavaScript['coucou_motor'] = function(block) {
    var dropdown_motor = block.getFieldValue('motor');
    var code = 'runPiRobotCommand("allbotsController.coucou", "' + dropdown_motor + '");';
    return code;
};

Blockly.JavaScript['allbot_sleep'] = function (block) {
    var value_time = Blockly.JavaScript.valueToCode(block, 'NBR_SEC', Blockly.JavaScript.ORDER_ATOMIC);
    return 'runPiRobotCommand("FrancasterController.allbot_sleep", ' + value_time + ');';
};