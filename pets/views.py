from django.shortcuts import render, redirect, get_object_or_404  # Adicione o redirect aqui em cima!
from .models import Pet
from .forms import PetForm, ClienteForm # Importando o nosso formulário

# Nova view da página inicial
def home(request):
    return render(request, 'pets/home.html')

# View que você já tinha
def painel_pets(request):
    pets_cadastrados = Pet.objects.all()
    return render(request, 'pets/painel.html', {'meus_pets': pets_cadastrados})

def cadastrar_pet(request):
    # Se o usuário clicou no botão "Salvar" (Enviou dados)
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save() # Salva direto no PostgreSQL!
            return redirect('painel') # Manda o usuário de volta pra tabela
            
    # Se o usuário só abriu a página (Modo leitura)
    else:
        form = PetForm()

    return render(request, 'pets/cadastrar_pet.html', {'form': form})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # TRUQUE DE UX: Salvou o cliente? Já joga ele pra tela de cadastrar o pet!
            return redirect('cadastrar_pet') 
    else:
        form = ClienteForm()

    return render(request, 'pets/cadastrar_cliente.html', {'form': form})

def excluir_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.delete()
    return redirect('painel')