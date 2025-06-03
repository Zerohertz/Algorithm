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

	var N int
	fmt.Fscanln(reader, &N)

	var f, res string
	fmt.Fscanln(reader, &f)
	res = f
	L := len(res)
	for i := 1; i < N; i++ {
		fmt.Fscanln(reader, &f)
		for j := 0; j < L; j++ {
			if res[j:j+1] != f[j:j+1] {
				res = res[:j] + "?" + res[j+1:L]
			}
		}
	}
	fmt.Fprintln(writer, res)
}
