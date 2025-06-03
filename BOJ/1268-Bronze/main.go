package main

import (
	"fmt"
)

func main() {
	var N, idx, M, tmp int
	fmt.Scan(&N)
	student := make([][5]int, N)
	for i := 0; i < N; i++ {
		for j := 0; j < 5; j++ {
			fmt.Scan(&student[i][j])
		}
	}
	res := make([][]int, N)
	for i := 0; i < N; i++ {
		row := make([]int, N)
		res[i] = row
	}
	for j := 0; j < 5; j++ {
		for i := 0; i < N-1; i++ {
			for k := i + 1; k < N; k++ {
				if student[i][j] == student[k][j] {
					res[i][k] = 1
					res[k][i] = 1
				}
			}
		}
	}
	idx = 1
	for i := 0; i < N; i++ {
		tmp = 0
		for j := 0; j < N; j++ {
			if res[i][j] == 1 {
				tmp += 1
			}
		}
		if M < tmp {
			M = tmp
			idx = i + 1
		}
	}
	fmt.Print(idx)
}
