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
        

    
    def set_command(self,ind:int,command:Command):
        if ind>=len(self.commands):
            self.commands.append(command)
            return 
        
        self.commands[ind]=Command
        

    
    def do(self,ind:int):
        if ind>=len(self.commands):
            return
        
        self.commands[ind].do()

    
    def undo(self,ind:int):
        if ind>=len(self.commands):
            return
        
        self.commands[ind].undo()
        
        

        

class LightBulb:

    def on(self):
        print("light on")

    def off(self):
        print("light off")


class LightCommand(Command):
    def __init__(self,lightbulb:LightBulb):
        self.lightbulb:LightBulb=lightbulb
        self.stack=[]
        self.current_state="on"

    def do(self):
        self.stack.append(self.current_state)
        if self.current_state=="on":
            self.lightbulb.off()
            self.current_state="off"

        else:
            self.lightbulb.on()
            self.current_state="on"

    
    def undo(self):
        if len(self.stack)==0:
            print(self.current_state)
            return 


        self.last_state=self.stack.pop()
        if self.last_state=="on":
            self.lightbulb.on()
            self.current_state="on"
            
        else:
            self.lightbulb.off()
            self.current_state="off"


    



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

    controller.do(0)
    controller.do(0)
    controller.do(0)
    controller.undo(0)
    controller.undo(0)
    controller.undo(0)







