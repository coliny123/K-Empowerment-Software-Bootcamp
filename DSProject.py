def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons)- 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가

if __name__ == "__main__":  # 메인함수 시작 표시
    pokemons = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀"]

    print(pokemons)
    insert_data(2, '야도란')  # 처음부터 6, 에 넣었으면 out of range
    print(pokemons)
    insert_data(6, '피존투')  # 처음에 야도란을 추가했기 때문에 늘어나서 가능
    print(pokemons)
