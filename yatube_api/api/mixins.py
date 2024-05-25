from rest_framework import mixins, viewsets


class CreateAndListFollowModel(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass
