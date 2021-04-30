import os

KMER_COUNTS_FILE_SUFFIX = ".counts"
KMER_COUNT_JF_FILE_NAME = "kmer_counts.jf"


class JellyfishExecutor:

    def __init__(self, fasta_file_path, k, reversed_complement, working_directory):
        self._fasta_file_path = fasta_file_path
        self._k = k
        self._reversed_complement = reversed_complement
        self._working_directory = working_directory

    def execute(self):
        kmers_counts_output_file_path = os.path.join(self._working_directory, KMER_COUNT_JF_FILE_NAME)
        count_command = self._get_count_command(kmers_counts_output_file_path)
        self._execute_command(count_command)

        output_file_path = os.path.join(self._working_directory,
                                        os.path.basename(self._fasta_file_path) + KMER_COUNTS_FILE_SUFFIX)
        dump_command = self._get_dump_command(kmers_counts_output_file_path, output_file_path)

        self._execute_command(dump_command)
        os.remove(kmers_counts_output_file_path)
        return output_file_path

    def _get_count_command(self, kmers_counts_output_file_path):
        if self._reversed_complement:
            return "jellyfish count -m {0} -s 100M -t 10 -C {1} -o {2}".format(self._k,
                                                                               self._fasta_file_path,
                                                                               kmers_counts_output_file_path)
        return "jellyfish count -m {0} -s 100M -t 10 {1} -o {2}".format(self._k,
                                                                        self._fasta_file_path,
                                                                        kmers_counts_output_file_path)

    @staticmethod
    def _get_dump_command(kmers_counts_output_file_path, output_file_path):
        return "jellyfish dump -c {0} > {1}".format(kmers_counts_output_file_path, output_file_path)

    @staticmethod
    def _execute_command(command):
        print("START\t - executing command {0}".format(command))
        return_value = os.system(command)
        if return_value != 0:
            raise Exception("Failed to execute command \"{0}\"".format(command))
        print("END\t - executing command {0}".format(command))
