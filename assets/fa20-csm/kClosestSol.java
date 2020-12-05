import java.util.*;

// To test your code, run
// `javac kClosestSol.java && java kClosestSol`

class kClosestSol {

    public static int[][] kClosest(int[][] points, int K) {
        int N = points.length;
        int[] dists = new int[N];
        for (int i = 0; i < N; ++i)
            dists[i] = dist(points[i]);
        Arrays.sort(dists);
        int distK = dists[K-1];
        int[][] ans = new int[K][2];
        int t = 0;
        for (int i = 0; i < N; ++i)
            if (dist(points[i]) <= distK)
                ans[t++] = points[i];
        return ans;
    }

    public static int dist(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
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