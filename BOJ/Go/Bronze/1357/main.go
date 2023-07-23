package main

import (
	"fmt"
	"strconv"
)

func Rev(tar int) int {
	var in, out string
	in = strconv.Itoa(tar)
	for i := len(in) - 1; i >= 0; i-- {
		out += in[i : i+1]
	}
	tar, _ = strconv.Atoi(out)
	return tar
}

func main() {
	var X, Y int
	fmt.Scan(&X, &Y)
	X = Rev(X)
	Y = Rev(Y)
	fmt.Print(Rev(X + Y))
}
