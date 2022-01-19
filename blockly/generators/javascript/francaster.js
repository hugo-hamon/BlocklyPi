Blockly.JavaScript['robot_motor_power'] = function(block) {
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

Blockly.JavaScript['control_key_down'] = function(block) {
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
	var callbackCode = 'var code = keyCode; if (charCode && code == 0) {code = charCode;}; if (code ==='+keyCode+') {'+statements_statements+'}';
	callbackCode = callbackCode.replace(/\n/g,"\\n");
	callbackCode = callbackCode.replace(/["]+/g,"\\\"");
	
	// Assemble JavaScript into code variable.
	var code = 'window.addKeyEventListenerForBlock("'+block.id+'", "'+type+'", "'+callbackCode+'");';
	return code;
};

Blockly.JavaScript['motor_move'] = function(block) {
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
    if(move == 're'){
    	value_power = value_power * -1;
    }
    if (dropdown_motor == 1) {
        alert("l'angle est " + value_power + " voila!");
        return '';
    }

	var code = 'runPiRobotCommand("setRobotMotorPower2", "' + dropdown_motor + '",' + value_power + ');';
	return code;
};

Blockly.JavaScript['dire'] = function(block) {
  var value_text = block.getFieldValue('TEXT');
  var code = 'runPiRobotCommand("speak", "' + value_text + '");';
  return code;
};

Blockly.JavaScript['repete'] = function(block) {
  var code = 'runPiRobotCommand("repeat");';
  return code;
};

Blockly.JavaScript['question'] = function(block) {
  var text_qstn = block.getFieldValue('QSTN');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("quest", "' + text_qstn + '");';
  return code;
};

Blockly.JavaScript['question_vocale'] = function(block) {
  var text_qstn = block.getFieldValue('QSTN');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("quest", "' + text_qstn + '");';
  return code;
};

Blockly.JavaScript['block_drt'] = function(block) {
	var value_power = Blockly.JavaScript.valueToCode(block, 'NBR_SEC',
			Blockly.JavaScript.ORDER_ATOMIC);
	var code = 'runPiRobotCommand("setDelay", ' + value_power + ');';
	return code;

};

Blockly.JavaScript['block_move_forward'] = function(block){
	var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD',
			Blockly.JavaScript.ORDER_ATOMIC);

    var code = 'runPiRobotCommand("doWalk", ' + value_nb_steps + ');';
	return code;
};

Blockly.JavaScript['block_move_forward_gn_cd'] = function(block){
	var value_nb_steps = Blockly.JavaScript.valueToCode(block, 'NBR_PAS_FORWARD',
			Blockly.JavaScript.ORDER_ATOMIC);

    var code = 'runPiRobotCommand("doWalk_gn_cd", ' + value_nb_steps + ');';
	return code;
};

Blockly.JavaScript['block_hi'] = function(block){
	var value_nb_hi = Blockly.JavaScript.valueToCode(block, 'NBR_HI',
			Blockly.JavaScript.ORDER_ATOMIC);

    var code = 'runPiRobotCommand("doHi", ' + value_nb_hi + ');';
	return code;
};

Blockly.JavaScript['block_motor_dc'] = function(block){
	var dropdown_motor = block.getFieldValue('MOVE');
	if(dropdown_motor  == 1){
		  alert("l'angle est voila!");
        return '';
	}
	var code = 'runPiRobotCommand("motor_dc", '+1+');';
	return code;
};

Blockly.JavaScript['block_yes'] = function(block){
	var dropdown_motor = block.getFieldValue('MOVE');
	if(dropdown_motor == "o"){
    		var code = 'runPiRobotCommand("do_yes");';
	}
	if(dropdown_motor == "n"){
		var code = 'runPiRobotCommand("do_no");';
	}
	return code;
};

Blockly.JavaScript['block_init'] = function(block){
	var code = 'runPiRobotCommand("do_init");';
	return code;
};
//*********************************************************