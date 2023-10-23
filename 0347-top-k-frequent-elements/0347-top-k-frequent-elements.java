class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequency = new HashMap<>();
        for(int i : nums){
            int value = frequency.getOrDefault(i, 0);
            frequency.put(i, value + 1);
        }
        frequency = frequency.entrySet().stream().sorted(
                Collections.reverseOrder(Map.Entry.comparingByValue()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                        (oldValue, newValue) -> oldValue, LinkedHashMap::new));
        int[] result = new int[k];
        int count = k;
        for(Map.Entry<Integer, Integer> entry : frequency.entrySet()){
            if(count == 0){
                break;
            }
            result[k-count] = entry.getKey();
            count--;
        }
        return result;
    }
}