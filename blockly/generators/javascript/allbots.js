Blockly.JavaScript['francaster_shift_motor_position'] = function (block) {
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

    var code = 'runPiRobotCommand("FrancasterController.shift_motor_position", "' + dropdown_motor + '",' + value_power + ');';
    return code;
};
