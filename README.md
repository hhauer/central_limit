# Visualizing the Central Limit Theorem #

This application is designed to allow users to interactively explore the central
limit theorem in their browser. It uses django to manage the back-end state and
generation of random data, and JavaScript for front-end visualization.

# API #
The AJAX API requires form POST to the various URLs. No data needs to be sent in
the POST, but a GET will return an error. (This is by design of the AJAX plugin,
which expects to do crazy things like, I don't know, modify a model.)

* /ajax/clt_app/random_integer.json
        Returns 'integer' a number between 0, 10 (inclusive) by the non-secure RNG.

* /ajax/clt_app/crypto_random.json
        Returns 'integer' a number between 0, 10 (inclusive) by the crypto-secure RNG.

* /ajax/clt_app/random_slice.json
        Generates a random string of 1024 zeroes and ones. This is stored in the user session, so repeat calls should use the same string. Returns the following members: 'string_count_0' and 'string_count_1', the count of ones and zeroes in the composite string. 'string' the string itself. 'sample' a random sample of 50 elements in the string. 'sample_count_0' and 'sample_count_1' the count of ones and zeroes in the sample.

* /ajax/clt_app/nonrandom_slice.json
        As above with the random_slice operation, but always uses a skewed string of 750 zeroes and 250 ones. Returns the same members.
