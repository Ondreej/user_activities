from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import generics, status
from rest_framework.response import Response


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityDetail(generics.RetrieveDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    # Override the delete method to add a permission check for the is_staff attribute
    def delete(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_staff:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
