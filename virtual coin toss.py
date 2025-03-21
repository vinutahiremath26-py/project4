import random

def coin_toss():
    
    return random.choice(['Heads', 'Tails'])

def multiple_tosses(n):
    
    results = {'Heads': 0, 'Tails': 0}
    
    for _ in range(n):
        result = coin_toss()
        results[result] += 1
    
    return results

def main():
    
    while True:
        try:
            flips = int(input("Enter the number of times you want to flip the coin: "))
            if flips <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue
        
        results = multiple_tosses(flips)
        total = flips
        heads_percentage = (results['Heads'] / total) * 100
        tails_percentage = (results['Tails'] / total) * 100
        
        print("\nResults:")
        print(f"Heads: {results['Heads']} ({heads_percentage:.2f}%)")
        print(f"Tails: {results['Tails']} ({tails_percentage:.2f}%)")
        
        retry = input("Do you want to toss again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thank you for using the coin toss simulator!")
            break

if __name__ == "__main__":
    main()
