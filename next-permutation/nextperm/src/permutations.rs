struct ElementSwaps {
    state: Vec<usize>
}

impl ElementSwaps {
    pub fn new(length: usize) -> ElementSwaps {
        ElementSwaps{
            state: vec![0;length as usize]
        }
    }
}

impl Iterator for ElementSwaps {
    type Item = (usize, usize);

    fn next(&mut self) -> Option< (usize, usize) > {
        return Some( (0,0) )
    }
}

#[cfg(test)]
mod tests {
    use super::ElementSwaps;
    
    #[test]
    fn simple() {
        let mut es = ElementSwaps::new(3);
        assert_eq!(es.next().unwrap(), (0, 1));
        assert_eq!(es.next().unwrap(), (1, 2));
        assert_eq!(es.next().unwrap(), (0, 1));
        assert_eq!(es.next().unwrap(), (1, 2));
        assert_eq!(es.next().unwrap(), (0, 1));
        assert!(es.next().is_none());
    }
}
