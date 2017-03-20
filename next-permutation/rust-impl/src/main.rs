mod stepper;

fn find_insertion_point(v: &Vec<i32>, val: i32, start: usize) -> usize {
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
        assert_eq!(find_insertion_point(&vec![2, 3, 1], 2, 1), 1);
        assert_eq!(find_insertion_point(&vec![1,3,2], 1, 1), 2);
        assert_eq!(find_insertion_point(&vec![1,4,3,2], 1, 1), 3);
    }

    #[test]
    #[should_panic]
    fn bad_start() {
        find_insertion_point(&vec![2, 3, 1], 2, 0);
    }
}

fn permute(arr: &mut Vec<i32>) {
    // The right-hand subarray is in descending order. Figure out how
    // far left that subarray goes.
    let mut subarray_start = arr.len() - 1;
    while subarray_start > 0 &&
        arr[subarray_start-1] >= arr[subarray_start] {
            subarray_start -= 1;
        }

    if subarray_start != 0 {
        let ins_idx = subarray_start - 1;
        let ins_val = arr[ins_idx];
        let ins_point = find_insertion_point(
            arr, ins_val, subarray_start);
        arr.swap(ins_point, ins_idx);
    }

    let subarr = &mut arr[subarray_start..];
    subarr.reverse();
}

#[cfg(test)]
mod permute {
    use super::permute;

    fn permute_wrapper(mut arr: Vec<i32>) -> Vec<i32> {
        permute(&mut arr);
        return arr
    }

    #[test]
    fn simple() {
        assert_eq!(permute_wrapper(vec![1,2]), vec![2,1]);
        assert_eq!(permute_wrapper(vec![2,1]), vec![1,2]);
    }
}


fn main() {
    println!("Hello, world!");
}
