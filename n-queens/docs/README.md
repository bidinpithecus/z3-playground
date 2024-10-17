# Solucionador de N-Rainhas

Este script resolve o problema das N-Rainhas usando um solver SAT. O problema das N-Rainhas consiste em colocar `N` rainhas em um tabuleiro de xadrez `N x N` de forma que nenhuma rainha ameace outra. Isso significa que duas rainhas não podem estar na mesma linha, coluna ou diagonal.

## Requisitos

- Python 3
- Z3 SMT solver (para bindings Python)

Certifique-se de ter o Z3 solver instalado. Se não estiver instalado, você pode instalá-lo usando:

```bash
pip install z3-solver
```

## Uso

Para executar o script, utilize o seguinte comando:

```bash
python src/main.py <número de rainhas>
```

Substitua `<número de rainhas>` pelo número de rainhas.

### Exemplo

```bash
python src/main.py 4
```

Este comando tenta resolver o problema das 4-Rainhas.

## Saída

A solução, se encontrada, é exibida como uma grade `N x N`. Cada linha representa uma linha no tabuleiro de xadrez, com `Q` indicando a posição de uma rainha e `·` indicando uma célula vazia.

### Exemplo de Saída

Para o problema das 4-Rainhas, a saída pode ser:

```smt
sat
· · Q ·
Q · · ·
· · · Q
· Q · ·
```

Isso representa uma solução válida onde nenhuma rainha ameaça outra.
