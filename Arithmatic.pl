 % Addition
add(X, Y, Z) :- Z is X + Y.

% Subtraction
subtract(X, Y, Z) :- Z is X - Y.

% Multiplication
multiply(X, Y, Z) :- Z is X * Y.

% Division
divide(X, Y, Z) :- Z is X / Y.

% Check even or odd
even(X):- 0 is X mod 2.
odd(X):- 1 is X mod 2.

% Compute the average of three numbers
average(X, Y, Z, Avg) :- Avg is (X + Y + Z) / 3.

% Queries examples
% ?- add(5, 3, Result).
% ?- multiply(6, 7, Result).
% ?- divide(20, 4, Result).
% ?- even(10).
% ?- average(4, 5, 6, Avg).
