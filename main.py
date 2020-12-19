"""Arquivo principal que será interpretado pelo interpretador."""
from datetime import datetime, time as datetime_time, timedelta



def main():
    global j

    tempo1 = input("Digite o horário de início\n")
    tempo2 = input("Digite o horário de conclusão\n")


    s = datetime.strptime(tempo1,  '%H:%M:%S')
    e = datetime.strptime(tempo2, '%H:%M:%S')
    diferenca_tempo(s,e)

    
    print(j)
    
        
 

def diferenca_tempo(comeco, fim):
    global j

    if isinstance(comeco, datetime_time): 
        comeco, fim = [datetime.combine(datetime.min, t) for t in [comeco, fim]]
    if comeco <= fim: 
        j = fim - comeco
    else: 
        fim += timedelta(1) 
        j = fim - comeco



if __name__ == '__main__':
    main()
