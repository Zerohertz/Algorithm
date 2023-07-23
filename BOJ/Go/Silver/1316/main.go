package main

import "fmt"

func group(s string) (res bool) {
	tmp := map[string]bool{}
	tmp[s[0:1]] = true
	for i := 1; i < len(s); i++ {
		if s[i:i+1] != s[i-1:i] {
			if !tmp[s[i:i+1]] {
				tmp[s[i:i+1]] = true
			} else {
				return
			}
		}
	}
	res = true
	return
}

func main() {
	var N, res int
	fmt.Scan(&N)
	var S string
	for i := 0; i < N; i++ {
		fmt.Scan(&S)
		if group(S) {
			res += 1
		}
	}
	fmt.Print(res)
}
