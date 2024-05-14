# Human Resources System

with open('Week11/hr_system.txt') as hr_system:
    for line in hr_system:
        line = line.strip()
        parts = line.split()

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = int(parts[3])

        paycheck = ((salary/12)/2)

        if job_title.lower() == 'engineer':
            paycheck = paycheck + 1000
        
        print(f'{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}')