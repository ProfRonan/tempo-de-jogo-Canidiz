# Especificação do exercício

Escrever um programa que lê o instante do início e do término do jogo, ambos subdivididos em
2 valores distintos, a saber: horas e minutos. Calcular e escrever a duração do jogo, também
em horas e minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas
e que o jogo pode iniciar em um dia e terminar no dia seguinte.

Escreva um script que leia dois horários no seguinte formato `HH:MM:SS` com um relógio de `24h`.
Calcule a duração do intervalo considerando um máximo de `24h`.

A saída do programa deve ser dada pelo seguinte formato: `HH:MM:SS` aonde esse formato é a quantidade de tempo do intervalo e deve ser utilizada apenas uma vez a função `print` para imprimir a saída.

## Exemplos

Entrada 1:

```markdown
08:30:00
12:45:30
```

Saída 1:

```markdown
04:15:30
```

Entrada 2:

```markdown
18:43:50
21:17:45
```

Saída 2:

```markdown
02:33:55
```

Entrada 3:

```markdown
22:17:16
21:16:15
```

Saída 3:

```markdown
22:58:59
```

Entrada 4:

```markdown
00:00:00
23:59:59
```

Saída 4:

```markdown
23:59:59
```

Entrada 5:

```markdown
00:00:00
00:00:00
```

Saída 5:

```markdown
24:00:00
```
