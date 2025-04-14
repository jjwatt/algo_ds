#!/usr/bin/env bash

quicksort() {
    local arr=("${@}")
    local len="${#arr[@]}"
    local output=

    [[ $len -le 1 ]] && echo -n "${arr[@]}" && return

    local pivot="${arr[0]}"
    local less=()
    local equal=()
    local greater=()

    for element in "${arr[@]}"; do
	[[ $element -lt $pivot ]] && less+=("$element")
	[[ $element -eq $pivot ]] && equal+=("$element")
	[[ $element -gt $pivot ]] && greater+=("$element")
    done
    local less_sorted
    local greater_sorted
    less_sorted=$(quicksort "${less[@]}")
    greater_sorted=$(quicksort "${greater[@]}")
    [[ -n $less_sorted ]] && output+="$less_sorted "
    output+="${equal[*]}"
    [[ -n $greater_sorted ]] && output+=" $greater_sorted"
    echo -n "$output"
}

main() {
    local mylist=(6 8 9 5 3 2 1 4 7)
    printf "Unsorted: %s\n" "${mylist[*]}"
    sorted=$(quicksort "${mylist[@]}")
    printf "Sorted: %s\n" "${sorted[*]}"
}

main "$@"
