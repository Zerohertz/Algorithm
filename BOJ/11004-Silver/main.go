package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N, K int
	fmt.Fscan(reader, &N, &K)
	l := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &l[i])
	}
	sort.Slice(l, func(i, j int) bool {
		return l[i] < l[j]
	})
	fmt.Fprint(writer, l[K-1])
}
