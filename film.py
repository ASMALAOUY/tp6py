from dataclasses import dataclass, field, asdict
import json


@dataclass(frozen=True, slots=True, order=True)
class Film:

    sort_index: float = field(init=False, repr=False, compare=True)

    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        
        if not (0 <= self.note <= 10):
            raise ValueError("La note doit être entre 0 et 10.")

        object.__setattr__(self, "sort_index", self.note)

    
    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Film(**data)
