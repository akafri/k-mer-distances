#!/usr/bin/python

from .kmers_merger import KmersMerger
from .jellyfish_executor import JellyfishExecutor


class KmerCounter:
    def __init__(self, fasta_file_path, k, reversed_complement, working_directory):
        self._fasta_file_path = fasta_file_path
        self._k = k
        self._reversed_complement = reversed_complement
        self._working_directory = working_directory

    def count(self):
        print("START\t - counting kmers for file: {0}, k: {1}".format(self._fasta_file_path, self._k))
        output_file = JellyfishExecutor(self._fasta_file_path,
                                        self._k,
                                        self._reversed_complement,
                                        self._working_directory).execute()
        print("END\t - counting kmers for file: {0}, k: {1}".format(self._fasta_file_path, self._k))
        return KmersMerger(results_file_path=output_file, k=self._k).merge()
