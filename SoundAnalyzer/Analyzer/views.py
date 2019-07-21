from django.shortcuts import render
from . import analyze
import json
import random

# Create your views here.
def index(request):
    if request.method == 'POST':
        return analyze_file(request)
    return render(request, 'Analyzer/index.html')


def analyze_file(request):
    audio_file = request.FILES.get("audioFile")
    sample_rate = analyze.get_sample_rate(audio_file.file.name)
    data = analyze.get_first_channel(audio_file)
    x_values = [x for x in range(len(data))]
    y_values = data #[random.randint(0,100) for x in range(100)]

    return render(request, 'Analyzer/analyze.html', {'sample_rate': sample_rate,
                                                     'x_values': json.dumps(x_values),
                                                     'y_values': json.dumps(y_values), })
