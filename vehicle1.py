import pandas as dp
df=dp.read_excel("veh.xlsx")
print(df)
def menu():
    n=0
    while(n!=3):
        print("1.user")
        print("2.admin")
        print("3.exit")
        n=int(input("select a option:"))
        if n==1:
            m=0
            while(m!=4):
                print("1.power")
                print("2.troque")
                print("3.Model_name")
                print("4.exist")
                m=int(input("select an option"))
                if m==1:
                    p=0
                    while(p!=4):
                        print("1..0-4 power")
                        print("2..5-7 power")
                        print("3..8-10 power")
                        print("4..exist")
                        p=int(input("enter a option:"))
                        if p==1:
                            df1=df.loc[(df['power']>0)&(df['power']<4)]
                            print(df1)
                        elif p==2:
                            df2=df.loc[(df['power']>5)&(df['power']<7)]
                            print(df2)
                        elif p==3:
                            df3.df.loc[(df['power']>8)&(df['power']<10)]
                            print(df3)
                        else:
                            print("exist from power")
                elif m==2:
                    t=0
                    while(t!=4):
                        print("1..0-4 torque")
                        print("2..5-7 torque")
                        print("3..8-10 torgue")
                        print("4..exist")
                        t = int(input("enter a option:"))
                        if t==1:
                            dt1=df.loc[(df['torque']>0)&(df['torque']<4)]
                            print(dt1)
                        elif t==2:
                            dt2=df.loc[(df['torque']>5)&(df['torque']<7)]
                            print(dt2)
                        elif t==3:
                            dt3=df.loc[(df['torque']>8)&(df['torque']<10)]
                            print(dt3)
                        else:
                            print("EXIST FROM Torque")
                elif m==3:
                    mn=input("enter the model name:")
                    dm1=df.loc[df['model_name']==mn]
                else:
                    print("exist from user view")
        elif n==2:
            print("edit ")
        else:
            print("exist from main menu")
menu()