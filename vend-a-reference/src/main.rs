mod shifters;
use shifters::*;

fn main() {
    let mut sm = 0;
    let RUNS = 10000;
    let LENGTH = 1000;
    for i in 0..RUNS {
        let mut shifter = shifters::CopyShifter::new(1337, LENGTH);
    }
}
