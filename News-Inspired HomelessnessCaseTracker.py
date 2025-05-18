import datetime
from typing import List

class HomelessnessCase:
    def __init__(self, country: str, case_id: str, name: str, age: int, 
                 legal_code: str, cause: str, city: str, date_reported: str):
        self.country = country
        self.case_id = case_id
        self.name = name
        self.age = age
        self.legal_code = legal_code
        self.cause = cause
        self.city = city
        self.date_reported = datetime.datetime.strptime(date_reported, "%Y-%m-%d")

    def __str__(self):
        return (f"[{self.country}] Case {self.case_id} - {self.name}, Age {self.age}\n"
                f"Location: {self.city}, Reported: {self.date_reported.date()}\n"
                f"Cause: {self.cause}, Code: {self.legal_code}\n"
                f"{'-'*50}")

# Common causes from actual news reports
CAUSES = [
    "Eviction after rent increase",
    "Escaping domestic violence",
    "Veteran with PTSD and no family support",
    "Youth aging out of care system",
    "Job loss during pandemic",
    "Mental health and addiction issues"
]

# Realistic case data (fictional names, based on real scenarios)
cases: List[HomelessnessCase] = [
    HomelessnessCase("US", "US1001", "Robert Jenkins", 47, "CATEGORY1", CAUSES[2], "Los Angeles", "2025-05-01"),
    HomelessnessCase("UK", "UK1001", "Claire Newton", 26, "HRA2017", CAUSES[0], "Manchester", "2025-05-06"),
    HomelessnessCase("US", "US1002", "Tamika Rogers", 35, "CATEGORY4", CAUSES[1], "Chicago", "2025-04-28"),
    HomelessnessCase("UK", "UK1002", "Ellie Smith", 19, "HA1996_PartVII", CAUSES[3], "London", "2025-05-02"),
    HomelessnessCase("US", "US1003", "Luis Moreno", 42, "CATEGORY2", CAUSES[4], "Phoenix", "2025-05-10"),
    HomelessnessCase("UK", "UK1003", "John Fryer", 54, "VAGRANCY1824", CAUSES[5], "Liverpool", "2025-05-07"),
]

# Filter function: list recent cases by country and cause
def filter_cases(country: str, cause_keyword: str):
    print(f"🔍 Filtering cases in {country} for cause matching '{cause_keyword}':\n")
    found = False
    for case in cases:
        if case.country == country and cause_keyword.lower() in case.cause.lower():
            print(case)
            found = True
    if not found:
        print("No matching cases found.")

# Example usage
filter_cases("US", "veteran")
print("\n")
filter_cases("UK", "rent increase")
