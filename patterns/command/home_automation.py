from abc import ABC, abstractmethod
from typing import Dict, Type, List


class Command(ABC):

    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Controller:
    def __init__(self):
        self.commands:List[Command]=[]
        self.state:List[bool]=[]

    
    def set_command(self,ind:int,command:Command):
        if ind>=len(self.commands):
            self.commands.append(command)
            self.state.append(0)
            return 
        
        self.commands[ind]=Command
        self.state[ind]=False

    
    def press(self,ind:int):
        if ind>=len(self.commands):
            return
        
        if self.state[ind]:
            self.commands[ind].undo()
            self.state[ind]=False
        
        else:
            self.commands[ind].do()
            self.state[ind]=True

        

class LightBulb:

    def on(self):
        print("light on")

    def off(self):
        print("light off")


class LightCommand(Command):
    def __init__(self,lightbulb:LightBulb):
        self.lightbulb:LightBulb=lightbulb

    def do(self):
        self.lightbulb.on()
    
    def undo(self):
        self.lightbulb.off()



class Fan:

    def on(self):
        print("Fan on")

    def off(self):
        print("Fan off")


class FanCommand(Command):
    def __init__(self,fan:Fan):
        self.fan:Fan=fan

    def do(self):
        self.fan.on()
    
    def undo(self):
        self.fan.off()


if __name__ == "__main__":
    lightbulb=LightBulb()
    fan=Fan()
    lightcommand=LightCommand(lightbulb)
    fancommand=FanCommand(fan)

    controller=Controller()
    controller.set_command(0,lightcommand)
    controller.set_command(1,fancommand)

    controller.press(0)
    controller.press(0)







