class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for(String word : strs){
            List<String> value = map.getOrDefault(sort(word), new ArrayList<>());
            value.add(word);
            map.put(sort(word), value);
        }
        return new ArrayList<>(map.values());
    }
    
    public String sort(String word){
        char[] arr = word.toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }
}