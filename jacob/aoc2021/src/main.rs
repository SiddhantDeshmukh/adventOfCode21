mod day0;

fn main(){
    //This function simply calls the Function of the Day

    //For ease of use, I'll build it as a 'match' check 
    //so only one variable needs to be changed.
    
    let day = 0;// change this for each day
    match day{
        0 => day0::main(),
        _=> println!("Oops, that day doesn't exist!"),
    }



}


