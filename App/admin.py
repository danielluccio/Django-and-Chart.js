from django.contrib import admin
from .models import Venda, Produto, Funcionario


admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(Funcionario)