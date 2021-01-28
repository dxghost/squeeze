from __future__ import annotations
from abc import ABC, abstractmethod



class EnergyFactory(ABC):
    # compute is an interface each energy function class should implement
    @abstractmethod
    def compute(self,rgb_matrix) -> list:
        pass


    
