public class IntArrayIterator implements IntIterator {
    private int index;
    private int[] array;

    public IntArrayIterator(int[] arr) {
        array = arr;
        // following line is optional
        index = 0;
    }

    public boolean hasNext() {
        return index < array.length;
    }

    public int next() {
        int value = array[index];
        index += 1;
        return value;
        // return array[index++];
    }
    public static void main(String[] args) {
        int[] arr ={1, 2, 3, 4, 5, 6};
        IntIterator iter = new IntArrayIterator(arr);
        if (iter.hasNext()) {
            System.out.println(iter.next());
        }
        if (iter.hasNext()) {
            System.out.println(iter.next() + 3);
        }
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }
    }
}