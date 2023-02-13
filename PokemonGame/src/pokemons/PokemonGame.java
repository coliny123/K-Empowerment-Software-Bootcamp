package pokemons;

import java.util.Scanner;

public class PokemonGame {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int menu = 0, pokemon_menu = 0, attack_menu = 0;
        String owner = null, skills = null;
        Pokemon p;

        while(true){
            System.out.printf("%d 마리의 포켓몬이 생성되었습니다. \n", Pokemon.count);
            System.out.print("1) 포켓몬 생성 2) 프로그램 종료 : ");
            menu = sc.nextInt();

            if(menu == 2){
                System.out.println("프로그램을 종료합니다.");
                break;
            }
            else if(menu == 1){
                System.out.print("1) 기라티나 2) 펄기아 3) 디아루가 : ");
                pokemon_menu = sc.nextInt();
                sc.nextLine();
                System.out.print("플레이어 이름 입력 : ");
                owner = sc.nextLine();
                System.out.print("사용 가능한 기술 입력(/로 구분하여 입력) : ");
                skills = sc.nextLine();
                if(pokemon_menu == 1){
                    p = new Giratina(owner, skills);
                }
                else if (pokemon_menu == 2) {
                    p = new Pulgia(owner, skills);
                }
                else if (pokemon_menu == 3) {
                    p = new Diaruga(owner, skills);
                }
                else{
                    System.out.println("메뉴에서 골라 주세요");
                    continue;
                }
                p.info();
                System.out.print("공격 번호 선택 : ");
                attack_menu = sc.nextInt();
                p.attack(attack_menu -1);
            }
            else {
                System.out.println("메뉴에서 골라 주세요");
            }
        }
    }
}