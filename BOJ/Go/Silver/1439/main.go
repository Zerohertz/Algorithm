package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	var c0, c1 int
	for i := 1; i < len(S); i++ {
		if S[i-1:i] == "0" && S[i:i+1] == "1" {
			c0++
		} else if S[i-1:i] == "1" && S[i:i+1] == "0" {
			c1++
		}
	}
	if c0 > c1 {
		fmt.Print(c0)
	} else {
		fmt.Print(c1)
	}
}
