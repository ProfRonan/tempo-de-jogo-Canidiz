"""Arquivo principal que será interpretado pelo interpretador."""
import datetime

def main():

    tempo1 = input("Digite o horário de início\n")
    tempo2 = input("Digite o horário de conclusão\n")

    sd = datetime.datetime(1,1,1) # Cria uma data de referência.
    ed = datetime.datetime(1,1,1) # Cria uma data de referência.
    s = datetime.time(*map(int, tempo1.split(':'))) # Cria um tempo baseado na entrada do usuário
    e = datetime.time(*map(int, tempo2.split(':'))) # Cria um tempo baseado na entrada do usuário
    start = datetime.datetime.combine(sd, s) # Junta a data com o tempo.
    end = datetime.datetime.combine(ed, e) # Junta a data com o tempo.
    # É necessário o combine por conta de não poder fazer somas e subtrações utilizando o tempo sem a data embutida.
    if end < start:
        # Caso o usuário tenha colocado um horário final menor que o inicial, então é pra somar um dia na data do fim.
        end = end + datetime.timedelta(days=1)
    interval = end - start
    print(str(interval))


if __name__ == '__main__':
    main()
