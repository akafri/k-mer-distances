from nucleutide import *


class KmersIterator:

    def __init__(self, k, reversed_complement):
        self._k = k
        self._reverse_complement = reversed_complement

    def get_kmers_dictionary(self):
        kmers_iterator_instance = self.iterator()
        kmers_dictionary = dict()
        for kmer in kmers_iterator_instance:
            if not self._reverse_complement:
                kmers_dictionary[kmer] = 0
            elif kmer not in kmers_dictionary and reverse_complement(kmer) not in kmers_dictionary:
                kmers_dictionary[kmer] = 0
        return kmers_dictionary

    def iterator(self):
        kmers = [0 for i in range(self._k)]
        cnt = 0
        index = self._k - 1
        while cnt < 4 ** self._k:
            cnt += 1
            yield ''.join([valid_nucleutides[kmers[i]] for i in range(len(kmers))])
            kmers[index] += 1

            for i in range(index, 0, -1):
                if kmers[i] == 4:
                    if i - 1 >= 0:
                        kmers[i - 1] += 1
                    kmers[i] = 0
                else:
                    break
