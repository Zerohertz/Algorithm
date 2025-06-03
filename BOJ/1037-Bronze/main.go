package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)

	arr := make([]uint32, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&arr[i])
	}
	var min uint32 = arr[0]
	var max uint32 = arr[0]
	for i := 1; i < N; i++ {
		if min > arr[i] {
			min = arr[i]
		}
		if max < arr[i] {
			max = arr[i]
		}
	}
	fmt.Print(min * max)
}
