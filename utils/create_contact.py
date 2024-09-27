import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 500

sys.path.append(str(DJANGO_BASE_DIR)) #faz com que o arquivo fique na raiz do projeto
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings' #mostra o caminho do settings do projeto
settings.USE_TZ = False

django.setup() #inicia o django

if __name__ == '__main__':
    import faker #biblioteca para gerar dados fake

    from contact.models import Category, Contact

    #Contact.objects.all().delete() #limpa toda a base de dados da categoria
    Category.objects.all().delete()

    fake = faker.Faker('pt-BR') #retorna uma biblioteca em português
    categories = ['Amigos', 'Família', 'Conhecidos'] #Uma lista de categorias

    django_categories = [Category(name=name) for name in categories] #Usa a lista de categorias para criar cada uma

    for category in django_categories:
        category.save() #salva as categorias na base de dados
    
    django_contacts = [] #Recebe uma lista

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile() #profile gera um dicionário com o perfil fake, basta extrair o que deseja
        email = profile['mail'] #Usando name fake do dicionário
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number() #Cria um phone fake
        created_date: datetime = fake.date_time_this_year()
        description = fake.text(max_nb_chars=100) #cria um texto fake de até 100 caracteres
        category = choice(django_categories) #choice seleciona uma categoria criada

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
                #Manda as informação para lista 'django_contacts' e salvando na memória
            )
        )
    if len(django_contacts) > 0: #Recebe a lista gerada
        Contact.objects.bulk_create(django_contacts) #Cria todas as informações da lista