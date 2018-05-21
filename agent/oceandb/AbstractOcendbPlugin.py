from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractOceandbPlugin(metaclass=ABCMeta):
    """Abstract interface for all persistence layer plugins.

    Expects the following to be defined by the subclass:
        - :attr:`type` (as a read-only property)
        - :func:`get_status`
        - :func:`write`
        - :func:`retrieve`
    """

    @abstractproperty
    def type(self):
        """A string denoting the type of plugin (e.g. BigchainDB, Kafka, etc)."""

    @abstractmethod
    def get_status(self):
        """Get the status of the persistence layer."""

    @abstractmethod
    def write(self, entity_data):
        """Write an entity into the persistence layer."""

    @abstractmethod
    def retrieve(self, entity_id):
        """Retrieve an entity from persistence layer using the entity_id."""

