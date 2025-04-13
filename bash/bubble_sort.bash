#!/bin/env bash

swap() {
    local arr_name="$1"
    local index1="$2"
    local index2="$3"

    local temp="${!arr_name[$index1]}"
    eval "${arr_name}[$index1]=\"${!arr_name[$index2]}\""
    eval "${arr_name}[$index2]=\"$temp\""
}



mylist=("a" "b")

printf "%s\n" "${mylist[@]}"

swap mylist 0 1

printf "%s\n" "${mylist[@]}"


