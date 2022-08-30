from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from .models import Tasks
from .serializers import TasksSerializer
from drf_yasg.utils import swagger_auto_schema


class TasksList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TasksSerializer

    def get_queryset(self):
        return Tasks.objects.filter(assignment=self.request.user)


class TasksCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TasksDelete(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TasksSerializer

    def get_queryset(self):
        return Tasks.objects.filter(assignment=self.request.user)


class TasksUpdate(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(request_body=TasksSerializer)
    def post(self, request, pk):
        serializer = TasksSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user_task = Tasks.objects.filter(id=pk, assignment=self.request.user)
        if 'total_hours_time' in self.request.data:
            self.request.data['total_hours_time'] = user_task.total_hours_time +\
                                                    float(self.request.data['total_hours_time'])
        Tasks.objects.filter(id=pk).update(**self.request.data)
        return Response({'result': 'The task has been updated'}, status=status.HTTP_200_OK)







