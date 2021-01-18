'''
**Beden Kitle Indeksi Hesaplama**
* Bir kisinin ağırlığının, boyuna göre normal olup olmadığını gösteren parametreye Beden Kitle İndeksi denir. 
* insanın kilosunu kişinin boy uzunluğunun karesine bölersek beden kitle indeksi ortaya çıkar. 
* Kullanıcıdan kilo ve boy uzunluğunu alip çıkan sonuç 25'in altindaysa NORMAL, 
* 25-30 arasında ise FAZLA KİLOLU, 
* 30-40 arasında ise OBEZ, 
* 40 ve üzerinde ise AŞIRI ŞİŞMAN şeklinde uyarı yazdiriniz.
'''
print(f'\nEnter the Requested Information:\n--------------------------------')
height=float(input('Height(cm): '))
weight=float(input('Weight(kg): '))
bmi=weight/((height/100)**2)
print(f'\nBMI(Body Mass Index): {bmi:.1f}\nYou are ',end='')
if bmi<25: 
    print('NORMAL')
elif bmi<30 and bmi>=25: 
    print('OVERWEIGHT')
elif bmi<40 and bmi>=30: 
    print('OBESE')
else: 
    print('EXTREME OBESE !')
    
healty_weight=((height/100)**2)*24.9
if bmi>=25:
    print(f'You have to lose {(weight-healty_weight):.1f} kilos to be healthy!')
