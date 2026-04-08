rom django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, Sum
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

@login_required
def dashboard(request):
    from .models import Equipamento, Reparo
    
    # Equipamentos por tipo
    tipos_qs = Equipamento.objects.values('tipo').annotate(total=Count('id_equipamento'))
    tipo_choices = dict(Equipamento.TYPE_CHOICES)
    tipos_labels = [tipo_choices.get(item['tipo'], item['tipo']) for item in tipos_qs]
    tipos_data = [item['total'] for item in tipos_qs]

    # Equipamentos por marca
    marcas_qs = Equipamento.objects.values('marca').annotate(total=Count('id_equipamento'))
    marca_choices = dict(Equipamento.BRAND_CHOICES)
    marcas_labels = [marca_choices.get(item['marca'], item['marca']) for item in marcas_qs]
    marcas_data = [item['total'] for item in marcas_qs]

    # Faturamento total
    faturamento_aggr = Reparo.objects.aggregate(total=Sum('custo_reparo'))
    faturamento = faturamento_aggr['total'] or 0.00
    
    context = {
        'tipos_labels': json.dumps(tipos_labels),
        'tipos_data': json.dumps(tipos_data),
        'marcas_labels': json.dumps(marcas_labels),
        'marcas_data': json.dumps(marcas_data),
        'faturamento_total': faturamento,
    }
    return render(request, 'sgo_app/dashboard.html', context)

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
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch, cm
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
        from io import BytesIO
        from datetime import datetime
        
        # Memória para o arquivo PDF
        buffer = BytesIO()
        
        # Documento ReportLab (página A4) com margens reduzidas para mais aproveitamento de espaço
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
        
        # Estilos customizados da nova identidade visual
        styles = getSampleStyleSheet()
        
        primary_color = colors.HexColor('#1E3A8A')    # Azul escuro elegante
        secondary_color = colors.HexColor('#3B82F6')  # Azul primary do tailwind
        bg_light = colors.HexColor('#F8FAFC')
        text_dark = colors.HexColor('#1E293B')
        text_muted = colors.HexColor('#64748B')
        
        title_style = ParagraphStyle(
            'PremiumTitle',
            parent=styles['Heading1'],
            fontName='Helvetica-Bold',
            fontSize=24,
            spaceAfter=10,
            alignment=TA_CENTER,
            textColor=primary_color
        )
        
        subtitle_style = ParagraphStyle(
            'PremiumSubtitle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=11,
            alignment=TA_CENTER,
            textColor=text_muted,
            spaceAfter=30
        )
        
        section_style = ParagraphStyle(
            'SectionTitle',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=14,
            spaceBefore=15,
            spaceAfter=10,
            textColor=primary_color,
            borderPadding=(0, 0, 4, 0)
        )
        
        normal_style = ParagraphStyle(
            'PremiumNormal',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=11,
            textColor=text_dark,
            leading=14,
            alignment=TA_JUSTIFY,
            spaceAfter=8
        )
        
        bold_style = ParagraphStyle(
            'PremiumBold',
            parent=normal_style,
            fontName='Helvetica-Bold'
        )
        
        story = []
        
        # Cabeçalho - Título
        story.append(Paragraph("LAUDO TÉCNICO DE REPARO", title_style))
        story.append(Paragraph("SGO — Sistema Avançado de Gestão de Oficina", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=2, color=primary_color, spaceAfter=20))
        
        # --- Seção 1: Dados Gerais ---
        story.append(Paragraph("1. DADOS DO REPARO", section_style))
        dados_reparo = [
            [Paragraph("<b>OS:</b>", normal_style), Paragraph(f"#{reparo.id_reparo:05d}", normal_style),
             Paragraph("<b>Técnico:</b>", normal_style), Paragraph(f"{reparo.id_tecnico.nome}", normal_style)],
            [Paragraph("<b>Entrada:</b>", normal_style), Paragraph(f"{reparo.data_entrada.strftime('%d/%m/%Y')}", normal_style),
             Paragraph("<b>Saída:</b>", normal_style), Paragraph(f"{reparo.data_saida.strftime('%d/%m/%Y') if reparo.data_saida else 'Em Andamento'}", normal_style)]
        ]
        
        t1 = Table(dados_reparo, colWidths=[1*inch, 2.7*inch, 1*inch, 2.7*inch])
        t1.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_light),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.white),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#E2E8F0')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t1)
        story.append(Spacer(1, 5))
        
        # --- Seção 2: Dados do Equipamento e Cliente ---
        story.append(Paragraph("2. INFORMAÇÕES DO CLIENTE E EQUIPAMENTO", section_style))
        
        cliente_endereco = reparo.id_equipamento.id_cliente.endereco
        cep_cliente = reparo.id_equipamento.id_cliente.cep
        endereco_fmt = f"{cliente_endereco}" + (f" - CEP: {cep_cliente}" if cep_cliente else "")
        
        dados_equip = [
            [Paragraph("<b>Cliente:</b>", normal_style), Paragraph(f"{reparo.id_equipamento.id_cliente.nome}", normal_style)],
            [Paragraph("<b>Contato:</b>", normal_style), Paragraph(f"{reparo.id_equipamento.id_cliente.telefone}", normal_style)],
            [Paragraph("<b>Endereço:</b>", normal_style), Paragraph(endereco_fmt, normal_style)],
            [Paragraph("<b>Aparelho:</b>", normal_style), Paragraph(f"{reparo.id_equipamento.get_tipo_display()} {reparo.id_equipamento.get_marca_display()} {reparo.id_equipamento.modelo}", normal_style)],
            [Paragraph("<b>Nº de Série:</b>", normal_style), Paragraph(f"{reparo.id_equipamento.numero_serial}", normal_style)],
        ]
        
        t2 = Table(dados_equip, colWidths=[1.8*inch, 5.6*inch])
        t2.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (0,-1), bg_light),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(t2)
        story.append(Spacer(1, 5))
        
        # --- Seção 3: Parecer Técnico ---
        story.append(Paragraph("3. DIAGNÓSTICO E SERVIÇOS", section_style))
        
        story.append(Paragraph("<b>Defeito Relatado:</b>", bold_style))
        story.append(Paragraph(reparo.descricao_defeito, normal_style))
        story.append(Spacer(1, 5))
        
        story.append(Paragraph("<b>Serviço Executado:</b>", bold_style))
        story.append(Paragraph(reparo.descricao_reparo, normal_style))
        story.append(Spacer(1, 5))
        
        if reparo.pecas_substituidas:
            story.append(Paragraph("<b>Peças Trocadas:</b>", bold_style))
            story.append(Paragraph(reparo.pecas_substituidas, normal_style))
            story.append(Spacer(1, 5))
            
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E2E8F0'), spaceBefore=10, spaceAfter=15))
        
        # --- Seção 4: Valores ---
        story.append(Spacer(1, 15))
        valor_style = ParagraphStyle(
            'ValorStyle',
            parent=styles['Heading2'],
            fontName='Helvetica-Bold',
            fontSize=16,
            textColor=colors.HexColor('#047857'),
            alignment=TA_RIGHT
        )
        
        dados_valor = [
            [Paragraph("CUSTO TOTAL DO REPARO:", ParagraphStyle('Sub', parent=valor_style, textColor=text_dark, fontSize=12, alignment=TA_RIGHT)), 
             Paragraph(f"R$ {reparo.custo_reparo:,.2f}".replace('.',','), valor_style)]
        ]
        t3 = Table(dados_valor, colWidths=[5.4*inch, 2*inch])
        t3.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#D1FAE5')), # Verde bem clarinho
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('TOPPADDING', (0,0), (-1,-1), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#34D399')),
        ]))
        story.append(t3)
        story.append(Spacer(1, 40))
        
        # Assinatura
        sig_data = [
            [HRFlowable(width="80%", thickness=1, color=colors.black)],
            [Paragraph("Assinatura do Cliente", ParagraphStyle('sig', parent=styles['Normal'], alignment=TA_CENTER, fontSize=9))]
        ]
        t_sig = Table(sig_data, colWidths=[4*inch])
        t_sig.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER')]))
        story.append(t_sig)
        
        # Rodapé com data
        story.append(Spacer(1, 15))
        rodape = Paragraph(f"Emissão local: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}", 
                           ParagraphStyle('Rodape', parent=styles['Normal'], fontSize=8, textColor=text_muted, alignment=TA_CENTER))
        story.append(rodape)
        
        # Build do Doc
        doc.build(story)
        
        buffer.seek(0)
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="os_{reparo_id:05d}_SGO.pdf"'
        
        return response
        
    except Exception:
        # Se o PDF falhar, exibe página HTML de contingência
        return render(request, 'sgo_app/relatorio_pdf.html', {'reparo': reparo})

def about(request):
    return render(request, 'sgo_app/about.html')
