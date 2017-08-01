from rest_framework import permissions
import logging

LOGGER = logging.getLogger(__name__)


class IsReleasedPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        user_perms = request.user.has_perms(['myapp.view_not_released'])
        LOGGER.debug('has "not released" permission? %r', user_perms)
        is_released = obj.is_released
        LOGGER.debug('is object "released"? %r', is_released)
        return user_perms if not is_released else is_released
