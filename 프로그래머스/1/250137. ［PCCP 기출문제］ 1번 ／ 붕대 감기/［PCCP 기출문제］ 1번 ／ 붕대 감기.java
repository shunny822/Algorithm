class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int t = bandage[0];
        int x = bandage[1];
        int y = bandage[2];
        int increase = 0;
        int healthMax = health;
        int attIdx = 0;
        int time = 0;
        int lastTime = attacks[attacks.length-1][0];
        
        while (time <= lastTime) {
            if (time == attacks[attIdx][0]) {
                health -= attacks[attIdx][1];
                attIdx++;
                increase = 0;
                
                if (health <= 0) {
                    return -1;
                }
            } else {
                health += x;
                increase++;

                if (increase == t) {
                    increase = 0;
                    health += y;
                }
                
                if (health > healthMax) {
                    health = healthMax;
                }
            }

            time++;
        }
        
        return health;
    }
}