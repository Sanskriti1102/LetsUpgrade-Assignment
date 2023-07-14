public class assignment1 {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };
        int rotationCount = 2;

        rotateArray(arr, rotationCount);

        // Print the rotated array
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    public static void rotateArray(int[] arr, int rotationCount) {
        // Perform the rotation operation
        for (int i = 0; i < rotationCount; i++) {
            int lastElement = arr[arr.length - 1];

            // Shift the elements to the right
            for (int j = arr.length - 1; j > 0; j--) {
                arr[j] = arr[j - 1];
            }

            arr[0] = lastElement;
        }
    }
}
