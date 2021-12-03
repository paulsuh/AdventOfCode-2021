#!/bin/sh

DAY_NUMBER_LEADING_ZERO=$(/bin/date "+%d")
DAY_NUMBER=$(/bin/date "+%e")
#echo $DAY_NUMBER_LEADING_ZERO
#echo $DAY_NUMBER

echo "https://adventofcode.com/2021/day/${DAY_NUMBER}/input"
#/usr/bin/curl -o "Day-${DAY_NUMBER_LEADING_ZERO}/input.txt" "https://adventofcode.com/2021/day/${DAY_NUMBER}/input"
