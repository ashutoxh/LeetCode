class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        if(n==1)
            return true;
        for(int i=0, j=n-1; i<n && j>=0;){
            if(!isAlphanumeric(s.charAt(i))){
                i++;
                continue;
            }
            if(!isAlphanumeric(s.charAt(j))){
                j--;
                continue;
            }
            if(Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j)))
                return false;
            i++;
            j--;
        }
        return true;
    }

    private static boolean isAlphanumeric(char code){
        if (!(code > 47 && code < 58) && // numeric (0-9)
                !(code > 64 && code < 91) && // upper alpha (A-Z)
                !(code > 96 && code < 123)) { // lower alpha (a-z)
                    return false;
        }
        return true;
    }
}