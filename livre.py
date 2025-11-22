from dataclasses import dataclass, field, asdict
import json

@dataclass(frozen=True, slots=True, order=True)
class Livre:
    sort_index: float = field(init=False, repr=False, compare=True)
    
    titre: str
    auteur: str
    annee: int
    prix: float

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.prix)

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit: float):
        return Livre(self.titre, self.auteur, self.annee, prix_reduit)

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Livre(**data)


livre = Livre("1984", "George Orwell", 1949, 9.90)
print(livre.to_json())

livre2 = livre.promo(5.99)
print(livre2)

livres = [
    Livre("A", "X", 1990, 50),
    Livre("B", "X", 1990, 10),
    Livre("C", "X", 1990, 30)
]

print(sorted(livres))
