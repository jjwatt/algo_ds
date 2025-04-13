#!/usr/bin/env bash

quicksort() {
    local arr=("${@}")
    local len="${#arr[@]}"

    if [[ $len -le 1 ]]; then
	printf "%s " "${arr[@]}"
	return
    fi

    local pivot="${arr[0]}"
    local less=()
    local equal=()
    local greater=()

    for element in "${arr[@]}"; do
	if [[ $element -lt $pivot ]]; then
	    less+=("$element")
	elif [[ $element -eq $pivot ]]; then
	    equal+=("$element")
	else
	    greater+=("$element")
	fi
    done

    # Combine results recursively
    quicksort "${less[@]}"
    printf "%s " "${equal[@]}"
    quicksort "${greater[@]}"
}

main() {
    local mylist=(6 8 9 5 3 2 1 4 7)
    printf "Unsorted: %s\n" "${mylist[*]}"
    sorted=$(quicksort "${mylist[@]}")
    printf "Sorted: %s\n" "${sorted[*]}"
}

main "$@"
