# Import Modules
import os
import csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Lists to store data
employee_id = []
first_name = []
last_name = []
dob_formatted = []
ssn_formatted = []
state_formatted = []


# Set path for employee_data
employee_csv = os.path.join( "employee_data.csv")

# Open txt File 
with open(employee_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip Headers
    next(csvreader)

    for row in csvreader:
        # Add Employee Id
        employee_id.append(row[0])

        # Add First Name and Last Name
        name_list = row[1].split()
        first_name.append(name_list[0])
        last_name.append(name_list[1])
        
        # Reformat Date of Birth
        dob_list = row[2].split("-")
        dob_formatted.append(f'{dob_list[1]}/{dob_list[2]}/{dob_list[0]}')
         
        # Reformat SSN
        ssn_list = row[3].split("-")
        ssn_formatted.append(f'***-**-{ssn_list[2]}')

        # Re-write State as State Abbreviation 
        state_formatted.append(f'{us_state_abbrev[row[4]]}')

    # Zip lists together
    cleaned_emp_csv = zip(employee_id, first_name, last_name, dob_formatted, ssn_formatted, state_formatted)
    sorted_emp_csv = sorted(cleaned_emp_csv, key=lambda row: row[1], reverse=True)

    # Set variable for output file
    output_file = os.path.join("employee_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB","SSN", "State"])

    # Write in zipped rows
    writer.writerows(sorted_emp_csv)
 