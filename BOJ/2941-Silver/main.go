package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	dict := []string{"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}
	fmt.Scan(&S)
	for i := 0; i < len(dict); i++ {
		S = strings.Replace(S, dict[i], "A", -1)
	}
	fmt.Println(len(S))
}
