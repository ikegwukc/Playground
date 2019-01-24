extends Label

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

var accum = 0

func _process(delta):
	accum += delta
	text = str(accum) # built in label property
	

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass

