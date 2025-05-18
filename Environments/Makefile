SHELL := /bin/bash

.PHONY: cpp-lc
cpp-lc:
	g++ leetcode.cpp -std=c++23 -o leetcode && ./leetcode && rm leetcode

.PHONY: cpp-boj
cpp-boj:
	g++ boj.cpp -std=c++23 -o boj && ./boj && rm boj

.PHONY: go-boj
go-boj:
	go run boj.go

.PHONY: java-boj
java-boj:
	java boj.java
