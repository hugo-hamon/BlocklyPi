Blockly.JavaScript['francaster-set_motor_position'] = function (block) {
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var angle = block.getFieldValue('ANGLE');

    // Generate the code ...
    return `runPiRobotCommand("francaster-set_motor_position", "${dropdown_motor_nb}","${angle}");`;
};

Blockly.JavaScript['francaster-shift_motor_position'] = function (block) {
    var dropdown_direction = block.getFieldValue('DIRECTION');
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var shift_angle = parseInt(block.getFieldValue('SHIFT_ANGLE'));

    if (dropdown_direction === "BACKWARD") {
        shift_angle = -shift_angle
    }

    return `runPiRobotCommand("francaster-shift_motor_position", "${dropdown_motor_nb}", "${shift_angle}");`;
};

Blockly.JavaScript['francaster-repeat'] = function (block) {
    return `runPiRobotCommand("repeat");`;
};

Blockly.JavaScript['francaster-answer_question'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return `runPiRobotCommand("francaster-answer_question", "${text_qstn}");`;
};

Blockly.JavaScript['francaster-sleep'] = function (block) {
    var sleepTime = Blockly.JavaScript.valueToCode(block, 'NBR_SEC', Blockly.JavaScript.ORDER_ATOMIC);
    return `runPiRobotCommand("francaster-sleep", "${sleepTime}");`;
};

Blockly.JavaScript['francaster_walk_n_steps'] = function (block) {
    var nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD', Blockly.JavaScript.ORDER_ATOMIC);

    return `runPiRobotCommand("francaster-walk_n_steps", "${nb_steps}");`;
};

Blockly.JavaScript['francaster_walk_n_steps_with_knee_lift'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD', Blockly.JavaScript.ORDER_ATOMIC);

    return `runPiRobotCommand("francaster-walk_n_steps_with_knee_lift", "${value_nb_steps}");`;
};

Blockly.JavaScript['francaster-do_hi'] = function (block) {
    var value_nb_hi = Blockly.JavaScript.valueToCode(block, 'NBR_HI', Blockly.JavaScript.ORDER_ATOMIC);

    return `runPiRobotCommand("francaster-do_hi", "${value_nb_hi}");`;
};

Blockly.JavaScript['francaster-do_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    return dropdown_motor === "o" ? `runPiRobotCommand("francaster-do_yes");` : `runPiRobotCommand("francaster-do_no");`;
};

Blockly.JavaScript['francaster-reset_position'] = function (block) {
    return `runPiRobotCommand("francaster-reset_position");`;
};
