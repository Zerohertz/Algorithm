package main

import (
	"fmt"
)

func main() {
	var tmp string
	var age, weight int
	for true {
		fmt.Scan(&tmp)
		fmt.Scan(&age)
		fmt.Scan(&weight)
		if tmp == "#" {
			break
		} else if age > 17 || weight >= 80 {
			fmt.Println(tmp, "Senior")
		} else {
			fmt.Println(tmp, "Junior")
		}
	}
}
