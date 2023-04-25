Blockly.JavaScript['allbot_set_motor_position'] = function (block) {
    let dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    let angle = block.getFieldValue('ANGLE');

    return `runPiRobotCommand("allbot_set_motor_position", "${dropdown_motor_nb}","${angle}");`;
};

Blockly.JavaScript['allbot_shift_motor_position'] = function (block) {
    let dropdown_direction = block.getFieldValue('DIRECTION');
    let dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    let shift_angle = parseInt(block.getFieldValue('SHIFT_ANGLE'));

    if (dropdown_direction === "BACKWARD") {
        shift_angle = -shift_angle
    }

    return `runPiRobotCommand("allbot_shift_motor_position", "${dropdown_motor_nb}", "${shift_angle}");`;
};

Blockly.JavaScript['allbot_reset_position'] = function (block) {
    return `runPiRobotCommand("allbot_reset_position");`;
};

Blockly.JavaScript['allbot_move_forward'] = function(block) {
    return 'runPiRobotCommand("allbot_move_forward");';
};

Blockly.JavaScript['allbot_move_backward'] = function(block) {
    return 'runPiRobotCommand("allbot_move_backward");';
};

Blockly.JavaScript['allbot_turn_left'] = function(block) {
    return 'runPiRobotCommand("allbot_turn_left");';
};

Blockly.JavaScript['allbot_turn_right'] = function(block) {
    return 'runPiRobotCommand("allbot_turn_right");';
};

Blockly.JavaScript['allbot_do_hi'] = function(block) {
    let dropdown_motor = block.getFieldValue('motor');
    return 'runPiRobotCommand("allbot_do_hi", "' + dropdown_motor + '");';
};


Blockly.JavaScript['allbot_sleep'] = function (block) {
    let value_time = block.getFieldValue('NBR_SEC');
    return 'runPiRobotCommand("allbot_sleep", ' + value_time + ');';
};