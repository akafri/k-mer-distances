import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from kmers.src.distance import KmersVectorDistance


class KmersDistanceTest(unittest.TestCase):
    RESOURCES_FOLDER_NAME = "resources"

    def test_d1_and_d2_distances(self):
        first_fasta_file_path = os.path.join(os.path.dirname(__file__), self.RESOURCES_FOLDER_NAME, "1.fa")
        second_fasta_file_path = os.path.join(os.path.dirname(__file__), self.RESOURCES_FOLDER_NAME, "2.fa")
        working_directory = os.path.join(os.path.dirname(__file__), self.RESOURCES_FOLDER_NAME)
        kmers_vector_distance = KmersVectorDistance(first_fasta_file_path=first_fasta_file_path,
                                                    second_fasta_file_path=second_fasta_file_path,
                                                    k=5,
                                                    working_directory=working_directory)

        self.assertEqual(1.0308599834618566, kmers_vector_distance.get_d1_distance())
        self.assertEqual(0.8017922732255149, kmers_vector_distance.get_d2_distance())

    def test_d1_and_d2_distances_given_first_and_second_fasta_files_are_identical(self):
        first_fasta_file_path = os.path.join(os.path.dirname(__file__), self.RESOURCES_FOLDER_NAME, "1.fa")
        working_directory = os.path.join(os.path.dirname(__file__), self.RESOURCES_FOLDER_NAME)
        kmers_vector_distance = KmersVectorDistance(first_fasta_file_path=first_fasta_file_path,
                                                    second_fasta_file_path=first_fasta_file_path,
                                                    k=5,
                                                    working_directory=working_directory)

        self.assertEqual(0.0, kmers_vector_distance.get_d1_distance())
        self.assertEqual(0.0, kmers_vector_distance.get_d2_distance())


if __name__ == '__main__':
    unittest.main()
