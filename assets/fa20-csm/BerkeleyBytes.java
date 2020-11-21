// To test your code, run `javac BerkeleyBytes.java && java BerkeleyBytes`
public class BerkeleyBytes {
    private static int maxAge = 149;
    public static int[] histogram(int[] ages) {
        int[] ageCounts = new int[maxAge + 1];
        for (int age : ages) {
            ageCounts[age] += 1;
        }
        return ageCounts;
    }
    public static int[] ageSort(int[] ages) {
        // YOUR CODE HERE
    }

    public static void main(String[] args) {
        int[] arr = {15, 3, 140, 5, 17, 34, 2, 4, 1, 20, 33, 33, 77, 44, 121};
        System.out.print("Input: ");
        for (int age : arr) {
            System.out.print(((Integer) age).toString() + " ");
        }
        System.out.println();
        ageSort(arr);
        System.out.print("Output: ");
        for (int age : arr) {
            System.out.print(((Integer) age).toString() + " ");
        }
        System.out.println();
    }
}