package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func abs(a, b int) int{
    tmp := a - b
    if tmp > 0{
        return tmp
    }
    return -1*tmp
}

func main() {
	file, err := os.Open("./input.txt")
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	lhs := make([]int, 1000)
	rhs := make([]int, 1000)
    rval_counter := make(map[int]int)

	idx := 0
	for scanner.Scan() {
		line := scanner.Text()
		values := strings.Split(line, "   ")
		lval, lerr := strconv.Atoi(values[0])
		check(lerr)
		lhs[idx] = lval
		rval, rerr := strconv.Atoi(values[1])
        rval_counter[rval] += 1
		check(rerr)
		rhs[idx] = rval
		idx += 1
	}

	sort.Ints(lhs)
	sort.Ints(rhs)
	differnce := 0
	for i, val := range lhs {
		differnce += abs(val, rhs[i])
	}
    similarity := 0
    for _, val := range lhs {
        similarity += val * rval_counter[val]
    }
	fmt.Println("Difference : ", differnce)
    fmt.Println("Similarity : ", similarity)
}
