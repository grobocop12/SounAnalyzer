from django.shortcuts import render
from . import analyze


# Create your views here.
def index(request):
    if request.method == 'POST':
        return analyze_file(request)
    return render(request, 'Analyzer/index.html')


def analyze_file(request):
    audio_file = request.FILES.get("audioFile")
    sample_rate = analyze.get_sample_rate(audio_file.file.name)
    return render(request, 'Analyzer/analyze.html', {'sample_rate': sample_rate})
