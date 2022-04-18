# DESENVOLVEDOR: MATHEUS DINIZ
# OBJETIVO: FACILITAR O ENCERRAMENTO DE CHAMADOS DE MOVIMENTAÇÃO\REMANEJAMENTO


import PySimpleGUI as sg



andares         = ['SS','T','1º','2º','3º','4º']
modeloDesktop   = ['Dell OptiPlex 5050', 'HP Elite 8300', 'Lenovo M93P']
modeloMonitor   = ['Dell P2317H', 'HP E2011P', 'ITAU TEC','Lenovo LS1921WA', 'Lenovo LT2223PWC', 'LG Flatron E2050T']
modeloRamal     = ['15', '20', '80']
modeloScanner   = ['Fujitsu Fi-6230', 'Fujitsu Fi-6770', 'Fujitsu ScanSnap S1500', 'Fujitsu ScanSnap S510', 'Kodak i1150', 'Kodak i2820']
mensagem = "Prezado(a), foi realizado o seguinte remanejamento:\n\n"
i=1
chamadoTicket = ''
origem = ''
andarOrigem = ''
destino = ''
andarDestino = ''


#TELA
def Tela(i):
    sg.theme('Reddit')
    #LAYOUT
    if i==1:
        layout = [[sg.Text('CITSmart', font='bold'),sg.Input(key='chamado', size=(10,0)), sg.Canvas(size=(100,0)),sg.Text(f'{i}º REMANEJAMENTO', font='bold')]]
    if i!=1:
        layout = [[sg.Text('CITSmart:', font='bold'),sg.Text(chamadoTicket, size=(10,0)), sg.Canvas(size=(100,0)),sg.Text(f'{i}º REMANEJAMENTO', font='bold')]]

    layout.append([
        [sg.Canvas(size=(0,5))],
        [sg.Canvas(size=(440,2), background_color='black')],
        [sg.Canvas(size=(0,5))],

        [sg.Text('ORIGEM', size=(9,0)),sg.Input(f'{origem}',key=f'origem{i}', size=(35,0)), sg.Text('ANDAR'),sg.Combo(andares, f'{andarOrigem}', key=f'andarO{i}')],
        [sg.Text('DESTINO', size=(9,0)),sg.Input(f'{destino}',key=f'destino{i}',size=(35,0)), sg.Text('ANDAR'),sg.Combo(andares, f'{andarDestino}',key=f'andarD{i}')],
        [sg.Text('USUÁRIO', size=(9,0)),sg.Input(key=f'responsavel{i}',size=(50,0))],
        [sg.Canvas(size=(0,5))],
        [sg.Text('DESKTOP', size=(9,0)),sg.Combo(modeloDesktop, key=f'desktop{i}', size=(23,0)), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioD{i}', size=(9,0))],
        [sg.Text('MONITOR 1', size=(9,0)),sg.Combo(modeloMonitor, key=f'monitor1{i}', size=(23,0)), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioM1{i}', size=(9,0))],
        [sg.Text('MONITOR 2', size=(9,0)),sg.Combo(modeloMonitor, key=f'monitor2{i}', size=(23,0)), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioM2{i}', size=(9,0))],
        [sg.Text('RAMAL', size=(9,0)), sg.Input(key=f'ramal{i}', size=(4,0)), sg.Text('OPENSTAGE.'), sg.Combo(modeloRamal,key=f'modeloR{i}'), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioR{i}', size=(9,0))],
        [sg.Text('MOU\TEC', size=(9,0)), sg.Checkbox('', default=True, key=f'mouseEteclado{i}')],

        [sg.Canvas(size=(0,2))],
        [sg.Canvas(size=(440,1), background_color='black')],
        [sg.Canvas(size=(0,2))],

        [sg.Text('SCANNER', size=(9,0)),sg.Combo(modeloScanner, key=f'scanner{i}', size=(23,0)), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioS{i}', size=(9,0))],
        [sg.Text('WEBCAM', size=(9,0)), sg.Text('MICROSOFT', size=(22,0)), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioWC{i}', size=(9,0))],
        [sg.Text('HEADSET', size=(9,0)),sg.Text('MICROSOFT', size=(22,0)), sg.Text('PATRIMÔNIO'), sg.Input(key=f'patrimonioH{i}', size=(9,0))],
        [sg.Canvas(size=(0,5))],

        [sg.Button('+', key='+',size=(26,0)), sg.Button('Enviar',key='enviar',button_color='green',size=(26,0))],
    ])
    #JANELA
    return sg.Window(f'Ajuda-ai', layout=layout, finalize=True, icon='icon.ico')



#COLETOR
def Coletor(mensagem):
    #PEGA VALORES DO FORMULARIO DE MOVIMENTAÇÃO PREENCHIDO
    if i==1:
        chamadoTicket = values['chamado']
    origem,andarOrigem = values[f'origem{i}'],values[f'andarO{i}']
    destino,andarDestino = values[f'destino{i}'],values[f'andarD{i}']
    responsavel = values[f'responsavel{i}']

    descktop,patrimonioD = values[f'desktop{i}'],values[f'patrimonioD{i}']
    monitor1,patrimonioM1 = values[f'monitor1{i}'],values[f'patrimonioM1{i}']
    monitor2,patrimonioM2 = values[f'monitor2{i}'],values[f'patrimonioM2{i}']
    ramal,modeloR,patrimonioR = values[f'ramal{i}'],values[f'modeloR{i}'],values[f'patrimonioR{i}']
    mouseEteclado = values[f'mouseEteclado{i}']

    scanner,patrimonioS  = values[f'scanner{i}'], values[f'patrimonioS{i}']
    patrimonioWC = values[f'patrimonioWC{i}']
    patrimonioH = values[f'patrimonioH{i}']

    #MONTAGEM DA MENSAGEM
    if i==1:
        mensagem += f'Chamado(CITSmart): {chamadoTicket}\n\n'
    mensagem += f'{i}º - REMANEJAMENTO\n'
    mensagem += 'Local: Bloco B \n'
    mensagem += f'Origem: {origem} - Andar: {andarOrigem}\n'
    mensagem += f'Destino: {destino} - Andar: {andarDestino}\n'
    if responsavel != '':
        mensagem += f'Responsável: {responsavel}\n'
    if ramal != '':
        mensagem += f'Fone: 2024-{ramal}\n'
    mensagem += f'Equipamentos:\n'
    if patrimonioD != '':
        mensagem += f'  Desktop: {descktop} - PATRIMÔNIO: {patrimonioD}\n'
    if patrimonioM1 != '':
        mensagem += f'  Monitor 1: {monitor1} - PATRIMÔNIO: {patrimonioM1}\n'
    if patrimonioM2 != '':
        mensagem += f'  Monitor 2: {monitor2} - PATRIMÔNIO: {patrimonioM2}\n'
    if patrimonioR != '':
        mensagem += f'  Ramal: {ramal} - Modelo: {modeloR} - PATRIMÔNIO: {patrimonioR}\n'
    if mouseEteclado == True:
        mensagem += '  Mouse e teclado (mouse e teclado não possuem patrimônios).\n'

    if patrimonioS != '':
        mensagem += f'  Scanner: {scanner} - PATRIMÔNIO: {patrimonioS}\n'
    if patrimonioWC != '':
        mensagem += f'  Webcam Microsoft - PATRIMÔNIO: {patrimonioWC}\n'
    if patrimonioH != '':
        mensagem += f'  Headset Microsoft - PATRIMÔNIO: {patrimonioH}\n'
    mensagem += '\n\n'

    #REORNO DA FUNÇÃO COLETOR
    if i==1:
        return mensagem, chamadoTicket, origem, andarOrigem, destino, andarDestino
    else:
        return mensagem, origem, andarOrigem, destino, andarDestino



#ABRE A PRIMEIRA TELA
tela1 = Tela(i)
#EXTRAIR DADOS
while True:
    window, eventos, values = sg.read_all_windows()
    #FECHAR TELA
    if window == tela1 and eventos == sg.WIN_CLOSED:
        break

    #LÓGICA DO ADICIONAR
    if window == tela1 and eventos == '+':
        if i==1:
            mensagem,chamadoTicket, origem, andarOrigem, destino, andarDestino = Coletor(mensagem)
        else:
            mensagem, origem, andarOrigem, destino, andarDestino = Coletor(mensagem)
        #tela1.un_hide()
        tela1.close()
        i=i+1
        tela1 = Tela(i)

    #LÓGICA DO ENVIAR
    if window == tela1 and eventos == 'enviar':
        if i==1:
            mensagem,chamadoTicket, origem, andarOrigem, destino, andarDestino = Coletor(mensagem)
        else:
            mensagem, origem, andarOrigem, destino, andarDestino = Coletor(mensagem)
        mensagem += 'Ao finalizar seu atendimento o sistema enviará uma pesquisa de satisfação sobre o atendimento realizado, ficaremos felizes em saber sua opinião.'

        #FECHA A TELA DE PREENCHIMENTO
        tela1.close()
        #CRIA UM ARQUIVO TXT COM AS INFORMAÇÕES DO REMANEJAMENTO
        with open(f"C:\Ajuda-ai\BKPs\Chamado-{chamadoTicket}-bkp.txt", "w", encoding="utf_8") as backup:
            backup.write(mensagem)
        #ABRE UMA TELA COM TODAS AS INFOMAÇÕES INSERIDAS NOS FORMULARIOS DE REMANEJAMENTO
        sg.popup_scrolled(mensagem, title='Copia-ai', icon='icon.ico')
        break




