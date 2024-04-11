
% Modified Listing 7.3: Planning in the blocks world
% For a planning problem in the blocks world, find solutions
% of a given length.

% input : set block/1 of blocks; set init/1 of atoms
% representing the initial state; set goal/1 of atoms
% representing the goal; length h of solutions.

block(1..b).

% choice of actions
action(move(B1, B2)) :- block(B1), block(B2), B1 != B2.
action(move(B, table)) :- block(B).
action(wait).

1 { occurs(A, T) : action(A) } m :- T = 0..h-1.
:- occurs(move(_, B), T), occurs(move(B, _), T).
A = wait :- occurs(wait,T), occurs(A,T).
        
% effects of actions
holds(loc(B, L), T+1) :- occurs(move(B, L), T).

% two blocks can’t be located on top of the same block
B1 = B2 :- holds(loc(B1, B), T), holds(loc(B2, B), T), block(B).

% a block can’t be moved unless it is clear
:- occurs(move(B, L), T), holds(loc(_, B), T).

% a block can’t be moved to its current location
:- occurs(move(B, L), T), holds(loc(B, L), T).

% existence and uniqueness of value
:- #count{ L : holds(loc(B, L), T) } != 1, block(B), T = 0..h.

% inertia
{ holds(loc(B, L), T+1) } :- holds(loc(B, L), T), T = 0..h-1.

% relationship between holds/2, init/1, and goal/1.
holds(C, 0) :- init(C).
:- not holds(C, h), goal(C).

#maximize{T : occurs(wait,T)}.
    
#show occurs/2.
