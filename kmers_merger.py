import operator

import kmers_iterator


class KmersMerger:
    def __init__(self, results_file_path, k):
        self._results_file_path = results_file_path
        self._k = k

    def merge_kmers(self):
        with open(self._results_file_path, 'r') as f:
            lines = f.readlines()

        kmers_dictionary = kmers_iterator.KmersIterator(self._k).get_kmers_dictionary()
        for line in lines:
            kmer, count = line.split(' ')
            count = int(count)
            kmers_dictionary[kmer] = count

        merged_counts = dict()
        for kmer, count in kmers_dictionary.items():
            merged_counts[kmer] = [count]

        sorted_kmers_dictionary = sorted(merged_counts.items(), key=operator.itemgetter(0))
        return sorted_kmers_dictionary
