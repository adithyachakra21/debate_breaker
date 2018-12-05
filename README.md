# debate_breaker

Adithya here!

As a debater myself, I was always anxious to know how many points I needed (how many rounds I needed to win) to break, or proceed to the elimination rounds of a debate tournament. This code does just that -- given the number of teams in the tournament, the number of teams that will "break" (e.g: the top 8 teams), and the number of rounds, it calculates the points necessary!

I went through multiple iterations of this code. At first, I used quite a complicated algorithm with many, many helper functions because I couldn't see an alternate way of solving the problem. You can find that old code in files old_debatebreaker.py and old_debatebreakerlib.py. Unfortunately it ran into a few pretty presistent bugs, so after a few days of furious debugging, I decided to scrap it altogether.

And then the next day, I realized with a "Eureka!" moment (quite literally: I said "Eureka!" out loud in the computer lab, attracting more than a few stares) that I had missed the most simple, straight-forward algorithm! With that, I coded the new version, which only has one helper function. You can find that code in files debatebreaker.py and debatebreakerlib.py.

TL;DR:

You can find my first iteration at old_debatebreaker.py and old_debatebreakerlib.py.
You can find my second, simpler iteration at debatebreaker.py and debatebreakerlib.py.

Enjoy!
