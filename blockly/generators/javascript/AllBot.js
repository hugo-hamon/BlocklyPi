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

Blockly.JavaScript['angle_motor'] = function(block) {
  var dropdown_motor = block.getFieldValue('motor');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'runPiRobotCommand("allbotsController.angle_motor", "' + dropdown_motor + '",' + value_angle + ');';
  return code;
};

Blockly.JavaScript['reset_position'] = function(block) {
	var code = 'runPiRobotCommand("allbotsController.reset_position");';
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
