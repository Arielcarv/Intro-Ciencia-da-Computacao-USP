def busca_sequencial (seq, x):
    """ (list, float) -> bool """
    for indice in range(len(seq)):
        if seq[indice] == x:
            return True
        return False