# Advent of Code

This is my repository for the [Advent of Code](https://adventofcode.com/) challenges.

I will be using Python 3.11 for this, in the hope to learn more advanced features of the language.

## Day 1: Trebuchet?!

Part 1 was pretty easy, make a list of characters and use the first and last character of each line to make a number. Then add all the numbers together.

Part 2 was a bit more difficult, first it enumerates forward and backward to find the first digit and it records the position of both. Then it uses a dictionary and find to see if there is an earlier digit (comparing positions) and rfind to see if there is a later digit. If there is, the new characters are recorded, joined, and then summed for an answer.

### My key takeaways:
* Using `line[::-1]` to reverse a string
* rfind to find strings in reverse


## Day 2: Cube Conundrum

The big challenge here was parsing the strings into a usable format. I've used a lot of nested loops here so nowhere near as efficient as i would like, however a dirty solution still works. I might come back to this and try and improve it. 

I was making some stupid mistakes with the way i set it up, particularly having the valid_games list which i initially set the range to constant values. Obviously then when the list changes size (testing) nothing works properly... 
I also broke out the logic checking into separate variables in order to make the debugging easier (thanks breakpoints, really useful here)

Due to other commitments, I was >24 hours late to this one, unfortunately this makes the personal leaderboard a bit pointless. I might start using a stopwatch from now on to get a better idea of how long it takes me to complete each challenge. 
It kind of helps being in a different timezone, it comes out at 6pm for me which is inconvenient but that's not as bad as 12am for some people!

### My key takeaways
* READ THE TASK - I made a bunch of stupid mistakes while working on it
* I need to learn more about breaking out of loops, too many nested loops and removing IDs from a list isn't ideal
* Could I be using regex here? Probably but I don't know how to use it yet
