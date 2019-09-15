import abc


class BioPlatformInitializer:

    def __init__(self):
        pass

    @abc.abstractmethod
    def init(self):
        raise NotImplementedError
