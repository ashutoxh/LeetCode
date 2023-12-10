class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();

        if(s.isEmpty())
            return true;
        if(s.length() % 2 != 0)
            return false;
        if(s.charAt(0) == ')' || s.charAt(0) == '}' || s.charAt(0) == ']')
            return false;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                brackets.push(s.charAt(i));
            else if(s.charAt(i) == ')' && !brackets.empty() && brackets.peek() == '(')
                brackets.pop();
            else if(s.charAt(i) == '}' && !brackets.empty() && brackets.peek() == '{')
                brackets.pop();
            else if(s.charAt(i) == ']' && !brackets.empty() && brackets.peek() == '[')
                brackets.pop();
            else
                return false;

        }
        return brackets.empty();
    }
}