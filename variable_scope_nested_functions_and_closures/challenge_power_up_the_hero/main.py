def create_power_up(multiplier):
    def multiply_power_up(base_stat):
        return multiplier * base_stat
    return multiply_power_up  # return the function you actually defined

power_up_double = create_power_up(2)
power_up_triple = create_power_up(3)

hero_attack = 10
hero_defense = 5

result_attack = power_up_double(hero_attack)
result_defense = power_up_triple(hero_defense)

print(result_attack)   # 20
print(result_defense)  # 15