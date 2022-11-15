use std::collections::HashMap;

#[derive(Debug)]
enum Items {
    Grass,
    Grasshopper,
    Frog,
    Snake,
    Eagle,
    Fox,
    Vole,
    Thrush,
    Slug,
    Rabbit,
}

#[derive(Debug)]
struct Chain {
    consumer: Items,
    consumables: tuple,
}

impl Chain {
    fn from(consumer: Items, consumables: ()) -> Self {
        Self { consumer, consumables }
    }
}

#[derive(Debug)]
struct FoodWeb {
    name: String,
    chains: Vec<Chain>,
}

impl FoodWeb {
    fn new() -> Self {
        let chains = vec![
            Chain::from(Items::Grasshopper, Items::Grass),
            Chain::from(Items::Rabbit, Items::Grass),
            Chain::from(Items::Slug, Items::Grass),
            Chain::from(Items::Thrush, (Items::Slug, Items::Grasshopper)),
            Chain::from(Items::Vole, Items::Grasshopper),
            Chain::from(Items::Frog, Items::Grasshopper),
            Chain::from(Items::Eagle, (Items::Frog, Items::Vole, Items::Thrush)),
            Chain::from(Items::Fox, (Items::Rabbit, Items::Frog, Items::Vole)),
        ];

        Self {
            name: "Example",
            chains,
        }
    }
}

fn main() {
    let food_web = FoodWeb::new();
    dbg!(food_web);
}