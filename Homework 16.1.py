def km_in_h(km):
    con_ratio = 0.2777777777777778
    m_in_sec = km * con_ratio
    print ("The speed value in m/sec:\n", m_in_sec)
if __name__ == '__main__':
    km_in_h(int(input("Input speed value in km:\n")))

