# Set Card Game Complexity and Solver with IP

The Set card game was released in 1991[^1], and has been studied extensively by mathmaticians over the last several decades for its unique combinatorial properties. In this writeup, we will highlight some of these results and provide example code for finding valid Sets. 

# What is Set? 
The traditional version of Set involves a deck of 81 cards. Each card has 4 properties (color, shape, shading, number) and each property has 3 versions. This create a total of $3^4 = 81$ cards in the deck. A "valid Set" involves a pair of 3 cards that for each property have either all the same value or all different values. Players play the game by dealing 12 cards face up and simultaneously look for valid Sets. When a player finds a valid set, they remove the set from board and 3 more cards are dealt to replace them. The game ends when there are no more valid Sets left or all cards have been exausted. A player wins the game if they have found more valid Sets than their opposition. 

<p align="center">
  <img src="./docs/sets-examples.jpg" width="500"/>
</p>
 
An example set board with n=12 cards, p=4 properties, and v=3 values.[^2] We will continue to use the notation {n, p, v} for the generalized parameters of Set because they are intuitive. Some papers use different notation such as {m, n, k} as a matter of preference. 


# Sidenote: Relation to Linear Algebra and Finite Fields
The cannonical version of Set with p=4 properties and v=3 values has an interesting property when represented as a finite field. If you represent each card as a vector in $F^4_3$ with the following encoding: [^3]

| Color  | Number | Shape  | Fill |
| ------------- | ------------- | ------------- | ------------- |
| 0 = Red | 0 = 1 symbol  | 0 = oval  | 0 = No fill  |
| 1 = Purple  | 1 = 2 symbols  | 1 = diamonds  | 1 = Shaded   |
| 2 = Green  | 2 = 3 symbols  | 2 = squigle  | 2 = Solid  |

a set can be shown to always form a line with modular wrap-around. 


# Complexity Results: Multi-Dimensional Matching

# Solver for valid Set with IP Formulation
Below is a generalization of the approach taken in the following source [^4] to formulate finding a valid Set with arbitrary N (cards on board), P (number of card parameters), and V (number of values for each parameter). 

<strong>*Maximize*</strong>
$$ 
N/A
$$

<strong>*Given*</strong>
$$ 
b_{i,p,v}
$$
$$ 
vsum_{p,v} = \sum_{i=0}^{i=N} \sum_{v=0}^{v=V} (inc[i] * b[i][p][v]) \forall { p,v }
$$

$$ 
z_{p,v} = 
$$

<strong>*Subject To*</strong>

We have exactly enough cards to form a set
$$
\sum_{i=0}^{i=n} inc[i] = p 
$$


$$
\sum_{i=0}^{i=n} inc[i] = p 
$$


# Sidenote: Minimum cards to deal before valid Set
# Sidenote: 2-card one-compliment rule 




# References
[^1]: https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf
[^2]: https://www.exodusbooks.com/set-game/9097/
[^3]: https://www.math.ucdavis.edu/~anne/FQ2014/set_game.pdf
[^4]: https://tommyodland.com/articles/2019/the-card-game-set-as-a-binary-integer-program/