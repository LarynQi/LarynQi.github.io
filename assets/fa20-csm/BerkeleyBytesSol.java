// To test your code, run `javac BerkeleyBytesSol.java && java BerkeleyBytesSol`

public class BerkeleyBytesSol {
    private static int maxAge = 149;
    public static int[] histogram(int[] ages) {
        int[] ageCounts = new int[maxAge + 1];
        for (int age : ages) {
            ageCounts[age] += 1;
        }
        return ageCounts;
    }
    public static int[] ageSort(int[] ages) {
        int[] ageCounts = histogram(ages);
        int curr = 0;
        for (int i = 0; i < ageCounts.length; i += 1) {
            for (int start = curr; curr < start + ageCounts[i]; curr += 1) {
                ages[curr] = i;
            }
        }
        return ages;
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