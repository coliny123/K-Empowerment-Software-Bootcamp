package Game;

import Game.Axe;
import Game.Barbarian;
import Game.Bow;
import Game.Sorceress;

public class Main {
    public static void main(String[] args) {

        Barbarian b1 = new Barbarian();
       Sorceress s1 = new Sorceress();
       Bow windForce = new Bow();
       Axe berserkerAxe = new Axe();
       b1.setWeapon(berserkerAxe);
       s1.setWeapon(windForce);
       s1.performWeapon();
       b1.performWeapon();
       s1.setWeapon(new Axe());
       s1.performWeapon();
       s1.info();
       b1.setWeapon(()-> System.out.println("신오브로 아이스볼을 발사"));  // WeaponBehavior이 input도 없고 return도 없어서 람다로 일회용 코드 작성
       b1.performWeapon();
    }
}