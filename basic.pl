% Facts
parent(rahim, karim).
parent(karim, hasan).
parent(rahim, salma).
parent(salma, nusrat).

% Rule to define grandparent relationship
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Rule to define sibling relationship
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Queries (examples to run)
% ?- grandparent(rahim, Who).
% ?- sibling(karim, Who).
