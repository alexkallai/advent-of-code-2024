package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
	"time"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func count(lst []int, number int) int {
	count := 0
	for i := 0; i < len(lst); i++ {
		if number == lst[i] {
			count += 1
		}
	}
	return count
}

func main() {
	// STARTING TIME MEASUREMENT
	start := time.Now()

	dat, err := os.ReadFile("input.txt")
	check(err)

	lines := strings.Split(string(dat), "\n")

	var left_list []int
	var right_list []int
	for _, line := range lines {
		str_numbers := strings.Split(line, "   ")
		left_no, err := strconv.Atoi(strings.TrimSpace(str_numbers[0]))
		check(err)
		right_no, err := strconv.Atoi(strings.TrimSpace(str_numbers[1]))
		check(err)
		left_list = append(left_list, left_no)
		right_list = append(right_list, right_no)

	}
	slices.Sort(left_list)
	slices.Sort(right_list)

	similarity_score := 0
	for i := 0; i < len(left_list); i++ {
		similarity_score += left_list[i] * count(right_list, left_list[i])
	}
	fmt.Println("Result:", similarity_score)

	// STOPPING TIME MEASUREMENT
	elapsed := time.Since(start)
	fmt.Println("Total time: ", elapsed)
}
