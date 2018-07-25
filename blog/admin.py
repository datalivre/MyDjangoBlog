from django.contrib import admin
from .models import Post

# o modelo Post é importado e definido aqui para ser visível
# na página de administração.
admin.site.register(Post)
