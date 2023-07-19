package main

import (
	"fmt"
)

func main() {
	var A, B, tmp, cnt int
	fmt.Scan(&A, &B)
	res := make([]int, 1001)
	tmp = 1
	cnt = 1
	for i := 1; i < 1001; i++ {
		fmt.Println(i, tmp)
		res[i] = res[i-1] + tmp
		if tmp == cnt {
			cnt = 1
			tmp += 1
		} else {
			cnt += 1
		}
	}
	fmt.Print(res[B] - res[A-1])
}
