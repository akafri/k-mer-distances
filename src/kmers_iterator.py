class KmersIterator:

    valid_nucleutides = ['A', 'C', 'G', 'T']

    def __init__(self, k):
        self._k = k

    def get_kmers_dictionary(self):
        return {kmer: 0 for kmer in self.iterator()}

    def iterator(self):
        kmers = [0 for _ in range(self._k)]
        cnt = 0
        index = self._k - 1
        while cnt < 4 ** self._k:
            cnt += 1
            yield ''.join([self.valid_nucleutides[kmers[i]] for i in range(len(kmers))])
            kmers[index] += 1

            for i in range(index, 0, -1):
                if kmers[i] == 4:
                    if i - 1 >= 0:
                        kmers[i - 1] += 1
                    kmers[i] = 0
                else:
                    break
