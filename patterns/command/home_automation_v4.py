from abc import ABC, abstractmethod


# ---------------- Command ----------------

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# ---------------- Invoker ----------------

class Controller:

    def __init__(self):
        self.commands = {}
        self.history = []

    def set_command(self, button, command):
        self.commands[button] = command

    def press(self, button):

        if button not in self.commands:
            print("No command assigned.")
            return

        command = self.commands[button]

        command.execute()

        self.history.append(command)

    def undo(self):

        if not self.history:
            print("Nothing to undo.")
            return

        command = self.history.pop()

        command.undo()


# ---------------- Receiver ----------------

class LightBulb:

    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True
        print("Light ON")

    def off(self):
        self.is_on = False
        print("Light OFF")


# ---------------- Concrete Commands ----------------

class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# ---------------- Receiver ----------------

class Fan:

    def __init__(self):
        self.speed = 1
        self.max_speed = 5

    def increase_speed(self):

        if self.speed < self.max_speed:
            self.speed += 1

        print(f"Fan Speed : {self.speed}")

    def decrease_speed(self):

        if self.speed > 1:
            self.speed -= 1

        print(f"Fan Speed : {self.speed}")


# ---------------- Concrete Commands ----------------

class FanIncreaseSpeedCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.increase_speed()

    def undo(self):
        self.fan.decrease_speed()


class FanDecreaseSpeedCommand(Command):

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.decrease_speed()

    def undo(self):
        self.fan.increase_speed()


# ---------------- Client ----------------

if __name__ == "__main__":

    light = LightBulb()
    fan = Fan()

    controller = Controller()

    controller.set_command("LIGHT_ON", LightOnCommand(light))
    controller.set_command("LIGHT_OFF", LightOffCommand(light))

    controller.set_command("FAN_UP", FanIncreaseSpeedCommand(fan))
    controller.set_command("FAN_DOWN", FanDecreaseSpeedCommand(fan))

    controller.press("LIGHT_ON")
    controller.press("FAN_UP")
    controller.press("FAN_UP")

    print("\nUndo Operations")

    controller.undo()
    controller.undo()
    controller.undo()