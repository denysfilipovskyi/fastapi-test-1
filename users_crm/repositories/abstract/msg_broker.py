from abc import ABC, abstractmethod


class AbstractMsgBrokerRepository(ABC):
    @abstractmethod
    async def connect():
        raise NotImplementedError

    @abstractmethod
    async def close():
        raise NotImplementedError

    @abstractmethod
    async def send_message():
        raise NotImplementedError

    @abstractmethod
    async def consume_messages():
        raise NotImplementedError
