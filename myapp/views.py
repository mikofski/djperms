# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import logging

LOGGER = logging.getLogger(__name__)

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from myapp.serializers import (
    UserSerializer, GroupSerializer, MyModelSerializer
)
from myapp.models import MyModel
from myapp.permissions import IsReleasedPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = (
        permissions.DjangoModelPermissionsOrAnonReadOnly,
        IsReleasedPermission
    )

    def get_queryset(self):
        user_perms = self.request.user.has_perms(['myapp.view_not_released'])
        LOGGER.debug('has "not released" permission? %r', user_perms)
        if user_perms:
            return self.queryset
        else:
            return MyModel.objects.filter(is_released=True)
