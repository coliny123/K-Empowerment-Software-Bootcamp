package pokemons;

public class Diaruga extends Pokemon{
    private  String name = "디아루가";
    public Diaruga(String owner, String skills){
        super(owner,skills);
        System.out.println(this.name);
    }

    @Override
    public void attack(int idx){
        System.out.printf("%s의 포켓몬 %s가 %s 공격 시전!\n", getOwner(), name,this.getSkills().get(idx));
    }
}
