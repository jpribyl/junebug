from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions


from chirps.models import Chirp
from .serializers import ChirpModelSerializer


class ChirpCreateAPIView(generics.CreateAPIView):
    serializer_class = ChirpModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChirpListAPIView(generics.ListAPIView):
    serializer_class = ChirpModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Chirp.objects.all().order_by("-timestamp")
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs
