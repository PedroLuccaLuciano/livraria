from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Autor, Categoria, Editora, Livro
from uploader.models import Image
from uploader.serializers import ImageSerializer


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model= Editora
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
    capa = ImageSerializer(required=False)

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
        depth = 1
        