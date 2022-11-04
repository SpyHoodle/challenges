use std::io::{self, Write};

fn main() {
    print!("Enter a date in the format YYYY-MM-DD: ");
    let _ = io::stdout().flush();
    let mut buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .unwrap();

    let date: Vec<u8> = buffer.trim_end().split("-").as_int().collect();

    if date.len() != 3 {
        println!("Error: Please enter in the format YYYY-MM-DD")
    }
    else if date[0].as_str().len() != 4 {
        println!("Error: Please enter in the format YYYY-MM-DD")
    }
    else if date[1].as_str().len() != 2 {
        println!("Error: Please enter in the format YYYY-MM-DD")
    }
    else if date[2].as_str().len() != 2 {
        println!("Error: Please enter in the format YYYY-MM-DD")
    }

    for item in date {
        println!("{}", item)
    }

}