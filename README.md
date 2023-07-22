# Random-Dig-Sites
 Requires Python (https://www.python.org/downloads/) and Cobra Tools (https://github.com/OpenNaja/cobra-tools).

This tool rewrites the research trees at random to simulate random dig sites from JWE1. It outputs tech tree files that need to be injected into the content0 main.ovl, replacing the base game tech trees. You need to repeat this process for every new randomization. 
Note that this mod also changes dinosaur unlocks to be automatic at the required star rating rather than being researched, and tightens up the unlock progress by having every species unlocked by 3 stars.

Included is an optional additional research edit to allow aviaries and lagoons to unlock at 0 stars.

TUTORIAL VID: https://www.youtube.com/watch?v=Pg90e25oPF4

CONTENTS:
randomdigs.py is the python tool that randomizes the research trees.
config controls a few settings for the python tool.
JWEstats.csv contains dinosaur information used by the randomization code.
LagoonAviaryEdit contans an optional research edit to removing the 2 star requirement for lagoons and aviaries. Inject this file into the content0 main.ovl with cobra tools.
