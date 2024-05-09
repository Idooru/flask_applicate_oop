from abc import *

from flask import Flask


class ControllerInterface(metaclass=ABCMeta):

    @abstractmethod
    def route(self, app: Flask):
        pass
