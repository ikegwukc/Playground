extends Panel

func _on_Button_pressed():
    get_node("Label").text = "HELLO!"

func _ready():
    get_node("Button").connect("pressed", self, "_on_Button_pressed")