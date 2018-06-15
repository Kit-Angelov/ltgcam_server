from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from rest_framework.exceptions import APIException
from . import serializers
from django.core.mail import send_mail


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
            send_mail('Звонок',
                      'Имя: {0}\nТелефон: {1}\nКомментарий: {2}\nДата: {3}'.format(fio,
                                                                                     phone,
                                                                                     comment,
                                                                                     new_order_call.time),
                      'info@ltgcam.ru',
                      ['info@ltgcam.ru', 'bb@ltgcam.ru'],
                      fail_silently=False,
            )
            return Response({'state': 'ok'})
        else:
            raise APIException('error')


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
            send_mail('Звонок По партнерству',
                      'Имя: {0}\nE-mail: {1}\nТелефон: {2}\nКомпания: {3}\nКомментарий: {4}\nДата: {5}'.format(fio,
                                                                                                               email,
                                                                                                               phone,
                                                                                                               company,
                                                                                                               comment,
                                                                                                               new_partner_call.time),
                      'info@ltgcam.ru',
                      ['info@ltgcam.ru', 'bb@ltgcam.ru'],
                      fail_silently=False,
                      )
            return Response({'state': 'ok'})
        else:
            raise APIException('error')


class OrderBuy(APIView):

    def post(self, request, format=None):
        print(request.data)
        name = request.data.get('name', None)
        phone = request.data.get('phone', None)
        email = request.data.get('email', None)
        city = request.data.get('city', None)
        index = request.data.get('index', None)
        address = request.data.get('address', None)
        pay_var = request.data.get('pay_var', None)
        product_ids = request.data.get('product_ids', None)

        try:
            products = []
            for id in product_ids:
                product = models.AutoModel.objects.get(id=id)
                products.append(product)
            sum = 0
            for product in products:
                sum += product.price
            new_order_buy = models.OrderBuy(name=name,
                                            phone=phone,
                                            email=email,
                                            city=city,
                                            index=index,
                                            address=address,
                                            pay_var=pay_var,
                                            sum=sum)
            new_order_buy.save()
            for item in products:
                new_order_buy.basket.add(item)
            names_products = ''
            for product in products:
                names_products += str(product.mark.name)
                names_products += ' '
                names_products += str(product.name)
                names_products += '\n'
            send_mail('Заказ',
                      'Имя: {0}\nE-mail: {1}\nТелефон: {2}\nГород: {3}\nИндекс: {4}\nАдрес: {5}\nВариант оплаты: {6}\nСумма: {7}\n Товары:\n{8}'.format(name,
                                                                                                               email,
                                                                                                               phone,
                                                                                                               city,
                                                                                                               index,
                                                                                                               address,
                                                                                                               pay_var,
                                                                                                               sum,
                                                                                                               names_products),
                      'info@ltgcam.ru',
                      ['info@ltgcam.ru', 'bb@ltgcam.ru'],
                      fail_silently=False,
                      )

            return Response({'state': 'ok'})
        except:
            raise APIException('error')
