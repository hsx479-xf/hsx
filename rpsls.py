#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2021/5/30
"""

import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(player_choice):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if player_choice=="ʯͷ":
	    number=0
    elif player_choice=="ʷ����":
	    number=1
    elif player_choice=="ֽ":
	    number=2
    elif player_choice=="����":
	    number=3
    elif player_choice=="����":
	    number=4
    return number 
	   	
	
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


   


def number_to_name(c_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if c_number==0:
	    name="ʯͷ"
    elif c_number==1:
	    name="ʷ����"
    elif c_number==2:
	    name="ֽ"
    elif c_number==3:
	    name="����"
    elif c_number==4:
	    name="����"
    return name

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    p_number=name_to_number(player_choice)
    print("����ѡ���ǣ�",player_choice)
    c_number=random.randrange(0,5)
    comp_number=number_to_name(c_number)
    print("�������ѡ���ǣ�",comp_number)

    if c_number==p_number:
	    print("���ͼ��������һ����")
    elif (c_number==0 and p_number==4) or (c_number==0 and p_number==3):
	    print("�����Ӯ��")
    elif (c_number==1 and p_number==4) or (c_number==1 and p_number==0):
        print("�����Ӯ��")
    elif (c_number==2 and p_number==0) or (c_number==2 and p_number==1):
	    print("�����Ӯ��")
    elif (c_number==3 and p_number==1) or (c_number==3 and p_number==2):
	     print("�����Ӯ��")
    elif (c_number==4 and p_number==2) or (c_number==4 and p_number==3):  
	    print("�����Ӯ��")
    elif (p_number==0 and c_number==4) or (p_number==0 and c_number==3):
	    print("��Ӯ��")
    elif (p_number==1 and c_number==4) or (p_number==1 and c_number==0):
        print("��Ӯ��")
    elif (p_number==2 and c_number==0) or (p_number==2 and c_number==1):
	    print("��Ӯ��")
    elif (p_number==3 and c_number==1) or (p_number==3 and c_number==2):
	    print("��Ӯ��")
    elif (p_number==4 and c_number==2) or (p_number==4 and c_number==3):
	    print("��Ӯ��")



    
    


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

   


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)



