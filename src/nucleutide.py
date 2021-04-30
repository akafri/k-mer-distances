valid_nucleutides = ['A', 'C', 'G', 'T']
complement_nucleutides_dictionary = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}


def reverse_complement(kmer):
    reversed_complement = ''
    for nucleutide in kmer.upper()[::-1]:
        reversed_complement += complement_nucleutides_dictionary[nucleutide]
    return reversed_complement
