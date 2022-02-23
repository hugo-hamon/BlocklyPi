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