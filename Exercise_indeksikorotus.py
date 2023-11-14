def evaluate(amount, percentage):
    return amount + (amount * (percentage / 100))


input_line = input("Enter the amount of the study benefits: ")
benefit = float(input_line)
benefits = evaluate(benefit, 1.17)
print("If the index raise is 1.17 percent,", "the study benefit,",
      "\nafter a raise,", "would be", benefits, "euros"
      "\nand if there was another index raise,",
      "the study\nbenefits would be as much as", evaluate(benefits, 1.17),
      "euros")
