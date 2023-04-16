# Meta-analysis of Set Card Game Complexity

The Set card game was released in 1991[^1], and has been studied extensively by mathmaticians over the last several decades for its unique combinatorial properties. In this writeup, we will highlight some of these results and provide example code for playing the Set card game. 

# What is Set? 
The traditional version of Set involves a deck of 81 cards. Each card has 4 properties (color, shape, shading, number) and each property has 3 versions. This create a total of $3^4 = 81$ cards in the deck. A "valid Set" involves a pair of 3 cards that for each property have either all the same value or all different values. Players play the game by dealing 12 cards face up and simultaneously look for valid Sets. When a player finds a valid set, they remove the set from board and 3 more cards are dealt to replace them. The game ends when there are no more valid Sets left or all cards have been exausted. A player wins the game if they have found more valid Sets than their opposition. 

<p align="center">
  <img src="./docs/sets-examples.jpg" width="500"/>
</p>
 
An example set board with n=12 cards, p=4 properties, and v=3 values.[^2] We will continue to use the notation {n, p, v} for the generalized parameters of Set because they are intuitive. Some papers use different notation such as {m, n, k} as a matter of preference. 


# Relation to Linear Algebra 
aa





# References
[^1]: https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf
[^2]: https://www.exodusbooks.com/set-game/9097/
[^3]: https://www.math.ucdavis.edu/~anne/FQ2014/set_game.pdf
