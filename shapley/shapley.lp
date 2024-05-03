#include "shapley.inp".

{ flight(X, Y) : init(X, Y)}.
% achieved: flight/2 is a subset of init/2. The set of all worlds is the power set of init/2.

{ primary(flight(X, Y)) : flight(X, Y) } = 1.
% achieved: primary/1 where each flight in a world is a "primary" flight in a new world.

secondary(flight(X, Y)) :- flight(X, Y), not primary(flight(X, Y)).
% achieved: secondary/1 where each non-primary flight is denoted as a secondary one.

% { value(0; 1) } = 1.

r :- secondary(flight(X, Y)), airport(X, us), airport(Y, fr).
r :- airport(X, us), airport(Z, fr), secondary(flight(X, Y)), secondary(flight(Y, Z)).

l :- flight(X, Y), airport(X, us), airport(Y, fr).
l :- airport(X, us), airport(Z, fr), flight(X, Y), flight(Y, Z).
l :- airport(X, us), airport(Z, fr), flight(X, Y), flight(Y, Z).

value(0) :- l, r.
value(0) :- not l, not r.
value(1) :- l, not r.
value(-1) :- not l, r.



%% value(0) :- secondary(flight(X, Y)), airport(X, us), airport(Y, fr).
%% value(0) :- secondary(flight(X, Y)), secondary(flight(Y, Z)), airport(X, us), airport(Z, fr).
%% % achieved: shapley value/1 of 0 if secondary flights have us->fr path <2.

%% value(0) :- primary(flight(X, Y)), not airport(X, us), airport(Y, fr).
%% value(0) :- primary(flight(X, Y)), airport(X, us), not airport(Y, fr).
%% value(0) :- primary(flight(X, Y)), secondary(flight(Y, Z)), not airport(X, us), airport(Z, fr).
%% value(0) :- secondary(flight(X, Y)), primary(flight(Y, Z)), airport(X, us), not airport(Z, fr).
%% % achieved: shapley value/1 of 0 if primary flight doesn't have us->fr path <2.

%% value(1) :- not value(0).
%% % achieved: shapley value/1 of 1 if primary makes valid path and secondary doesn't.

shapley(flight(X, Y), card(N), value(A)) :- primary(flight(X, Y)), N = #count{ U, V : flight(U, V) }, value(A). 

#show secondary/1.
#show shapley/3.
