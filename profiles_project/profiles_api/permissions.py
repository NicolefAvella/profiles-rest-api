from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''permitir al usuario solo modificar su perfil, no el de los demas'''

    def has_object_permission(self, request, view, obj):
        '''verifica edit perfil solo para usuario'''

        if request.method in permissions.SAFE_METHODS:
            return True

            return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    '''solo actualiza es status el usuario log'''

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
