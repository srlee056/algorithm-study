import sys

n, m = map(int, sys.stdin.readline().split())

pokemons = []
for _ in range(n):
    pokemon = sys.stdin.readline().rstrip()
    pokemons.append(pokemon)

pokemons_dict = {}

for i, pokemon in enumerate(pokemons):
    pokemons_dict[str(int(i) + 1)] = pokemon
    pokemons_dict[pokemon] = str(int(i) + 1)


for _ in range(m):
    question = sys.stdin.readline().rstrip()

    print(pokemons_dict[question])
