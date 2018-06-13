from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from rest_framework.exceptions import APIException
from . import serializers


class Mark(viewsets.ReadOnlyModelViewSet):

    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class AutoModel(viewsets.ReadOnlyModelViewSet):

    queryset = models.AutoModel.objects.all()
    serializer_class = serializers.AutoModelSerializer


class OrderCall(APIView):

    def post(self, request, format=None):
        fio = request.data.get('fio', None)
        phone = request.data.get('phone', None)
        comment = request.data.get('comment', None)

        if (fio is not None) and (phone is not None):
            new_order_call = models.OrderCall(fio=fio, phone=phone, comment=comment)
            new_order_call.save()
            return Response({'state': 'ok'})
        else:
            return APIException('error')


class PartnersCall(APIView):

    def post(self, request, format=None):
        fio = request.data.get('fio', None)
        phone = request.data.get('phone', None)
        email = request.data.get('email', None)
        company = request.data.get('company', None)
        comment = request.data.get('comment', None)

        if (fio is not None) and (phone is not None) and (email is not None):
            new_partner_call = models.PartnersCall(fio=fio, phone=phone, email=email, company=company, comment=comment)
            new_partner_call.save()
            return Response({'state': 'ok'})
        else:
            return APIException('error')


class OrderBuy(APIView):

    def post(self, request, format=None):
        name = request.data.get('name', None)
        phone = request.data.get('phone', None)
        email = request.data.get('email', None)
        city = request.data.get('city', None)
        index = request.data.get('index', None)
        address = request.data.get('address', None)
        pay_var = request.data.get('pay_var', None)
        product_ids = request.data.get('product_ids', None)

        try:
            products = models.AutoModel.objects.filter(id__in=product_ids)
            new_order_buy = models.OrderBuy(name=name,
                                            phone=phone,
                                            email=email,
                                            city=city,
                                            index=index,
                                            address=address,
                                            pay_var=pay_var)
            new_order_buy.save()
            for item in products:
                new_order_buy.basket.add(item)

            return Response({'state': 'ok'})
        except Exception as e:
            APIException(e)
