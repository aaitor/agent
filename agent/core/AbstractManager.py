import abc


class AbstractManager(metaclass=abc.ABCMeta):
    """Abstract class in charge of provide the common functions of the different Managers"""

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """
