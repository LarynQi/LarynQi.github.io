import java.util.*;

// To test your code, run
// `javac kClosest.java && java kClosest`

class kClosest {

    public static int[][] kClosest(int[][] points, int K) {
        // YOUR CODE HERE
    }

    private static void printArr(int[][] arr) {
        System.out.print("[");
        for (int[] el : arr) {
            if (!(el.equals(arr[arr.length - 1]))) {
                System.out.print("[" + el[0] + ", " + el[1] + "], ");
            } else {
                System.out.print("[" + el[0] + ", " + el[1] + "]");
            }
        }
        System.out.println("]");
    }
    
    public static void main(String[] args) {
        int[][] test0 = {{3, 3}, {5, -1}, {-2, 4}};
        System.out.print("Input: ");
        printArr(test0);
        System.out.print("Output: ");
        printArr(kClosest(test0, 2));
    }
}