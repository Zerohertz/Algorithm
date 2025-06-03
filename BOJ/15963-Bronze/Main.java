import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.valueOf(st.nextToken());
        long M = Long.valueOf(st.nextToken());

        if (N == M) {
            bw.write("1");
        } else {
            bw.write("0");
        }
        bw.flush();

        br.close();
        bw.close();
    }
}
