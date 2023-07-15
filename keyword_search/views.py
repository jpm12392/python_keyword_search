from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

import os, json
import pandas as pd





## keyword based search
class SearchKeywordAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # try:
            keyword = self.request.GET.get('keyword', None)
            path_to_json = r"C:\Users\jpm12\Downloads\patent_jsons\patent_jsons"
            json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
            if keyword in json_files:
                context = {'status': True,'message': 'Data found successfully','data':keyword}
            else:
                context = {'status': False,'message': 'No Record Found!!!'}

            return Response(context, status=status.HTTP_200_OK)
        # except Exception as e:
        #     context = {'status': False, 'message': 'Something Went Wrong'}
        #     return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
