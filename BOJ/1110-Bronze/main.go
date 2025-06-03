package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N, org, cnt, a, b int
	var n string
	fmt.Scan(&N)
	org = N
	n = strconv.Itoa(N)
	cnt = 1
	for true {
		if len(n) == 1 {
			N, _ = strconv.Atoi(n)
			b = N
		} else {
			a, _ = strconv.Atoi(n[0:1])
			b, _ = strconv.Atoi(n[1:2])
			N = a + b
		}
		n = strconv.Itoa(N)
		if len(n) == 1 {
			n = strconv.Itoa(b) + n
		} else {
			n = strconv.Itoa(b) + n[1:2]
		}
		N, _ = strconv.Atoi(n)
		if N == org {
			break
		} else {
			cnt += 1
		}
	}
	fmt.Print(cnt)
}
