package main

import (
	"fmt"
	"sort"
)

type TeamName struct {
	name  string
	score int
}

func score(yondu string, name string, sl []int) int {
	var res int
	res = 1
	sl2 := make([]int, len(sl))
	for i := 0; i < len(sl); i++ {
		sl2[i] = sl[i]
	}
	for i := 0; i < len(name); i++ {
		for j := 0; j < len(yondu); j++ {
			if name[i:i+1] == yondu[j:j+1] {
				sl2[j] += 1
			}
		}
	}
	for i := 0; i < len(yondu)-1; i++ {
		for j := i + 1; j < len(yondu); j++ {
			res *= sl2[i] + sl2[j]
		}
	}
	res %= 100
	return res
}

func main() {
	const asdf string = "LOVE"
	var YONDU string
	var N int
	fmt.Scan(&YONDU)
	fmt.Scan(&N)
	TN := make([]TeamName, N)
	sl := make([]int, len(asdf))
	for i := 0; i < len(asdf); i++ {
		for j := 0; j < len(YONDU); j++ {
			if asdf[i:i+1] == YONDU[j:j+1] {
				sl[i] += 1
			}
		}
	}
	for i := 0; i < N; i++ {
		fmt.Scan(&TN[i].name)
		TN[i].score = score(asdf, TN[i].name, sl)
	}
	sort.Slice(TN, func(i, j int) bool {
		if TN[i].score == TN[j].score {
			return TN[i].name < TN[j].name
		} else {
			return TN[i].score > TN[j].score
		}
	})
	fmt.Print(TN[0].name)
}
