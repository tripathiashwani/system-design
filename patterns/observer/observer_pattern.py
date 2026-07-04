from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, order):
        pass

class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Channel(Observable):
    def __init__(self):
        self.__subscribers: list[Observer] = []
        self.__latest_video: str = None

    def register_observer(self, subscriber: Observer):
        self.__subscribers.append(subscriber)

    def remove_observer(self, subscriber: Observer):
        self.__subscribers.remove(subscriber)

    def notify_observers(self):
        for observer in self.__subscribers:
            observer.update()

    def get_latest_video(self) -> str:
        return self.__latest_video

    def set_latest_video(self, video: str):
        self.__latest_video = video
        self.notify_observers()



class Subscriber(Observer):
    def __init__(self, name: str):
        self.__name = name
        self.__subscribed_channel: Channel = None

    def update(self):
        print(f"{self.__name} has been notified of a new video!")
        if self.__subscribed_channel:
            print(f"Latest video: {self.__subscribed_channel.get_latest_video()}")

    def subscribe(self, channel: Channel):
        self.__subscribed_channel = channel
        channel.register_observer(self)



if __name__ == "__main__":
    channel = Channel()

    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")

    subscriber1.subscribe(channel)
    subscriber2.subscribe(channel)

    channel.set_latest_video("Observer Pattern Explained!")