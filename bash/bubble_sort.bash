#/usr/bin/env bash

swap() {
  local -n arr="$1"
  local index1="$2"
  local index2="$3"

  local temp="${arr[$index1]}"
  arr[$index1]="${arr[$index2]}"
  arr[$index2]="$temp"
}

bubblesort() {
  local ar=("${@}")
  declare -n arr_ref="ar"
  local len="${#ar[@]}"
  local swapped

  for ((i=0; i < len - 1; i++)); do
    swapped=0
    for ((j=0; j < len - i - 1; j++)); do
      local current="${arr_ref[$j]}"
      local next="${arr_ref[$((j + 1))]}"
      if [[ "$current" > "$next" ]]; then
        swap "arr_ref" "$j" "$((j + 1))"
        swapped=1
      fi
    done
    if ((swapped == 0)); then
      break
    fi
  done

  printf "%s " "${arr_ref[@]}"
  echo ""
}

main() {
    local mylist=(e d c b a)
    bubblesort "${mylist[@]}"
}

main "$@"
