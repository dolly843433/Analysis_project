from django.core.management.base import BaseCommand
import xml.etree.ElementTree as ET

from django.utils import connection

from analysis_app.models import AnalysisSummary, Demographics, AnalyzableData, Details
import pandas as pd
import os
from django.conf import settings

from analysis_app.utils import xml_to_dict


class Command(BaseCommand):
    help = 'Analyze data and store in database'

    def handle(self, *args, **kwargs):
        # xlsx file extracting
        # excel_file_path = os.path.join(settings.BASE_DIR, 'static/data/data.xlsx')
        # df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
        # analysis_summary = AnalysisSummary.objects.create(analysis_name="Data Analysis")
        # for i, row in df.iterrows():
        #     AnalyzableData.objects.create(analysis_id  = analysis_summary.id , Entity=row['Name of Individual or Entity'], type=row['Type'], Name_type=row['Name Type'],Date_ofBirth=row['Date of Birth'],place_of_birth=row['Place of Birth'],citizenship=row['Citizenship'],adress=row['Address'],  Additional_information=row['Additional Information'],listing_information=row['Listing Information'], Commities=row['Committees'],Control_Date=row['Control Date'])
        # for citizenship, count in df['Citizenship'].value_counts().items():
        #     Demographics.objects.create(analysis_summary=analysis_summary, type="Citizenship", value=citizenship,count=count)
        # for birthplace, count in df['Place of Birth'].value_counts().items():
        #     Demographics.objects.create(analysis_summary=analysis_summary, type="Birthplace", value=birthplace,count=count)

        # xml file extracting
        xml_file_path = os.path.join(settings.BASE_DIR, 'static/data/data.xml')
        tree = ET.parse(xml_file_path)
        root = tree.getroot()


        data_dict = xml_to_dict(root)

        for i, row in data_dict.iterrows():
            Details.objects.create(Date_of_Issue=row['Date of Issue (dd/mm/yyyy)'],Validity=row['Validity'],Order_Number_Hebrew=row['Order Number-Hebrew'],Order_Number_English=row['Order Number - English'], Row=row=['Row'],Full_Name_Hebrew=row['Full Name - Hebrew'],Full_name_English=row['Full name - English'],Full_name_Arabic=row['Full name - Arabic'],AKA_Hebrew=row['AKA-Hebrew'], Nickname_Hebrew=row['Nickname - Hebrew'],AKA_English=row['AKA - English'],Nickname_English=row['Nickname-English'],Identification_Number=row['Identification Number'],Company_Registration_Number=row['Company Registration Number'],DOB=row['DOB (dd/mm/yy)'],Street_1_Hebrew=row['Street 1 - Hebrew'], Street_1_English=row['Street 1- English'],Street_2_Hebrew=row['Street 2- Hebrew'],Street_2_English=row['Street 2 - English'], Building_Number=row['Building Number'], Floor=row['Floor'],City_Hebrew=row['City/Village - Hebrew'], City_English=row['City/Village - English'],Country_Hebrew=row['Country/Entity - Hebrew'], Country_English=row['Country/Entity - English'],Postal_Code=row['Postal Code'],   Phone_Number_1=row['Phone Number 1'],Phone_Number_2=row['Phone Number 2'], Email_1=row['Email 1 '], Email_2=row['Email 2'],Email_2=row['Email 2'],Organizational_Affiliation_Hebrew=row['Organizational Affiliation Hebrew'],Organizational_Affiliation_English=row['Organizational Affiliation English'],Seizure_Amount=row['Seizure Amount  '],Reason_Hebrew=row['Reason - Hebrew'],Reason_English=row['Reason - English'],ank_account_hebrew=row['bank account hebrew'], bank_account_english=row['bank account english'])

        # data_dict[0]['Validity']
