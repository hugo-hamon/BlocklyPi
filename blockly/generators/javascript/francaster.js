Blockly.JavaScript['francaster_set_motor_power'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'POWER', Blockly.JavaScript.ORDER_ATOMIC);
    var dropdown_motor = block.getFieldValue('MOTOR');


    // Check the input ...
    if (value_power > 100) {
        alert("Maximum motor power for the robot is 100.");
        return '';
    }
    if (value_power < -100) {
        alert("Minimum motor power for the robot is 100.");
        return '';
    }

    // Generate the code ...
    return 'runPiRobotCommand("FrancasterController.setMotorPower", "' + dropdown_motor + '",' + value_power + ');';
};

Blockly.JavaScript['francaster_shift_motor_position'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'POWER2', Blockly.JavaScript.ORDER_ATOMIC);
    var dropdown_motor = block.getFieldValue('MOTOR2');
    var move = block.getFieldValue('MOVE');
    // Check the input ...
    if (value_power > 180) {
        alert("Maximum motor power for the robot is 180.");
        return '';
    }
    if (value_power < 0) {
        alert("Minimum motor power for the robot is 0.");
        return '';
    }
    if (move === 're') {
        value_power = value_power * -1;
    }
    if (dropdown_motor === 1) {
        alert("l'angle est " + value_power + " voila!");
        return '';
    }

    return 'runPiRobotCommand("FrancasterController.shiftMotorPosition", "' + dropdown_motor + '",' + value_power + ');';
};

Blockly.JavaScript['francaster_repeat_after_me'] = function (block) {
    return 'runPiRobotCommand("repeat");';
};

Blockly.JavaScript['francaster_ask_question'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return 'runPiRobotCommand("FrancasterController.answerQuestion", "' + text_qstn + '");';
};

Blockly.JavaScript['francaster_sleep'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'NBR_SEC', Blockly.JavaScript.ORDER_ATOMIC);
    return 'runPiRobotCommand("FrancasterController.setDelay", ' + value_power + ');';
};

Blockly.JavaScript['francaster_make_n_step'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD', Blockly.JavaScript.ORDER_ATOMIC);

    return 'runPiRobotCommand("FrancasterController.walk", ' + value_nb_steps + ');';
};

Blockly.JavaScript['francaster_make_n_steps_with_knee_lift'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD', Blockly.JavaScript.ORDER_ATOMIC);

    return 'runPiRobotCommand("FrancasterController.walkNStepsWithKneeLift", ' + value_nb_steps + ');';
};

Blockly.JavaScript['francaster_say_hi'] = function (block) {
    var value_nb_hi = Blockly.JavaScript.valueToCode(block, 'NBR_HI', Blockly.JavaScript.ORDER_ATOMIC);

    return 'runPiRobotCommand("FrancasterController.doHi", ' + value_nb_hi + ');';
};

Blockly.JavaScript['francaster_say_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    return dropdown_motor === "o"
        ? 'runPiRobotCommand("FrancasterController.doYes");'
        : 'runPiRobotCommand("FrancasterController.doNo");';
};

Blockly.JavaScript['francaster_reset_position'] = function (block) {
    return 'runPiRobotCommand("FrancasterController.reset_position");';
};
//*********************************************************