class HomelessnessCase:
    def __init__(self, country, case_id, person_name, legal_code, description):
        self.country = country
        self.case_id = case_id
        self.person_name = person_name
        self.legal_code = legal_code
        self.description = description

    def display_case(self):
        print(f"Case ID: {self.case_id}")
        print(f"Name: {self.person_name}")
        print(f"Country: {self.country}")
        print(f"Legal Code: {self.legal_code}")
        print(f"Description: {self.description}")
        print("-" * 40)


# UK Legal Codes (examples)
uk_codes = {
    "HA1996_PartVII": "Housing Act 1996 - Part VII (Homelessness)",
    "HRA2017": "Homelessness Reduction Act 2017",
    "VAGRANCY1824": "Vagrancy Act 1824 (Being Repealed)",
}

# US Legal Codes (examples)
us_codes = {
    "MCKINNEY1987": "McKinney-Vento Homeless Assistance Act",
    "HEARTH2009": "HEARTH Act (Homeless Emergency Assistance and Rapid Transition to Housing)",
    "CATEGORY1": "Literally Homeless (HUD Category 1)",
    "CATEGORY2": "Imminent Risk of Homelessness (HUD Category 2)",
}

# Example case data
cases = [
    HomelessnessCase("UK", "UK001", "Sarah Williams", "HRA2017", "Relief duty applied due to family eviction."),
    HomelessnessCase("US", "US001", "Jason Brooks", "CATEGORY1", "Living in a shelter in New York."),
    HomelessnessCase("UK", "UK002", "James O'Neill", "VAGRANCY1824", "Cautioned under vagrancy law (pending reform)."),
    HomelessnessCase("US", "US002", "Maria Lopez", "MCKINNEY1987", "Assistance provided for child's school access."),
]

# Display all cases
for case in cases:
    case.display_case()
