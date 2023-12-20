from api.v1.client.serializers.blog_serializer import UserSerializer, ArticleSerializer, CommentSerializer, CategorySerializer

from rest_framework import viewsets, mixins, authentication, permissions, permission_classes

from main.models import User, Article, Comment, Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category', 'published']


class ArticleOnlyPublishedViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet,
    ):
    queryset = Article.objects.filter(published=True).all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @permission_classes([permissions.IsAuthenticated])
    def create(self, request):
        pass
    @permission_classes([permissions.IsAuthenticated])
    def update(self, request, pk=None):
        pass
    @permission_classes([permissions.IsAuthenticated])
    def destroy(self, request, pk=None):
        pass


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @permission_classes([permissions.IsAuthenticated])
    def create(self, request):
        pass
    @permission_classes([permissions.IsAuthenticated])
    def update(self, request, pk=None):
        pass
    @permission_classes([permissions.IsAuthenticated])
    def destroy(self, request, pk=None):
        pass


class ArticleManageViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['category', 'published']
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]