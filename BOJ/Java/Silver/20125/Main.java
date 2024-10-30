import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    static char BODY = '*';
    static char GROUND = '_';

    private static boolean findHeart(char[][] map, int i, int j) {
        return map[i][j] == BODY
                && map[i - 1][j] == BODY
                && map[i + 1][j] == BODY
                && map[i][j - 1] == BODY
                && map[i][j + 1] == BODY;
    }

    private static int[] findHeart(char[][] map, int N) {
        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < N - 1; j++) {
                if (findHeart(map, i, j)) {
                    return new int[] { i, j };
                }
            }
        }
        return null;
    }

    private static int length(char[][] map, int N, int tx, int ty, int dx, int dy) {
        int cnt = -1;
        while (0 <= tx && tx < N && 0 <= ty && ty < N) {
            if (map[ty][tx] == GROUND) {
                break;
            }
            cnt += 1;
            tx += dx;
            ty += dy;
        }
        return cnt;
    }

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.valueOf(br.readLine());
        char[][] map = new char[N][N];
        for (int i = 0; i < N; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < N; j++) {
                map[i][j] = tmp.charAt(j);
            }
        }
        int[] heartAxis = findHeart(map, N);
        bw.write(String.format("%s %s", heartAxis[0] + 1, heartAxis[1] + 1));
        bw.newLine();
        int center = length(map, N, heartAxis[1], heartAxis[0], 0, 1);
        bw.write(String.format("%s %s %s %s %s",
                length(map, N, heartAxis[1], heartAxis[0], -1, 0),
                length(map, N, heartAxis[1], heartAxis[0], 1, 0),
                center,
                length(map, N, heartAxis[1] - 1, heartAxis[0] + center + 1, 0, 1) + 1,
                length(map, N, heartAxis[1] + 1, heartAxis[0] + center + 1, 0, 1) + 1));

        bw.flush();

        br.close();
        bw.close();
    }
}
