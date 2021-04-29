import numpy as np
from kmers_counter import *


class KmersVectorDistance:

    def __init__(self, first_fasta_file_path, second_fasta_file_path, k):
        self._first_fasta_file_path = first_fasta_file_path
        self._second_fasta_file_path = second_fasta_file_path
        self._k = k

    def get_d1_distance(self):
        first_kmers_vector = KmersVector(fasta_file_path=self._first_fasta_file_path,
                                         k=self._k,
                                         reversed_complement=False).get_kmers_vector()

        second_kmers_vector = KmersVector(fasta_file_path=self._second_fasta_file_path,
                                          k=self._k,
                                          reversed_complement=False).get_kmers_vector()

        return VectorsDistance(first_kmers_vector=first_kmers_vector,
                               second_kmers_vector=second_kmers_vector).get_distance()

    def get_d2_distance(self):
        first_kmers_vector = KmersVector(fasta_file_path=self._first_fasta_file_path,
                                         k=self._k,
                                         reversed_complement=True).get_kmers_vector()

        second_kmers_vector = KmersVector(fasta_file_path=self._second_fasta_file_path,
                                          k=self._k,
                                          reversed_complement=True).get_kmers_vector()

        return VectorsDistance(first_kmers_vector=first_kmers_vector,
                               second_kmers_vector=second_kmers_vector).get_distance()


class KmersVector:
    def __init__(self, fasta_file_path, k, reversed_complement):
        self._fasta_file_path = fasta_file_path
        self._k = k
        self._reversed_complement = reversed_complement

    def get_kmers_vector(self):
        kmers_dictionary = KmerCounter(fasta_file_path=self._fasta_file_path,
                                       k=self._k,
                                       reversed_complement=self._reversed_complement).count()

        kmers_values = [float(value) for value in kmers_dictionary.values()]
        length = sum(kmers_values)
        if length != 0:
            return np.array(kmers_values) / length
        else:
            return np.array(kmers_values)


class VectorsDistance:
    def __init__(self, first_kmers_vector, second_kmers_vector):
        self._vector_a = first_kmers_vector
        self._vector_b = second_kmers_vector

    def get_distance(self):
        return np.linalg.norm(self._vector_a - self._vector_b)
