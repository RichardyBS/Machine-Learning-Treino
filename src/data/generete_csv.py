import pandas as pd
import numpy as np
import os

# Definir os dados
data = {
    'Descricao_Problema': [
        'Carro não liga', 
        'Ruído estranho ao frear', 
        'Aquecimento do motor após 15 minutos', 
        'Perda de potência em subidas', 
        'Vibração no volante', 
        'Direção dura', 
        'Fumaça saindo do escapamento', 
        'Cheiro de gasolina dentro do carro', 
        'Luz do óleo acesa', 
        'Freios não respondem', 
        'Carro engasga', 
        'Perda de eficiência de combustível', 
        'Problemas ao engatar marchas', 
        'Barulho de arranhão ao acelerar', 
        'Luz do motor acesa', 
        'Acelerador não responde', 
        'Problemas na suspensão', 
        'Ruído no motor', 
        'Carro puxa para um lado', 
        'Desempenho irregular do motor', 
        'Carro treme ao acelerar', 
        'Problemas no ar condicionado', 
        'Luzes do painel piscando', 
        'Carro não acelera', 
        'Rachaduras no para-brisa', 
        'Fugas de óleo', 
        'Problemas com a transmissão', 
        'Aumento no consumo de combustível', 
        'Carro faz barulho ao dar partida', 
        'Escapamento ruidoso', 
        'Problemas na bomba de combustível', 
        'Carro derrapa em curvas', 
        'Falha no sistema de injeção', 
        'Luz de bateria acesa', 
        'Vazamento de líquido de arrefecimento', 
        'Carro não responde ao freio', 
        'Acelerador travado', 
        'Problemas com a embreagem', 
        'Suspensão estourada', 
        'Carro puxa ao acelerar', 
        'Ruído de batida ao dirigir', 
        'Problemas no sistema de ignição', 
        'Aquecimento do óleo', 
        'Carro não mantém a marcha lenta', 
        'Carro vibra ao parar', 
        'Problemas no alternador', 
        'Luzes de freio não acendem', 
        'Barulho de estalo ao virar', 
        'Problemas com o sistema elétrico', 
        'Carro não desliga', 
        'Ruído metálico ao dirigir', 
        'Carro derrapando em chuva', 
        'Problemas na válvula de controle', 
        'Carro não responde ao pedal', 
        'Fumaça azul do escapamento', 
        'Problemas no catalisador', 
        'Ruído no eixo', 
        'Perda de potência ao subir', 
        'Carro vibra ao dirigir', 
        'Carro faz barulho ao desacelerar', 
        'Luz de ABS acesa', 
        'Problemas com o sistema de exaustão', 
        'Carro engasga ao acelerar', 
        'Problemas na caixa de direção', 
        'Ruído de rolamento', 
        'Carro não acelera corretamente', 
        'Carro treme ao soltar a embreagem', 
        'Luz de airbag acesa', 
        'Problemas no comando de válvulas', 
        'Carro não arranca com facilidade', 
        'Cheiro de queimado no carro', 
        'Barulho de solavancos', 
        'Carro faz barulho ao virar a chave', 
        'Problemas com o sistema de refrigeração', 
        'Carro não mantém a velocidade', 
        'Luzes de alerta acesas', 
        'Carro não retoma a aceleração', 
        'Problemas com o filtro de ar', 
        'Carro vibra ao ligar', 
        'Barulho de explosão no motor', 
        'Problemas no sensor de oxigênio', 
        'Carro não para completamente', 
        'Ruído ao girar a chave', 
        'Problemas com o sistema de combustível', 
        'Carro não responde ao volante', 
        'Fumaça preta do escapamento', 
        'Carro não acelera como deveria', 
        'Problemas com o motor de arranque', 
        'Barulho de engrenagem', 
        'Carro não segura a marcha', 
        'Problemas na bomba d\'água', 
        'Carro faz barulho ao virar', 
        'Luz de injeção acesa', 
        'Problemas com o sistema de transmissão'
    ],
    'pecas': [
    'Bateria', 
    'Pastilhas de freio', 
    'Radiador', 
    'Motor', 
    'Balanceamento das rodas', 
    'Coluna de direção', 
    'Sistema de escape', 
    'Sistema de combustível', 
    'Óleo do motor', 
    'Sistema de freios', 
    'Sistema de injeção', 
    'Filtro de combustível', 
    'Sistema de escapamento', 
    'Sistema de ignição', 
    'Suspensão', 
    'Motor', 
    'Alinhamento das rodas', 
    'Sistema de injeção', 
    'Sistema de suspensão', 
    'Ar condicionado', 
    'Painel de instrumentos', 
    'Sistema de aceleração', 
    'Para-brisa', 
    'Sistema de lubrificação', 
    'Transmissão', 
    'Sistema de combustível', 
    'Sistema de arranque', 
    'Sistema de escape', 
    'Bomba de combustível', 
    'Sistema de suspensão', 
    'Sistema de injeção', 
    'Bateria', 
    'Sistema de arrefecimento', 
    'Sistema de freios', 
    'Acelerador', 
    'Embreagem', 
    'Suspensão', 
    'Sistema de direção', 
    'Sistema de ignição', 
    'Óleo do motor', 
    'Sistema de marcha lenta', 
    'Sistema de suspensão', 
    'Alternador', 
    'Sistema de iluminação', 
    'Sistema de direção', 
    'Sistema elétrico', 
    'Sistema de escape', 
    'Sistema de controle', 
    'Pedal de freio', 
    'Catalisador', 
    'Eixo', 
    'Sistema de potência', 
    'Sistema de vibração', 
    'Sistema de desaceleração', 
    'Sistema de ABS', 
    'Sistema de escape', 
    'Caixa de direção', 
    'Rolamento', 
    'Sistema de aceleração', 
    'Embreagem', 
    'Airbag', 
    'Comando de válvulas', 
    'Sistema de ignição', 
    'Sistema de escape', 
    'Sistema de refrigeração', 
    'Sistema de velocidade', 
    'Sistema de alerta', 
    'Sistema de aceleração', 
    'Filtro de ar', 
    'Sistema de ignição', 
    'Sensor de oxigênio', 
    'Sistema de frenagem', 
    'Sistema de combustível', 
    'Sistema de direção', 
    'Catalisador', 
    'Motor de arranque', 
    'Engrenagem', 
    'Embreagem', 
    'Bomba d\'água', 
    'Sistema de direção', 
    'Sistema de injeção', 
    'Sistema de transmissão', 
    'Sistema de lubrificação', 
    'Freio de estacionamento', 
    'Sistema de climatização', 
    'Mangueira de combustível', 
    'Filtro de óleo', 
    'Sistema de ventilação',
    'Sistema de transmissão automática',
    'Módulo de controle do motor',
    'Sensores de velocidade',       
    'Interruptor de luz',            
    'Sistema de ignição digital',
    'Válvula termostática'
    ],
    'Sintomas': [
        'Carro não liga', 
        'Ruído ao frear', 
        'Motor superaquecido', 
        'Falta de potência em subidas', 
        'Vibração ao dirigir', 
        'Dificuldade na direção', 
        'Fumaça no escapamento', 
        'Cheiro de gasolina', 
        'Luz do óleo acesa', 
        'Freios ineficazes', 
        'Engasgos ao acelerar', 
        'Baixo rendimento de combustível', 
        'Dificuldade nas marchas', 
        'Barulho ao acelerar', 
        'Luz do motor acesa', 
        'Acelerador não responde', 
        'Dificuldade na suspensão', 
        'Ruído no motor', 
        'Carro puxa para um lado', 
        'Desempenho instável', 
        'Tremor ao acelerar', 
        'Problemas no ar condicionado', 
        'Luzes piscando', 
        'Carro não acelera', 
        'Rachaduras no vidro', 
        'Vazamentos de óleo', 
        'Problemas na transmissão', 
        'Aumento no consumo de combustível', 
        'Barulho ao iniciar', 
        'Escapamento barulhento', 
        'Problemas na bomba de combustível', 
        'Derrapagem em curvas', 
        'Falha na injeção', 
        'Luz da bateria acesa', 
        'Vazamento de refrigerante', 
        'Problemas com o freio', 
        'Acelerador travado', 
        'Problemas com a embreagem', 
        'Suspensão danificada', 
        'Carro puxa ao acelerar', 
        'Barulho ao dirigir', 
        'Falha no sistema de ignição', 
        'Aquecimento do óleo', 
        'Marcha lenta instável', 
        'Tremores ao parar', 
        'Problemas no alternador', 
        'Luzes de freio não acendem', 
        'Estalos ao virar', 
        'Problemas elétricos', 
        'Carro não desliga', 
        'Barulho metálico ao dirigir', 
        'Derrapagem na chuva', 
        'Problemas na válvula', 
        'Acelerador não responde', 
        'Fumaça azul', 
        'Problemas no catalisador', 
        'Ruído no eixo', 
        'Perda de potência em subidas', 
        'Tremores ao dirigir', 
        'Barulho ao desacelerar', 
        'Luz de ABS acesa', 
        'Problemas no exaustor', 
        'Engasgos ao acelerar', 
        'Problemas na direção', 
        'Ruído de rolamento', 
        'Desempenho irregular', 
        'Tremores ao soltar a embreagem', 
        'Luz do airbag acesa', 
        'Problemas nas válvulas', 
        'Dificuldade para arrancar', 
        'Cheiro de queimado', 
        'Barulho de solavancos', 
        'Barulho ao virar a chave', 
        'Problemas no sistema de refrigeração', 
        'Velocidade instável', 
        'Luzes de alerta acesas', 
        'Acelerador não responde', 
        'Problemas no filtro de ar', 
        'Tremores ao ligar', 
        'Barulho de explosão', 
        'Falha no sensor de oxigênio', 
        'Carro não para completamente', 
        'Barulho ao girar a chave', 
        'Problemas no sistema de combustível', 
        'Volante não responde', 
        'Fumaça preta', 
        'Desempenho irregular', 
        'Problemas no motor de arranque', 
        'Barulho de engrenagem', 
        'Marcha não segura', 
        'Problemas na bomba d\'água', 
        'Barulho ao virar', 
        'Luz de injeção acesa', 
        'Problemas na transmissão'
    ],
    'Solucoes': [
    'Substituir a bateria',  # Carro não liga
    'Trocar as pastilhas de freio',  # Ruído ao frear
    'Verificar e substituir o radiador',  # Motor superaquecido
    'Substituir o filtro de combustível',  # Falta de potência em subidas
    'Trocar o pivô de suspensão',  # Vibração ao dirigir
    'Verificar e substituir a caixa de direção',  # Dificuldade na direção
    'Reparar o sistema de escape',  # Fumaça no escapamento
    'Trocar a bomba de combustível',  # Cheiro de gasolina
    'Substituir o sensor de óleo',  # Luz do óleo acesa
    'Trocar os discos de freio',  # Freios ineficazes
    'Verificar e substituir os injetores',  # Engasgos ao acelerar
    'Substituir o filtro de ar',  # Baixo rendimento de combustível
    'Verificar e ajustar o câmbio',  # Dificuldade nas marchas
    'Trocar o rolamento de roda',  # Barulho ao acelerar
    'Substituir as velas de ignição',  # Luz do motor acesa
    'Trocar o acelerador',  # Acelerador não responde
    'Trocar os amortecedores',  # Dificuldade na suspensão
    'Substituir a correia dentada',  # Ruído no motor
    'Trocar o kit de polias',  # Carro puxa para um lado
    'Verificar e substituir a central de injeção',  # Desempenho instável
    'Verificar e substituir o motor',  # Tremor ao acelerar
    'Verificar e ajustar o ar condicionado',  # Problemas no ar condicionado
    'Trocar o painel de luzes',  # Luzes piscando
    'Substituir a válvula termostática',  # Carro não acelera
    'Trocar o vidro',  # Rachaduras no vidro
    'Substituir as juntas do motor',  # Vazamentos de óleo
    'Verificar e substituir o sistema de transmissão',  # Problemas na transmissão
    'Verificar e ajustar a injeção',  # Aumento no consumo de combustível
    'Trocar o motor de partida',  # Barulho ao iniciar
    'Reparar o sistema de exaustão',  # Escapamento barulhento
    'Substituir a bomba de combustível',  # Problemas na bomba de combustível
    'Verificar e ajustar a suspensão',  # Derrapagem em curvas
    'Substituir o filtro de combustível',  # Falha na injeção
    'Trocar o alternador',  # Luz da bateria acesa
    'Substituir a bomba d\'água',  # Vazamento de refrigerante
    'Verificar e substituir o cilindro de freio',  # Problemas com o freio
    'Trocar o acelerador',  # Acelerador travado
    'Substituir o disco de embreagem',  # Problemas com a embreagem
    'Trocar os amortecedores',  # Suspensão danificada
    'Verificar e substituir os pivôs de direção',  # Carro puxa ao acelerar
    'Trocar o rolamento de roda',  # Barulho ao dirigir
    'Verificar e substituir o sistema de ignição',  # Falha no sistema de ignição
    'Substituir o radiador',  # Aquecimento do óleo
    'Trocar a válvula de controle de marcha lenta',  # Marcha lenta instável
    'Trocar o disco de freio',  # Tremores ao parar
    'Verificar e substituir o alternador',  # Problemas no alternador
    'Substituir as lâmpadas de freio',  # Luzes de freio não acendem
    'Trocar a junta homocinética',  # Estalos ao virar
    'Verificar e ajustar o sistema elétrico',  # Problemas elétricos
    'Substituir o motor de partida',  # Carro não desliga
    'Trocar o sistema de exaustão',  # Barulho metálico ao dirigir
    'Substituir os pneus',  # Derrapagem na chuva
    'Trocar a válvula termostática',  # Problemas na válvula
    'Verificar e substituir o acelerador',  # Acelerador não responde
    'Trocar o motor de exaustão',  # Fumaça azul
    'Substituir o catalisador',  # Problemas no catalisador
    'Trocar o rolamento do eixo',  # Ruído no eixo
    'Substituir a bomba de combustível',  # Perda de potência em subidas
    'Verificar e substituir a suspensão',  # Tremores ao dirigir
    'Trocar os amortecedores',  # Barulho ao desacelerar
    'Substituir o sensor de ABS',  # Luz de ABS acesa
    'Verificar e substituir o sistema de exaustão',  # Problemas no exaustor
    'Verificar e substituir os injetores',  # Engasgos ao acelerar
    'Verificar e ajustar a direção',  # Problemas na direção
    'Trocar o rolamento de roda',  # Ruído de rolamento
    'Substituir a correia de alternador',  # Desempenho irregular
    'Verificar e ajustar o sistema de embreagem',  # Tremores ao soltar a embreagem
    'Substituir o sensor de airbag',  # Luz do airbag acesa
    'Trocar as válvulas de controle',  # Problemas nas válvulas
    'Verificar e substituir o sistema de ignição',  # Dificuldade para arrancar
    'Trocar os fios de ignição',  # Cheiro de queimado
    'Substituir os amortecedores',  # Barulho de solavancos
    'Trocar o motor de partida',  # Barulho ao virar a chave
    'Verificar e substituir o radiador',  # Problemas no sistema de refrigeração
    'Trocar o sensor de velocidade',  # Velocidade instável
    'Substituir o painel de luzes',  # Luzes de alerta acesas
    'Trocar o acelerador',  # Acelerador não responde
    'Trocar o filtro de ar',  # Problemas no filtro de ar
    'Verificar e substituir o motor de arranque',  # Tremores ao ligar
    'Trocar a bomba de combustível',  # Barulho de explosão
    'Substituir o sensor de oxigênio',  # Falha no sensor de oxigênio
    'Verificar e substituir o freio de mão',  # Carro não para completamente
    'Trocar o motor de partida',  # Barulho ao girar a chave
    'Verificar e ajustar o sistema de combustível',  # Problemas no sistema de combustível
    'Trocar a caixa de direção',  # Volante não responde
    'Substituir o motor de exaustão',  # Fumaça preta
    'Trocar o filtro de combustível',  # Desempenho irregular
    'Substituir o motor de arranque',  # Problemas no motor de arranque
    'Trocar o sistema de transmissão',  # Barulho de engrenagem
    'Substituir o câmbio automático',  # Marcha não segura
    'Trocar a bomba d\'água',  # Problemas na bomba d\'água
    'Verificar e substituir os pivôs de direção',  # Barulho ao virar
    'Trocar o sensor de injeção',  # Luz de injeção acesa
    'Substituir o sistema de transmissão'  # Problemas na transmissão
]
}

# Verificar o comprimento de cada lista
lengths = {key: len(value) for key, value in data.items()}
print(lengths)

# Criar o DataFrame
df = pd.DataFrame(data)

# Verificar o comprimento das colunas
expected_length = len(df['Descricao_Problema'])
for column in ['pecas', 'Sintomas', 'Solucoes']:
    if len(df[column]) != expected_length:
        # Adiciona NaN para igualar o comprimento
        df[column] = df[column].reindex(range(expected_length), fill_value=np.nan)

print(df.head())

# Salvar os dados em um arquivo CSV
df.to_csv('./dataset.csv', index=False)
print("Arquivo CSV criado com sucesso!")
