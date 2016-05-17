Conference: dotsecurity-2016
Tags: Security, Cryptography
Filmed: 2016-05-22
Author: annecanteaut
Image: https://farm2.staticflickr.com/1674/26401095720_baa66edda4_k_d.jpg
Title: The struggle for secure cryptography
Curator: sylvinus
Category: Security
Summary: Which cryptographic primitives can be trusted? Anne argues that the only reliable ones are those which have been chosen after an open competition (like the AES or SHA-3) and which have been carefully analyzed by all participants.
Slides: https://www.rocq.inria.fr/secret/Anne.Canteaut/Publications/dotsecurity16.pdf
Video: https://www.youtube.com/watch?v=uT4hrWkbBxM
Template: talk
Date: 2016-05-13 14:41:56

Cryptographic primitives, like encryption schemes, hash functions... are the core of most security applications. But the trust that users place in these algorithms has been repeatedly violated. There are many examples of attacks which exploit weaknesses of the underlying cryptographic primitives, like the recent Logjam and Sloth attacks against TLS.

So when can we trust cryptography? It should be clear that we cannot trust algorithms which do not have public design rationale and which have not been thoroughly studied. Most notably, the primitives recommended by the cryptographic community are those which have been chosen after an international competition.

Within such an open contest, like the AES and the SHA-3 selection processes, all proposals have been carefully analyzed by all participants; their security margins have been evaluated. This ongoing cryptanalytic effort is the only reliable security argument to consider when deciding which primitive to trust.