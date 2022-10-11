use std::f64::consts::PI;

fn f(x: f64) -> f64 {
    x.sin()
}

fn integrate(a: f64, b: f64, n: i64) -> f64 {
    let delta_x = (b - a) / n as f64;
    let mut psi = a + (delta_x / 2.0);
    let mut area = 0.0;
    for _ in 0..n {
        area = area + (f(psi) * delta_x);
        psi = psi + delta_x;
    }
    return area
}

fn main() {
    let area = integrate(0.0, PI, 9999999);
    println!("{area:.9}")
}