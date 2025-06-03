import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        /*
         * 1. 강의실 좌표를 list 형태로 입력 받고 좌표를 오름차순으로 정렬 -> axis
         * 2. 정렬된 list에 대해 각각의 거리 차이 list 산출 (heap 사용) -> diff
         * 3. 가장 큰 거리 차이는 텔레포트 사용
         */

        st = new StringTokenizer(br.readLine());
        int[] axis = new int[N + 1];
        axis[0] = 0;
        for (int i = 1; i < N + 1; i++) {
            axis[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(axis);

        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            heap.add(-(axis[i + 1] - axis[i]));
        }

        int cnt = 0;
        for (int i = 0; i < K; i++) {
            heap.poll();
        }
        while (0 < heap.size()) {
            cnt -= heap.poll();
        }
        bw.write(String.valueOf(cnt));

        bw.flush();

        br.close();
        bw.close();
    }
}
