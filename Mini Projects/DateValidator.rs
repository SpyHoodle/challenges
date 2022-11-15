use std::io::{self, Write};
use std::collections::HashMap;

enum Months {
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December,
}

enum Date {
    Year,
    Month,
    Day
}

fn incorrect_format() {
    println!("Error: Please enter in the format YYYY-MM-DD")
}

fn is_leap(year: usize) -> bool {
    if year % 400 == 0 {
        true
    } else if year % 4 == 0 && year % 100 != 0 {
        true
    } else {
        false
    };
}

fn valid(date: Vec<usize>) -> bool {
    if date.len() != 3 {
        incorrect_format()
        return false;
    } else if date[Date::Year].len() != 4 || date[Date::Month].len() != 2 || data[Date::Day].len() != 2 {
        incorrect_format()
        return false;
    } else {
        let days_in_months = HashMap::from([
            (Months::January,   31),
            (Months::February,  28),
            (Months::March,     31),
            (Months::April,     30),
            (Months::May,       31),
            (Months::June,      30),
            (Months::July,      31),
            (Months::August,    31),
            (Months::September, 30),
            (Months::October,   31),
            (Months::November,  30),
            (Months::December,  31),
        ]);

        if is_leap(date[Date::Year]) {
            let feb = days_in_months.entry(Months::Februrary).and_modify(|feb| *feb = 29).or_insert(29);
        };

        if date[Date::Month].parse::<usize>().unwrap() > 12

        return true;
    }
}

fn main() {
    print!("Enter a date in the format YYYY-MM-DD: ");
    let _ = io::stdout().flush();
    let mut buffer = String::new();
    io::stdin()
        .read_line(&mut buffer)
        .unwrap();

    let date: Vec<&str> = buffer.trim_end().split("-").collect();
    let result = valid(date);

    if result {
        println!("Valid!");
    } else {
        println!("Invalid!");
    };
}
