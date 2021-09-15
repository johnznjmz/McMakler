from django.db.models import Count
from rest_framework import permissions, views
from rest_framework.response import Response

from .models import Mcmackler
from .serializers import McMacklerSerializer


class McMacklerView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        field = request.query_params.get('field', None)  # GET column name from pram feild
        method = request.query_params.get('method', None)  # GET choice of methods (value or common) from pram method

        while field:
            queryset = Mcmackler.objects.values(field).order_by('id')  # create queryset based on column name in variable field
            if method == 'values':
                result = queryset.distinct().count()  # count distcint values in the queryset
                break

            elif method == 'common':
                frequent_value = queryset.annotate(freq_value=Count(field)).order_by('-freq_value')[0]  # caluclate most frequent value in the queryset
                result = list(frequent_value.values())[0]  # pass frequent value to variable result
                break

            else:
                result = "Column not found"  # return result for a non-existing column
                break
        else:
            result = "Give parameters"  # return result when no prameters are given

        method_result = [{"result": result}]

        if type(result) == int:
            results = McMacklerIntSerializer(method_result, many=True).data
        else:
            results = McMacklerCharSerializer(method_result, many=True).data

        return Response(results)
