#!/bin/env bash

printitems() {
    haystack=("${@}")
    echo "Elements in haystack: "
    for item in "${haystack[@]}"; do
	echo "$item"
    done
}


insertionsort() {
    local ar=("${@}")
    len="${#ar[@]}"
    for ((j=1; j < len; j++)); do
	local key="${ar[j]}"
	local i=$((j - 1))
	while ((i >= 0 && ar[i] > key)); do
	    # Shift elements right
	    ar[$((i+1))]="${ar[$i]}"
	    ((i--))
	done
	# Insert key into new position
	ar[$((i+1))]="$key"
    done
    printf "%s\n" "${ar[*]}"
}

main() {
    local mylist=(5 4 3 2 1)
    insertionsort "${mylist[@]}"
}

main "$@"

