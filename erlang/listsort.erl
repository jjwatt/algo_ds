% This is file 'listsort.erl' (the compiler is made this way)
-module(listsort).
% Export by_length with 1 parameter (don't care about the type and name)
-export([by_length/1]).

by_length(Lists) ->
     % use 'qsort/2' and provides an anonymous fn as a param.
    qsort(Lists, fun(A,B) -> length(A) < length(B)
end).

qsort([], _) ->
    []; % If list is empty, return an empty list.
qsort([Pivot|Rest], Smaller) ->
    % Partition list with 'Smaller' elements in front of Pivot and not-'Smaller'
    % elements after 'Pivot' and sort the sublists.
    qsort([X || X <- Rest, Smaller(X,Pivot)], Smaller)
    ++ [Pivot] ++
    qsort([Y || Y <- Rest, not(Smaller(Y, Pivot))], Smaller).

