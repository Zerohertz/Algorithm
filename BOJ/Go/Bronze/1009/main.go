package main

import (
	"fmt"
)

func powInt(x, y int) int {
	var res int = 1
	for i := 0; i < y; i++ {
		res = (res * x) % 10
	}
	return res
}

// OVERFLOW...
// func powInt(x, y int64) int64 {
// 	return int64(math.Pow(float64(x), float64(y)))
// }

func main() {
	var T int
	var a, b, res int
	fmt.Scan(&T)
	for i := 0; i < T; i++ {
		fmt.Scan(&a, &b)
		res = powInt(a, b)
		if res == 0 {
			fmt.Println(10)
		} else {
			fmt.Println(res)
		}
	}
}
