from abc import ABC, abstractmethod


class ImageClassifierModel(ABC):
    @abstractmethod
    def predict(self, input) -> list[float]:
        raise NotImplementedError
