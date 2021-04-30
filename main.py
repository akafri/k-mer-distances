#!/usr/bin/python
import os
import sys

from distance import *


def main(first_fasta_file_path, second_fasta_file_path, k):
    kmers_vector_distance = KmersVectorDistance(first_fasta_file_path=first_fasta_file_path,
                                                second_fasta_file_path=second_fasta_file_path,
                                                k=k)

    print("\nD1 distance: {}\n".format(kmers_vector_distance.get_d1_distance()))
    print("\nD2 distance: {}\n".format(kmers_vector_distance.get_d2_distance()))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("Not enough parameters supplied. Expected parameters are: [first_fasta_file_path] "
                        "[second_fasta_file_path] [k]")
    first_fast_file = sys.argv[1]
    if not os.path.exists(first_fast_file):
        raise Exception("Path {} does not exist".format(first_fast_file))

    second_fast_file = sys.argv[2]
    if not os.path.exists(second_fast_file):
        raise Exception("Path {} does not exist".format(second_fast_file))

    k = int(sys.argv[3])
    if k < 1 or k > 10:
        raise Exception("{} is an invalid k value. 0 < k <= 10".format(k))

    main(first_fast_file, second_fast_file, k)
