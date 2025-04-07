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
	key="${ar[j]}"
	((i=j-1))
	while ((i >= 0 && ar[i] > key)); do
	    echo "$i"
	    ((i=i-1))
	done
    done
}

main() {
    mylist=(5 4 3 2 1)
    insertionsort "${mylist[@]}"
}

main "$@"

