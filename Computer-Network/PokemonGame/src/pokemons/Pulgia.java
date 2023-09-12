package pokemons;

public class Pulgia extends Pokemon{
    private  String name = "디아루가";
    public Pulgia(String owner, String skills){
        super(owner,skills);
        System.out.println(this.name);
    }
    @Override
    public void attack(int idx){
        System.out.printf("%s의 포켓몬 %s가 %s 공격 시전!\n", getOwner(), name,this.getSkills().get(idx));
    }

    public void swim(){
        System.out.printf("%s 가 수영을 합니다\n", this.name);
    }
}