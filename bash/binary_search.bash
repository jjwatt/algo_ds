#!/usr/bin/env bash

printitems() {
    haystack=("${@}")
    echo "Elements in haystack: "
    for item in "${haystack[@]}"; do
	echo "$item"
    done
}

binsearch() {
    local needle="$1"
    shift
    local haystack=("${@}")
    local length="${#haystack[@]}"
    local high=$((length - 1))
    local low=0
    local mid
    echo "needle = $needle"
    echo "haystack = ${haystack[*]}"
    while [[ $low -le $high ]]; do 
	mid=$(( (low + high) / 2 ))
	if [[ ${haystack[$mid]} -eq $needle ]]; then
	    echo "$mid"
	    return 0
	fi
	if [[ ${haystack[$mid]} -lt $needle ]]; then
	    # Search the right side
	    low=$(( mid + 1 ))
	else
	    high=$((mid - 1))
	fi
    done
    echo ""
}

main() {
    mylist=(1 2 3 4 5)
    binsearch 4 "${mylist[@]}"
}

main "$@"
