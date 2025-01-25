import flet as ft
from controllers.auth_login import cLogin

def pLogin(page):
    entrada_nome = ft.TextField(label="Digite o seu nome")
    entrada_senha = ft.TextField(label="Digite a sua senha")
    
    # Botão de login
    login_button = ft.ElevatedButton("Login", on_click=lambda e: cLogin(page, entrada_nome, entrada_senha))
    
    page.add(entrada_nome, entrada_senha, login_button)
    page.update()

