package main

import "fmt"

func main() {
	var T, x, y, res int
	fmt.Scan(&T)
	var dhj [][]int
	for i := 0; i < 100; i++ {
		dhj = append(dhj, make([]int, 100))
	}
	for i := 0; i < T; i++ {
		fmt.Scan(&x, &y)
		for tx := x; tx < x+10; tx++ {
			for ty := y; ty < y+10; ty++ {
				dhj[tx][ty] = 1
			}
		}
	}
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			res += dhj[i][j]
		}
	}
	fmt.Print(res)
}
