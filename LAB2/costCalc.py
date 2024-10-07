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
