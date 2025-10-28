parent(dad1, son1).
parent(dad1, son2).
parent(mom1, daughter1).
parent(dad2, son3).

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
