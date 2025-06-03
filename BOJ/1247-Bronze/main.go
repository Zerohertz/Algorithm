package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func solution(reader *bufio.Reader, writer *bufio.Writer) {
	var N, tmp, res, ovf int
	res = 0
	ovf = 0
	fmt.Fscanln(reader, &N)
	for i := 0; i < N; i++ {
		fmt.Fscanln(reader, &tmp)
		if res > 0 && tmp > 0 && tmp > math.MaxInt-res {
			ovf += 1
		} else if res < 0 && tmp < 0 && tmp < math.MinInt-res {
			ovf -= 1
		}
		res += tmp
	}
	if ovf < 0 {
		fmt.Fprintln(writer, "-")
	} else if ovf > 0 {
		fmt.Fprintln(writer, "+")
	} else if res == 0 {
		fmt.Fprintln(writer, "0")
	} else if res > 0 {
		fmt.Fprintln(writer, "+")
	} else if res < 0 {
		fmt.Fprintln(writer, "-")
	}
}

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	solution(reader, writer)
	solution(reader, writer)
	solution(reader, writer)
}
