// Try vending references from iterators for great zero-copy justice.

enum ShifterState {
    New{
        val: i32,
    },
    Partial{
        idx: usize
    },
    Complete
}

pub struct Shifter {
    arr:   Vec<i32>,
    state: ShifterState
}

impl Shifter {
    pub fn new(val: i32, len: usize) -> Shifter {
        Shifter {
            arr: vec![0; len],
            state: ShifterState::New{val:val}
        }
    }
    
    pub fn next(&mut self) -> Option<&Vec<i32>> {
        match self.state {
            ShifterState::New {val} => {
                self.arr[0] = val;
                self.state = ShifterState::Partial{idx:0};
                Some(&self.arr)
            },
            ShifterState::Partial{idx} => {
                let val = self.arr[idx];
                self.arr[idx] = 0;
                let nidx = idx + 1;
                if nidx == self.arr.len() - 1 {
                    self.state = ShifterState::Complete;
                } else {
                    self.state = ShifterState::Partial{idx:nidx};
                }
                self.arr[nidx] = val;
                Some(&self.arr)
            },
            ShifterState::Complete => None
        }
    }
}

pub struct CopyShifter {
    arr:   Vec<i32>,
    state: ShifterState
}

impl CopyShifter {
    pub fn new(val: i32, len: usize) -> CopyShifter {
        CopyShifter {
            arr: vec![0; len],
            state: ShifterState::New{val:val}
        }
    }
}

impl Iterator for CopyShifter {
    type Item = Vec<i32>;

    fn next(&mut self) -> Option<Vec<i32>> {
        match self.state {
            ShifterState::New {val} => {
                self.arr[0] = val;
                self.state = ShifterState::Partial{idx:0};
                Some(self.arr.clone())
            },
            ShifterState::Partial{idx} => {
                let val = self.arr[idx];
                self.arr[idx] = 0;
                let nidx = idx + 1;
                if nidx == self.arr.len() - 1 {
                    self.state = ShifterState::Complete;
                } else {
                    self.state = ShifterState::Partial{idx:nidx};
                }
                self.arr[nidx] = val;
                Some(self.arr.clone())
            },
            ShifterState::Complete => None
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Shifter;
    use super::CopyShifter;

    #[test]
    fn simple() {
        let mut shifter = Shifter::new(10, 3);
        assert_eq!(*shifter.next().unwrap(), vec![10, 0, 0]);
        assert_eq!(*shifter.next().unwrap(), vec![0, 10, 0]);
        assert_eq!(*shifter.next().unwrap(), vec![0, 0, 10]);
        assert!(shifter.next().is_none());
    }

    #[test]
    fn copysimple() {
        let mut shifter = CopyShifter::new(10, 3);
        assert_eq!(shifter.next().unwrap(), vec![10, 0, 0]);
        assert_eq!(shifter.next().unwrap(), vec![0, 10, 0]);
        assert_eq!(shifter.next().unwrap(), vec![0, 0, 10]);
        assert!(shifter.next().is_none());
    }

    const SIZE: usize = 10000000;
    use test::Bencher;
    #[bench]
    fn bench_copy(b: &mut Bencher) {
        let mut shifter = CopyShifter::new(1337, SIZE);
        b.iter(|| {
            shifter.next().unwrap().len()
        });
    }

    #[bench]
    fn bench_quick(b: &mut Bencher) {
        let mut shifter = Shifter::new(1337, SIZE);
        b.iter(|| {
            shifter.next().unwrap().len()
        });
    }
}
