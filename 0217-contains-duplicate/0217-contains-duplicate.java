class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> visited = new HashSet<>();
        for(int i : nums){
            if(visited.contains(i))
                return true;
            else
                visited.add(i);
        }
        return false;
    }
}