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
    }
}