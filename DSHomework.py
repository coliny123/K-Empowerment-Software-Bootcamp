def find_data(name, power):
    find_pos = -1
    for i in range(len(pokemons)):
        keys = list(pokemons[i].keys())
        print(pokemons[i][keys[0]])
        if power >= pokemons[i][keys[0]]:
            find_pos = i
            break

    if find_pos == -1:
        find_pos = len(pokemons)

    new_pokemon_dict = {name: power}
    insert_data(find_pos, new_pokemon_dict)


def insert_data(idx, new_pokemon_dict):
    if idx < 0 or idx > len(pokemons):
        print("범위를 벗어났습니다")
        return
    pokemons.append(None)
    len_pokemons = len(pokemons)

    for i in range(len_pokemons -1, idx, -1):
        pokemons[i] = pokemons[i-1]
        pokemons[i-1] = None

    pokemons[idx] = new_pokemon_dict

# def sort_data():
#     keys = []
#     for i in range(len(pokemons)):
#         key = list(pokemons[i].keys())
#         keys.append(key)
#     po_at = []
#     for key in keys:
#         start = 0
#         for i in range(start,len(pokemons)):
#             po_at[i] = pokemons[i][key[0]]
#             start += 1
#             break
#         for j in range(len(po_at)):
#             if po_at[j] >= po_at[j+1]:
#                 pokemons[j], pokemons[j+1] = pokemons[j+1], pokemons[j]
#
#     print(pokemons)






if __name__ == "__main__":
    pokemons = [{"피카츄":150}, {"라이츄":80}, {"파이리":50}, {"꼬북이": 15}]

    # sort_data()
    name = input("추가할 포켓몬 : ")
    power = int(input("공격력 : "))

    find_data(name, power)
    print(pokemons)


