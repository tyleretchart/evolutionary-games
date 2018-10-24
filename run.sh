#!/bin/bash

for i in {1..10}; do
	for g in "stag_hunt" "prisoners_dilemma" "battle_of_the_sexes"; do
		for b in .95 .99; do
			python3 main.py -t 1 -b $b -g $g --random -a all_a all_b tft not_tft exploit &
		done
	done
done

wait
