# Internet Speed Tweet Bot

Day 51 was to create a project that would use selenium to automatically run an [internet speed test](https://www.speedtest.net/), 
pull the download and upload speed information, and compare that with set expected minimums. If below the minimum expected, the 
application would then log into twitter and tweet our disappointment to whichever internet provider is being used.

This project was made with the assumption that all internet service providers guarantee a certain minimum speed based on the max
speed paid for. Unfortunately I have Spectrum, and spectrum gives absolutely no such guarantee. Because of this I simply made the
application tweet from my account, but not actually tweet at anyone simply to prove functionality.