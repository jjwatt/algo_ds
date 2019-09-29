%% qsort:qsort(List)
%% Sort a list of items
-module(qsort).
-export([qsort/1]).

qsort([]) ->
    []; % If list is empty, return an empty list.
qsort([Pivot|Rest]) ->
    % Compose recursively a list with 'Front' for all elements that should be
    % before 'Pivot' then 'Pivot' then 'Back' for all elements that should be
    % after 'Pivot'
    qsort([Front || Front <- Rest, Front < Pivot]) ++
        [Pivot] ++
    qsort([Back || Back <- Rest, Back >= Pivot]).

