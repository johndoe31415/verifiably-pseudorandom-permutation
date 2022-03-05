# vrperm
This is a generator for verifiably pseudorandom permutations that can be
influenced by participants. Why would you need this?

Imagine you're assigning topics to students at random. How can you prove as the
lecturer that you had pre-decided the topics and gave them out at random?
Here's how:

  1. Determine the number of topics (and students) in a machine-readable
	 fashion (JSON format)
  2. Create a SHA256 hash over that data. Publish that hash with your students.
	 At this point, the permutation is already fixed.
  3. Ask your students to provide "seed" input to the CSPRNG. They do not know
	 how this will determine the permutation, but given that the hash is fixed,
     it also means the lecuturer cannot retroactively change the order of topics.
  4. Finally, perform the permutation (with all seed inputs) and publish the
	 original file. If the hashes match, it shows that the game was not rigged.


## License
GNU GPL-3
