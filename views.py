from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .serializer import CategorySerializer
from .services import ctg_one, ctg_list
from recipe.models import Category


class CategoryView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def get_object(self, pk):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound('Narmalni id kirit bunaqa it yoq sanda')
        return root

    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            result = ctg_one(kwargs['pk'])
        else:
            result = ctg_list(requests)
        return Response(result, status=HTTP_200_OK)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.create(serializer.data)
        response = ctg_one(root.pk)
        return Response(response, status=HTTP_200_OK)

    def put(self, requests, *args, **kwargs):
        root = self.get_object(kwargs['pk'])
        print(root, "keldi")
        serializer = self.get_serializer(data=requests.data, instance=root)
        print(serializer, "boshogriq keldi")
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        response = ctg_one(root.pk)
        return Response(response, status=HTTP_200_OK)

    def delete(self, requests, *args, **kwargs):
        self.get_object(kwargs['pk']).delete()
        return Response({"success": "bu narsa o'chirildi"}, status=HTTP_200_OK)







