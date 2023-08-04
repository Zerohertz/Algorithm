package main

import "fmt"

func main() {
	var N, L int
	fmt.Scan(&N, &L)

	flag := true
	for size := L; size < 101; size++ {
		M := N - size*(size-1)/2
		if M%size == 0 && M >= 0 {
			start := M / size
			for j := start; j < start+size; j++ {
				fmt.Print(j, " ")
			}
			flag = false
			break
		}
	}
	if flag {
		fmt.Print(-1)
	}
}
