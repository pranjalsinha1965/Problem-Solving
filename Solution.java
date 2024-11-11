/*
    Time complexity: O(N)
    Space complexity: O(1)

    Where 'N' is the input array 'A'.
*/
package TUF.Arrays;
public class Solution {
    public static int isSorted(int n, int []a) {
        // Iterating over the array 'A'.
        for (int i = 0; i < n - 1; i++) {
            if (a[i + 1] < a[i]) {
                return 0;
            }
        }
        return 1;
    }
}
