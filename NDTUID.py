class NDTUID:
    # method name in constructor
    def __init__(self, method, methodName, techniques, testSpecifications):
        self.method = method  # Public Attribute
        self.methodName = methodName                            #
        self.techniques = techniques                           #
        self.testSpecifications = testSpecifications     #

        def get_methodName(self):
            return(self.methodName)

        def get_techniques(self):
            return (self.techniques)

        def get_testSpecifications(self):
            return (self.testSpecifications)


# Sample Object
PT = NDTUID(
    # Method {Method:UID}
    {"PT": 1},
    # methodName for terminology consolidation
    ["Dye Penetrant Inspection", "Dye Penetrant Testing", "Dye Penetrant Evaluation"],
    # techniques
    {
        # Nested Dictionary
        #          {Type: UID}
        'Type': {'Type I: Flourescent': 1, 'Type III: Colour Contrast': 2, 'Type III: Dual Purpose': 3},
        #          {Method: UID}
        'Method': {"MethodA: Water Washable": 1, "Method B: Post Emulsified Lipophilic": 2, "Method C: Solvent Removable": 3, "Method D: Post Emulsified Hydrophilic": 4, "Method E: Water and Solvent Removable": 5},
        #          {Form: UID}
        'Form': {"form a: Dry Powder": 1, "form b: Water - Soluble": 2, "form c: Water-Suspendable": 3, "form d: Non Aqueous for Type I": 4, "form e: Non Aqueous for Type II and III": 5, "form f: Special Application": 6},
        #          {Sensitivity: UID}
        'Sensitivity': {"Level 0.5": 1, "Level 1": 2, "Level 2": 3, "Level 3": 4, "Level 4": 5},
    },
    # testSpecifications {Spec:UID}
    {'ISO 3452 -1': 1, 'ASME IX': 2}
)

# Nested Dictionary to define method paremeters
# NDTmethods = {
# Methods are defined as per ISO 9712
# 'AT': {'UID': 000000, },
# 'ET': {'UID': 000000, },
# 'IT': {'UID': 000000, },
# 'LT': {'UID': 000000, },
# 'MT': {'UID': 000000, 'Terminology': ['Magnetic Particle Testing', 'Magnetic Particle Inspection', 'Magnetic Particle Evaluation']},
# 'PT': {'UID': 000000, 'Terminology': ['Dye Penetrant Testing', 'Dye Penetrant Inspection', 'Dye Penetrant Evaluation'], },
# 'RT': {'UID': 000000, },
# 'ST': {'UID': 000000, },
# 'UT': {'UID': 000000, },
# 'VT': {'UID': 000000, }
# }
