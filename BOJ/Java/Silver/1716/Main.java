import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        while (true) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int k = Integer.valueOf(st.nextToken());

            if (n == k && n == -1) {
                break;
            }

            st = new StringTokenizer(br.readLine());
            int[] coefficients = new int[n + 1];
            for (int i = 0; i < n + 1; i++) {
                coefficients[i] = Integer.valueOf(st.nextToken());
            }
            for (int i = n; i >= k; i--) {
                coefficients[i - k] -= coefficients[i];
                coefficients[i] = 0;
            }

            Deque<Integer> stack = new ArrayDeque<>();
            for (int i = n; i >= 0; i--) {
                if (coefficients[i] == 0) {
                    continue;
                }
                stack.addFirst(coefficients[i]);
            }
            if (stack.size() == 0) {
                stack.addFirst(0);
            }
            while (stack.size() > 0) {
                bw.write(String.valueOf(stack.removeFirst()));
                bw.write(" ");
            }
            bw.write("\n");
        }

        bw.flush();

        br.close();
        bw.close();
    }
}
