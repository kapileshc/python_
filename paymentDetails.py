from personalDetails import  personalDetails

from officialDetails import officialDetails

class paymentDetails(personalDetails,officialDetails):

    def generate_payslip(self):
        return 'generating the payslip'
