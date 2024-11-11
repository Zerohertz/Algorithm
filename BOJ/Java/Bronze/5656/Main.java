import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static boolean calculate(long a, String operator, long b) {
        if (operator.equals(">")) {
            return a > b;
        }
        if (operator.equals(">=")) {
            return a >= b;
        }
        if (operator.equals("<")) {
            return a < b;
        }
        if (operator.equals("<=")) {
            return a <= b;
        }
        if (operator.equals("==")) {
            return a == b;
        }
        if (operator.equals("!=")) {
            return a != b;
        }
        return false;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int i = 1;
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long a = Long.valueOf(st.nextToken());
            String operator = st.nextToken();
            long b = Long.valueOf(st.nextToken());

            if (operator.equals("E")) {
                break;
            }

            bw.write(String.format("Case %s: ", i));
            if (calculate(a, operator, b)) {
                bw.write("true\n");
            } else {
                bw.write("false\n");
            }
            i++;
        }

        bw.flush();

        br.close();
        bw.close();
    }
}
