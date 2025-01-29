use regex::Regex;
use std::env;
use std::fs::read_to_string;
use std::path::PathBuf;

// We create a custom enum to be able to hold different types of data in the same list (Vecs of int
// and bools).

#[derive(Debug)]
enum YesNoNums {
    Numbers(Vec<i32>),
    Active(Command),
}

#[derive(Debug)]
enum Command {
    Do,
    Dont,
}

fn path_maker(filename: &str) -> PathBuf {
    let manifest_dir = env::var("CARGO_MANIFEST_DIR").unwrap();
    let input_path = PathBuf::from(manifest_dir)
        .join("..") // Go up to the rust directory
        .join("..") // Go up to the project root
        .join("inputs")
        .join(filename);
    input_path
}

fn find_elements(text: String) -> Vec<String> {
    let re = Regex::new(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))").unwrap();
    let matches: Vec<String> = re
        .find_iter(&text)
        .map(|m| m.as_str().to_string())
        .collect();
    matches
}

fn main() {
    let path = path_maker("3_input.txt");
    let text: String = read_to_string(path).expect("Wrong file name");

    // Use our created regex function to find elements
    let elements = find_elements(text);

    let find_number = Regex::new(r"\d{1,3}").unwrap();

    let mut all_operations: Vec<YesNoNums> = Vec::new();

    for element in elements {
        if element.starts_with("mul") {
            let mut pair = Vec::new();
            for m in find_number.find_iter(&element) {
                let parsed: i32 = m.as_str().parse().unwrap();
                pair.push(parsed);
            }
            // Here, we sort our values in their relevant enum type by checking the start

            all_operations.push(YesNoNums::Numbers(pair));
        } else if element == "do()" {
            all_operations.push(YesNoNums::Active(Command::Do));
        } else {
            all_operations.push(YesNoNums::Active(Command::Dont));
        }
    }

    let mut counter: i32 = 0;
    let mut counter_with_commands: i32 = 0;
    let mut active_switch: bool = true;

    for pair in all_operations {
        match pair {
            YesNoNums::Numbers(pair) => {
                let value = pair[0] * pair[1];
                counter += &value;

                if active_switch {
                    counter_with_commands += value
                };
            }
            YesNoNums::Active(Command::Do) => active_switch = true,
            YesNoNums::Active(Command::Dont) => active_switch = false,
        }
    }

    println!("Total count:{}", counter);
    println!("Total count with commands:{}", counter_with_commands);
}
