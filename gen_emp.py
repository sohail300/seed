import json

# Provided employee data
data = [
    {
        "employee": {
            "first_name": "Miguel",
            "middle_name": "",
            "last_name": "Rodriguez",
            "contact_number": "+1-555-345-6789",
            "email": "miguel.rodriguez@example.com",
            "professional_email": "miguel.rodriguez@company.com",
            "nationality": [
                "Mexican"
            ],
            "religion": "Catholic",
            "gender": "Male",
            "date_of_birth": "1988-03-10",
            "category": "General",
            "marital_status": "Single",
            "blood_group": "A-",
            "critical_medical_ailment": False,
            "ailment_name": None,
            "fathers_name": "Carlos Rodriguez",
            "fathers_occupation": "Business Owner",
            "mothers_name": "Rosa Rodriguez",
            "mothers_occupation": "Accountant",
            "spouse_name": None,
            "spouse_occupation": None,
            "current_work_location": "Bangalore",
            "emergency_contact_number": "+1-555-789-0123",
            "emergency_contact_name": "Carlos Rodriguez",
            "emergency_contact_relationship": "Father",
            "id_proof": "Passport",
            "pan_number": "LMNOP7890Q",
            "employment_type": "Full-Time",
            "designation_id": 1,
            "role_ids": [
                1
            ],
            "department_id": 1,
            "company_id": 1,
            "supervisor_id": "EMP0001"
        },
        "address": [
            {
                "type": "Permanent",
                "street": "789 Oak Lane",
                "country": "United States",
                "state": "Texas",
                "city": "Austin",
                "district": "Downtown",
                "pincode": "78701"
            }
        ],
        "qualification": [
            {
                "qualification": "Bachelors Degree",
                "specialization": "Software Engineering",
                "university": "University of Texas",
                "school_college": "School of Computer Science",
                "gpa_or_percentage": 88.3,
                "course_start_date": "2006-09-01",
                "course_end_date": "2010-05-31",
                "course_ongoing": False
            }
        ],
        "language": [
            {
                "language": "English",
                "proficiency": "Proficient",
                "communication_ability": [
                    "Read",
                    "Write",
                    "Speak"
                ]
            },
            {
                "language": "Spanish",
                "proficiency": "Native",
                "communication_ability": [
                    "Read",
                    "Write",
                    "Speak"
                ]
            }
        ],
        "employment": {
            "years_of_relevant_experience": 12.0
        },
        "employment_history": [
            {
                "employer_name": "GlobalTech Solutions",
                "role": "Senior Developer",
                "salary": 105000.0,
                "employment_start_date": "2010-06-15",
                "employment_end_date": "2021-10-31",
                "currently_working": False,
                "additional_employment_information": "Lead developer for cloud migration projects"
            }
        ],
        "employee_offer": {
            "date_of_joining": "2022-01-03T08:30:00.000Z",
            "work_location": [
                "Office"
            ],
            "ctc": 115000,
            "periodic_payment_amount": 115000,
            "payment_frequency": "Monthly"
        },
        "employee_offer_payroll_breakup": [
            {
                "earning_id": "home_allowance",
                "calc_value": 46000.0
            }
        ],
        "bank_details": {
            "beneficiary_name": "Miguel Rodriguez",
            "account_number": "456789012345",
            "ifsc_code": "BANK0009012",
            "account_type": "Savings"
        },
        "nominee": [
            {
                "nominee_name": "Carlos Rodriguez",
                "relationship_with_nominee": "Father",
                "percentage_share": 100.0
            }
        ],
        "additional_details": {
            "has_relative_working": False,
            "relative_name": "Carlos Rodriguez",
            "relative_employee_id": "EMP0001",
            "relationship_type": "Uncle",
            "source": "Referral"
        },
        "job_application": {
            "application_id": "APP34567",
            "job_id": "JOB78901",
            "source": "Referral"
        }
    }
]

base_number = 5551000000
# Generate 50 variations
result = []
for i in range(1, 51):
    emp = json.loads(json.dumps(data[0]))  # Deep copy
    emp['employee']['first_name'] = f"Employee{i}"
    emp['employee']['email'] = f"employee{i}@example.com"
    emp['employee']['professional_email'] = f"employee{i}@company.com"
    number = base_number + i
    contact_number = f"+1-{str(number)[:3]}-{str(number)[3:6]}-{str(number)[6:]}"
    emp['employee']['contact_number'] = contact_number
    emp['bank_details']['beneficiary_name'] = f"Employee{i}"
    emp['nominee'][0]['nominee_name'] = "Carlos Rodriguez"
    result.append(emp)

with open("employees_two.json", "w") as f:
    json.dump(result, f, indent=2)

print("✅ 50 employees saved to employees.json")
