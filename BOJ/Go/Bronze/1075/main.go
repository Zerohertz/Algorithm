package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N, F, tmp int
	var S string
	fmt.Scan(&N, &F)
	S = strconv.Itoa(N)
	S = S[:len(S)-2] + "00"
	tmp, _ = strconv.Atoi(S)
	for true {
		if tmp%F == 0 {
			break
		}
		tmp += 1
	}
	S = strconv.Itoa(tmp)
	fmt.Print(S[len(S)-2:])
}
