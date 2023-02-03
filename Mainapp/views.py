from django.shortcuts import render,HttpResponse
import pandas as pd
import os
from .models import CsvFiles,Candles
from django.core import serializers
# Create your views here.
def home(request):
    try:
        if request.method=="POST":
            file_data = request.FILES.get('csv')
            timeframe = request.POST.get('tf')
            CsvFiles(file=file_data).save()
            a = pd.read_csv(os.path.join('media/file_uploads',str(file_data)))
            candles = [
                        Candles(
                            Date = a.iloc[row][1],
                            Open = a.iloc[row][3], 
                            High = a.iloc[row][4],
                            Low = a.iloc[row][5],
                            Close = a.iloc[row][6],
                        )
                        for row in range(0,len(a.index),int(timeframe))
                    ]
            with open("media/json_files/file.json", "w") as out:
                data = serializers.serialize("json", candles)
                out.write(data)


            
        return render(request,'home.html')
    except Exception as e:
        return HttpResponse("some error occuered : ",str(e))