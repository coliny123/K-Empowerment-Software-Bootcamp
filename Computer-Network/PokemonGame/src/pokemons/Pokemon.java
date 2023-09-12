package pokemons;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public abstract class Pokemon{
    private String owner;
    private List<String> skills;  // 이걸 따라 가니까 14줄처럼 ArrayList 에서는 생략가능
    public static int count = 0;
    public Pokemon(String owner, String skiils) {
        this.owner = owner;
        StringTokenizer st = new StringTokenizer(skiils, "/");
        this.skills = new ArrayList<String>();  // ArrayList 에서 상위 class List로 변경한 것 <String>은 <>로 생략 가능
        while (st.hasMoreTokens()) {
            this.skills.add(st.nextToken());
        }
        System.out.print("포켓몬 생성 : ");
        Pokemon.count += 1;
    }
    public void info(){
        int idx = 0;
        System.out.printf("%s의 포켓몬이 사용 가능한 스킬\n", owner);
        for(String skill : skills){  // skills가 리스트니까 for each 구문 사용
            //  == System.out.printf("%d : %s\n", ++idx, this.skills.get(idx));
            System.out.println(++idx + " : " + skill);
        }
    }

    public void attack(int idx){
        System.out.printf("%s 공격 시전!\n", this.skills.get(idx));
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public List<String> getSkills() {
        return skills;
    }

    public void setSkills(List<String> skills) {
        this.skills = skills;
    }
}