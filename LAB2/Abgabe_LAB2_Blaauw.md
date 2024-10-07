# P02 – String literals / Conditionals

## 2.2 Cost calculation (selective: WI, DS, MI)
[Link to costCalc.py](./costCalc.py)

```python
def calculate_project_cost():
    budget = float(input("Geben Sie das Gesamtbudget ein: "))
    months = int(input("Geben Sie die Projektdauer in Monaten ein: "))
    machine_type = input("Geben Sie den Maschinentyp ein (A oder B): ").strip().upper()
    
    if machine_type == "A":
        machine_cost = 25000
        material_cost = (47 * 335) + (119 * 1520)
        specialist_cost_per_hour = 150
    elif machine_type == "B":
        machine_cost = 40000
        material_cost = 159 * 865
        specialist_cost_per_hour = 175
    else:
        return "Ungültiger Maschinentyp! Bitte wählen Sie entweder 'A' oder 'B'."
    
    total_machine_material_cost = machine_cost + material_cost
    if total_machine_material_cost > 0.25 * budget:
        return f"Die Kosten für Maschinen und Materialien ({total_machine_material_cost}) überschreiten 25% des Budgets ({0.25 * budget})."
    
    labor_budget = budget - total_machine_material_cost
    manager_hours = months * 42
    manager_cost = manager_hours * 200
    
    if not (0.08 * labor_budget <= manager_cost <= 0.12 * labor_budget):
        return f"Die Projektmanagementkosten ({manager_cost}) liegen nicht zwischen 8-12% des Arbeitsbudgets ({labor_budget})."
    
    max_specialist_hours = (labor_budget - manager_cost) / specialist_cost_per_hour
    total_labor_hours = manager_hours + max_specialist_hours
    
    return {
        "Kosten für Maschinen und Materialien": total_machine_material_cost,
        "Arbeitskosten": labor_budget,
        "Projektmanagement-Stunden": manager_hours,
        "Spezialisten-Arbeitsstunden": int(max_specialist_hours),
        "Gesamte Arbeitsstunden": int(total_labor_hours),
        "Projektmanagement-Kosten in % der Arbeitskosten": round((manager_cost / labor_budget) * 100, 2)
    }

result = calculate_project_cost()
print(result)
```

## 2.4 Rock Paper Scissors
[Link to rockPaperScissor.py](./rockPaperScissor.py)

```python
import random

ascii_art = r"""

  _________      .__                             _________ __         .__         __________               .__              
 /   _____/ ____ |  |__   ___________   ____    /   _____//  |_  ____ |__| ____   \______   \_____  ______ |__| ___________ 
 \_____  \_/ ___\|  |  \_/ __ \_  __ \_/ __ \   \_____  \\   __\/ __ \|  |/    \   |     ___/\__  \ \____ \|  |/ __ \_  __ \
 /        \  \___|   Y  \  ___/|  | \/\  ___/   /        \|  | \  ___/|  |   |  \  |    |     / __ \|  |_> >  \  ___/|  | \/
/_______  /\___  >___|  /\___  >__|    \___  > /_______  /|__|  \___  >__|___|  /  |____|    (____  /   __/|__|\___  >__|   
        \/     \/     \/     \/            \/          \/           \/        \/                  \/|__|           \/       
                                                     
"""

options = ["Schere", "Stein", "Papier"]
user_score = 0
computer_score = 0

print(ascii_art)

while user_score < 3 and computer_score < 3:
    print("1. Schere")
    print("2. Stein")
    print("3. Papier")
    user_input = input("Wählen Sie von 1-3: ")
    user_choice = options[int(user_input) - 1] if user_input.isdigit() and 1 <= int(user_input) <= 3 else None

    computer_choice = random.choice(options)

    if user_choice is None:
        print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")
        continue

    print("\nDu hast gewählt:", user_choice)
    print("Computer hat gewählt:", computer_choice)
    
    if user_choice == computer_choice:
        print("Unentschieden!")
    elif (user_choice == "Stein" and computer_choice == "Schere") or \
         (user_choice == "Schere" and computer_choice == "Papier") or \
         (user_choice == "Papier" and computer_choice == "Stein"):
        print("Du gewinnst diese Runde!")
        user_score += 1
    else:
        print("Computer gewinnt diese Runde!")
        computer_score += 1

    print(f"\nScore: Player {user_score} - {computer_score} Computer\n")

if user_score == 3:
    print("Du das Spiel gewonnen!")
else:
    print("Computer das das Spiel gewonnen")

```
