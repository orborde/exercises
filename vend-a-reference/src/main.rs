#![feature(test)]

extern crate test;

mod shifters;
use shifters::*;

fn main() {
    println!("GO GO GO SLOW");
    let mut sm = 0;
    let RUNS = 200;
    let LENGTH = 1000;
    for i in 0..RUNS {
        let mut shifter = shifters::Shifter::new(1337, LENGTH);
        loop {
            let v = shifter.next();
            match v {
                Some(v) => {
                    sm += v.iter().sum();
                },
                None => { break }
            };
        }
    }
}
