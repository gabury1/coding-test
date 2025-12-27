import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
dict = {}

for i in range(N) :
    name = input().strip()
    no = i + 1
    dict[name] = str(no)
    dict[str(no)] = name
    

for _ in range(M) :
    p = input()
    print(f"{dict.get(p)}")

    """
    26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
    
    """