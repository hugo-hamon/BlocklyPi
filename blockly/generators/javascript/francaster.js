Blockly.JavaScript['set_motor_power'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'POWER',
        Blockly.JavaScript.ORDER_ATOMIC);
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
    var code = 'runPiRobotCommand("setRobotMotorPower", "' + dropdown_motor + '",' + value_power + ');';
    return code;
};

Blockly.JavaScript['control_key_down'] = function (block) {
    // The inputs ...
    var statements_statements = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
    var dropdown_key = block.getFieldValue('KEY');
    var dropdown_type = block.getFieldValue('TYPE');

    // Determine the key code to listen for.
    var keyCode = 0;
    if (dropdown_key === 'UP') {
        keyCode = 38;
    } else if (dropdown_key === 'DOWN') {
        keyCode = 40;
    } else if (dropdown_key === 'RIGHT') {
        keyCode = 39;
    } else if (dropdown_key === 'LEFT') {
        keyCode = 37;
    } else {
        return '';
    }

    // Determine the type of event to listen to.
    var type = "keydown";
    if (dropdown_type === 'UP') {
        type = "keyup";
    } else if (dropdown_type === 'DOWN') {
        type = "keydown";
    } else {
        return '';
    }

    // Generate the code for the callback (using only keyCode an charCode).
    var callbackCode = 'var code = keyCode; if (charCode && code == 0) {code = charCode;}; if (code ===' + keyCode + ') {' + statements_statements + '}';
    callbackCode = callbackCode.replace(/\n/g, "\\n");
    callbackCode = callbackCode.replace(/["]+/g, "\\\"");

    // Assemble JavaScript into code variable.
    var code = 'window.addKeyEventListenerForBlock("' + block.id + '", "' + type + '", "' + callbackCode + '");';
    return code;
};

Blockly.JavaScript['shift_motor_position'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'POWER2',
        Blockly.JavaScript.ORDER_ATOMIC);
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
    if (move == 're') {
        value_power = value_power * -1;
    }
    if (dropdown_motor == 1) {
        alert("l'angle est " + value_power + " voila!");
        return '';
    }

    var code = 'runPiRobotCommand("setRobotMotorPower2", "' + dropdown_motor + '",' + value_power + ');';
    return code;
};

Blockly.JavaScript['francster_say_hi'] = function (block) {
    var value_text = block.getFieldValue('TEXT');
    var code = 'runPiRobotCommand("speak", "' + value_text + '");';
    return code;
};

Blockly.JavaScript['francster_repeat_after_me'] = function (block) {
    var code = 'runPiRobotCommand("repeat");';
    return code;
};

Blockly.JavaScript['francster_ask_question'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    // TODO: Assemble JavaScript into code variable.
    var code = 'runPiRobotCommand("quest", "' + text_qstn + '");';
    return code;
};

Blockly.JavaScript['question_vocale'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    // TODO: Assemble JavaScript into code variable.
    var code = 'runPiRobotCommand("quest", "' + text_qstn + '");';
    return code;
};

Blockly.JavaScript['francaster_sleep'] = function (block) {
    var value_power = Blockly.JavaScript.valueToCode(block, 'NBR_SEC',
        Blockly.JavaScript.ORDER_ATOMIC);
    var code = 'runPiRobotCommand("setDelay", ' + value_power + ');';
    return code;

};

Blockly.JavaScript['francaster_make_n_step'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD',
        Blockly.JavaScript.ORDER_ATOMIC);

    var code = 'runPiRobotCommand("doWalk", ' + value_nb_steps + ');';
    return code;
};

Blockly.JavaScript['francster_make_n_steps_with_knee_lift'] = function (block) {
    var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD',
        Blockly.JavaScript.ORDER_ATOMIC);

    var code = 'runPiRobotCommand("doWalk_gn_cd", ' + value_nb_steps + ');';
    return code;
};

Blockly.JavaScript['francaster_say_hi'] = function (block) {
    var value_nb_hi = Blockly.JavaScript.valueToCode(block, 'NBR_HI',
        Blockly.JavaScript.ORDER_ATOMIC);

    var code = 'runPiRobotCommand("doHi", ' + value_nb_hi + ');';
    return code;
};

Blockly.JavaScript['francster_say_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    if (dropdown_motor == "o") {
        var code = 'runPiRobotCommand("do_yes");';
    }
    if (dropdown_motor == "n") {
        var code = 'runPiRobotCommand("do_no");';
    }
    return code;
};

Blockly.JavaScript['francster_reset_position'] = function (block) {
    var code = 'runPiRobotCommand("do_init");';
    return code;
};
//*********************************************************