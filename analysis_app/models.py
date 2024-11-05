from django.db import models

# Create your models here.

class AnalysisSummary(models.Model):
    id = models.AutoField(primary_key=True)
    analysis_name = models.CharField(max_length=255)
    table_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class AnalyzableData(models.Model):
    id = models.AutoField(primary_key=True)
    analysis_summary = models.ForeignKey(AnalysisSummary, on_delete=models.CASCADE, related_name='analyzableData')
    Entity=models.CharField(max_length=255)
    type=models.CharField(max_length=255,null=True)
    Name_type=models.CharField(max_length=255,null=True)
    Date_ofBirth=models.CharField(max_length=255,null=True)
    place_of_birth=models.TextField(null=True)
    citizenship=models.CharField(max_length=255,null=True)
    adress=models.TextField(max_length=255,null=True)
    Additional_information=models.TextField(null=True)
    listing_information=models.TextField(null=True)
    Commities=models.CharField(max_length=255,null=True)
    Control_Date=models.DateField(null=True,blank=True)


class Demographics(models.Model):
    id = models.AutoField(primary_key=True)
    analysis_summary = models.ForeignKey(AnalysisSummary, on_delete=models.CASCADE, related_name='demographics')
    type = models.CharField(max_length=255)
    value = models.TextField()
    count = models.IntegerField()

class Details(models.Model):
    id = models.AutoField(primary_key=True)
    analysis_summary = models.ForeignKey(AnalysisSummary, on_delete=models.CASCADE, related_name='details')
    Date_of_Issue=models.DateField(null=True)
    Validity=models.DateField(null=True)
    Order_Number_Hebrew=models.TextField(null=True)
    Order_Number_English=models.TextField(null=True)
    Row=models.IntegerField(null=True)
    Full_Name_Hebrew=models.TextField(null=True)
    Full_name_English=models.TextField(null=True)
    Full_name_Arabic=models.TextField(null=True)
    AKA_Hebrew=models.TextField(null=True)
    Nickname_Hebrew=models.TextField(null=True)
    AKA_English=models.TextField(null=True)
    Nickname_English=models.TextField(null=True)
    Identification_Number=models.TextField(null=True)
    Company_Registration_Number=models.TextField(null=True)
    DOB=models.DateField(null=True)
    Street_1_Hebrew=models.TextField(null=True)
    Street_1_English=models.TextField(null=True)
    Street_2_Hebrew=models.TextField(null=True)
    Street_2_English=models.TextField(null=True)
    Building_Number=models.TextField(null=True)
    Floor=models.TextField(null=True)
    City_Hebrew=models.TextField(null=True)
    City_English=models.TextField(null=True)
    Country_Hebrew=models.TextField(null=True)
    Country_English=models.TextField(null=True)
    Postal_Code=models.IntegerField(null=True)
    Phone_Number_1=models.TextField(null=True)
    Phone_Number_2=models.TextField(null=True)
    Email_1=models.TextField(null=True)
    Email_2=models.TextField(null=True)
    Email_2=models.TextField(null=True)
    Organizational_Affiliation_Hebrew=models.TextField(null=True)
    Organizational_Affiliation_English=models.TextField(null=True)
    Seizure_Amount=models.TextField(null=True)
    Reason_Hebrew=models.TextField(null=True)
    Reason_English=models.TextField(null=True)
    bank_account_hebrew=models.TextField(null=True)
    bank_account_english=models.TextField(null=True)
    LastPrinted =models.DateTimeField(null=True)
    Created=models.DateTimeField(null=True)
    LastSaved=models.DateTimeField(null=True)
    Version=models.FloatField(null=True)

class JsonEntity(models.Model):
    id = models.AutoField(primary_key=True)
    entity_id = models.CharField(max_length=100, unique=True)
    caption = models.CharField(max_length=255)
    schema = models.CharField(max_length=50)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()
    last_change = models.DateTimeField()
    target = models.BooleanField(default=False)
    analysis_summary = models.ForeignKey(AnalysisSummary, on_delete=models.CASCADE, related_name='jsonEntity')

class Referent(models.Model):
    id = models.AutoField(primary_key=True)
    referent = models.CharField(max_length=255)
    json_entity = models.ForeignKey(JsonEntity, on_delete=models.CASCADE, related_name='referent')

class Dataset(models.Model):
    id = models.AutoField(primary_key=True)
    dataset = models.CharField(max_length=255)
    json_entity = models.ForeignKey(JsonEntity, on_delete=models.CASCADE, related_name='dataset')

class Property(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField()  
    json_entity = models.ForeignKey(JsonEntity, on_delete=models.CASCADE, related_name='property')

