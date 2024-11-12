from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import CommonMatchingTable,MasterTable
from .serializers import MatchingTableSerializer,MasterTableSerializer

class IsAdminUserAndStaff(permissions.BasePermission):
    """
    Custom permission to only allow users with is_staff, is_superuser, and is_admin set to True.
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.is_staff and
            request.user.is_superuser and
            getattr(request.user, 'is_admin', False)
        )

class MatchingTableCreateView(generics.CreateAPIView):
    queryset = CommonMatchingTable.objects.all()
    serializer_class = MatchingTableSerializer
    permission_classes = [IsAdminUserAndStaff]


class MatchingTableListView(generics.ListAPIView):
    queryset = CommonMatchingTable.objects.all()
    serializer_class = MatchingTableSerializer
    permission_classes = [IsAdminUserAndStaff]

#Msater Table Creation

class MasterTableCreateView(generics.CreateAPIView):
    queryset = MasterTable.objects.all()
    serializer_class = MasterTableSerializer
    permission_classes = [IsAdminUserAndStaff]

    def create(self, request, *args, **kwargs):
        # Handle multiple objects by passing many=True
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)