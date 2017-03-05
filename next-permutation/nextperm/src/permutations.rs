struct ElementSwaps {
    state: Vec<usize>
}

impl ElementSwaps {
    pub fn new(length: usize) -> ElementSwaps {
        assert!(length >= 2);
        ElementSwaps{
            state: vec![0;length as usize]
        }
    }

    fn incr(&mut self) -> usize {
        let mut idx = 0;
        while idx < self.state.len() {
            let cur = self.state[idx];
            assert!(cur <= idx);

            let carry = cur == idx;
            if !carry {
                self.state[idx] += 1;
                return idx;
            }

            self.state[idx] = 0;
            idx += 1;
        }

        idx
    }
}

impl Iterator for ElementSwaps {
    type Item = (usize, usize);

    fn next(&mut self) -> Option< (usize, usize) > {
        let right_side = self.incr();
        if right_side == self.state.len() {
            None
        } else {
            Some( (right_side-1, right_side) )
        }
    }
}

struct Permutations<T> {
    swaps: ElementSwaps,
    vec: Vec<T>
}

impl<T: Clone> Permutations<T> {
    pub fn new(vec: Vec<T>) -> Permutations<T> {
        Permutations {
            swaps: ElementSwaps::new(vec.len()),
            vec:   vec.clone()
        }
    }
}

impl <T: Clone> Iterator for Permutations<T> {
    type Item = Vec<T>;
    fn next(&mut self) -> Option<Vec<T>> {
        match self.swaps.next() {
            Some( (x, y) ) => {
                self.vec.swap(x,y);
                Some(self.vec.clone())
            },
            None => None
        }
    }
}

#[cfg(test)]
mod tests {
    mod internals {
        use super::super::ElementSwaps;

        #[test]
        fn swaps3() {
            let mut es = ElementSwaps::new(3);
            assert_eq!(es.next().unwrap(), (0, 1));
            assert_eq!(es.next().unwrap(), (1, 2));
            assert_eq!(es.next().unwrap(), (0, 1));
            assert_eq!(es.next().unwrap(), (1, 2));
            assert_eq!(es.next().unwrap(), (0, 1));
            assert!(es.next().is_none());
        }
    }

    use super::Permutations;
    #[test]
    fn perms3() {
        let v = vec![1, 2, 3];
        let mut perms = Permutations::new(v);
        assert_eq!(perms.next().unwrap(), vec![2, 1, 3]);
    }
}
