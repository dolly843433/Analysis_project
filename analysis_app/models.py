from django.db import models

# Create your models here.

class AnalysisSummary(models.Model):
    id = models.AutoField(primary_key=True)
    analysis_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
class AnalyzableData(models.Model):
    id = models.AutoField(primary_key=True)
    analysis = models.ForeignKey(AnalysisSummary, on_delete=models.CASCADE, related_name='AnalyzableData')
    Entity=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    Name_type=models.CharField(max_length=255)
    Date_ofBirth=models.CharField(max_length=255)
    place_of_birth=models.TextField()
    citizenship=models.CharField(max_length=255)
    adress=models.TextField(max_length=255)
    Additional_information=models.TextField()
    listing_information=models.TextField()
    Commities=models.CharField(max_length=255)
    Control_Date=models.DateField(null=True,blank=True)


class Demographics(models.Model):
    id = models.AutoField(primary_key=True)
    analysis_summary = models.ForeignKey(AnalysisSummary, on_delete=models.CASCADE, related_name='demographics')
    type = models.CharField(max_length=255)
    value = models.TextField()
    count = models.IntegerField()

class Details(models.Model):
    Date_of_Issue=models.DateField()
    Validity=models.models.DateField()
    Order_Number_Hebrew=models.CharField(max_length=255)
    Order_Number_English=models.CharField(max_length=255)
    Row=models.IntegerField()
    Full_Name_Hebrew=models.CharField(max_length=255)
    Full_name_English=models.CharField(max_length=255)
    Full_name_Arabic=models.CharField(max_length=255)
    AKA_Hebrew=models.CharField(max_length=255)
    Nickname_Hebrew=models.CharField(max_length=255)
    AKA_English=models.CharField(max_length=255)
    Nickname_English=models.CharField(max_length=255)
    Identification_Number=models.CharField(max_length=255)
    Company_Registration_Number=models.CharField(max_length=255)
    DOB=models.DateField()
    Street_1_Hebrew=models.CharField(max_length=255)
    Street_1_English=models.CharField(max_length=255)
    Street_2_Hebrew=models.CharField(max_length=255)
    Street_2_English=models.CharField(max_length=255)
    Building_Number=models.CharField(max_length=255)
    Floor=models.CharField(max_length=255)
    City_Hebrew=models.CharField(max_length=255)
    City_English=models.CharField(max_length=255)
    Country_Hebrew=models.CharField(max_length=255)
    Country_English=models.CharField(max_length=255)
    Postal_Code=models.IntegerField()
    Phone_Number_1=models.IntegerField()
    Phone_Number_2=models.IntegerField()
    Email_1=models.CharField(max_length=255)
    Email_2=models.CharField(max_length=255)
    Email_2=models.CharField(max_length=255)
    Organizational_Affiliation_Hebrew=models.CharField(max_length=255)
    Organizational_Affiliation_English=models.CharField(max_length=255)
    Seizure_Amount=models.CharField(max_length=255)
    Reason_Hebrew=models.TextField()
    Reason_English=models.TextField()
    bank_account_hebrew=models.CharField(max_length=255)
    bank_account_english=models.CharField(max_length=255)




    LastPrinted =models.DateTimeField()
    Created=models.DateTimeField()
    LastSaved=models.DateTimeField()
    Version=models.FloatField()