# Advent of Code

This is my repository for the [Advent of Code](https://adventofcode.com/) challenges.

I will be using Python 3.11 for this, in the hope to learn more advanced features of the language.

## Day 1: Trebuchet?!

Part 1 was pretty easy, make a list of characters and use the first and last character of each line to make a number. Then add all the numbers together.

Part 2 was a bit more difficult, first it enumerates forward and backward to find the first digit and it records the position of both. Then it uses a dictionary and find to see if there is an earlier digit (comparing positions) and rfind to see if there is a later digit. If there is, the new characters are recorded, joined, and then summed for an answer.

### My key takeaways:
* Using `line[::-1]` to reverse a string
* rfind to find strings in reverse
