from abc import ABC, abstractmethod


class Talkative(ABC):
    @abstractmethod
    def talk(self) -> str:
        pass


class Walkable(ABC):
    @abstractmethod
    def walk(self) -> str:
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self) -> str:
        pass


class Projectable(ABC):
    @abstractmethod
    def projection(self) -> str:
        pass


class Robot:
    def __init__(
        self,
        talker: Talkative,
        walker: Walkable,
        flyer: Flyable,
        projector: Projectable
    ):
        self.talker = talker
        self.walker = walker
        self.flyer = flyer
        self.projector = projector

    def talk(self):
        return self.talker.talk()

    def walk(self):
        return self.walker.walk()

    def fly(self):
        return self.flyer.fly()

    def projection(self):
        return self.projector.projection()


class SimpleTalker(Talkative):
    def talk(self) -> str:
        return "Beep Boop"


class AdvancedTalker(Talkative):
    def talk(self) -> str:
        return "Hello, I am an advanced robot."


class SimpleWalker(Walkable):
    def walk(self) -> str:
        return "Walking on two legs."


class AdvancedWalker(Walkable):
    def walk(self) -> str:
        return "Walking with advanced balance and speed."


class SimpleFlyer(Flyable):
    def fly(self) -> str:
        return "Flying with basic capabilities."


class AdvancedFlyer(Flyable):
    def fly(self) -> str:
        return "Flying with advanced aerodynamics and speed."


class SimpleProjector(Projectable):
    def projection(self) -> str:
        return "Projecting simple images."


class AdvancedProjector(Projectable):
    def projection(self) -> str:
        return "Projecting advanced images."


class CompanionRobot(Robot):
    pass


class WorkerRobot(Robot):
    pass


if __name__ == "__main__":
    robot1 = CompanionRobot(
        SimpleTalker(),
        SimpleWalker(),
        SimpleFlyer(),
        SimpleProjector()
    )

    robot2 = WorkerRobot(
        AdvancedTalker(),
        AdvancedWalker(),
        AdvancedFlyer(),
        AdvancedProjector()
    )

    print(robot1.talk())
    print(robot1.walk())
    print(robot1.fly())
    print(robot1.projection())

    print(robot2.talk())
    print(robot2.walk())
    print(robot2.fly())
    print(robot2.projection())