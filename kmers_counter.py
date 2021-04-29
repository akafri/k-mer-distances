#!/usr/bin/python

from kmers_iterator import *


class KmerCounter:
    def __init__(self, fasta_file_path, k, reversed_complement):
        self._fasta_file_path = fasta_file_path
        self._k = k
        self._reversed_complement = reversed_complement

    def count(self):
        print("counting kmers for file: {0}, k: {1}".format(self._fasta_file_path, self._k))

        nucleutides = self._read_nucleutide_stream()
        if self._reversed_complement:
            return self._count_with_reverse_complement(nucleutides)
        return self._count_without_reverse_complement(nucleutides)

    def _count_with_reverse_complement(self, nucleutides):
        print("START - counting kmers with reverse complement")
        kmers_dictionary = KmersIterator(self._k, True).get_kmers_dictionary()
        for i in range(len(nucleutides) - self._k):
            kmer = nucleutides[i:i + self._k]
            if all(c in nucleutides for c in kmer):
                reversed_complement_kmer = reverse_complement(kmer)
                if kmer in kmers_dictionary.keys():
                    kmers_dictionary[kmer] += 2
                else:
                    kmers_dictionary[reversed_complement_kmer] += 2
        print("END - counting kmers with reverse complement")
        return kmers_dictionary

    def _count_without_reverse_complement(self, nucleutides):
        print("START - counting kmers without reverse complement")
        kmers_dictionary = KmersIterator(self._k, False).get_kmers_dictionary()
        for i in range(len(nucleutides) - self._k):
            kmer = nucleutides[i:i + self._k]
            if all(nucleutide in valid_nucleutides for nucleutide in kmer):
                kmers_dictionary[kmer] += 1
        print("DONE - counting kmers without reverse complement")
        return kmers_dictionary

    def _read_nucleutide_stream(self):
        print("START - reading nucleutide stream from path {}".format(self._fasta_file_path))
        with open(self._fasta_file_path, 'r') as f:
            f.readline()
            content = f.read().replace("\n", "").upper()
            print("DONE - reading nucleutide stream from path {}".format(self._fasta_file_path))
            return content

