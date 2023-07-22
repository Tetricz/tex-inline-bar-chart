#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Directory constants
TABLE_DATA_DIR = "tex/figures/data"
DATA_DIR = ""


def get_box(style, x1, x2):
    points = f"({x1},0) -- ({x1},1) -- ({x2},1) -- ({x2},0) -- cycle"
    return f"\\draw [{style}] {points}; "


def get_boxes(n_row, counts):
    boxes = [""] * n_row
    n_responces = sum(counts[0])
    opts = "xscale=8.7,yscale=0.25"

    for i, counts_i in enumerate(counts):
        x1 = 0
        n_responces = sum(counts[i])
        for j, counts_j in enumerate(counts_i):
            x2 = x1 + counts_j / n_responces
            color = ""
            match j:
                case 0:
                    color = "Firebrick1!100"
                case 1:
                    color = "Firebrick1!50"
                case 2:
                    color = "gray!30"
                case 3:
                    color = "Green1!30"
                case 4:
                    color = "Green1!100"
            boxes[i] += get_box(f"fill={color}", x1, x2)
            x1 = x2

        boxes[i] = (
            "\\cellcolor{white} " +
            f"\\begin{{tikzpicture}}[{opts}] {boxes[i]} \end{{tikzpicture}}"
        )

    return boxes

def create_inline_header(index, n_row, counts):

    header = f"{{ \\bf  {index} }}"
    header = f"{header} & {{ \\bf {sum(counts[n_row])}}}"

    if (n_row+1)%2 == 0:
        header = f"\\rowcolor{{gray!20}} {header}"

    return f"{header} &"

def write_inline_bar(qids, counts, filename):
    with open(os.path.join(TABLE_DATA_DIR, filename), "w") as fd:

        res = get_boxes(len(counts), counts)
        for i, qid in enumerate(qids):
            header = create_inline_header(qid, i, counts)
            fd.write(f"{header} {res[i]} \\\\\n")

if __name__ == "__main__":

    ids = ["one", "two", "three", "four",]
    counts = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1],]

    write_inline_bar(ids, counts, "example_data.tex")
