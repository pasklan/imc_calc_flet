import flet as ft


def main(page: ft.Page):
    banner_container = ft.Container(
        visible=False,  # Inicialmente oculto
        bgcolor=ft.colors.AMBER,
        padding=10,
        content=ft.Row(
            controls=[
                ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.WHITE, size=40),
                ft.Text("Mensagem do banner", color=ft.colors.WHITE, size=16, expand=True),
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color=ft.colors.WHITE,
                    on_click=lambda e: close_banner(),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )

    def show_banner(message, bgcolor, icon):
        # Configura e exibe o banner
        banner_container.bgcolor = bgcolor
        banner_container.content.controls[0].icon = icon
        banner_container.content.controls[1].value = message
        banner_container.visible = True
        page.update()

    def close_banner():
        # Oculta o banner
        banner_container.visible = False
        page.update()

    def show_warning_banner(e):
        show_banner(
            "Ops, preencha todos os campos!",
            ft.colors.AMBER,
            ft.icons.WARNING_AMBER_ROUNDED,
        )

    def show_error_banner(e):
        show_banner(
            "Ops, informe valores numéricos!",
            ft.colors.RED,
            ft.icons.ERROR_OUTLINE_ROUNDED,
        )

    def handle_img(gen, imc):
        if gen == "Feminino":
            img_data = [
                ("figure_1.png", "Magreza grave!", imc < 16.9),
                ("figure_2.png", "Magreza Moderada!", 17 <= imc < 18.4),
                ("figure_4.png", "Peso saudável!", 18.5 <= imc < 24.9),
                ("figure_5.png", "Sobrepeso!", 25 <= imc < 29.9),
                ("figure_6.png", "Obesidade grau I!", 30 <= imc < 34.9),
                ("figure_7.png", "Obesidade severa!", 35 <= imc < 39.9),
                ("figure_8.png", "Obesidade mórbida", imc >= 40),
            ]
        else:
            img_data = [
                ("figure2_1.png", "Magreza grave!", imc < 16.9),
                ("figure2_2.png", "Magreza Moderada!", 17 <= imc < 18.4),
                ("figure2_4.png", "Peso saudável!", 18.5 <= imc < 24.9),
                ("figure2_5.png", "Sobrepeso!", 25 <= imc < 29.9),
                ("figure2_6.png", "Obesidade grau I!", 30 <= imc < 34.9),
                ("figure2_7.png", "Obesidade severa!", 35 <= imc < 39.9),
                ("figure2_8.png", "Obesidade mórbida", imc >= 40),
            ]
        for src, text, condition in img_data:
            if condition:
                img_result.src = src
                details.value = text
                break

    def validar_float(v):
        try:
            v = v.replace(',', '.')
            return float(v)
        except ValueError:
            return None

    def calcular_imc(e):
        if not peso.value or not altura.value or not genero.value:
            show_warning_banner(e)
        elif not validar_float(peso.value) or not validar_float(altura.value):
            show_error_banner(e)
        else:
            peso_value = float(peso.value)
            altura_value = float(altura.value.replace(',', '.'))
            imc = peso_value / (altura_value ** 2)
            imc = f"{imc:.2f}"
            IMC.value = f"Seu IMC é {imc}"
            handle_img(genero.value, float(imc))
            peso.value, altura.value, genero.value = "", "", ""
            page.update()

    # Configuração da página
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        title=ft.Text("Calculadora de IMC"),
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    page.window.width, page.window.height = 400, 800

    # Inputs e botões
    altura = ft.TextField(label="Altura", hint_text="Por favor insira sua altura")
    peso = ft.TextField(label="Peso", hint_text="Por favor informe seu peso")
    genero = ft.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
        ],
    )
    b_calcular = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc, )
    # button_column = ft.Column(
    #     controls=[b_calcular],
    #     alignment=ft.MainAxisAlignment.CENTER,
    #     horizontal_alignment=ft.CrossAxisAlignment.CENTER
    # )

    # Exibição de resultados
    IMC = ft.Text("Seu IMC é ...", size=30)
    details = ft.Text("Insira seus dados:", size=20)
    img_result = ft.Image(src="logo.png", width=100, height=100, fit=ft.ImageFit.CONTAIN)

    img_row = ft.Row(
        controls=[
            IMC,
            img_result,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Layout principal
    main_content = ft.Column(
        [
            img_row,
            details,
            altura,
            peso,
            genero,
            ft.Row(
                controls=[b_calcular],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        expand=True,
    )

    # Adiciona o banner ao topo do layout
    page.add(
        ft.Column(
            [
                banner_container,  # Banner no topo
                main_content,      # Conteúdo principal
            ],
            expand=True,
        )
    )


ft.app(main)
