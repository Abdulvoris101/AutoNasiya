from dateutil.relativedelta import relativedelta
from core.models import FinancialStatus
import hashlib
import os
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY

class HashePassword:

    @classmethod
    def hash_password(cls, password):
        
        # Combine password and salt, then hash
        combined = password.encode('utf-8')
        hashed = hashlib.sha256(combined).hexdigest()
        
        return hashed


    @classmethod
    def check_password(cls, password, hashed_password):
        hashed_input, _ = cls.hash_password(password)

        return hashed_password == hashed_input


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


    def calc_finishedAt(self):
        instance = self.instance

        # calculate duration in months
        self.finishedAt = instance.startedAt + relativedelta(months=instance.duration)
        

    

    def calc_monthlyPayment(self):
        # Calculate monthly payment of customer
        self.amountOfMonth = self.totalPrice / self.instance.duration


    def call(self):
        self.calc_totalPrice()
        self.calc_finishedAt()
        self.calc_monthlyPayment()