from abc import ABC, abstractmethod
from typing import Dict, Type, List


class Command(ABC):

    @abstractmethod
    def press(self):
        pass



class Controller:
    def __init__(self):
        self.commands:List[Command]=[]

    
    def set_command(self,ind:int,command:Command):
        if ind>=len(self.commands):
            self.commands.append(command)
            return 
        
        self.commands[ind]=command

    
    def press(self,ind:int):
        if ind>=len(self.commands):
            return
        
        self.commands[ind].press()

        

class LightBulb:

    def on(self):
        print("light on")

    def off(self):
        print("light off")


class LightCommand(Command):
    def __init__(self,lightbulb:LightBulb):
        self.lightbulb:LightBulb=lightbulb
        self.state=0
        

    def press(self):
        if self.state:
            self.lightbulb.off()
            self.state=0
        
        else:
            self.lightbulb.on()
            self.state=1


class Fan:

    def rotate_clockwise(self):
        print("Fan speed increased")

    def rotate_anticlockwise(self):
        print("Fan speed decreased")


class FanCommand(Command):
    def __init__(self,fan:Fan):
        self.fan:Fan=fan
        self.max_speed=6
        self.current_speed=1

    def press(self):
        if self.current_speed<self.max_speed:
            self.fan.rotate_clockwise()
            self.current_speed+=1
        
        else:
            self.fan.rotate_anticlockwise()
            self.current_speed=1


if __name__ == "__main__":
    lightbulb=LightBulb()
    fan=Fan()
    lightcommand=LightCommand(lightbulb)
    fancommand=FanCommand(fan)

    controller=Controller()
    controller.set_command(0,lightcommand)
    controller.set_command(1,fancommand)

    controller.press(1)
    controller.press(1)
    controller.press(1)
    controller.press(1)
    controller.press(1)
    controller.press(1)
    controller.press(1)







