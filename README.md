# a chess program for the ages
why use an optimized and functional library when you can not??? in short: here i mess around and try to program a game of chess which can be played from command line. maybe i'll even add a gui someday.

* bitboards????? pfffffffffffffft

* late move reduction? centipawns? mating nets? haha we don't do that stuff here amigo

* wavedashing? f-tilt? get outta here

### if anything, it can print a chessboard:
```
  _a__b__c__d__e__f__g__h_
8| R  N  B  Q  K  B  N  R |
7| P  P  P  P  P  P  P  P |
6| -  -  -  -  -  -  -  - |
5| -  -  -  -  -  -  -  - |
4| -  -  -  -  -  -  -  - |
3| -  -  -  -  -  -  -  - |
2|(P)(P)(P)(P)(P)(P)(P)(P)|
1|(R)(N)(B)(Q)(K)(B)(N)(R)|
```
  
anyways, this is basically the next stockfish

### Update: added basic moves from cmd line; here's the first few moves of the sicilian!
```
  _a__b__c__d__e__f__g__h_
8| R  -  B  Q  K  B  N  R |
7| P  P  -  P  P  P  P  P |
6| -  -  N  -  -  -  -  - |
5| -  -  -  -  -  -  -  - |
4| -  -  - (N)(P) -  -  - |
3| -  -  -  -  -  -  -  - |
2|(P)(P)(P) -  - (P)(P)(P)|
1|(R)(N)(B)(Q)(K)(B) - (R)|
```


### Sample QGD gameplay:
```
White to move.
1. King | 2. Queen | 4. Bishop | 5. Knight | 0. Pawn |
Please enter a number to select what kind of piece you want to move: 5
0. Go back. | 1. Knight at b1 | 2. Knight at g1 | 
Please enter a number to select a piece to move: 1
0. Go back. | 1. Nc3 | 2. Nd2 | 3. Na3 | 
Enter the move you want to make: 1
Enter 1 to confirm your move. 0 to go back: 1
White makes a move!
  _a__b__c__d__e__f__g__h_
8| R  N  B  Q  K  B  N  R |
7| P  P  P  -  -  P  P  P |
6| -  -  -  -  P  -  -  - |
5| -  -  -  P  -  -  -  - |
4| -  - (P)(P) -  -  -  - |
3| -  - (N) -  -  -  -  - |
2|(P)(P) -  - (P)(P)(P)(P)|
1|(R) - (B)(Q)(K)(B)(N)(R)|
```

### To-do
* Add move history

* Add castling

* Add check, 50mr, checkmate, stalemate, 3fold

* Maybe add resigning or something
