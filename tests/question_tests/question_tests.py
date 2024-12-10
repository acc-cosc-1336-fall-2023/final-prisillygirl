#write function tests here, don't add input('') statements here!
import unittest

from question_a.question_a import test_config
from question_d.question_d import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
        

    def test_get_most_likely_ancestor_consensus(self):
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"
        
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
       
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 4)
        self.assertEqual(result[2], 10)

        




