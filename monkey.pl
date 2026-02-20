% Goal state
goal(st(someone, somebox, floor, has_item)).

% Actions / Moves
move(st(Person, Box, floor, Hand),
     walk(Person, NewPos),
     st(NewPos, Box, floor, Hand)).

move(st(Person, Person, floor, Hand),
     push_box(Person, NewPos),
     st(NewPos, NewPos, floor, Hand)).

move(st(Person, Person, floor, Hand),
     climb_box,
     st(Person, Person, on_box, Hand)).

move(st(_, _, on_box, no_item),
     grab_item,
     st(_, _, on_box, has_item)).

% Solve predicate
solve(State, []) :-
    goal(State).

solve(State, [Act | Rest]) :-
    move(State, Act, NextState),
    solve(NextState, Rest).
