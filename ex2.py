from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float  

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Film(**data)

film1 = Film("Nope", "Jordan Peele", 2022, 8.5)
film2 = Film("The Pursuit of Happyness", "Gabriele Muccino", 2006, 19.0)

print(film1.to_json())

print(film1.est_classique())  
print(film2.est_classique())  
json_str = '{"titre": "Le Seigneur des Anneaux", "realisateur": "Peter Jackson", "annee": 2001, "note": 9.1}'
film3 = Film.from_json(json_str)
print(film3.to_json())

favoris = [film1, film2, film3]
favoris_json = json.dumps([f.to_json() for f in favoris], ensure_ascii=False)
print(favoris_json)
