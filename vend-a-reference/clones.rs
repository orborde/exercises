// Not part of the library. I just put this together to see what the
// compiler was doing under the hood.

fn vendvec(v: &Vec<i32>) -> Vec<i32> {
    v.clone()
}
    

fn main() {
    let mut v: Vec<i32> = Vec::new();
    v.push(1);
    v.push(2);
    v.push(3);
    v.push(4);
    v.push(5);
    let q = vendvec(&v);
    let sm: i32 = q.iter().sum();
    println!("{}", sm);
}
