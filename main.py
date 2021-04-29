#!/usr/bin/python

from distance import *


def main(first_fasta_file, second_fasta_file, k):
    kmers_vector_distance = KmersVectorDistance(first_fasta_file_path=first_fasta_file,
                                                second_fasta_file_path=second_fasta_file,
                                                k=k)

    print("D1 distance: {}", kmers_vector_distance.get_d1_distance())
    print("D2 distance: {}", kmers_vector_distance.get_d2_distance())


if __name__ == '__main__':
    main("files/1.fa", "files/2.fa", 2)
