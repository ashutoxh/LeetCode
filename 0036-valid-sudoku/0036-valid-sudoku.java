class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean hasValidRows = checkRows(board);
        // System.out.println("hasValidRows " + hasValidRows);
        if(!hasValidRows)
            return false;
        boolean hasValidColumns = checkColumns(board);
        // System.out.println("hasValidColumns " + hasValidColumns);
        if(!hasValidColumns)
            return false;
        boolean hasValidGrid = checkGrid(board);
        // System.out.println("hasValidGrid " + hasValidGrid);
        if(!hasValidGrid)
            return false;
        return true;
    }

    private static boolean checkRows(char[][] board){
        for(int row=0; row<board.length; row++){
            Set<Character> unique = new HashSet<>();
            for(int col=0; col<board[0].length; col++){
                if(board[row][col] == '.')
                    continue;
                if(unique.contains(board[row][col])){
                    return false;
                } else{
                    unique.add(board[row][col]);
                }
            }
        }
        return true;
    }

    private static boolean checkColumns(char[][] board){
        for(int row=0; row<board.length; row++){
            Set<Character> unique = new HashSet<>();
            for(int col=0; col<board[0].length; col++){
                if(board[col][row] == '.')
                    continue;
                if(unique.contains(board[col][row])){
                    return false;
                } else{
                    unique.add(board[col][row]);
                }
            }
        }
        return true;
    }

    private static boolean checkGrid(char[][] board){
        for (int gridRow = 0; gridRow < 9; gridRow += 3) {
            for (int gridCol = 0; gridCol < 9; gridCol += 3) {
                Set<Character> unique = new HashSet<>();
                for (int row = gridRow; row < gridRow + 3; row++) {
                    for (int col = gridCol; col < gridCol + 3; col++) {
                        if(board[row][col] == '.')
                            continue;
                        if(unique.contains(board[row][col])){
                            return false;
                        } else{
                            unique.add(board[row][col]);
                        }
                    }
                }
                // System.out.println(unique);
            }
        }
        return true;
    }
}