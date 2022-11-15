use std::io::{self, Write};

struct Date {
    year: usize,
    month: usize,
    day: usize,
}

fn print_result(result: bool) {
    if result {
        println!("The date is valid!")
    } else {
        println!("The date is invalid!")
    }
}

fn is_leap(year: usize) -> bool {
    if year % 400 == 0 {
        true
    } else if year % 4 == 0 && year % 100 != 0 {
        true
    } else {
        false
    }
}

fn valid(date: Date) -> bool {
    let mut days_in_months: [usize; 12] = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

    if is_leap(date.year) { days_in_months[1] = 29; };

    if date.month > 12 || date.month < 1 {
        println!("Error: Months cannot be greater than 12 (December) or less than 01 (January).");
        return false;
    } else if date.day > days_in_months[date.month - 1] {
        println!("Error: There are not enough days in the month for day {}.", date.day);
        return false;
    } else if date.day < 1 {
        println!("Error: The day cannot be less than 01.");
        return false;
    };

    return true;
}

fn valid_format(date: &Vec<&str>) -> bool {
    if date[0].len() != 4 || date[1].len() != 2 || date[2].len() != 2 { 
        println!("Error: Date is not in the format YYYY-MM-DD.");
        false 
    } else { 
        true 
    }
}

fn main() {
    println!("--- Date Validator ---");
    print!("Enter a date in the format YYYY-MM-DD: ");
    io::stdout().flush().unwrap();
    let mut buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .unwrap();

    let date: Vec<&str> = buffer.trim_end().split("-").collect();
    let result = valid_format(&date);

    if result {
        let date = Date {
            year: date[0].parse().unwrap(),
            month: date[1].parse().unwrap(),
            day: date[2].parse().unwrap(),
        };
    
        let result = valid(date);
        print_result(result);
    } else {
        print_result(result);
    };
}
