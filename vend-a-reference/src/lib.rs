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

struct Shifter {
    arr:   Vec<i32>,
    state: ShifterState
}

impl Shifter {
    fn new(val: i32, len: usize) -> Shifter {
        Shifter {
            arr: vec![0; len],
            state: ShifterState::New{val:val}
        }
    }
    
    fn next(&mut self) -> Option<&Vec<i32>> {
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

#[cfg(test)]
mod tests {
    use super::Shifter;

    #[test]
    fn simple() {
        let mut shifter = Shifter::new(10, 3);
        assert_eq!(*shifter.next().unwrap(), vec![10, 0, 0]);
        assert_eq!(*shifter.next().unwrap(), vec![0, 10, 0]);
        assert_eq!(*shifter.next().unwrap(), vec![0, 0, 10]);
        assert!(shifter.next().is_none());
    }
}
