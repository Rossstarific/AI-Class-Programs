
locations( s, a, b, c, d, e, f, g ).
path( s, a, 300 ).
path( s, d, 20 ).
path( a, b, 1500 ).
path( a, d, 400 ).
path( d, c, 2000 ).
path( d, e, 3 ).
path( b, c, 9 ).
path( e, b, 200 ).
path( e, f, 400 ).
path( c, g, 12 ).
path( f, g, 800 ).
cost( Dist, plane, Cost):-
    Cost is Dist*1.
cost( Dist, train, Cost):-
    Cost is Dist*0.75.
cost( Dist, bus, Cost):-
    Cost is Dist*0.60.
cost( Dist, car, Cost):-
    Cost is Dist*0.40.
cost( Dist, walk, Cost):-
    Cost is Dist*0.
time( Dist, plane, Time):-
    Time is Dist/500.
time( Dist, train, Time ):-
    Time is Dist/120.
time( Dist, bus, Time ):-
    Time is Dist/80.
time( Dist, car, Time ):-
    Time is Dist/100.
time( Dist, walk, Time ):-
    Time is Dist/5.
connected( X, Y, Z ) :-
    path( X, Y, Z );
    path( Y, X, Z ).
trip( Start, End, Visited, Result ) :-
    trip( Start, End, [Start], 0, Visited, Result ).
preftrip( Start, End, Point1, Point2, Visited, Result ):-
    trip( Start, End, [Start], 0, Visited, Result ),
    member( Point1, Visited ),
    member( Point2, Visited ).
trip( Start, End, Waypoints, DistAcc, Visited, TotalDist) :-
    connected( Start, End, Dist ),
    reverse( [End|Waypoints], Visited ),
    TotalDist is DistAcc + Dist.
trip( Start, End, Waypoints, DistAcc, Visited, TotalDist ) :-
    connected( Start, Waypoint, Dist ),
    \+ member( Waypoint, Waypoints ),
    NewDistAcc is DistAcc + Dist,
    trip( Waypoint, End, [Waypoint|Waypoints], NewDistAcc, Visited, TotalDist ).
shortest( Start, End, Path, Length ) :-
    setof([P,L], trip(Start,End,P,L), Set),
    Set = [_|_], %fail if empty
    minimal(Set, [Path, Length]).
shortest( Start, End, Point1, Point2, Path, Length ):-
    setof([P,L], preftrip(Start,End,Point1,Point2,P,L), Set),
    Set = [_|_],
    minimal(Set, [Path, Length]).
minimal([F|R], M) :-
    min(R, F, M).
min([],M,M).
min([[P,L]|R],[_,M],Min) :-
    L < M,
    !,
    min(R,[P,L],Min).
min([_|R],M,Min) :-
    min(R,M,Min).

answerToTwo( Start, End, Point1, Point2, Visited, Distance, ShortCycle, TotalDistance, Mode, Price ) :-
    shortest( Start, End, Point1, Point2, Visited, Distance ),
    reverse( Visited, [_|Y] ),
    append( Visited, Y, ShortCycle ),
    TotalDistance is Distance*2,
    cost( TotalDistance, Mode, Price ).
answerToOne( Start, End, Point1, Point2, Visited, Distance, ShortCycle, TotalDistance, Mode, Time ) :-
    shortest( Start, End, Point1, Point2, Visited, Distance ),
    reverse( Visited, [_|Y] ),
    append( Visited, Y, ShortCycle ),
    TotalDistance is Distance*2,
    time( TotalDistance, Mode, Time ).
answerToThree( Start, End, Visited, Distance, ShortCycle, TotalDistance ) :-
    shortest( Start, End, Visited, Distance ),
    reverse( Visited, [_|Y] ),
    append( Visited, Y, ShortCycle),
    TotalDistance is Distance*2.
bestTrip( Start, End, Point1, Point2, Visited, Distance, ShortCycle, TotalDistance, Mode, Price, Time ):-
    shortest( Start, End, Point1, Point2, Visited, Distance ),
    reverse( Visited, [_|Y] ),
    append( Visited, Y, ShortCycle ),
    TotalDistance is Distance*2,
    cost( TotalDistance, Mode, Price ),
    time( TotalDistance, Mode, Time ).


/*
1.
for a trip that goes through b, e, and c that is less than 15 hours,
type

"?- answerToOne( s, c, b, e, Visited, Distance, FinalTrip,
TotalDistance, Mode, Time )."

into the command line. Then keep hitting ";" to get every time option
based on the available types of transportation.



2.
for a trip that goes through two preferred points (in this case, b
and e) and ends at c, type

"?- answerToTwo( s, c, b, e, Visited, Distance, FinalTrip,
TotalDistance, Mode, Price )."

into the command line. Then, keep hitting ";" to get every price option
based on the available types of transportation.



3.
for the shortest trip between s and c, type

"?- answerToThree( s, c, Visited, Distance, FinalTrip, TotalDistance )."

into the command line.



4.
to find the absolute best trip that gives back both price AND time,
type

"?- bestTrip( s, c, b, e, Visited, Distance, FinalTrip, TotalDistance,
Mode, Price, Time )."

into the command line.


REMEMBER THIS FOR THE INSTRUCTIONS:
In 1, 2, and 4, the first and second paramaters are the start and end
respectively, and the next two parameters are the points you want the
trip to visit. This means that you can enter ANYTHING into these first 4
and the program will return the shortest path that starts at the first,
ends at the second, and passes through the next two points. Just letting
you know this so you can test it.

KEY:
Distance is in km
Price is in $
Time is in hours

*/









