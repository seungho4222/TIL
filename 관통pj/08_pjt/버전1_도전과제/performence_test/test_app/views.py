from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd


@api_view(['GET'])
def data(request):
    csv_path = "data/test_data.CSV"
    df = pd.read_csv(csv_path, encoding='cp949')
    data = df.to_dict('records')
    return JsonResponse({'dat': data})


@api_view(['GET'])
def nan_data(request):
    csv_path = "data/test_data_has_null.CSV"
    df = pd.read_csv(csv_path, encoding='cp949')
    df.fillna('NULL', inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'dat': data})


@api_view(['GET'])
def algorithm(request):
    csv_path = "data/test_data_has_null.CSV"
    df = pd.read_csv(csv_path, encoding='cp949')
    df.fillna(0, inplace=True)
    data = df.to_dict('records')

    df_sum = 0  # 2080.0
    df_len = 0  # 45

    for d in data:
        if d['나이']:
            df_sum += d['나이']
            df_len += 1

    avg = df_sum / df_len  # 46.22222222222222
    
    df['diff'] = abs(df['나이'] - avg)
    new_df = df.sort_values(by=['diff'])
    new_data = new_df.to_dict('records')[:10]

    return JsonResponse({'dat': new_data})


# 배상훈
# @api_view(['GET'])
# def algorithm(request):
#     csv_path = "data/test_data_has_null.CSV"
#     df = pd.read_csv(csv_path, encoding='cp949')
#     df.dropna(axis=0,  inplace=True, subset=['나이'])
#     avg_value = df["나이"].mean()
#     df['diff']=abs(df['나이'] - avg_value)
#     df = df.nsmallest(n=10, columns='diff', keep='first')
#     df.fillna('NULL', inplace=True)
#     data = df.to_dict('records')
#     return JsonResponse({'dat': data})
