#include "shapley-2.inp".

#script(python)

from math import factorial

def shapley_expr(count, card, maximum):
    return int( 100 * round( (count.number) * ( factorial(card.number - 1) * factorial(maximum.number - card.number) / factorial(maximum.number) ) , 2) )

def floatify(n):
    return str(n.number / 100)

#end.

tmp(card(C), flight(X, Y), sum(N)) :- shapley(world(_), flight(X, Y), card(C), value(_)), N = #sum{ V, W : shapley(world(W), flight(X, Y), card(C), value(V)) }.

max(M) :- M = #max{ C : tmp(card(C), flight(X, Y), sum(N)) }.

tmp2( flight(X, Y), value( @shapley_expr(N, C, M) ) ) :- max(M), tmp(card(C), flight(X, Y), sum(N)).

shapley( flight(X, Y), value( @floatify(F) ) ) :- tmp2(flight(X, Y), value(_)), F = #sum{ V : tmp2(flight(X, Y), value(V)) }.

#show shapley/2.


