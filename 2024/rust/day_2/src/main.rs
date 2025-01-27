use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

fn path_maker(filename: &str) -> String {
    let manifest_dir = env::var("CARGO_MANIFEST_DIR").unwrap();
    let input_path = PathBuf::from(manifest_dir)
        .join("..") // Go up to the rust directory
        .join("..") // Go up to the project root
        .join("inputs")
        .join(filename); // ACTUAL FILE NAME!
    let output = input_path.to_str().expect("Likely error in file name.");
    output.to_string()
}

fn read_lines(filename: &str) -> Vec<Vec<i32>> {
    // This function reads from a text file and returns two vectors of ints

    // Initialize two mutable vectors to store data

    let mut vec: Vec<Vec<i32>> = Vec::new();
    // let mut vec_b: Vec<i32> = Vec::new();
    //
    // Read file by opening file and initializing reader
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    // Read all lines
    let lines = reader.lines();

    // Iterate through lines
    for line in lines {
        // Remove whitespace and make sub-arrays for each line.
        let mut sub_vec = Vec::new();
        for digit in line.unwrap().split_whitespace().into_iter() {
            sub_vec.push(digit.parse::<i32>().unwrap())
        }
        vec.push(sub_vec);
    }
    vec
}

fn is_safe(line: &Vec<i32>) -> bool {
    let mut ascending = true;
    let mut descending = true;

    // The window method compares values next to eachother, awesome!

    for window in line.windows(2) {
        if window[0] > window[1] {
            ascending = false;
        }
        if window[0] < window[1] {
            descending = false;
        }
        if !ascending && !descending {
            return false;
        }
        if (window[1] - window[0]).abs() > 3 {
            return false;
        }
        if (window[1] - window[0]).abs() < 1 {
            return false;
        }
    }

    true
}

fn dampener(line: &Vec<i32>) -> bool{
    for i in 0..line.len() {
        let mut line_copy = line.clone();
        line_copy.remove(i);
        if is_safe(&line_copy) {return true};

    }
    return false
}

fn main() {
    let input_path = path_maker("2_input.txt");
    let data = read_lines(&input_path);


    let mut counter = 0;
    let mut damp_counter = 0;
    for line in data {
        if is_safe(&line) {
            counter += 1;
        } else {
            if dampener(&line) {damp_counter += 1};
        }
    }
    println!("Non-damped count is {}.", &counter);
    let total = counter + damp_counter;
    println!("Total is {}.", total)

}
