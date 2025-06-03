package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N, ai, bi, tmp int
	var Ns, as, bs string
	var flag bool
	fmt.Scan(&N)
	Ns = strconv.Itoa(N)
	for i := 1; i < len(Ns); i++ {
		ai = 1
		bi = 1
		as = Ns[:i]
		bs = Ns[i:]
		for j := 0; j < len(as); j++ {
			tmp, _ = strconv.Atoi(as[j : j+1])
			ai *= tmp
		}
		for j := 0; j < len(bs); j++ {
			tmp, _ = strconv.Atoi(bs[j : j+1])
			bi *= tmp
		}
		if ai == bi {
			flag = true
			break
		}
	}
	if flag {
		fmt.Print("YES")
	} else {
		fmt.Print("NO")
	}
}
