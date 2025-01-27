use std::time::Instant;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn read_lines(filename: &str) -> (Vec<i32>, Vec<i32>) {
    // This function reads from a text file and returns two vectors of ints

    // Initialize two mutable vectors to store data

    let mut vec_a: Vec<i32> = Vec::new();
    let mut vec_b: Vec<i32> = Vec::new();

    // Read file by opening file and initializing reader
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    // Read all lines
    let lines = reader.lines();

    // Iterate through lines
    for line in lines {
        // Remove whitespace and enumerate through lines to push data to the right array
        for (i, number) in line.unwrap().split_whitespace().enumerate() {
            match i {
                0 => vec_a.push(number.parse().unwrap()),
                1 => vec_b.push(number.parse().unwrap()),
                _ => continue,
            }
        }
    }
    (vec_a, vec_b)
}

fn compare_lists(vec_a: &Vec<i32>, vec_b: &Vec<i32>) -> i32 {
    let mut cumulative: i32 = 0;
    for i in 0..vec_a.len() {
        cumulative += vec_a[i].max(vec_b[i]) - vec_a[i].min(vec_b[i])
        // println!("{:?}", i);
        // println!("{:?}", vec_a[i]);
        // println!("{:?}", vec_b[i]);
    }
    cumulative
}

fn calculate_similarity(vec_a: &Vec<i32>, vec_b: &Vec<i32>) -> i32 {
    let mut score = 0;

    for i in vec_a {
        for j in vec_b {
            if i == j {
                score += i
            }
        }
    }
    score
}

fn main() {
    // THIS ONLY WORKS IF RUNNING CARGO FROM THE LOCATION OF THE SRC

    let (mut a, mut b): (Vec<i32>, Vec<i32>) = read_lines("../resources/input.txt");
    // println!("{:?}", a);
    // println!("{:?}", b);
    let start = Instant::now();
    a.sort();
    b.sort();
    // println!("{:?}", a);
    // println!("{:?}", b);
    let difference = compare_lists(&a, &b);
    println!("Difference between lists is: {:?}", difference);
    let score = calculate_similarity(&a, &b);
    println!("Similarity between lists is: {:?}", score);
    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
}
