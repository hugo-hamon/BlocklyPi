Blockly.JavaScript['francaster_set_motor_position'] = function (block) {
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var angle = block.getFieldValue('ANGLE');

    return `runPiRobotCommand("francaster_set_motor_position", "${dropdown_motor_nb}","${angle}");`;
};

Blockly.JavaScript['francaster_shift_motor_position'] = function (block) {
    var dropdown_direction = block.getFieldValue('DIRECTION');
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var shift_angle = parseInt(block.getFieldValue('SHIFT_ANGLE'));

    if (dropdown_direction === "BACKWARD") {
        shift_angle = -shift_angle
    }

    return `runPiRobotCommand("francaster_shift_motor_position", "${dropdown_motor_nb}", "${shift_angle}");`;
};

Blockly.JavaScript['francaster_speak'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return `runPiRobotCommand("francaster_speak", "${text_qstn}");`;
};

Blockly.JavaScript['francaster_repeat'] = function (block) {
    return `runPiRobotCommand("francaster_repeat");`;
};

Blockly.JavaScript['francaster_answer_question'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return `runPiRobotCommand("francaster_answer_question", "${text_qstn}");`;
};

Blockly.JavaScript['francaster_sleep'] = function (block) {
    var sleepTime = block.getFieldValue("NB_SEC");
    return `runPiRobotCommand("francaster_sleep", "${sleepTime}");`;
};

Blockly.JavaScript['francaster_walk_n_steps'] = function (block) {
    var nb_steps = block.getFieldValue('NB_STEPS');

    return `runPiRobotCommand("francaster_walk_n_steps", "${nb_steps}");`;
};

Blockly.JavaScript['francaster_walk_n_steps_with_knee_lift'] = function (block) {
    var nb_steps = block.getFieldValue('NB_STEPS');

    return `runPiRobotCommand("francaster_walk_n_steps_with_knee_lift", "${nb_steps}");`;
};

Blockly.JavaScript['francaster_do_hi'] = function (block) {
    var value_nb_hi = block.getFieldValue('NB_HI');

    return `runPiRobotCommand("francaster_do_hi", "${value_nb_hi}");`;
};

Blockly.JavaScript['francaster_do_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    return dropdown_motor === "o" ? `runPiRobotCommand("francaster_do_yes");` : `runPiRobotCommand("francaster_do_no");`;
};

Blockly.JavaScript['francaster_reset_position'] = function (block) {
    return `runPiRobotCommand("francaster_reset_position");`;
};

Blockly.JavaScript['francaster_listen_and_answer'] = function (block) {
    return `runPiRobotCommand("francaster_listen_and_answer");`;
};

Blockly.JavaScript['francaster_dance'] = function (block) {
    return `runPiRobotCommand("francaster_dance");`;
};

Blockly.JavaScript['francaster_start_camera'] = function (block) {
    return `runPiRobotCommand("francaster_start_camera");`;
}

Blockly.JavaScript['francaster_stop_camera'] = function (block) {
    return `runPiRobotCommand("francaster_stop_camera");`;
}
