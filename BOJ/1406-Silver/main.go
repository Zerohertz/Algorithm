package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	var sc = bufio.NewScanner(os.Stdin)
	var wr = bufio.NewWriter(os.Stdout)
	defer wr.Flush()
	var lt, rt []rune
	sc.Buffer(make([]byte, 100100), 100100)
	sc.Scan()
	lt = []rune(sc.Text())

	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())

	for i := 0; i < n; i++ {
		sc.Scan()
		command := sc.Text()
		switch command {
		case "L":
			if len(lt) > 0 {
				rt = append(rt, lt[len(lt)-1])
				lt = lt[:len(lt)-1]
			}
		case "D":
			if len(rt) > 0 {
				lt = append(lt, rt[len(rt)-1])
				rt = rt[:len(rt)-1]
			}
		case "B":
			if len(lt) > 0 {
				lt = lt[:len(lt)-1]
			}
		default:
			lt = append(lt, rune(command[2]))
		}
	}

	for i := len(rt) - 1; i >= 0; i-- {
		lt = append(lt, rt[i])
	}

	for _, c := range lt {
		_, _ = wr.WriteRune(c)
	}
}
