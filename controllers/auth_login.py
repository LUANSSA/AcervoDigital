import flet as ft

def cLogin(page, nome_field, senha_field):
    nome = nome_field.value
    senha = senha_field.value
    
    # Validação (simples)
    if not nome or not senha:
        if not nome:
            nome_field.error_text = "Nome é obrigatório"
        elif not senha:
            senha_field.error_text = "Senha é obrigatória"
        page.update()
    else:
        page.clean()
        page.add(ft.Text(f"Bem-vindo, {nome}!"))
        page.update()
