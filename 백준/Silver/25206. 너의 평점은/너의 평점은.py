arr = []
n = 0
sum_grade = 0
grade = {'A+' : 4.5,
         'A0' : 4.0,
         'B+' : 3.5,
         'B0' : 3.0,
         'C+' : 2.5,
         'C0' : 2.0,
         'D+' : 1.5,
         'D0' : 1.0,
         'F' : 0.0}

while True:
    try:
        line = list(input().split())
        arr.append(line)        
    except:
        break

arr = [entry for entry in arr if entry[2] != 'P']
            
for i in range(len(arr)):
    grade_num = grade[arr[i][2]] 
    s = float(arr[i][1])   
    cal_grade = s * grade_num
    n += s
    sum_grade += cal_grade
    
print(sum_grade / n)