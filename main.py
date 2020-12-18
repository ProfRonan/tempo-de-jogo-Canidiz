"""Arquivo principal que será interpretado pelo interpretador."""
from datetime import datetime, time as datetime_time, timedelta


def main():
    tempo1 = input("Digite o horário de início\n")
    tempo2 = input("Digite o horário de conclusão\n")

    for time_range in [tempo1,tempo2]: 

        s = datetime.strptime(tempo1, '%H:%M:%S')
        e = datetime.strptime(tempo2, '%H:%M:%S')

        print(diferenca_tempo(s, e))
        assert diferenca_tempo(s, e) == diferenca_tempo(s.time(), e.time())
 

def diferenca_tempo(comeco, fim):
    if isinstance(comeco, datetime_time): 
        assert isinstance(fim, datetime_time)
        comeco, fim = [datetime.combine(datetime.min, t) for t in [comeco, fim]]
    if comeco <= fim: 
        return fim - comeco
    else: 
        fim += timedelta(1) 
        assert fim > comeco
        return fim - comeco



if __name__ == '__main__':
    main()
