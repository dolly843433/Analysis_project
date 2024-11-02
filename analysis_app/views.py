

from django.shortcuts import render
from .models import AnalysisSummary, Demographics
from django.db.models import Q
import json

import json
from django.shortcuts import render
from .models import AnalysisSummary, Demographics

def analysis_results(request):
    analysis_summary = AnalysisSummary.objects.filter(table_name='AnalyzableData').latest('created_at')
    
    # Fetch all Demographics related to the analysis summary
    demographics_data = Demographics.objects.filter(analysis_summary=analysis_summary)

    # Divide data into two categories: 'birthplace' and 'citizenship'
    birthplace_data = list(demographics_data.filter(type='Birthplace').values('value', 'count'))
    citizenship_data = list(demographics_data.filter(type='Citizenship').values('value', 'count'))
   
    # Pass serialized data to the template
    context = {
        'birthplace_data': json.dumps(birthplace_data),
        'citizenship_data': json.dumps(citizenship_data),
    }

    return render(request, 'analysis.html', context)

