'''Fluxo de leitura dos AC's e comunicação com a API'''
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import time
import numpy as np
import json
import urllib3
from datetime import datetime
from register import *


#Lê ficheiro .json com ip's e endereços modbus
with open('address.json','r') as json_file:
    address = json.load(json_file)

#Salva os ip em uma lista
ip = []
for i in address:
    ip.append(i)
#print(ip)

#salva os endereços em uma lista
add = []
for i in address.values():
    add.append(i)
#print(add)



#Função para conectar a API
def connect(temp, ip, address, mode, fan, setPoint):
    http = urllib3.PoolManager()
    url = "https://certigarve.pt/mti/plan1/v7/" + str(temp) + "/" + ip.replace(".","-") + "/" + address + "/" + mode + "/" + fan + "/" + setPoint +"/ModbusAC/"
    res = http.request('GET',url)
    return res.data.decode("utf-8")
    ''' Plataform return
        Mode | LDR | FAN | SetPoint | Priority
        '''


#Função para tomada de decisão
def decision(dados, resposta):
#---- Quando a plataforma tem prioridade
    if resposta[4] == 1: 
        if resposta[0] == 0: #Desligado
            ac.write_single_register(regOn,0)
            return 'Desligado'
        elif resposta[0] == 1: #Quente
            if resposta[1] < 15: #Modo Quiet
                ac.write_single_register(regOn,1) #Liga ac
                ac.write_single_register(regMode,2) #Quente
                ac.write_single_register(regFan,2) #Ventilação min
                ac.write_single_register(regSetPoint,300) #Set point 30C
                return 'Mode: Hot - Quiet'
            else:
                ac.write_single_register(regOn,1) #Liga ac
                ac.write_single_register(regMode,2) #Quente
                ac.write_single_register(regFan,1) #Ventilação medium
                ac.write_single_register(regSetPoint,300) #Set point 30C
                return 'Mode: Hot'
        elif resposta[0] == 2: #Modo Frio
            if resposta[1] < 15: #Modo Quiet
                ac.write_single_register(regOn,1) #Liga ac
                ac.write_single_register(regMode,1) #Frio
                ac.write_single_register(regFan,2) #Ventilação min
                ac.write_single_register(regSetPoint,180) #Set point 18C
                return 'Mode: Cool - Quiet'
            else:
                ac.write_single_register(regOn,1) #Liga ac
                ac.write_single_register(regMode,1) #Frio
                ac.write_single_register(regFan,1) #Ventilação medium
                ac.write_single_register(regSetPoint,180) #Set point 18C
                return 'Mode: Cool'
        if dados[3] != resposta[2]: #Verifica se a Fan é igual ao que está na plataforma
            ac.write_single_coil(regFan,resposta[2])

        if dados[2] != resposta[3]: #Verifica se o setPoint é igual ao que está na plataforma
            ac.write_single_register(regSetPoint,resposta[3])

#------ Quando o controle tem prioridade
    elif resposta[4] == 0:
        return 'Controle com a prioridade'



#Função para Loop de leituras e comunicações
def routineLoop ():
    global ac, dados
    
    for i in ip: #Entra na lista de ip's
        for x in add[ip.index(i)]: #entra na lista de endereços
            ac = ModbusClient(host= i,auto_open=True, unit_id=x)
            readTemp = ac.read_input_registers(0) #Leitura da temperatura lida pelo ac
            dados = ac.read_holding_registers(2,26)
            if bool(readTemp) == False: #Se o valor for falso pula para o próximo ac
                break
            if dados[0] == 0: dados[3] = 0
            resposta = connect(int(readTemp[0]),str(i),str(x),str(dados[1]),str(dados[3]),str(dados[2])) #Envia os dados para API e recebe a resposta
            resposta = json.loads(resposta)
            decisao = decision(dados, resposta)
            d = datetime.now()
            print(decisao + " | " + str(d.hour) + ":" + str(d.minute) + ":" + str(d.second))
            ac.close()
            


while True:

    routineLoop()






    
    
    

