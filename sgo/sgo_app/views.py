"""Views: autenticação, cadastros e geração de relatório em PDF."""
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cliente, Equipamento, Tecnico, Reparo
from .forms import ClienteForm, EquipamentoForm, TecnicoForm, ReparoForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'sgo_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    from .models import Cliente, Tecnico, Equipamento, Reparo
    
    context = {
        'clientes_count': Cliente.objects.count(),
        'tecnicos_count': Tecnico.objects.count(),
        'equipamentos_count': Equipamento.objects.count(),
        'reparos_count': Reparo.objects.count(),
    }
    return render(request, 'sgo_app/home.html', context)

# --- Clientes ---
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'sgo_app/cliente_list.html', {'clientes': clientes})

@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'sgo_app/cliente_form.html', {'form': form, 'title': 'Novo Cliente'})

@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, id_cliente=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'sgo_app/cliente_form.html', {'form': form, 'title': 'Editar Cliente'})

@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, id_cliente=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente removido com sucesso!')
        return redirect('cliente_list')
    return render(request, 'sgo_app/delete_confirm.html', {'object': cliente, 'object_name': 'Cliente'})

# --- Técnicos ---
@login_required
def tecnico_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'sgo_app/tecnico_list.html', {'tecnicos': tecnicos})

@login_required
def tecnico_create(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Técnico cadastrado com sucesso!')
            return redirect('tecnico_list')
    else:
        form = TecnicoForm()
    return render(request, 'sgo_app/tecnico_form.html', {'form': form, 'title': 'Novo Técnico'})

@login_required
def tecnico_edit(request, pk):
    tecnico = get_object_or_404(Tecnico, id_tecnico=pk)
    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Técnico atualizado com sucesso!')
            return redirect('tecnico_list')
    else:
        form = TecnicoForm(instance=tecnico)
    return render(request, 'sgo_app/tecnico_form.html', {'form': form, 'title': 'Editar Técnico'})

@login_required
def tecnico_delete(request, pk):
    tecnico = get_object_or_404(Tecnico, id_tecnico=pk)
    if request.method == 'POST':
        tecnico.delete()
        messages.success(request, 'Técnico removido com sucesso!')
        return redirect('tecnico_list')
    return render(request, 'sgo_app/delete_confirm.html', {'object': tecnico, 'object_name': 'Técnico'})

# --- Equipamentos ---
@login_required
def equipamento_list(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'sgo_app/equipamento_list.html', {'equipamentos': equipamentos})

@login_required
def equipamento_create(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm()
    return render(request, 'sgo_app/equipamento_form.html', {'form': form, 'title': 'Novo Equipamento'})

@login_required
def equipamento_edit(request, pk):
    equipamento = get_object_or_404(Equipamento, id_equipamento=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('equipamento_list')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'sgo_app/equipamento_form.html', {'form': form, 'title': 'Editar Equipamento'})

@login_required
def equipamento_delete(request, pk):
    equipamento = get_object_or_404(Equipamento, id_equipamento=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento removido com sucesso!')
        return redirect('equipamento_list')
    return render(request, 'sgo_app/delete_confirm.html', {'object': equipamento, 'object_name': 'Equipamento'})

# --- Reparos ---
@login_required
def reparo_list(request):
    reparos = Reparo.objects.all()
    return render(request, 'sgo_app/reparo_list.html', {'reparos': reparos})

@login_required
def reparo_create(request):
    if request.method == 'POST':
        form = ReparoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reparo cadastrado com sucesso!')
            return redirect('reparo_list')
    else:
        form = ReparoForm()
    return render(request, 'sgo_app/reparo_form.html', {'form': form, 'title': 'Novo Reparo'})

@login_required
def reparo_edit(request, pk):
    reparo = get_object_or_404(Reparo, id_reparo=pk)
    if request.method == 'POST':
        form = ReparoForm(request.POST, instance=reparo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reparo atualizado com sucesso!')
            return redirect('reparo_list')
    else:
        form = ReparoForm(instance=reparo)
    return render(request, 'sgo_app/reparo_form.html', {'form': form, 'title': 'Editar Reparo'})

@login_required
def reparo_delete(request, pk):
    reparo = get_object_or_404(Reparo, id_reparo=pk)
    if request.method == 'POST':
        reparo.delete()
        messages.success(request, 'Reparo removido com sucesso!')
        return redirect('reparo_list')
    return render(request, 'sgo_app/delete_confirm.html', {'object': reparo, 'object_name': 'Reparo'})

# --- Relatório em PDF ---
@login_required
def gerar_relatorio_pdf(request, reparo_id):
    reparo = get_object_or_404(Reparo, id_reparo=reparo_id)
    
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
        from io import BytesIO
        from datetime import datetime
        
        # Memória para o arquivo PDF
        buffer = BytesIO()
        
        # Documento ReportLab (página A4)
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
        
        # Estilos de parágrafo
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#334155')
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            textColor=colors.HexColor('#334155')
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6
        )
        
        # Conteúdo do relatório (lista de fluxo)
        story = []
        
        # Cabeçalho
        story.append(Paragraph("RELATÓRIO DE REPARO", title_style))
        story.append(Paragraph("SGO — Sistema de Gestão de Oficina", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Dados do reparo
        story.append(Paragraph("INFORMAÇÕES DO REPARO", heading_style))
        
        reparo_data = [
            ['Código do reparo:', str(reparo.id_reparo)],
            ['Data de Entrada:', reparo.data_entrada.strftime('%d/%m/%Y')],
            ['Data de Saída:', reparo.data_saida.strftime('%d/%m/%Y') if reparo.data_saida else 'Em andamento'],
            ['Técnico Responsável:', reparo.id_tecnico.nome],
        ]
        
        reparo_table = Table(reparo_data, colWidths=[2*inch, 4*inch])
        reparo_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8f9fa')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(reparo_table)
        story.append(Spacer(1, 20))
        
        # Dados do equipamento e do cliente
        story.append(Paragraph("INFORMAÇÕES DO EQUIPAMENTO", heading_style))
        
        equipamento_data = [
            ['Cliente:', reparo.id_equipamento.id_cliente.nome],
            ['Telefone:', reparo.id_equipamento.id_cliente.telefone],
            ['Tipo:', reparo.id_equipamento.get_tipo_display()],
            ['Marca:', reparo.id_equipamento.get_marca_display()],
            ['Modelo:', reparo.id_equipamento.modelo],
            ['Número de série:', reparo.id_equipamento.numero_serial],
            ['Endereço:', reparo.id_equipamento.id_cliente.endereco],
        ]
        
        equipamento_table = Table(equipamento_data, colWidths=[2*inch, 4*inch])
        equipamento_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8f9fa')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(equipamento_table)
        story.append(Spacer(1, 20))
        
        # Defeito relatado
        story.append(Paragraph("DESCRIÇÃO DO DEFEITO", heading_style))
        story.append(Paragraph(reparo.descricao_defeito, normal_style))
        story.append(Spacer(1, 15))
        
        # Serviço realizado
        story.append(Paragraph("DESCRIÇÃO DO REPARO", heading_style))
        story.append(Paragraph(reparo.descricao_reparo, normal_style))
        story.append(Spacer(1, 15))
        
        # Peças substituídas
        if reparo.pecas_substituidas:
            story.append(Paragraph("PEÇAS SUBSTITUÍDAS", heading_style))
            story.append(Paragraph(reparo.pecas_substituidas, normal_style))
            story.append(Spacer(1, 15))
        
        # Valor do reparo
        story.append(Paragraph("CUSTO TOTAL DO REPARO", heading_style))
        custo_style = ParagraphStyle(
            'CustoStyle',
            parent=styles['Normal'],
            fontSize=16,
            textColor=colors.HexColor('#2e7d32'),
            alignment=TA_CENTER
        )
        story.append(Paragraph(f"R$ {reparo.custo_reparo:.2f}", custo_style))
        story.append(Spacer(1, 30))
        
        # Data e hora de geração
        story.append(Paragraph(f"Relatório gerado em {datetime.now().strftime('%d/%m/%Y às %H:%M')}", 
                              ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, alignment=TA_CENTER)))
        
        # Monta o PDF no buffer
        doc.build(story)
        
        # Resposta HTTP com anexo
        buffer.seek(0)
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="relatorio_reparo_{reparo_id}.pdf"'
        
        return response
        
    except Exception:
        # Se o PDF falhar, exibe página HTML de contingência
        return render(request, 'sgo_app/relatorio_pdf.html', {'reparo': reparo})

def about(request):
    return render(request, 'sgo_app/about.html')
