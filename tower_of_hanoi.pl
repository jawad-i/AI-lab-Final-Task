% Move a single disk
move_hanoi(1, From, To, _) :-
    write('Shift disk 1 from '), write(From),
    write(' to '), write(To), nl.

% Move N disks
move_hanoi(N, From, To, Aux) :-
    N > 1,
    K is N - 1,
    move_hanoi(K, From, Aux, To),
    write('Shift disk '), write(N),
    write(' from '), write(From),
    write(' to '), write(To), nl,
    move_hanoi(K, Aux, To, From).
