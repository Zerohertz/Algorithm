package main

import (
	"fmt"
	"strings"
)

func main() {
	var N, M, r1, r2 int
	r1, r2 = 0, 0
	fmt.Scan(&N, &M)
	castle := make([]string, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&castle[i])
		if strings.Repeat(".", M) == castle[i] {
			r1 += 1
		}
	}
	var flag bool
	for j := 0; j < M; j++ {
		flag = true
		for i := 0; i < N; i++ {
			if castle[i][j:j+1] == "X" {
				flag = false
				break
			}
		}
		if flag {
			r2 += 1
		}
	}
	if r1 > r2 {
		fmt.Print(r1)
	} else {
		fmt.Print(r2)
	}
}
