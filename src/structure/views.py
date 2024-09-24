from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from rest_framework.views import APIView


class CategoryListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     if request.user:
    #         data = request.data
    #         # data = {
    #         #     'title': request.data.get('title'),
    #         #     'slug': request.data.get('slug'),
    #         #     'user': request.user.id
    #         # }
    #         serializer = CategorySerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({'error': 'User must be authenticated'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryCreateAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, category_id):

        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def get(self, request, category_id, *args, **kwargs):

        category = self.get_object(category_id)
        if not category:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id, *args, **kwargs):

        category = self.get_object(category_id)
        if not category:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, *args, **kwargs):
        category_instance = self.get_object(category_id)
        if not category_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        category_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class ProductRuleListAPIView(APIView):

    def get(self, request):
        product_rules = ProductRule.objects.all()
        serializer = ProductRuleSerializer(product_rules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, *args, **kwargs):
        # if request.user:
            serializer = ProductRuleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'error': 'User must be authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        
class ProductRuleDetailAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return ProductRule.objects.get(id=pk)
        except ProductRule.DoesNotExist:
            return None
    
    def get(self, request, pk, *args, **kwargs):
        product_rule = self.get_object(pk)
        if not product_rule:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductRuleSerializer(product_rule)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request, pk, *args, **kwargs):

        product_rule = self.get_object(pk)
        if not product_rule:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer =  ProductRuleSerializer(instance=product_rule, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request,pk, *args, **kwargs):

        product_rule = self.get_object(pk)
        if not product_rule:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        product_rule.delete()
        return Response(
            {"res":"product_rule deleted"},
            status=status.HTTP_200_OK
        )
    

class ComfortListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        comforts = Comfort.objects.all()
        serializer = ComfortSerializer(comforts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ComfortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ComfortDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            comfort = Comfort.objects.get(id=pk)
        except Comfort.DoesNotExist:
            return None
    
    def get(self, request, pk, *args, **kwargs):
        comfort = self.get_object(pk)
        if not comfort:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ComfortSerializer(comfort)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        comfort_instance = self.get_object(pk)
        if not comfort_instance:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ComfortSerializer(isinstance=comfort_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        comfort = self.get_object(pk)
        if not comfort:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        comfort.delete()
        return Response({"message": "Object with todo id was deleted"}, status=status.HTTP_200_OK)
    
class ProductImageListAPIView(APIView):
    def get(self,request, *args, **kwargs):
        product_images = ProductImage.objects.all()
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductImageDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            product_image = ProductImage.objects.get(id=pk)
        except ProductImage.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs ):
        product_image = self.get_object(pk)
        if not product_image:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductImageSerializer(product_image)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        product_image = self.get_object(pk)
        if not product_image:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductImageSerializer(isinstance=product_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        product_image = self.get_object(pk)
        if not product_image:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        product_image.delete()
        return Response({"message":"Product image deleted"}, status=status.HTTP_200_OK)


class ProductListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return None
    
    def get(self,request, pk, *args , **kwargs ):
        product = self.get_object(pk)
        if not product:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk, *args, **kwargs):
        product = self.get_object(pk)
        if not product:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(isinstance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        if not product:
            return Response(
                {"raise":"Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST)
        product.delete()
        return Response({"message": "Product deleted"}, status=status.HTTP_200_OK)
