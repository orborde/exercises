// TODO: This is a crappy name for this.
// TODO: Parameterize index type.
pub struct Stepper {
    state: Vec<usize>,
    end:   usize
}

impl Stepper {
    fn incr_at(&mut self, idx: usize) {
        assert!(self.state[idx] < self.end);
        self.state[idx] += 1;
        if self.state[idx] == self.end && idx > 0 {
            self.incr_at(idx-1);
            self.state[idx] = self.state[idx-1];
        }
    }
    
    fn incr(&mut self) {
        let last_idx = self.state.len() - 1;
        self.incr_at(last_idx);
    }
}

impl Iterator for Stepper {
    type Item = Vec<usize>;
    
    fn next(&mut self) -> Option<Self::Item> {
        if self.state.len() == 0 || self.state[0] == self.end {
            return None
        }

        let ret = self.state.clone();
        self.incr();
        Some(ret)
    }
}

pub fn stepper(start: usize, end: usize, length: usize) -> Stepper {
    Stepper {
        state: vec![start; length],
        end:   end
    }
}

#[cfg(test)]
mod tests {
    use super::stepper;

    #[test]
    fn simple() {
        let mut stp = stepper(1, 4, 3);
        assert_eq!(stp.next().unwrap(), vec![1, 1, 1]);
        assert_eq!(stp.next().unwrap(), vec![1, 1, 2]);
        assert_eq!(stp.next().unwrap(), vec![1, 1, 3]);
        assert_eq!(stp.next().unwrap(), vec![1, 2, 2]);
        assert_eq!(stp.next().unwrap(), vec![1, 2, 3]);
        assert_eq!(stp.next().unwrap(), vec![1, 3, 3]);
        assert_eq!(stp.next().unwrap(), vec![2, 2, 2]);
        assert_eq!(stp.next().unwrap(), vec![2, 2, 3]);
        assert_eq!(stp.next().unwrap(), vec![2, 3, 3]);
        assert_eq!(stp.next().unwrap(), vec![3, 3, 3]);
        assert!(stp.next().is_none());
    }

    #[test]
    fn zerolen() {
        let mut stp = stepper(1, 4, 0);
        assert!(stp.next().is_none());
    }

    #[test]
    fn rangeone() {
        let mut stp = stepper(1, 2, 4);
        assert_eq!(stp.next().unwrap(), vec![1, 1, 1, 1]);
        assert!(stp.next().is_none());
    }

    #[test]
    fn rangezero() {
        let mut stp = stepper(1, 1, 4);
        assert!(stp.next().is_none());
    }
}
