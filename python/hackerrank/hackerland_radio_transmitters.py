#!/usr/bin/env python3
# Hackerland is a one-dimensional city with houses aligned at integral
# locations along a road. The Mayor wants to install radio transmitters
# on the roofs of the city's houses. Each transmitter has a fixed range
# meaning it can transmit a signal to all houses within that number of
# units distance away.

# Given a map of Hackerland and the transmission range, determine the
# minimum number of transmitters so that every house is within range of
# at least one transmitter. Each transmitter must be installed on top of
# an existing house.


def hackerland_radio_transmitters(x: list[int], k: int) -> int:
    x.sort()
    n = len(x)
    transmitters = 0
    i = 0

    while i < n:
        transmitters += 1

        # Phase 1: Find the furthest house to the right that can cover x[i].
        # Max reach to the right from x[i] is x[i] + k.
        target_cov = x[i] + k
        while i < n and x[i] <= target_cov:
            i += 1

        # The transmitter must be installed on the last house we passed.
        transmitter_loc = x[i - 1]

        # Phase 2: Skip all houses covered by this transmitter to the right.
        # The transmitter covers up to transmitter_loc + k.
        reach = transmitter_loc + k
        while i < n and x[i] <= reach:
            i += 1

    return transmitters
