#!/usr/bin/python
import os

from kmers_merger import KmersMerger


class KmerCounter:
    def __init__(self, fasta_file_path, k, reversed_complement, working_directory):
        self._fasta_file_path = fasta_file_path
        self._k = k
        self._reversed_complement = reversed_complement
        self._working_directory = working_directory

    def count(self):
        print("counting kmers for file: {0}, k: {1}".format(self._fasta_file_path, self._k))
        kmers_counts_output_file = os.path.join(self._working_directory, "mer_counts.jf")
        if self._reversed_complement:
            self._count_with_reverse_complement(kmers_counts_output_file)
        else:
            self._count_without_reverse_complement(kmers_counts_output_file)

        output_file = os.path.join(self._fasta_file_path + ".counts")
        jellyfish_dump_cmd = "jellyfish dump -c {0} > {1}".format(kmers_counts_output_file, output_file)
        print("Execution command: {}".format(jellyfish_dump_cmd))
        os.system(jellyfish_dump_cmd.format(output_file))
        os.remove(kmers_counts_output_file)
        return KmersMerger(results_file_path=output_file, k=self._k).merge_kmers()

    def _count_with_reverse_complement(self, kmers_counts_output_file):
        print("START - counting kmers with reverse complement")
        jellyfish_count_cmd = "jellyfish count -m {0} -s 100M -t 10 -C {1} -o {2}".format(self._k,
                                                                                          self._fasta_file_path,
                                                                                          kmers_counts_output_file)
        print("Execution command: {}".format(jellyfish_count_cmd))
        os.system(jellyfish_count_cmd)
        print("END - counting kmers with reverse complement")

    def _count_without_reverse_complement(self, kmers_counts_output_file):
        print("START - counting kmers with reverse complement")
        jellyfish_count_cmd = "jellyfish count -m {0} -s 100M -t 10 {1} -o {2}".format(self._k,
                                                                                       self._fasta_file_path,
                                                                                       kmers_counts_output_file)
        print("Execution command: {}".format(jellyfish_count_cmd))
        os.system(jellyfish_count_cmd)
        print("END - counting kmers with reverse complement")
