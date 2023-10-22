class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        for(char c : s.toCharArray()){
            sMap.put(c, sMap.getOrDefault(c, 0) + 1);
        }
        for(char c : t.toCharArray()){
            sMap.put(c, sMap.getOrDefault(c, 0) - 1);
        }
        System.out.println(sMap);
        for(int frequency : sMap.values()){
            if(frequency != 0)
                return false;
        }
        return true;
    }
}