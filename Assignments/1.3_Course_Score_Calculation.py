
'''
**Ders Puani Hesaplama**

* Kullanıcıdan Adi, Soyadi, Ogrenci Numarasi, 4 ders adi, bu derslerin Vize ve Final notlari istenecektir. 
* Vize notunun % 40′ı ile Final Notunun %60′ınin toplamı yil sonu ortalamasini verecektir. 
* Ortalama 50‘den küçükse ekranda “KALDI“, 50 ve üstüyse ekranda “GEÇTİ” yazdırılacaktır. 
* Bu yazdirma islemi 4 ders icinde yapilacak ve dersler alt alta yazdirilacaktir.
'''

lesson_count=4

id_info=['First Name','Last Name','School Number']
edu=['Lesson','Midterm Point','Final Point','Grade']

first_name,last_name,school_number,lesson,midterm_point,final_point,grade='','','','','','',''

id_var=[first_name,last_name,school_number]
edu_var=[lesson,midterm_point,final_point,grade]

report=[]

print(f'\nEnter the Student Personal Infos:\n-------------------------------------')
for i, v in enumerate(id_info):
    id_var[i]=input(f'{v}:').capitalize()

print(f'\nEnter the Student Lectural Infos:\n-------------------------------------')
for i in range(lesson_count):
    for index, j in enumerate(edu):
        if index==0:
            edu_var[index]=input(f'{j}_{i+1}: ').capitalize()
        elif index <3:
            edu_var[index]=int(input(f'{edu_var[0]} {j}: '))
        else:
            edu_var[index]= 0.4*edu_var[1]+0.6*edu_var[2]
    if edu_var[3]>=50: 
        print(f'\n{id_var[0]} {id_var[1]} PASSED the {edu_var[0]} class!\nGrade is {edu_var[3]:.1f}...\n')
        report.append(f'{edu_var[0]}: PASSED')
    else: 
        print(f'\n{id_var[0]} {id_var[1]} FAILED the {edu_var[0]} class!\nGrade is {edu_var[3]:.1f}...\n')
        report.append(f'{edu_var[0]}: FAILED')

print(f'{id_var[0]} {id_var[1]} Report Card:\n-------------------------------------')
print(f'School Number: {id_var[2]}')
print(*report,sep='\n')




