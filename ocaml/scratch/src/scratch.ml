open Core

let rec insert lst x =
  match lst with
  |  [] -> [x]
  | y :: ys when x <= y -> x :: y :: ys
  | y :: ys -> y :: insert ys x
;;

(* let insertion_sort = List.fold_left insert [];; *)
(* Core.Std List.fold_left needs named args *)
let insertion_sort = List.fold_left ~f:insert ~init:[];;

(* bubblesort *)
let rec bubblesort s =
  let rec _bubbler = function
    | x :: x2 :: xs when x > x2 ->
      x2 :: _bubbler (x :: xs)
    | x :: x2 :: xs ->
      x :: _bubbler (x2 :: xs)
    | s -> s
  in
  let t = _bubbler s in
  if t = s then t
  else bubblesort t

