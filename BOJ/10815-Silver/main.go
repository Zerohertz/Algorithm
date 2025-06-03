package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N, M int
	fmt.Fscan(reader, &N)
	var sg map[int]bool
	sg = make(map[int]bool)
	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &M)
		sg[M] = true
	}
	fmt.Fscan(reader, &M)
	for i := 0; i < M; i++ {
		fmt.Fscan(reader, &N)
		_, flag := sg[N]
		if flag {
			fmt.Fprint(writer, "1 ")
		} else {
			fmt.Fprint(writer, "0 ")
		}
	}
}
