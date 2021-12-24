#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "d", "f", "g", "l", "u"}
    b = {"d", "e", "f", "m", "n", "z"}
    c = {"h", "i", "r", "x", "y"}
    d = {"a", "e", "f", "k", "r", "s", "x"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    bu = u.difference(b)

    y = (a.intersection(bu)).union(c.difference(d))
    print(f"y = {y}")
