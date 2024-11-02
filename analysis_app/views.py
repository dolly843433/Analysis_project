

from django.shortcuts import render
from .models import AnalysisSummary, Demographics
from django.db.models import Q
import json

def analysis_results(request):
    analysis_summary = AnalysisSummary.objects.latest('created_at')

    # Fetch all Demographics and TemporalData related to the analysis summary
    demographics_data = list(Demographics.objects.filter(analysis_summary=analysis_summary).values('value', 'count'))


    # Pass serialized data to the template
    context = {
        'demographics_data': json.dumps(demographics_data),

    }
    return render(request, 'analysis.html', context)
