Consider an iterator that generates all permutations of some input
vector; most such iterators create an entirely new vector object and
return it with each call to next(). However, if the iterator's user is
running some computation over each permutation, and then discarding
it, you could just as well return a reference to the current
permutation (stored in the iterator itself). As long as the caller
"finishes" with the current permutation before it asks for the next
one, you never need to create any new vectors.

This library demonstrates how that could work, using Rust's lifetime
management semantics to prevent the caller from re-using the
reference. Instead of something so complicated as a permutation
generator, I've implemented a "shifter" iterator.

```
test shifters::tests::bench_copy ... bench:      19,366 ns/iter (+/- 2,773)
test shifters::tests::bench_ref  ... bench:          15 ns/iter (+/- 0)
```

Nice!
