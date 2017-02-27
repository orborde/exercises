fn find_insertion_point(v: Vec<i32>, val: i32, start: usize) -> usize {
    assert!(start > 0);
    assert!(v.len() > 0);

    let end = v.len() - 1;

    for idx in start+1 .. end+1 {
        if v[idx] <= val {
            return idx-1
        }
    }
    return end
}

#[cfg(test)]
mod find_insertion_point {
    use super::find_insertion_point;
    
    #[test]
    fn simple() {
        assert_eq!(find_insertion_point(vec![2, 3, 1], 2, 1), 1);
        assert_eq!(find_insertion_point(vec![1,3,2], 1, 1), 2);
        assert_eq!(find_insertion_point(vec![1,4,3,2], 1, 1), 3);
    }

    #[test]
    #[should_panic]
    fn bad_start() {
        find_insertion_point(vec![2, 3, 1], 2, 0);
    }
}

fn main() {
    println!("Hello, world!");
}
