Blockly.Blocks['control_key_down'] = {
    init: function () {
        this.setHelpUrl('http://www.example.com/');
        this.setColour(210);
        this.appendDummyInput().appendField(new Blockly.FieldDropdown([
            ["On ↓ key", "DOWN"], ["On ↑ key", "UP"],
            ["On ← key", "LEFT"], ["On → key", "RIGHT"]]), "KEY")
            .appendField(new Blockly.FieldDropdown([["up", "UP"], ["down", "DOWN"]]), "TYPE");

        this.appendStatementInput("STATEMENTS");
        this.setTooltip('');
    }
};
