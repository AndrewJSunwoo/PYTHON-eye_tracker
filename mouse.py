from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position
mouse.position = (1500, 200)
mouse.move(20, 12)
mouse.click(Button.right, 1)

