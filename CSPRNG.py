#	vrperm - Create verifiably pseudorandom permutations
#	Copyright (C) 2022-2022 Johannes Bauer
#
#	This file is part of vrperm.
#
#	vrperm is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	vrperm is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with vrperm; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>

import hashlib

class CSPRNG():
	def __init__(self, seed):
		assert(isinstance(seed, bytes))
		assert(len(seed) >= 32)
		self._seed = seed
		self._state = 0
		self._buffer = bytearray()

	def _fill(self):
		state_bytes = self._state.to_bytes(length = 8, byteorder = "big")
		self._state += 1
		digest = hashlib.sha256(self._seed + state_bytes).digest()
		self._buffer += digest

	def next(self, length = 1):
		while len(self._buffer) < length:
			self._fill()
		(result, self._buffer) = (self._buffer[:length], self._buffer[length:])
		return result

	def nextint(self, modulus):
		bits = (modulus - 1).bit_length()
		bytelength = (bits + 7) // 8
		mask = (1 << bits) - 1
		while True:
			nextval = int.from_bytes(self.next(length = bytelength), byteorder = "little") & mask
			if nextval < modulus:
				return nextval

	def shuffle(self, target):
		n = len(target)
		for i in range(n - 1):
			j = self.nextint(n - i) + i
			assert(i <= j < n)
			(target[i], target[j]) = (target[j], target[i])

if __name__ == "__main__":
	p = CSPRNG(bytes(32))
	for i in range(1000000):
#		z = list(range(2))
#		p.shuffle(z)
#		print(z)
		print(p.nextint(3))
