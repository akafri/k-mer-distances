#!/usr/bin/python
import os
import sys

from distance import *


def main(first_fasta_file_path, second_fasta_file_path, k, working_directory):
    kmers_vector_distance = KmersVectorDistance(first_fasta_file_path=first_fasta_file_path,
                                                second_fasta_file_path=second_fasta_file_path,
                                                k=k,
                                                working_directory=working_directory)

    print("\nD1 distance: {}\n".format(kmers_vector_distance.get_d1_distance()))
    print("\nD2 distance: {}\n".format(kmers_vector_distance.get_d2_distance()))


if __name__ == '__main__':
    if len(sys.argv) != 5:
        raise Exception("Not enough parameters supplied. Expected parameters are: [first_fasta_file_path] "
                        "[second_fasta_file_path] [k] [working_directory]")
    first_fasta_file_path = sys.argv[1]
    if not os.path.exists(first_fasta_file_path):
        raise Exception("Path {} does not exist".format(first_fasta_file_path))

    second_fasta_file_path = sys.argv[2]
    if not os.path.exists(second_fasta_file_path):
        raise Exception("Path {} does not exist".format(second_fasta_file_path))

    k = int(sys.argv[3])
    if k < 1 or k > 10:
        raise Exception("{} is an invalid k value. 0 < k <= 10".format(k))

    working_directory = sys.argv[4]
    if not os.path.exists(working_directory):
        raise Exception("Path {} does not exist".format(working_directory))

    if os.system("which jellyfish") != 0:
        raise Exception("Jellyfish is not installed")

    main(first_fasta_file_path=first_fasta_file_path,
         second_fasta_file_path=second_fasta_file_path,
         k=k,
         working_directory=working_directory)
