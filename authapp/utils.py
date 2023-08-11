from dateutil.relativedelta import relativedelta
from core.models import FinancialStatus
from django.core.exceptions import ObjectDoesNotExist


class CalculateAutoFields:
    def __init__(self, instance):
        self.instance = instance


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
            currentAmount = FinancialStatus.objects.get(customerPurchase=instance)
        except ObjectDoesNotExist:
            raise Exception("Please add FinancialStatus object to this product")