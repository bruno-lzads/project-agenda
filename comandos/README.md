

Configurar o git

```

git config --global user.name 'Seu nome"
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configurar o .gitignore
git remote add origin git@github.com:bruno-lzads/project-agenda.git
configurando ssh
git init
git add .
git commit -m 'Mensagem'

```
Projeto Agenda - Passos

* Criar app e setar ele em project/settings.py > INSTALLED_APPS
* Criar NewFolder > base_templates -- para usar consistência em html, exemplo: cabeçalho; rodapé; navbar; etc
* Criar NewFolder > base_static -- para usar consistência em css, exemplos: fontes; cores; display; etc
* Carregar os arquivos static na base.html >> Exemplo:
```
    {% load static %} // para carregar os arquivos static
    <link rel="stylesheet" href="{% static 'global/css/style.css' %}"> // para referênciar o arquivo static css
```
* Configurar o settings do projeto inserindo base_templates em TEMPLATES > 'DIRS' e criar um BASE_DIR / 'base_tamplates'
* Configurar o settings do projeto inserindo base_static abaixo de STATIC_URL > criar STATICFILES_DIRS = ( BASE_DIR / 'base_static')
* Criar um pasta templates no app; criar uma pasta com o namespace do app; e criar um arquivo html >>> É o html principal do app
* Criar arquivo urls.py no app
* Criar uma views no app >> irá carregar o index.html do template dentro do app >>> Exemplo:
```
    from django.shortcuts import render

    def index(request):
        return render(
            request,
            'contact/index.html',
        )
```
* Ligar a view em uma url; ligar a view na url do app >> Exemplo
```
    from django.urls import path
    from contact import views  //Importa as views criadas

    app_name = 'contact'  //namespace para não gerar erro

    urlpatterns = [
        path('', views.index, name='index'),  //seta o index criado em views e utiliza o namespace
    ]
```
* Referênciar a url do app na url padrão, que se encontra na urls do settings em project >> Exemplo:
```
    from django.urls import path, include //importando o include

    urlpatterns = [
        path('', include('contact.urls')), //Referênciando a urls do app
        path('admin/', admin.site.urls),
    ]
```

