# break
for x in range(5) :
    if x == 3 :
        break # ทำงานเมื่อไหร่หยุดทำซ้ำ
    print(f'IoT {x}')

print('+++++++++++')
print('+++++++++++')

# continue
for y in range(5) : 
    if y == 3 :
        continue # ทำงานเมื่อไหร่ จนรอบนั้นนไปรอบต่อไปทันที
    print(f'SAU {y}')