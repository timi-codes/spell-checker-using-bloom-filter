

import math
import hash_fn


class BloomFilter:
    """
    filter: a bit array with all bits to zero.
    capacity(n): Number of items expected to be stored
    fp(p): Probability of false positive
    itemSize(m): Number of bits per element
    numOfHashFns(k): Number of hash functions
    """
    filter = []
    capacity = None
    fp = 0.01
    itemSize = None
    numOfHashFns = 1

    def __init__(self, n, fp):
        self.capacity = n
        self.fp = fp
        self.itemSize, self.numOfHashFns = self._calculate_optimal_m_k(n, fp)
        self.filter = [0] * self.itemSize

    def insert(self, item):
        #Insert items by applying the hash functions and setting the corresponding bits to 1
        for hash_value in self._computeHashes(item):
            self.filter[hash_value] = 1

    def _computeHashes(self, data):
        hash_values = []

        for i in len(self.numOfHashFns):
            # Use different seeds for different hash functions
            seed = str(i + 1)
            hash = hash_fn(seed + data)
            hash_values.append(hash % self.itemSize)

        return hash_values

    def _calculate_optimal_m_k(self, n, p):
        # https://en.wikipedia.org/wiki/Bloom_filter
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        k = (m / n) * math.log(2)
        return int(math.ceil(m)), int(math.ceil(k))
