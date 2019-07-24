from django.shortcuts import render
from . import analyze
import json
import random


# Create your views here.
def index(request):
    if request.method == 'POST' and 'audioFile' in request.FILES:
        return analyze_file(request)
    return render(request, 'Analyzer/index.html')


def analyze_file(request):
    audio_file = request.FILES.get('audioFile')
    data, time, spectrogram = analyze.analyze(audio_file)

    return render(request, 'Analyzer/analyze.html', {'x_values': json.dumps(time),
                                                     'y_values': json.dumps(data), })
