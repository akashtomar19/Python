class Subject:
    def __init__(self):
        self.observers = []
        self.scored = False

    def set_scored(self, score):
        self.scored = score
        self.notify()

    def add_observer(self, obs):
        self.observers.append(obs)

    def notify(self):
        for o in self.observers:
            o.update()

    def get_scored(self):
        return self.scored


class Observer:
    def __init__(self, sub, exc_level):
        self.subject = sub
        self.excitement_level = exc_level
        sub.add_observer(self)

    def update(self):
        pass

    def get_subject(self):
        return self.subject

    def set_excitement_level(self, exc_level):
        self.excitement_level = exc_level

    def get_excitement_level(self):
        return self.excitement_level


class YoungConcreteObserver(Observer):
    def __init__(self, sub, div):
        super().__init__(sub, div)

    def update(self):
        scored = self.get_subject().get_scored()
        self.set_excitement_level(self.get_excitement_level() + 1)

        if scored and self.get_excitement_level() > 100:
            print("Young Observer's team scored!! His excitementLevel is", self.get_excitement_level(), "don't drink and drive !!")
        else:
            print("Team didn't score. Nothing to worry")


class OldConcreteObserver(Observer):
    def __init__(self, sub, div):
        super().__init__(sub, div)

    def update(self):
        scored = self.get_subject().get_scored()
        self.set_excitement_level(self.get_excitement_level() + 1)

        if scored and self.get_excitement_level() > 150:
            print("Old Observer's team scored!! His excitementLevel is", self.get_excitement_level(), "Risk of heart attack !!")
        else:
            print("Team didn't score. Nothing to worry")


sub = Subject()
young_observer = YoungConcreteObserver(sub, 101)
old_observer = OldConcreteObserver(sub, 151)
sub.set_scored(True)
