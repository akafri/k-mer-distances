import numpy as np

from .kmers_counter import KmerCounter


class KmersVectorDistance:

    def __init__(self, first_fasta_file_path, second_fasta_file_path, k, working_directory):
        self._first_fasta_file_path = first_fasta_file_path
        self._second_fasta_file_path = second_fasta_file_path
        self._k = k
        self._working_directory = working_directory

    def get_d1_distance(self):
        first_kmers_vector = KmersVector(fasta_file_path=self._first_fasta_file_path,
                                         k=self._k,
                                         reversed_complement=False,
                                         working_directory=self._working_directory).get_kmers_vector()

        second_kmers_vector = KmersVector(fasta_file_path=self._second_fasta_file_path,
                                          k=self._k,
                                          reversed_complement=False,
                                          working_directory=self._working_directory).get_kmers_vector()

        return VectorsDistance(first_kmers_vector=first_kmers_vector,
                               second_kmers_vector=second_kmers_vector).get_distance()

    def get_d2_distance(self):
        first_kmers_vector = KmersVector(fasta_file_path=self._first_fasta_file_path,
                                         k=self._k,
                                         reversed_complement=True,
                                         working_directory=self._working_directory).get_kmers_vector()

        second_kmers_vector = KmersVector(fasta_file_path=self._second_fasta_file_path,
                                          k=self._k,
                                          reversed_complement=True,
                                          working_directory=self._working_directory).get_kmers_vector()

        return VectorsDistance(first_kmers_vector=first_kmers_vector,
                               second_kmers_vector=second_kmers_vector).get_distance()


class KmersVector:

    def __init__(self, fasta_file_path, k, reversed_complement, working_directory):
        self._fasta_file_path = fasta_file_path
        self._k = k
        self._reversed_complement = reversed_complement
        self._working_directory = working_directory

    def get_kmers_vector(self):
        kmers_dictionary = KmerCounter(fasta_file_path=self._fasta_file_path,
                                       k=self._k,
                                       reversed_complement=self._reversed_complement,
                                       working_directory=self._working_directory).count()
        kmers_values = [float(value[1][0]) for value in kmers_dictionary]
        length = sum(kmers_values)
        if length != 0:
            return np.array(kmers_values) / length
        else:
            return np.array(kmers_values)


class VectorsDistance:

    def __init__(self, first_kmers_vector, second_kmers_vector):
        self._first_kmer_vector = first_kmers_vector
        self._second_kmer_vector = second_kmers_vector

    def get_distance(self):
        return np.linalg.norm(self._first_kmer_vector - self._second_kmer_vector, ord=1)
