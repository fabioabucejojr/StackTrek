Donation = float(input("Target Donation: "))
number_of_puzzle = float(input("Number of Puzzles: "))
number_of_talkingdoll = float(input("Number of Talking Dolls: "))
number_of_teddybear = float(input("Number of Teddy Bears: "))
number_of_pokemonplushie = float(input("Number of Pokemon Plushies: "))
number_of_bigtoytruck = float(input("Number of Big Toy Truck: "))

total_money_remaining = 0

PUZZLE = 14
TALKING_DOLL = 3
TEDDY_BEAR = 20.2
POKEMON_PLUSHIE = 8.20
BIG_TOY_TRUCK = 10.65

total_items_purchased = number_of_puzzle + number_of_talkingdoll + number_of_teddybear + number_of_pokemonplushie + number_of_bigtoytruck
total_price = ((PUZZLE * number_of_puzzle) + (TALKING_DOLL * number_of_talkingdoll) + (TEDDY_BEAR * number_of_teddybear) + (POKEMON_PLUSHIE * number_of_pokemonplushie) + (BIG_TOY_TRUCK * number_of_bigtoytruck))

if total_items_purchased >= 50: 
    Discount = total_price - (total_price * 0.25)
    rental_fee = Discount * 0.10 
    total_money_remaining = Discount - rental_fee

if total_money_remaining >= Donation:
    total_money_left = total_money_remaining - Donation
    print(f"Yes! {total_money_left:.2f} dollars left.")

else:
    money_needed = total_money_remaining - Donation 
    print(f"Not enough money! {money_needed:.2f} dollars needed.")
