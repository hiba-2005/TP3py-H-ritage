from bibliotheque import Livre, Magazine
docs = [
    Livre("1984", 1949, "George Orwell"),
    Magazine("Science & Vie", 2023, 456),
    Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
]

for d in docs:
    d.afficher()