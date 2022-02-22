Blockly.JavaScript['francaster_set_motor_power'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'POWER', Blockly.JavaScript.ORDER_ATOMIC);
    var dropdown_motor = block.getFieldValue('MOTOR');

    // Generate the code ...
    return 'runPiRobotCommand("robotController.set_motor_position", "' + dropdown_motor + '",' + value_power + ');';
};

Blockly.JavaScript['francaster_shift_motor_position'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'POWER2', Blockly.JavaScript.ORDER_ATOMIC);
    var dropdown_motor = block.getFieldValue('MOTOR2');
    var move = block.getFieldValue('MOVE');

    return 'runPiRobotCommand("robotController.shift_motor_position", "' + dropdown_motor + '",' + value_power + ');';
};

Blockly.JavaScript['francaster_repeat_after_me'] = function (block) {
    return 'runPiRobotCommand("repeat");';
};

Blockly.JavaScript['francaster_ask_question'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return 'runPiRobotCommand("FrancasterController.answer_question", "' + text_qstn + '");';
};

Blockly.JavaScript['francaster_sleep'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'NBR_SEC', Blockly.JavaScript.ORDER_ATOMIC);
    return 'runPiRobotCommand("FrancasterController.setDelay", ' + value_power + ');';
};

Blockly.JavaScript['francaster_walk_n_steps'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD', Blockly.JavaScript.ORDER_ATOMIC);

    return 'runPiRobotCommand("FrancasterController.walk_n_steps", ' + value_nb_steps + ');';
};

Blockly.JavaScript['francaster_walk_n_steps_with_knee_lift'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD', Blockly.JavaScript.ORDER_ATOMIC);

    return 'runPiRobotCommand("FrancasterController.walk_n_steps_with_knee_lift", ' + value_nb_steps + ');';
};

Blockly.JavaScript['francaster_say_hi'] = function (block) {
    var value_nb_hi = Blockly.JavaScript.valueToCode(block, 'NBR_HI', Blockly.JavaScript.ORDER_ATOMIC);

    return 'runPiRobotCommand("FrancasterController.do_hi", ' + value_nb_hi + ');';
};

Blockly.JavaScript['francaster_say_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    return dropdown_motor === "o"
        ? 'runPiRobotCommand("FrancasterController.do_yes");'
        : 'runPiRobotCommand("FrancasterController.do_no");';
};

Blockly.JavaScript['francaster_reset_position'] = function (block) {
    return 'runPiRobotCommand("FrancasterController.reset_position");';
};
