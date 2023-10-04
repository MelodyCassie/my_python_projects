from unittest import TestCase

from Classworks.native import Native


class Test(TestCase):

 def test_native(self):
     our_native = Native("Melody","scv776")
     print(our_native.scv_id)
     print(our_native.name)
