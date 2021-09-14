from django.db.models import Count
from rest_framework import permissions, views
from rest_framework.response import Response

from .models import Mcmackler
from .serializers import McMacklerSerializer


class McMacklerView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        field = request.query_params.get('field', None)
        method = request.query_params.get('method', None)

        while field:
            queryset = Mcmackler.objects.values(field).order_by('id')

            if method == 'values':
                result = queryset.distinct().count()
                break

            elif method == 'common':
                frequent_value = queryset.annotate(freq_value=Count(field)).order_by('-freq_value')[0]
                result = list(frequent_value.values())[0]
                break

            else:
                result = "Column not found"
                break
        else:
            result = "Give parameters"

        method_result = [{"result": result}]

        results = McMacklerSerializer(method_result, many=True).data

        return Response(results)
