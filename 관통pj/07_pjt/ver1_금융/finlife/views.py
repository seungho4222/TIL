from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer


api_key = settings.API_KEY
url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
response = requests.get(url).json()

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response(response)


@api_view(['GET'])
def save_deposit_products(request):
    for base in response.get('result').get('baseList'):
        base_data = {
            'fin_prdt_cd': base.get('fin_prdt_cd'),
            'kor_co_nm': base.get('kor_co_nm'),
            'fin_prdt_nm': base.get('fin_prdt_nm'),
            'etc_note': base.get('etc_note'),
            'join_deny': base.get('join_deny'),
            'join_member': base.get('join_member'),
            'join_way': base.get('join_way'),
            'spcl_cnd': base.get('spcl_cnd'),
        }
        for key, value in base_data.items():
            if value == None:
                base_data[key] = -1
        serializer = DepositProductsSerializer(data=base_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    # print(response.get('result').get('optionList'))
    for option in response.get('result').get('optionList'):
        product = DepositProducts.objects.get(fin_prdt_cd = option.get('fin_prdt_cd'))
        option_data = {
            'product': product,
            'fin_prdt_cd': option.get('fin_prdt_cd'),
            'intr_rate_type_nm': option.get('intr_rate_type_nm'),
            'intr_rate': option.get('intr_rate'),
            'intr_rate2': option.get('intr_rate2'),
            'save_trm': option.get('save_trm'),
        }
        if option_data['intr_rate'] == None:
            option_data['intr_rate'] = -1
        print(option_data)
        serializer = DepositOptionsSerializer(data=option_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return Response({'message': 'okay'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    options = product.depositoptions_set.all()
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    option_list = DepositOptions.objects.all()
    # 최고 우대금리 저장 => 키 값으로 사용
    high_rate = 0
    high_options = []
    for option in option_list:
        if option.intr_rate2 > high_rate:
            high_rate = option.intr_rate2
            high_options = []
            high_options.append(option)
        elif option.intr_rate2 == high_rate:
            high_options.append(option)
    print(high_options)
    result = []
    # 최고 우대 금리인 옵션과 그에 해당하는 상품을 저장하여 출력
    for options in high_options:
        print(options.product)
        print(options)
        s_product = DepositProductsSerializer(options.product)
        s_options = DepositOptionsSerializer(options)

        high_rate_info = {
            "deposit_product": s_product.data,
            "options" : s_options.data,
        }

        result.append(high_rate_info)

    return Response(result)
    
