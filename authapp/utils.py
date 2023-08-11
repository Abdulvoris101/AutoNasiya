from dateutil.relativedelta import relativedelta
from core.models import FinancialStatus
from django.core.exceptions import ObjectDoesNotExist


class CalculateAutoFields:
    def __init__(self, instance):
        self.instance = instance
        self.call()

    def calc_totalPrice(self):
        instance = self.instance

        # Remove starting fee 
        amountWithoutFee = instance.costProduct - instance.startingFee 

        # calculate total price without startingfee
        self.totalPrice = (instance.taxRate / 100) * amountWithoutFee + amountWithoutFee


    def calc_duration(self):
        instance = self.instance

        # calculate duration in months
        duration = relativedelta(instance.finishedAt, instance.startedAt)
        
        # Convert to normal nums
        self.duration = duration.months + 12 * duration.years
    

    def calc_monthlyPayment(self):
        # Calculate monthly payment of customer
        self.amountOfMonth = self.totalPrice / self.duration

    def calc_nextPayment(self):
        instance = self.instance
        
        try:
            currentSum = FinancialStatus.objects.get(productPurchase=instance).amount
            reverseSum = currentSum * -1
            self.nextPaymentAmount =  self.amountOfMonth + (reverseSum)

        except ObjectDoesNotExist:
            raise Exception("Iltimos FinancialStatus object yarating ushbu product uchun")

    def call(self):
        self.calc_totalPrice()
        self.calc_duration()
        self.calc_monthlyPayment()
        self.calc_nextPayment()