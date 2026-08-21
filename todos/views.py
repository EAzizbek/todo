from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date']

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        completed = self.request.query_params.get('completed')
        if completed is not None:
            queryset = queryset.filter(completed=completed.lower() == 'true')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
