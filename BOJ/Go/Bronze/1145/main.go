package main

import (
	"fmt"
)

func main() {
	var N [5]int
	var cnt, res int
	fmt.Scan(&N[0], &N[1], &N[2], &N[3], &N[4])
	res = 1
	for true {
		cnt = 0
		for i := 0; i < 5; i++ {
			if res%N[i] == 0 {
				cnt += 1
			}
		}
		if cnt >= 3 {
			break
		} else {
			res += 1
		}
	}
	fmt.Print(res)
}
