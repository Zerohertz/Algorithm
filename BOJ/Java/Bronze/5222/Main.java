import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    static int START = 'A';

    private static String preprocess(String keyword, String plaintext) {
        StringBuilder result = new StringBuilder(keyword);
        for (int i = 0; i < plaintext.length() - keyword.length(); i++) {
            result.append(keyword.charAt(i % keyword.length()));
        }
        return result.toString();
    }

    private static String encrypt(String keyword, String plaintext) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < keyword.length(); i++) {
            int _keyword = keyword.charAt(i);
            int _plaintext = plaintext.charAt(i);
            int tmp = (_keyword + _plaintext - START * 2) % 26 + START;
            result.append((char) tmp);
        }
        return result.toString();
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.valueOf(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String keyword = st.nextToken();
            String plaintext = st.nextToken();
            keyword = preprocess(keyword, plaintext);
            bw.write("Ciphertext: ");
            bw.write(encrypt(keyword, plaintext));
            bw.newLine();
        }

        bw.flush();

        br.close();
        bw.close();
    }
}
