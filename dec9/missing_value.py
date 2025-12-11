def missing_value(m_list,c_list):
    num=0
    for i in range(len(m_list)):
        if m_list[i] not in  c_list:
            num=m_list[i]
    print(num)
missing_value([10,20,30,40,50],[10,20,40,50])