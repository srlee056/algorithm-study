import sys

n, m = map(int, sys.stdin.readline().split())

pokemons = []
for _ in range(n):
    pokemon = sys.stdin.readline().rstrip()
    pokemons.append(pokemon)

pokemons_dict = {}

for i, pokemon in enumerate(pokemons):
    pokemons_dict[pokemon] = str(i + 1)


for _ in range(m):
    question = sys.stdin.readline().rstrip()

    if question.isdigit():
        print(pokemons[int(question) - 1])
    else:
        print(pokemons_dict[question])
